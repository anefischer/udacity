import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, monotonically_increasing_id
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format
from pyspark.sql.types import TimestampType

config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS']['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    '''
            Description: Create a Spark Session
                
            Parameters:
                    -
                    
            Returns:
                    -
    '''    
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    '''
            Description: Processes the song data stored in JSON-files via Spark and stores them in parquet files in an S3 container
            
            Parameters:
                    spark (handle): handle to Spark Session
                    input_data (string): path to Input directory on S3
                    output_data (string): path to Output directory on S3
                    
            Returns:
                    -
    '''    
    
    # get filepath to song data file
    song_data = os.path.join(input_data, 'song_data/*/*/*/*.json')
    
    # read song data file
    df = spark.read.json(song_data)

    # extract columns to create songs table
    songs_table = df.select('song_id', 'title', 'artist_id', 'year', 'duration').drop_duplicates()
    
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.parquet(f'{output_data}/songs_table', mode='overwrite', partitionBy=['year', 'artist_id'])

    # extract columns to create artists table
    artists_table =  df.select('artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude').drop_duplicates()
    
    # write artists table to parquet files
    artists_table.write.parquet(f'{output_data}/artists_table', mode='overwrite')


def process_log_data(spark, input_data, output_data):
    '''
            Description: Processes the log data stored in JSON-files via Spark and stores them in parquet files in an S3 container
            
            Parameters:
                    spark (handle): handle to Spark Session
                    input_data (string): path to Input directory on S3
                    output_data (string): path to Output directory on S3
                    
            Returns:
                    -
    '''
    
    # get filepath to log data file
    log_data = os.path.join(input_data, 'log_data/*/*/*.json')
    #log_data=  os.path.join(input_data, "*.json") #debug using local files
    
    # read log data file
    df = spark.read.json(log_data) 
    
    # filter by actions for song plays
    df = df.filter(df['page'] == 'NextSong') 

    # extract columns for users table    
    users_table  = df.select('userId', 'firstName', 'lastName', 'gender', 'level').distinct()
    
    # write users table to parquet files
    users_table.write.parquet(f'{output_data}/users_table', mode='overwrite')

    # create timestamp column from original timestamp column
    get_timestamp = udf(lambda x: datetime.fromtimestamp(x / 1000), TimestampType())
    df = df.withColumn('timestamp', get_timestamp(df.ts))
    
    # create datetime column from original timestamp column
    get_datetime = udf(lambda x: to_date(x), TimestampType())
    df = df.withColumn('datetime', get_datetime(df.ts))
    
    # extract columns to create time table
    time_table = df.select("ts","timestamp").drop_duplicates() \
                    .withColumn("hour", hour(col('timestamp'))) \
                    .withColumn("day", dayofmonth(col('timestamp'))) \
                    .withColumn("week", weekofyear(col('timestamp'))) \
                    .withColumn("month", month(col('timestamp'))) \
                    .withColumn("year", year(col('timestamp'))) \
                    .withColumn("weekday", date_format(col('timestamp'),'E'))  
                    
    
    # write time table to parquet files partitioned by year and month
    time_table.write.parquet(f'{output_data}/time_table', mode='overwrite', partitionBy=["year", "month"])

    # read in song data to use for songplays table
    song_df = spark.read.parquet(f'{output_data}/songs_table')

    # extract columns from joined song and log datasets to create songplays table  
    songplays_table = df.join(song_df, df.song == song_df.title, how='inner')\
                        .select(monotonically_increasing_id().alias("songplay_id"),"ts",col("userId").alias("user_id"),"level","song_id","artist_id", col("sessionId").alias("session_id"), "location", col("userAgent").alias("user_agent")) \
                        .join(time_table, df.ts == time_table.ts, how="inner")\
                        .select("songplay_id", "user_id", "level", "song_id", "artist_id", "session_id", "location", "user_agent", "year", "month") \
                        .drop_duplicates()
                 
        
    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.parquet(f'{output_data}/songplays_table', mode='overwrite', partitionBy=["year", "month"])

def main():
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://adinef/"

    # use local files for debugging
    #input_data = "data/"
    #output_data = "temp/"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
