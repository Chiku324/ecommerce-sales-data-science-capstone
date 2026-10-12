"""
E-commerce Sales Analysis Capstone
Dataset: synthetic demo data created for learning and portfolio practice.
Run: python analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "ecommerce_sales.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Order_Date"])
required = {"Order_ID", "Order_Date", "Product", "Category", "Region",
            "Sales_Channel", "Quantity", "Unit_Price_INR", "Revenue_INR"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")

# Basic data quality checks
df = df.drop_duplicates(subset=["Order_ID"])
df = df.dropna(subset=["Order_Date", "Product", "Quantity", "Revenue_INR"])
df = df[(df["Quantity"] > 0) & (df["Revenue_INR"] >= 0)]
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

summary = {
    "orders": int(df["Order_ID"].nunique()),
    "total_units": int(df["Quantity"].sum()),
    "total_revenue_inr": round(float(df["Revenue_INR"].sum()), 2),
    "average_order_revenue_inr": round(float(df.groupby("Order_ID")["Revenue_INR"].sum().mean()), 2),
    "date_start": str(df["Order_Date"].min().date()),
    "date_end": str(df["Order_Date"].max().date()),
}
pd.DataFrame([summary]).to_csv(OUT / "overall_summary.csv", index=False)
df.groupby("Category", as_index=False)["Revenue_INR"].sum().sort_values(
    "Revenue_INR", ascending=False
).to_csv(OUT / "revenue_by_category.csv", index=False)
df.groupby("Region", as_index=False)["Revenue_INR"].sum().sort_values(
    "Revenue_INR", ascending=False
).to_csv(OUT / "revenue_by_region.csv", index=False)
df.groupby("Sales_Channel", as_index=False)["Revenue_INR"].sum().sort_values(
    "Revenue_INR", ascending=False
).to_csv(OUT / "revenue_by_channel.csv", index=False)
df.groupby("Month", as_index=False)["Revenue_INR"].sum().sort_values(
    "Month"
).to_csv(OUT / "monthly_revenue.csv", index=False)
df.groupby("Product", as_index=False).agg(
    Revenue_INR=("Revenue_INR", "sum"),
    Units_Sold=("Quantity", "sum"),
    Orders=("Order_ID", "nunique")
).sort_values("Revenue_INR", ascending=False).to_csv(
    OUT / "product_performance.csv", index=False
)

# Save charts for README/report
monthly = df.groupby("Month")["Revenue_INR"].sum().sort_index()
plt.figure(figsize=(10, 5))
monthly.plot(marker="o")
plt.title("Monthly Revenue (INR)")
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUT / "monthly_revenue.png", dpi=160)
plt.close()

category = df.groupby("Category")["Revenue_INR"].sum().sort_values()
plt.figure(figsize=(8, 5))
category.plot(kind="barh")
plt.title("Revenue by Category")
plt.xlabel("Revenue (INR)")
plt.tight_layout()
plt.savefig(OUT / "revenue_by_category.png", dpi=160)
plt.close()

print("Analysis complete. Files saved in outputs/")
print(pd.DataFrame([summary]).to_string(index=False))
