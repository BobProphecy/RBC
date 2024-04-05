from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from a3_self_join.config.ConfigStore import *
from a3_self_join.udfs.UDFs import *

def stooges(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("employee_id", StringType(), True), StructField("f_name", StringType(), True), StructField("l_name", StringType(), True), StructField("title", StringType(), True), StructField("manager_id", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/FileStore/bobwelshmer/sample_data/stooges.csv")
