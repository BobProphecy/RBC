from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from a3_self_join.config.ConfigStore import *
from a3_self_join.udfs.UDFs import *

def managers(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(~ col("title").isin(lit("Associate")))
