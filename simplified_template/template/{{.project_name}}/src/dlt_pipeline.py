# Databricks notebook source
# MAGIC %md
# MAGIC # {{.project_name}} - Delta Live Tables Pipeline (Python)
# MAGIC
# MAGIC {{- if eq .enable_unity_catalog "yes"}}
# MAGIC **Unity Catalog:** `{{.catalog_name}}.{{.schema_name}}`
# MAGIC {{- end}}

# COMMAND ----------

import dlt
from pyspark.sql import functions as F

# COMMAND ----------

# MAGIC %md
# MAGIC ## Bronze Layer - Raw Data Ingestion

# COMMAND ----------

@dlt.table(
    comment="Raw data ingestion - Bronze layer",
    table_properties={
        "quality": "bronze",
        "pipelines.autoOptimize.managed": "true"
    }
)
def bronze_raw_data():
    """Ingest raw data into bronze layer"""
    return (
        spark.range(0, 10000)
        .select(
            F.col("id"),
            F.rand().alias("value"),
            (F.col("id") % 100).alias("category"),
            F.current_timestamp().alias("ingested_at")
        )
    )

# COMMAND ----------

# MAGIC %md
# MAGIC ## Silver Layer - Cleaned and Validated Data

# COMMAND ----------

@dlt.table(
    comment="Cleaned and validated data - Silver layer",
    table_properties={
        "quality": "silver",
        "pipelines.autoOptimize.managed": "true"
    }
)
@dlt.expect_or_drop("valid_value", "value >= 0 AND value <= 1")
@dlt.expect("valid_id", "id >= 0")
def silver_cleaned_data():
    """Clean and validate bronze data"""
    return (
        dlt.read("bronze_raw_data")
        .withColumn("value_normalized", F.col("value") * 100)
        .withColumn("processed_at", F.current_timestamp())
    )

# COMMAND ----------

# MAGIC %md
# MAGIC ## Gold Layer - Business Aggregates

# COMMAND ----------

@dlt.table(
    comment="Business aggregates - Gold layer",
    table_properties={
        "quality": "gold",
        "pipelines.autoOptimize.managed": "true"
    }
)
def gold_category_summary():
    """Aggregate data by category for business reporting"""
    return (
        dlt.read("silver_cleaned_data")
        .groupBy("category")
        .agg(
            F.count("*").alias("record_count"),
            F.avg("value_normalized").alias("avg_value"),
            F.stddev("value_normalized").alias("stddev_value"),
            F.min("value_normalized").alias("min_value"),
            F.max("value_normalized").alias("max_value")
        )
    )
