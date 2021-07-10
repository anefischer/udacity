# Udacity Data Engineering Nanodegree Program ND027

This project is part of the Udacity Data Engineering Nanodegree Program.

## Datawarehouse

This project is an evolution of the previous projects within the course. 
An ETL (Extract, Transform and Load) pipeline loads data from S3 transforms it using spark and loads it back to S3.

### Instructions: Prerequisites, Installing and Running 

- Setup an S3 bucket and store login in df.cfg.
- Process the data from the S3 sources with etl.py.

etl.py file can be run as shown:
```
python etl.py 
```

### Project Files

```
.
├── data/                  Data Folder
├── etl.py                 ETL script to process the data
├── README.md              Readme of the project
```


### Database Schema Design

- songplays: records in log data associated with song plays 
- users: users in the app.
- songs: songs from the music database
- artists: artists from the music database
- time: timestamps of records in songplays broken down into specific units
