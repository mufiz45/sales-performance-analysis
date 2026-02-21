import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/sales_data.csv")

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Extract Month
df["Month"] = df["Order_Date"].dt.to_period("M")

# Monthly Revenue
monthly_revenue = df.groupby("Month")["Revenue"].sum()

print("Monthly Revenue:")
print(monthly_revenue)

# Plot Monthly Revenue
monthly_revenue.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Product Performance
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

print("\nTop Performing Products:")
print(top_products)

# Region Performance
region_sales = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

print("\nRegion-wise Revenue:")
print(region_sales)
