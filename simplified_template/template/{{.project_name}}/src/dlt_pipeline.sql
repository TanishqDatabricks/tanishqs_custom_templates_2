-- Databricks notebook source
-- MAGIC %md
-- MAGIC # {{.project_name}} - Delta Live Tables Pipeline (SQL)
-- MAGIC
-- MAGIC {{- if eq .enable_unity_catalog "yes"}}
-- MAGIC **Unity Catalog:** `{{.catalog_name}}.{{.schema_name}}`
-- MAGIC {{- end}}

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Bronze Layer - Raw Data Ingestion

-- COMMAND ----------

CREATE OR REFRESH STREAMING LIVE TABLE bronze_raw_data
COMMENT "Raw data ingestion - Bronze layer"
TBLPROPERTIES (
  "quality" = "bronze",
  "pipelines.autoOptimize.managed" = "true"
)
AS SELECT
  id,
  RAND() as value,
  id % 100 as category,
  current_timestamp() as ingested_at
FROM (
  SELECT explode(sequence(0, 9999)) as id
);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Silver Layer - Cleaned and Validated Data

-- COMMAND ----------

CREATE OR REFRESH STREAMING LIVE TABLE silver_cleaned_data (
  CONSTRAINT valid_value EXPECT (value >= 0 AND value <= 1) ON VIOLATION DROP ROW,
  CONSTRAINT valid_id EXPECT (id >= 0)
)
COMMENT "Cleaned and validated data - Silver layer"
TBLPROPERTIES (
  "quality" = "silver",
  "pipelines.autoOptimize.managed" = "true"
)
AS SELECT
  id,
  value,
  value * 100 as value_normalized,
  category,
  ingested_at,
  current_timestamp() as processed_at
FROM STREAM(LIVE.bronze_raw_data);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Gold Layer - Business Aggregates

-- COMMAND ----------

CREATE OR REFRESH LIVE TABLE gold_category_summary
COMMENT "Business aggregates - Gold layer"
TBLPROPERTIES (
  "quality" = "gold",
  "pipelines.autoOptimize.managed" = "true"
)
AS SELECT
  category,
  COUNT(*) as record_count,
  AVG(value_normalized) as avg_value,
  STDDEV(value_normalized) as stddev_value,
  MIN(value_normalized) as min_value,
  MAX(value_normalized) as max_value
FROM LIVE.silver_cleaned_data
GROUP BY category;
