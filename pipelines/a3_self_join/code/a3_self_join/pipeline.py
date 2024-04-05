from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from a3_self_join.config.ConfigStore import *
from a3_self_join.udfs.UDFs import *
from prophecy.utils import *
from a3_self_join.graph import *

def pipeline(spark: SparkSession) -> None:
    df_stooges = stooges(spark)
    df_mgr_stooges = mgr_stooges(spark)
    df_employees_with_managers = employees_with_managers(spark, df_stooges, df_mgr_stooges)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("a3_self_join")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/a3_self_join")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/a3_self_join", config = Config)(pipeline)

if __name__ == "__main__":
    main()
