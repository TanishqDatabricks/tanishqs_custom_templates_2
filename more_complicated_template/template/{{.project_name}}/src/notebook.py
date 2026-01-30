# Databricks notebook source
# MAGIC %md
# MAGIC # {{.project_name}} - Hello World Notebook

# COMMAND ----------

print("Hello from {{.project_name}}!")
print(f"Spark version: {spark.version}")

# COMMAND ----------

# Create simple data
data = [
    (1, "Hello"),
    (2, "World"),
    (3, "From"),
    (4, "{{.project_name}}")
]

df = spark.createDataFrame(data, ["id", "message"])
display(df)

# COMMAND ----------

print("✅ Notebook completed successfully!")
