from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dbx2snow.config.ConfigStore import *
from dbx2snow.udfs.UDFs import *

def table_snow(spark: SparkSession, in0: DataFrame):
    options = dict()
    writer = in0.write.format("snowflake").options(**options)
    writer = writer.option("dbtable", "top_sales_ppg")
    writer = writer.mode("overwrite")
    writer.save()
