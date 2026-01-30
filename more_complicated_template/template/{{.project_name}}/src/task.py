"""
{{.project_name}} - Main Task
Simple hello world example
"""

from pyspark.sql import SparkSession

def main():
    # Create Spark session
    spark = SparkSession.builder.appName('{{.project_name}}').getOrCreate()

    print('Hello from {{.project_name}}!')
    print(f'Spark version: {spark.version}')

    # Create simple data
    data = [
        (1, "Hello"),
        (2, "World"),
        (3, "From"),
        (4, "{{.project_name}}")
    ]

    df = spark.createDataFrame(data, ["id", "message"])
    df.show()

    print('Job completed successfully!')
    spark.stop()

if __name__ == '__main__':
    main()
