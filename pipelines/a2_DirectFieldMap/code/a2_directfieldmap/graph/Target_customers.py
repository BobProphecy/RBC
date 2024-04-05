from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from a2_directfieldmap.config.ConfigStore import *
from a2_directfieldmap.udfs.UDFs import *

def Target_customers(spark: SparkSession, in0: DataFrame):
    writer = in0.write\
                 .format("snowflake")\
                 .options(**{
        "sfUrl": "https://tu22760.ap-south-1.aws.snowflakecomputing.com/",
        "sfUser": "DEMOACCOUNT",
        "sfPassword": "DEMOACCOUNT",
        "sfDatabase": "BOBW",
        "sfSchema": "DEMO_OUTPUT",
        "sfWarehouse": "",
        "sfRole": ""
                 })
    writer = writer.option("dbtable", "rbc_cust_target")
    writer = writer.mode("overwrite")
    writer.save()
