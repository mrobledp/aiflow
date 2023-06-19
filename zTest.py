from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

from datetime import datetime, timedelta


with DAG(
    dag_id='zTest',
    schedule_interval='0 0 * * *',
    start_date=datetime(2023, 6, 18),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['Prueba', 'Ejecutar python program'],
    params={"example_key": "example_value"},
) as dag:
    
    # [START howto_operator_bash]
    ejecucion = BashOperator(
        task_id='ejecucion',
        #############>>>>>>>>>>>>>>>bash_command='echo "Here is the message: \'{{ dag_run.conf["example_key"]}}\'"',
        bash_command='python3 /opt/airflow/mario/argumentos.py {{ dag_run.conf["example_key"]}}',
        params = {}
    )
    
ejecucion

if __name__ == "__main__":
    dag.cli()


"""
{
    "example_key": "['Elemento uno', 'Elemento dos', 'Elemento tres']"
}
"""