## Data Lake

ETL pipeline that reads raw Sparkify song and log data from S3, transforms it with PySpark into analytics-ready dimensional tables, and writes them back to S3 as partitioned Parquet — the lake equivalent of the Postgres / Redshift versions of this dataset.

### Stack
PySpark, AWS S3 (runs locally or on EMR)

### Schema (Star, Parquet on S3)
- **Fact** — `songplays`: partitioned by year and month
- **Dimensions** — `users`, `artists`, `songs` (partitioned by year, artist), `time` (partitioned by year, month)

### Files
```
.
├── etl.py   Spark job: read S3 → transform → write S3 as Parquet
└── dl.cfg   AWS credentials (gitignored)
```

### Run
```
python etl.py
```
