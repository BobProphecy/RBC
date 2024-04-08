from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from a2_directfieldmap.config.ConfigStore import *
from a2_directfieldmap.udfs.UDFs import *

def SNOW(spark: SparkSession, in0: DataFrame):
    writer = in0.write\
                 .format("snowflake")\
                 .options(**{
        "sfUrl": "https://tu22760.ap-south-1.aws.snowflakecomputing.com",
        "sfUser": "DEMOACCOUNT",
        "sfPassword": "jck5yjn5bpf9uzx*DMJ",
        "sfDatabase": "BOBW",
        "sfSchema": "DEMO_OUTPUT",
        "sfWarehouse": "COMPUTE_WH",
        "sfRole": ""
                 })
    writer = writer.option("dbtable", "tar_sales_table")
    writer = writer.mode("overwrite")
    writer.save()
