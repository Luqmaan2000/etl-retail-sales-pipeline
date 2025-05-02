# %%
import pandas as pd
import os



# Load the correct CSV path

csv_path = os.path.join("superstore-dataset-final", "Sample - Superstore.csv")
df = pd.read_csv(csv_path, encoding='latin1')

print("✅ CSV Loaded Successfully:")

# ------------ Transform Data -----------------
# %%
df.columns = [col.strip().lower().replace(" ","_") for col in df.columns]

# %%
# Removing null values

if df.isnull().values.any():
    raise ValueError("Dataset contains error values")
else:
    print("No missing values detected")


# %%
# Changing profits and sales to 2 decimal places

df['profit'] = df['profit'].round(2)
df['sales'] = df['sales'].round(2)

# %%
# Convert Dates + Engineer New Column

df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

## Delivery duration

df['delivery_days'] = (df['ship_date']-df['order_date'])


# %%
# Optimizing Data Types (Categorical Columns)

cat_cols = ['segment','country','region','city','sub-category','ship_mode','product_name']
for col in cat_cols:
    df[col] = df[col].astype('category')

print('Converted categorical columns into categories')

# %%
# Summary Stats
# Sales & Profit by Category
category_summary = df.groupby('category')[['sales','profit']].sum().sort_values(by='sales',ascending = False)
print("Total Sales and Profit by Category")
print(category_summary)

# Average Delivery Time By Region

delivery_by_region = df.groupby('region')['delivery_days'].mean().sort_values()
print('\n Average Time of Deliveries by Region')
print(delivery_by_region)

# Top 5 Sub Categories by Total Sales

top_subcats = df.groupby('sub-category')['sales'].sum().sort_values(ascending = False).head(5)
print('\n Top Sub Categories by Sales:')
print(top_subcats)

# ----------- Load Phase ------------------
# %%
import sqlite3

conn = sqlite3.connect("sales_data.db")

df.to_sql("sales",conn, index = False)


# %%

query = """
SELECT category, SUM(sales) as total_sales
From sales  
Group by category  
order by total_sales Desc
"""
result = pd.read_sql(query,conn)
print(result)
# %%
