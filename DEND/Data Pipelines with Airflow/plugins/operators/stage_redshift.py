from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.contrib.hooks.aws_hook import AwsHook

"""
StageToRedshiftOperator creates a node in the dag 
which loads data from S3 json files to staging tables on redshift cluster.
"""
class StageToRedshiftOperator(BaseOperator):
    
    ui_color = '#358140'

    copy_sql = """
        COPY {}
        FROM '{}'
        ACCESS_KEY_ID '{}'
        SECRET_ACCESS_KEY '{}'
        FORMAT AS json '{}'
    """
    
    @apply_defaults
    def __init__(self,
                 aws_credentials_id="",
                 redshift_conn_id="",
                 s3_bucket="",
                 s3_key="",
                 json="",                 
                 table="",
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.aws_credentials_id = aws_credentials_id
        self.redshift_conn_id = redshift_conn_id
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.json = json
        self.table = table
        
    def execute(self, context):
        
        self.log.info("StageToRedshiftOperator: AWShook") 
        aws_hook = AwsHook(self.aws_credentials_id)
        credentials = aws_hook.get_credentials()
        
        self.log.info("StageToRedshiftOperator: PostgresHook") 
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        self.log.info("StageToRedshiftOperator: DELTE FROM {}".format(self.table)) 
        redshift.run("DELETE FROM {}".format(self.table))
        self.log.info("StageToRedshiftOperator: Success")
        
        self.log.info("StageToRedshiftOperator: COPY TABLE {}".format(self.table)) 
        redshift.run(StageToRedshiftOperator.copy_sql.format(
            self.table,
            "s3://{}/{}".format(self.s3_bucket,  self.s3_key),
            credentials.access_key,
            credentials.secret_key,
            self.json
        ))
        self.log.info("StageToRedshiftOperator: Success")





