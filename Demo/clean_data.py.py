import pandas as pd

# Load messy data
df = pd.read_csv("Dirty_Sales_Data.csv")

# Clean data
df = df.drop_duplicates()
df['customer'] = df['customer'].str.title()
df['order_date'] = pd.to_datetime(df['order_date'])
df['price_usd'] = df['price'].replace('[₹,k]', '', regex=True).astype(float)

# Save clean data
df.to_csv("Clean_Sales_Data.csv", index=False)
print("✅ Data cleaned successfully!")