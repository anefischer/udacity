# Udacity Data Engineering Nanodegree Program ND027

This project is part of the Udacity Data Engineering Nanodegree Program.

## Datawarehouse

This project is an evolution of the previous projects within the course. Instead of a local storage data is processed on an AWS redshift cluster.
An ETL (Extract, Transform and Load) pipeline that transfers data from AWS S3 into these tables using Python and SQL is written.

### Instructions: Prerequisites, Installing and Running 

- Setup an aws redshift cluster and store the information in dwh.cfg.
- Create the database tables with create_tables.py.
- Process the data from the S3 sources with etl.py.

create_tables.py and etl.py file can be run as shown:
```
python create_tables.py 
python etl.py 
```

### Project Files

```
.
├── data/                  Data Folder
├── create_tables.py       Script to create database and tables
├── etl.py                 ETL script to process the data
├── README.md              Readme of the project
├── sql_queries.py         SQL queries used in ETL process and to create the tables
```


### Database Schema Design

- (new) staging_events: staging table for event data
- (new) staging_songs: staging table for song data
- songplays: records in log data associated with song plays 
- users: users in the app.
- songs: songs from the music database
- artists: artists from the music database
- time: timestamps of records in songplays broken down into specific units

## Review:

Here are some resources to learn further:

- Top 8 Best Practices for High-Performance ETL Processing Using Amazon Redshift: https://aws.amazon.com/blogs/big-data/top-8-best-practices-for-high-performance-etl-processing-using-amazon-redshift/
- How I built a data warehouse using Amazon Redshift and AWS services in record time: https://aws.amazon.com/blogs/big-data/how-i-built-a-data-warehouse-using-amazon-redshift-and-aws-services-in-record-time/
- Redshift ETL: 3 Ways to load data into AWS Redshift: https://panoply.io/data-warehouse-guide/redshift-etl/
- 2X Your Redshift Speed With Sortkeys and Distkeys: https://www.sisense.com/blog/double-your-redshift-performance-with-the-right-sortkeys-and-distkeys/

Please note that Redshift does not enforce unique, primary-key, and foreign-key constraints. Even though they are informational only, the query optimizer uses those constraints to generate more efficient query plans.
Ref:
https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-defining-constraints.html
http://www.sqlhaven.com/amazon-redshift-what-you-need-to-think-before-defining-primary-key/

Include an ER Diagram to show how the different tables are connected.
You can make use of online tools like https://www.lucidchart.com/
