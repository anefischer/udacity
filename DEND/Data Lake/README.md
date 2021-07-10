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


## Review

A few articles of interest:
- TOP FIVE DIFFERENCES BETWEEN DATA LAKES AND DATA WAREHOUSES: https://www.blue-granite.com/blog/bid/402596/top-five-differences-between-data-lakes-and-data-warehouses
- What Is A Data Lake? A Super-Simple Explanation For Anyone: https://www.forbes.com/sites/bernardmarr/2018/08/27/what-is-a-data-lake-a-super-simple-explanation-for-anyone/#4f61b70d76e0
- When Should We Load Relational Data to a Data Lake?: https://www.sqlchick.com/entries/2018/11/13/when-should-we-load-relational-data-to-a-data-lake

Partitioning helps queries to run much faster. See this article on detailed info on partition, https://mungingdata.com/apache-spark/partitionby/

Refer good READMEs on web:
- https://github.com/matiassingers/awesome-readme
- https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project
- https://medium.com/@meakaakka/a-beginners-guide-to-writing-a-kickass-readme-7ac01da88ab3
- 
Suggestions:
- Add a screenshot or an image (ER Diagram) showing how the fact and dimension tables are connected.
- You can make use of online tools like https://www.lucidchart.com/
