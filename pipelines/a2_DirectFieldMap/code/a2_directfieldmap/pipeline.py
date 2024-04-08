from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from a2_directfieldmap.config.ConfigStore import *
from a2_directfieldmap.udfs.UDFs import *
from prophecy.utils import *
from a2_directfieldmap.graph import *

def pipeline(spark: SparkSession) -> None:
    df_RAW_customers = RAW_customers(spark)
    DBX_SQL_DW(spark, df_RAW_customers)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/a2_DirectFieldMap")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/a2_DirectFieldMap", config = Config)(pipeline)

if __name__ == "__main__":
    main()
