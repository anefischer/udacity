## Data Modeling with Postgres

ETL pipeline that loads the Sparkify music-streaming dataset (song metadata + user activity logs) from local JSON files into a Postgres star schema optimized for song-play analytics.

### Stack
Python, psycopg2, PostgreSQL, Jupyter

### Schema (Star)
- **Fact** — `songplays`: records of song-play events from log data
- **Dimensions** — `users`, `songs`, `artists`, `time`

### Files
```
.
├── data/                Source JSON files (song + log data)
├── create_tables.py     Drops and creates database + tables
├── sql_queries.py       DDL and DML statements
├── etl.py               ETL pipeline
├── etl.ipynb            Notebook used during development
├── test.ipynb           Validation queries
└── requirements.txt
```

### Run
Requires a local PostgreSQL on port 5432.
```
pip install -r requirements.txt
python create_tables.py
python etl.py
```
