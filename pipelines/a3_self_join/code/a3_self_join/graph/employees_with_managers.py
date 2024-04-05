from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from a3_self_join.config.ConfigStore import *
from a3_self_join.udfs.UDFs import *

def employees_with_managers(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.manager_id") == col("in1.employee_id")), "left_outer")\
        .select(col("in0.employee_id").alias("employee_id"), col("in0.f_name").alias("f_name"), col("in0.l_name").alias("l_name"), col("in0.title").alias("title"), col("in0.manager_id").alias("manager_id"), col("in1.f_name").alias("mgr_f_name"), col("in1.l_name").alias("mgr_l_name"))
