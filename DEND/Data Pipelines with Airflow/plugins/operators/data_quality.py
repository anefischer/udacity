from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

"""
DataQualityOperator creates a node in the dag 
which Checks the tables for data quality problems.
"""
class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 dq_checks=[],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id,
        self.dq_checks = dq_checks
        
    def execute(self, context):
        
        self.log.info("DataQualityOperator: PostgresHook") 
        redshift = PostgresHook(self.redshift_conn_id)

       if len(self.dq_checks) <= 0:
            self.log.info("DataQualityOperator: Error No checks")
            return
        
        errors = 0
        
        for dq_check in self.dq_checks:
            check_sql = dq_check.get('check_sql')
            expected_result = dq_check.get('expected_result')

            try:
                self.log.info("DataQualityOperator: Check - {}".format(check_sql))
                records = redshift.get_records(check_sql)[0]
            except Exception as e:
                self.log.info("DataQualityOperator: Error - {}".format(e))

            if expected_result != records[0]:
                errors += 1
                self.log.info("DataQualityOperator: Failed - {}".format(check_sql))
 
        if errors > 0:
            raise ValueError('DataQualityOperator: Failed')
        else:
            self.log.info("DataQualityOperator: Success")      
        
     