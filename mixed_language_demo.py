# Databricks notebook source
# MAGIC %md
# MAGIC # Simple Databricks Notebook with Python, R, SQL, and Markdown
# MAGIC This notebook demonstrates a combination of Python, R, SQL, and Markdown cells
# MAGIC in Databricks. It performs basic operations, suitable for a low-cost AWS
# MAGIC Databricks environment.
# MAGIC ### Steps:
# MAGIC 1. Perform basic Python operations.
# MAGIC 2. Use R for basic calculations.
# MAGIC 3. Execute SQL queries on an in-memory table.
# MAGIC 4. Add comments and explanations using Markdown.
# MAGIC 5. One more comment
# MAGIC
# MAGIC

# COMMAND ----------

# COMMAND ----------

# Python: Create a sample data frame with Amar, Akbar, and Anthony 
import pandas as pd

# Sample data
data = {
    "Name": ["Amar", "Akbar", "Anthony"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000],
    "Department": ["HR", "IT", "Finance"]
}

def create_dataframe():
    """
    Function to create a Pandas DataFrame
    """
    return pd.DataFrame(data)

def print_dataframe_summary(df):
    """
    Print a summary of the DataFrame
    """
    print("DataFrame Summary:")
    print(df.describe())

# If running directly, create the DataFrame and display the summary
if __name__ == "__main__":
    df = create_dataframe()
    print_dataframe_summary(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Python Code Explanation:
# MAGIC - Created a Pandas DataFrame with sample data (Name, Age, Salary).
# MAGIC - Converted it into a Spark DataFrame for use in Databricks.
# MAGIC - Displayed the Spark DataFrame using the `display` function.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Python Code Explanation:
# MAGIC - Created a Pandas DataFrame with sample data (Name, Age, Salary, Department).
# MAGIC - Converted it into a Spark DataFrame for use in Databricks.
# MAGIC - Displayed the Spark DataFrame using the `display` function.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### R Code Explanation:
# MAGIC - Created a numeric vector `numbers` with five values.
# MAGIC - Calculated the mean of the numbers using the `mean` function.
# MAGIC - Printed the result to the output.
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- SQL: Create and query a temporary table
# MAGIC CREATE OR REPLACE TEMP VIEW employee AS
# MAGIC SELECT * FROM VALUES
# MAGIC     ('Alice', 25, 50000),
# MAGIC     ('Bob', 30, 60000),
# MAGIC     ('Charlie', 35, 70000)
# MAGIC AS employees(Name, Age, Salary);
# MAGIC
# MAGIC -- Query the table
# MAGIC SELECT Name, Salary FROM employee WHERE Salary > 55000;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### SQL Code Explanation:
# MAGIC - Created a temporary table `employee` using the `CREATE OR REPLACE TEMP VIEW` command.
# MAGIC - Inserted sample data for employees (Name, Age, Salary).
# MAGIC - Queried the table to select employees with a salary greater than 55,000.
# MAGIC

# COMMAND ----------

# Python: Stop all active sessions to minimize costs
# This ensures you don't leave any expensive resources running
spark.catalog.clearCache()

