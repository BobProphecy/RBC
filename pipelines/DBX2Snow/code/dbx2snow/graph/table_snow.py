from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dbx2snow.config.ConfigStore import *
from dbx2snow.udfs.UDFs import *

def table_snow(spark: SparkSession, in0: DataFrame):
    writer = in0.write\
                 .format("snowflake")\
                 .options(**{
        "sfUrl": "https://tu22760.ap-south-1.aws.snowflakecomputing.com/",
        "sfUser": "DEMOACCOUNT",
        "sfPassword": "jck5yjn5bpf9uzx*DMJ",
        "sfDatabase": "BOBW",
        "sfSchema": "DEMO_OUTPUT",
        "sfWarehouse": "",
        "sfRole": ""
                 })
    writer = writer.option("dbtable", "top_sales_ppg")
    writer = writer.mode("overwrite")
    writer.save()
