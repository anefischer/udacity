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
