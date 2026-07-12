from airflow.sdk import dag, task
from airflow.operators.bash import BashOperator
import pendulum

default_args = {
    "retries": 3,
    "retry_delay": pendulum.duration(minutes=10),
}

@dag(
    dag_id="orchestrate",
    schedule="0 11 * * *",
    start_date=pendulum.datetime(2026, 7, 11, tz="UTC"),
    catchup=False,
    default_args=default_args,
)

def orchestrate():
    @task
    def ingest_cdc():
        return "simple dag"
        # ws = WorkspaceClient(
        #     host="",
        #     token=""
        # )

        # job_trigger = ws.jobs.run_now(
        #     job_id="")

        # while True:
            
        #     jb_run = ws.jobs.get_run(run_id=job_trigger["run_id"])

        #     print(f"Job run status:{jb_run.state.lifecycle_state}, result_state: {jb_run.state.result_state}")

        #     if jb_run["state"] in [RunLifeCycle.TERMINATED, RunLifeCycle.SKIPPED, RunLifeCycle.INTERNAL_ERROR]:
        #         if jb_run["result_state"] == RunLifeCycle.SUCCESS:
        #             print(f"Job {jb_run['id']} succeeded.")
        #             break
        #         else:
        #             raise Exception(f"Job {jb_run['id']} finished with state: {jb_run['state']}")
        #             break
            
        #     time.sleep(5)

    @task.bash
    def clean_target():
        return "rm -rf /opt/airflow_dbt/walmart_de/target && rm -rf /opt/airflow_dbt/walmart_de/logs && rm -rf /opt/airflow_dbt/walmart_de/dbt_modules"
    
    @task.bash
    def source_freshness():
        # manually set the working directory using cd command before running
        return "cd /opt/airflow_dbt/walmart_de && dbt source freshness"
    
    # source_freshness = BashOperator(
    #     task_id="source_freshness",
    #     cwd="/opt/airflow_dbt/walmart_de",
    #     bash_command="dbt source freshness"
    # )

    silver_technical = BashOperator(
        task_id="silver_technical",
        cwd="/opt/airflow_dbt/walmart_de",
        bash_command="dbt run --select silver_technical"
    )

    silver_technical_test = BashOperator(
        task_id="silver_technical_test",
        cwd="/opt/airflow_dbt/walmart_de",
        bash_command="dbt test --select silver_technical"
    )

    silver_business = BashOperator(
        task_id="silver_business",
        cwd="/opt/airflow_dbt/walmart_de",
        bash_command="dbt run --select silver_business"
    )

    silver_business_test = BashOperator(
        task_id="silver_business_test",
        cwd="/opt/airflow_dbt/walmart_de",
        bash_command="dbt test --select silver_business"
    )

    gold_ephemeral = BashOperator(
        task_id="gold_ephemeral",
        cwd="/opt/airflow_dbt/walmart_de",
        bash_command="dbt run --select gold/ephemeral"
    )

    gold_dimensions = BashOperator(
        task_id="gold_dimensions",
        cwd="/opt/airflow_dbt/walmart_de",
        bash_command="dbt snapshot"
    )

    gold_fact = BashOperator(
        task_id="gold_fact",
        cwd="/opt/airflow_dbt/walmart_de",
        bash_command="dbt run --select gold/fact"
    )

    #dependencies (DAG)
    ingest_cdc() >> clean_target() >> source_freshness() >> silver_technical >> silver_technical_test >> silver_business >> silver_business_test >> gold_ephemeral >> gold_dimensions >> gold_fact

orchestrate_dag = orchestrate()