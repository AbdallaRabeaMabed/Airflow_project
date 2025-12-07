from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime , timedelta
from airflow.models import Variable
import pendulum
from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.sensors.sql import SqlSensor


def process_data():
    print("records exist...")

with DAG(
    'check_data',
    description='A simple DAG to check data existence with SqlSensor',
    start_date=datetime(2025, 12, 4, 6, tzinfo=pendulum.timezone("Africa/Cairo")),
    dagrun_timeout=timedelta(minutes=45),
    schedule='*/30 * * * *',
    catchup=False
) as dag:
    
    check_data_existence = SqlSensor(
        task_id='check_data_existence',
        conn_id='postgres_default',
        sql=''' select * FROM customers where customers.customer_name = 'Abdalla Johnson'; ''',
        poke_interval=10,
        timeout=30,
        mode='reschedule',
    )

    process_data_task = PythonOperator(
        task_id='process_data_task',
        python_callable=process_data,
        
    )

    check_data_existence >> process_data_task