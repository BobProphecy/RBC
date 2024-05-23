import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from gywxvb9dtbtjqwmwd49cea_.tasks import customers_orders, report_top_customers
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "gYwxvB9DTbTjQwMwd49ceA_", 
    schedule_interval = "0 0 * * 1", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "P1Mfmhdo"}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2024, 3, 12, tz = "UTC"), 
    catchup = True
) as dag:
    customers_orders_op = customers_orders()
    report_top_customers_op = report_top_customers()
    customers_orders_op >> report_top_customers_op
