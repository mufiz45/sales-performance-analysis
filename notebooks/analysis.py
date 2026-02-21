import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/sales_data.csv")

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Calculate Profit
df["Profit"] = df["Revenue"] - df["Cost"]

# Calculate Profit Margin (%)
df["Profit_Margin"] = (df["Profit"] / df["Revenue"]) * 100

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

# Monthly Profit
monthly_profit = df.groupby("Month")["Profit"].sum()

print("\nMonthly Profit:")
print(monthly_profit)

# Most Profitable Products
profit_by_product = df.groupby("Product")["Profit"].sum().sort_values(ascending=False)

print("\nMost Profitable Products:")
print(profit_by_product)

# Highest Margin Products
margin_by_product = df.groupby("Product")["Profit_Margin"].mean().sort_values(ascending=False)

print("\nHighest Average Profit Margin Products:")
print(margin_by_product)

# Product Performance
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

print("\nTop Performing Products:")
print(top_products)

# Region Performance
region_sales = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

print("\nRegion-wise Revenue:")
print(region_sales)
