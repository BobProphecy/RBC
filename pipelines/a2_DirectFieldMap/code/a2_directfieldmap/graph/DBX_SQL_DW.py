from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from a2_directfieldmap.config.ConfigStore import *
from a2_directfieldmap.udfs.UDFs import *

def DBX_SQL_DW(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`bobwelshmer`.`demo_output`.`customer_tbl`")
