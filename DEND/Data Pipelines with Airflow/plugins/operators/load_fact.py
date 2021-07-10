from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

"""
LoadFactOperator creates a node in the dag 
which loads the fact table songplays from staging tables.
"""
class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="redshift",
                 table="",                 
                 sql="",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql = sql
        
    def execute(self, context):
        
        self.log.info("LoadFactOperator: PostgresHook") 
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        self.log.info("LoadFactOperator: INSERT INTO {} {}".format(self.table, self.sql))         
        redshift.run("INSERT INTO {} {}".format(self.table, self.sql))        
        self.log.info("LoadFactOperator: Success")
        