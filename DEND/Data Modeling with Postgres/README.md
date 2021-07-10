# Udacity Data Engineering Nanodegree Program ND027

This project is part of the Udacity Data Engineering Nanodegree Program.

## Data Modeling with Postgres

In this project fact and dimension tables for a star schema for a particular analytic focus are defined. 
An ETL (Extract, Transform and Load) pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL is written.

### Instructions: Prerequisites, Installing and Running 
Install requirements with pip3 install -r requirements.txt.
Set up a local [PostgreSQL](https://www.postgresql.org/docs/9.1/runtime.html) on port 5432.
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
├── etl.ipynb              Jupyter Notebook to experiment with ETL process
├── etl.py                 ETL script based on Jupyter Notebook
├── requirements.txt       Requirments to install the Python environment
├── README.md              Readme of the project
├── sql_queries.py         SQL queries used in ETL process
└── test.ipynb             Jupyter Notebook to test
```


### Database Schema Design
- fact table songplays: records in log data associated with song plays 
- dimension table users: users in the app.
- dimension table song: songs from the music database
- dimension table artists: artists from the music database
- dimension table time: timestamps of records in songplays broken down into specific units.