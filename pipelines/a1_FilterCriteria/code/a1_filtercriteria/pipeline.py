from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from a1_filtercriteria.config.ConfigStore import *
from a1_filtercriteria.udfs.UDFs import *
from prophecy.utils import *
from a1_filtercriteria.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)
    df_Filter_Acct_Category = Filter_Acct_Category(spark, df_customers)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/a1_FilterCriteria")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/a1_FilterCriteria", config = Config)(pipeline)

if __name__ == "__main__":
    main()
