from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

"""
LoadDimensionOperator creates a node in the dag 
which truncates (optional) and loads the dimension table from staging tables.
"""
class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="redshift",
                 table="",
                 sql="",
                 truncate=True,                 
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql = sql
        self.truncate = truncate
        
    def execute(self, context):
        
        self.log.info("LoadDimensionOperator: PostgresHook") 
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        if self.truncate:
            self.log.info("LoadDimensionOperator: TRUNCATE TABLE {}".format(self.table)) 
            redshift.run("TRUNCATE TABLE {}".format(self.table))
            self.log.info("LoadDimensionOperator: Success")
        
        self.log.info("LoadDimensionOperator: {}".format(self.sql.format(self.table))) 
        redshift.run(self.sql.format(self.table))
        self.log.info("LoadDimensionOperator: Success")
