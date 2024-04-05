from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from a1_filtercriteria.config.ConfigStore import *
from a1_filtercriteria.udfs.UDFs import *

def Filter_Acct_Category(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(col("account_flags").isin(lit("E"), lit("A")))
