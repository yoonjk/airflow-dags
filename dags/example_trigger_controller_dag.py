from __future__ import annotations

import pendulum

from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

with DAG(
    dag_id="example_trigger_controller_dag",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    schedule_interval="@once",
    tags=['example'],
) as dag:
    trigger = TriggerDagRunOperator(
        task_id="test_trigger_dagrun",
        trigger_dag_id="example_trigger_target_dag",  # Ensure this equals the dag_id of the DAG to trigger
        conf={"message": "Hello World"},
    )
