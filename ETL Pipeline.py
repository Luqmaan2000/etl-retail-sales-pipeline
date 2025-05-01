import pandas as pd
import os

# Load the correct CSV path

csv_path = os.path.join("superstore-dataset-final", "Sample - Superstore.csv")
df = pd.read_csv(csv_path, encoding='latin1')

print("✅ CSV Loaded Successfully:")
print(df.head())
