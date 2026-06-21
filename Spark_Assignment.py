from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create Spark Session

spark = SparkSession.builder 
.appName("Employee Data Cleaning and Aggregation") 
.getOrCreate()

# Read CSV File

df = spark.read.csv(
"employee.csv",
header=True,
inferSchema=True
)

print("=" * 50)
print("ORIGINAL DATA")
print("=" * 50)
df.show()

# Remove Duplicate Records

df = df.dropDuplicates()

print("=" * 50)
print("AFTER REMOVING DUPLICATES")
print("=" * 50)
df.show()

# Handle Null Values

df = df.fillna({
"age": 0,
"salary": 0,
"region": "Unknown"
})

print("=" * 50)
print("AFTER HANDLING NULL VALUES")
print("=" * 50)
df.show()

# Rename Column

df = df.withColumnRenamed(
"salary",
"monthly_salary"
)

# Change Datatype

df = df.withColumn(
"monthly_salary",
col("monthly_salary").cast("integer")
)

# Create Derived Column

df = df.withColumn(
"annual_salary",
col("monthly_salary") * 12
)

print("=" * 50)
print("AFTER TRANSFORMATIONS")
print("=" * 50)
df.show()

# Filtering Records

filtered_df = df.filter(
(col("age") >= 20) &
(col("age") <= 30)
)

print("=" * 50)
print("FILTERED EMPLOYEES (AGE 20-30)")
print("=" * 50)
filtered_df.show()

# Aggregations

print("=" * 50)
print("AGGREGATION RESULTS")
print("=" * 50)

print("Total Employees:", df.count())

df.select(
avg("monthly_salary").alias("Average Salary")
).show()

df.select(
min("monthly_salary").alias("Minimum Salary")
).show()

df.select(
max("monthly_salary").alias("Maximum Salary")
).show()

df.select(
sum("monthly_salary").alias("Total Salary")
).show()

# GroupBy Aggregation

print("=" * 50)
print("REGION-WISE ANALYSIS")
print("=" * 50)

result = df.groupBy("region").agg(
count("*").alias("employee_count"),
avg("monthly_salary").alias("average_salary"),
sum("monthly_salary").alias("total_salary")
)

result.show()

# HAVING Condition

print("=" * 50)
print("REGIONS WITH TOTAL SALARY > 30000")
print("=" * 50)

result.filter(
col("total_salary") > 30000
).show()

print("=" * 50)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 50)

spark.stop()
