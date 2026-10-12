# E-commerce Sales Analysis — Data Science Capstone

## Project overview
This beginner-friendly capstone analyzes order-level e-commerce sales to understand revenue patterns by month, product category, region, and sales channel. It demonstrates data cleaning, exploratory data analysis (EDA), aggregation, visualization, and evidence-based recommendations.

**Important:** `ecommerce_sales.csv` is a synthetic practice dataset generated for this portfolio project. It is not real company/customer data and should not be presented as real business evidence.

## Questions explored
1. What is total revenue and how many units were sold?
2. Which product categories and products contribute the most revenue?
3. How does revenue vary by month?
4. Which regions and sales channels generate the most revenue?
5. What practical business actions could be tested based on these patterns?

## Tools
- Python
- pandas
- matplotlib
- CSV data

## Project structure
- `ecommerce_sales.csv` — sample order data
- `analysis.py` — data validation, cleaning, analysis, exports, and charts
- `report.docx` — written capstone report
- `requirements.txt` — Python dependencies
- `outputs/` — generated summary CSVs and chart images (created after running the script)

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python analysis.py`
5. Open the `outputs` folder to inspect the results.

## Data dictionary
- `Order_ID`: unique order-line identifier
- `Order_Date`: date of the order
- `Product`: product name
- `Category`: product category
- `Region`: broad sales region
- `Sales_Channel`: sales platform
- `Quantity`: units purchased
- `Unit_Price_INR`: listed unit price before discount
- `Discount_Rate`: discount fraction
- `Revenue_INR`: quantity multiplied by discounted unit price

## Methodology
The script checks required columns, removes duplicate order IDs, removes rows missing key fields, filters invalid quantities/revenue, and then summarizes revenue across dimensions. Charts are saved to `outputs/`.

## Limitations and next steps
The data is synthetic and intentionally small, so findings are illustrative rather than business-validated. A next version could use a verified public dataset, include product costs and profit, add customer cohorts, create an interactive Power BI dashboard, or evaluate a forecasting model using a time-based train/test split.

## Portfolio note
When publishing, state clearly that this is a learning project using synthetic data. Do not claim the results came from a real company.
