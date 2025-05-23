# ETL Pipeline Retail Project
 
 This project demonstrates end-to-end ETL pipeline using Python and SQLite on a retail dataset from kaggle. It includes:

 - Automating dataset download using the Kaggle API
 - Extracting and loading CSV data
 - Handling file encoding issues
 - Preparing for data cleaning and transformation

 ## Progress Log
 - [x] Connected to Kaggle API and downloaded dataset
 - [x] Extracted dataset into dataframe using pandas with encoding fix
 - [x] Loading into SQLite database

 ## Transformation Process Completed
 - Cleaned column names (snake_case)
 - Verified dataset has no missing values
 - Converted order_date and ship_date to datetime
 - Created delivery_days and profit_margin columns
 - Optimized categorical columns using pandas `category` dtype
 - Ran grouped summary stats:
  - Total sales and profit by category
  - Average delivery days by region
  - Top 5 sub-categories by sales

## ✅ Load Phase

- Created a local SQLite database file: `sales_data.db`
- Loaded the transformed pandas DataFrame into a SQL table named `sales`
- Ran SQL queries using `pandas.read_sql()` to validate and analyze:
  - Total sales by category
  - Verified successful data load