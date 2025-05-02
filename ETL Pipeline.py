# %%
import pandas as pd
import os



# Load the correct CSV path

csv_path = os.path.join("superstore-dataset-final", "Sample - Superstore.csv")
df = pd.read_csv(csv_path, encoding='latin1')

print("✅ CSV Loaded Successfully:")
df.head(2)


# Transform Data
# %%
df.columns = [col.strip().lower().replace(" ","_") for col in df.columns]
df.head(2)

# %%
# Removing null values

if df.isnull().values.any():
    raise ValueError("Dataset contains error values")
else:
    print("No missing values detected")


# %%
# Convert Dates + Engineer New Column

df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

## Delivery duration

df['delivery_days'] = (df['ship_date']-df['order_date'])

df[['order_date','ship_date','delivery_days']].head(2)

# %%
