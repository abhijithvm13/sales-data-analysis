import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("sales.csv")

print(df)

print("\nFirst 5 rows: \n",df.head())

print("\nDataset info:")
print(df.info())

print("\n Columns name: ",df.columns)


# Data Cleaning & Preparation


#removing duplicate values
df=df.drop_duplicates()

#check missing values
print("Missing values:\n",df.isnull().sum())

# Convert Date column to datetime
df["Date"]=pd.to_datetime(df["Date"])

# Create Revenue column
df["Revenue"]=df["Price"]*df["Quantity"]

print("\nCleaned Data:\n",df.head())

# Data Analysis

# Total Revenue
total_revenue=df["Revenue"].sum()
print("\n Total revenue:",total_revenue)

# Category-wise revenue
category_revenue=df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
print("\nCategory wise Revenue:",category_revenue)

#Region-wise revenue
region_revenue=df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print("\nRegion wise Revenue:",region_revenue)

# Product-wise revenue
product_revenue=df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print("\nProduct wise Revenue:",product_revenue)

# ****Visualization****

# Category-wise revenue
# This helps to understand which category contributes the most

category_revenue.plot(kind="bar",color="skyblue",edgecolor="black")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()

# Top 5 products based on revenue
# Using horizontal bar for better readability

top5=product_revenue.head(5).plot(kind="barh", color="lightgreen", ec="black")
plt.title("Top 5 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.grid(True)
plt.tight_layout()
plt.show()

# Region-wise revenue
region_revenue.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()

# Sales trend over time
daily_sales=df.groupby("Date")["Revenue"].sum()

daily_sales.plot(marker="o")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()


print("\n--- Key Insights ---")
print("1. Total revenue generated:", total_revenue)
print("2. Highest revenue category:", category_revenue.idxmax())
print("3. Best performing region:", region_revenue.idxmax())
print("4. Top selling product by revenue:", product_revenue.idxmax())






