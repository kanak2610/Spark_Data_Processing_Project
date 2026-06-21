# Employee Data Processing using Apache Spark (PySpark)

## Project Overview

In today's data-driven world, organizations generate massive volumes of structured and unstructured data. Traditional processing frameworks often struggle with speed and scalability when handling large datasets. Apache Spark addresses these challenges through distributed and in-memory computing.

This project demonstrates a complete data processing pipeline using Apache Spark DataFrames. The workflow includes data cleaning, transformation, filtering, schema modification, aggregation, and analytical reporting on employee data.

---

## Objectives

The primary objectives of this project are:

* Understand the limitations of MapReduce.
* Explore Apache Spark architecture and DataFrames.
* Perform data cleaning operations on raw datasets.
* Handle missing and inconsistent values.
* Remove duplicate records.
* Apply filtering and transformation techniques.
* Modify schemas and datatypes.
* Create derived columns.
* Perform aggregation and GroupBy operations.
* Understand shuffle and wide transformations.
* Generate meaningful business insights from processed data.

---

## Why Apache Spark?

### Limitations of MapReduce

* High disk I/O operations
* Slower processing for iterative tasks
* Complex development workflow
* Limited support for real-time analytics

### Advantages of Apache Spark

* In-memory processing
* Faster execution compared to MapReduce
* Easy-to-use APIs
* Distributed computing support
* Scalable architecture
* Efficient DataFrame operations
* Supports SQL, Streaming, Machine Learning, and Graph Processing

---

## Dataset Description

The dataset contains employee-related information:

| Column | Description     |
| ------ | --------------- |
| id     | Employee ID     |
| name   | Employee Name   |
| age    | Employee Age    |
| salary | Monthly Salary  |
| region | Employee Region |

The dataset intentionally contains:

* Duplicate records
* Missing values
* Inconsistent entries

These issues simulate real-world data quality challenges.

---

## Data Processing Pipeline

Raw Dataset
↓
Data Ingestion
↓
Duplicate Removal
↓
Null Value Handling
↓
Schema Modification
↓
Data Transformation
↓
Filtering
↓
Aggregation
↓
GroupBy Analysis
↓
Business Insights

---

## Data Cleaning Operations

### Duplicate Removal

Duplicate records were identified and removed using Spark DataFrame operations to improve data quality and ensure accurate analysis.

### Missing Value Handling

The following strategies were applied:

* Missing Age → Replaced with 0
* Missing Salary → Replaced with 0
* Missing Region → Replaced with "Unknown"

### Schema Standardization

* Renamed salary column to monthly_salary
* Applied datatype casting
* Improved dataset consistency

---

## Transformations Performed

### Filtering

Employee records were filtered based on predefined age conditions.

### Derived Column

A new column named annual_salary was created using:

Annual Salary = Monthly Salary × 12

This transformation enables yearly compensation analysis.

---

## Aggregation Analysis

The following aggregation functions were performed:

* Count
* Sum
* Average
* Minimum
* Maximum

These operations help summarize employee salary statistics efficiently.

---

## Region-wise Analysis

Using GroupBy operations, the project calculates:

* Number of Employees
* Average Salary
* Total Salary

This provides a regional overview of workforce distribution and salary trends.

---

## Narrow and Wide Transformations

### Narrow Transformations

Examples:

* select()
* filter()

Characteristics:

* No data shuffle
* Faster execution
* Operates within partitions

### Wide Transformations

Examples:

* groupBy()
* aggregate()

Characteristics:

* Data shuffle occurs
* Requires redistribution of data across partitions
* More computationally intensive

---

## Key Insights

* Duplicate employee records were successfully removed.
* Missing values were handled effectively.
* Dataset consistency was improved through schema modifications.
* Annual salary calculations enabled deeper compensation analysis.
* Region-wise aggregation provided meaningful business insights.
* Apache Spark significantly simplified large-scale data processing tasks.

---

## Technologies Used

* Python
* Apache Spark (PySpark)
* Spark DataFrames
* CSV Dataset
* GitHub

---

## Project Structure

Celebal_Spark_Assignment/

├── employee.csv

├── spark_assignment.py

├── README.md

├── requirements.txt

├── .gitignore

└── screenshots/

---

## Conclusion

This project demonstrates an end-to-end data engineering workflow using Apache Spark. Through data cleaning, transformation, filtering, aggregation, and analytical reporting, the project showcases how Spark can efficiently process and analyze datasets at scale.

The implementation highlights Spark's ability to deliver fast, scalable, and reliable data processing solutions, making it one of the most powerful frameworks in modern data engineering.
