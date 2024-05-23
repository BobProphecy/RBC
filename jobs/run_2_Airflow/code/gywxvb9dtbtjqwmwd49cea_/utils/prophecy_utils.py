from airflow.decorators import task

db_pipeline_id_to_path_dict = {
    "pipelines/a1_FilterCriteria": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/a1_FilterCriteria-1.0-py3-none-any.whl", 
    "pipelines/a3_self_join": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/a3_self_join-1.0-py3-none-any.whl", 
    "pipelines/a2_DirectFieldMap": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/a2_DirectFieldMap-1.0-py3-none-any.whl", 
    "pipelines/DBX2Snow": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/DBX2Snow-1.0-py3-none-any.whl", 
    "pipelines/farmers-markets-irs": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/farmers_markets_irs-1.0-py3-none-any.whl", 
    "pipelines/report_top_customers": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/report_top_customers-1.0-py3-none-any.whl", 
    "pipelines/customers_orders": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/customers_orders-1.0-py3-none-any.whl", 
    "pipelines/join_agg_sort": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/join_agg_sort-1.0-py3-none-any.whl"
}


def task_wrapper(task_id):

    def decorator(func):

        @task(task_id = task_id)
        def wrapper(*args, **context):
            ## running the actual method.
            return func(*args, **context).execute(context)

        return wrapper

    return decorator

pipeline_package_name = {
    "pipelines/a3_self_join": "a3_self_join", 
    "pipelines/a1_FilterCriteria": "a1_FilterCriteria", 
    "pipelines/a2_DirectFieldMap": "a2_DirectFieldMap", 
    "pipelines/join_agg_sort": "join_agg_sort", 
    "pipelines/customers_orders": "customers_orders", 
    "pipelines/report_top_customers": "report_top_customers", 
    "pipelines/DBX2Snow": "DBX2Snow", 
    "pipelines/farmers-markets-irs": "farmers-markets-irs"
}
