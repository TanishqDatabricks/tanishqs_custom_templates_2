# Databricks notebook source
# MAGIC %md
# MAGIC # {{.project_name}} - Delta Live Tables Pipeline (Python)
# MAGIC
# MAGIC Simple "Hello World" DLT pipeline example

# COMMAND ----------

import dlt
from pyspark.sql import functions as F

# COMMAND ----------

@dlt.table(
    comment="Simple hello world table"
)
def hello_world_data():
    """Create a simple hello world dataset"""
    return spark.createDataFrame(
        [
            (1, "Hello", "World"),
            (2, "Delta", "Live"),
            (3, "Tables", "Demo")
        ],
        ["id", "word1", "word2"]
    )

# COMMAND ----------

@dlt.table(
    comment="Combined hello world message"
)
def hello_world_message():
    """Combine words into a message"""
    return (
        dlt.read("hello_world_data")
        .withColumn("message", F.concat_ws(" ", F.col("word1"), F.col("word2")))
        .withColumn("created_at", F.current_timestamp())
    )
