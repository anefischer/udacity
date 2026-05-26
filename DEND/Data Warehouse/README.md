## Data Warehouse

ETL pipeline that copies raw Sparkify event and song data from S3 into staging tables on AWS Redshift, then transforms them into a star schema for analytics queries — the cloud-warehouse evolution of the Postgres version of this project.

### Stack
AWS Redshift, S3, psycopg2

### Schema
- **Staging** — `staging_events`, `staging_songs`: raw copy from S3 via `COPY`
- **Fact** — `songplays`
- **Dimensions** — `users`, `songs`, `artists`, `time`

Sort keys and distribution keys are chosen to optimize the most frequent joins on the fact table.

### Files
```
.
├── create_tables.py    Drops and creates staging + analytics tables
├── sql_queries.py      DDL, COPY-from-S3, and INSERT transformations
├── etl.py              Loads staging from S3, then populates the star schema
└── dwh.cfg             Redshift connection + IAM role (gitignored)
```

### Run
Requires a running Redshift cluster and an IAM role with S3 read access.
```
python create_tables.py
python etl.py
```
