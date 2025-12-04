from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime , timedelta
from airflow.models import Variable
import pendulum

with DAG(
    'myfirstdag',
    description='A simple DAG ',
    start_date=datetime(2025, 12, 4, 6, tzinfo=pendulum.timezone("Africa/Cairo")),
    dagrun_timeout=timedelta(minutes=45),
    schedule='*/5 * * * *',
    catchup=False
) as dag:
    
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres_default',
        sql='sql/create_customer.sql'
    )

    insert_data = PostgresOperator(
        task_id='insert_data',
        postgres_conn_id='postgres_default',
        sql='sql/insert_data.sql'
    )

    create_table >> insert_data