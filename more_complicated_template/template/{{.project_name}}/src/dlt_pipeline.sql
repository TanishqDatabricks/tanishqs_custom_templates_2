-- Databricks notebook source
-- MAGIC %md
-- MAGIC # {{.project_name}} - Delta Live Tables Pipeline (SQL)
-- MAGIC
-- MAGIC Simple "Hello World" DLT pipeline example

-- COMMAND ----------

CREATE OR REFRESH LIVE TABLE hello_world_data
COMMENT "Simple hello world table"
AS SELECT
  id,
  word1,
  word2
FROM (
  VALUES
    (1, 'Hello', 'World'),
    (2, 'Delta', 'Live'),
    (3, 'Tables', 'Demo')
) AS t(id, word1, word2);

-- COMMAND ----------

CREATE OR REFRESH LIVE TABLE hello_world_message
COMMENT "Combined hello world message"
AS SELECT
  id,
  word1,
  word2,
  CONCAT(word1, ' ', word2) as message,
  current_timestamp() as created_at
FROM LIVE.hello_world_data;
