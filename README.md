# End-to-End Sales Analytics

A comprehensive sales analytics project for data-driven insights and reporting.

## Project Structure

```
end-to-end-sales-analytics/
├── data/
│   ├── raw/          # Original, unmodified data files
│   └── processed/    # Cleaned and transformed datasets
├── notebooks/        # Jupyter notebooks for exploration and analysis
├── src/             # Python modules and reusable code
├── dashboard/       # Dashboard application files
└── outputs/         # Generated reports, visualizations, and results
```

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Add your raw data to `data/raw/`
4. Run analysis notebooks in `notebooks/`

## Technologies

- Python
- Pandas
- Jupyter Notebook
- Data Visualization (Matplotlib, Seaborn, Plotly)

# 📊 Sales Performance Analysis Dashboard

## 🧾 Project Overview

This project analyzes historical sales data to uncover key business insights related to revenue, profit, growth trends, product performance, and regional contribution.

The goal of this analysis is to:
- Identify top-performing products and categories
- Understand regional and city-wise sales distribution
- Analyze profitability trends
- Detect low-profit products
- Track sales growth over the years

This project includes data cleaning, feature engineering, exploratory data analysis (EDA), and dashboard visualization.

---

## 📂 Dataset Information

The dataset contains transactional sales data including:

- Order Date
- Ship Date
- City
- Region
- Category
- Product Name
- Sales
- Profit
- Quantity

### 🛠 Data Cleaning & Feature Engineering

The following steps were performed:

- Converted Order Date and Ship Date to datetime format
- Removed duplicate records
- Created Shipping Duration (Ship Date – Order Date)
- Extracted Year, Month, and Day from Order Date
- Exported cleaned dataset for analysis

---

## 🧰 Tools & Technologies Used

- Python (Pandas, Matplotlib, Seaborn)
- Power BI
- Jupyter Notebook
- Git & GitHub

---

## 📈 Key Performance Indicators (KPIs)

| Metric | Value |
|--------|--------|
| 💰 Total Sales | 2.30M |
| 📈 Total Profit | 286K+ |
| 📦 Total Quantity Sold | 38K |
| 📊 Overall Profit Margin | 12.47% |

---

## 📊 Dashboard Insights

### 1️⃣ Sales by City
- Highest sales concentration observed in North America
- Strong sales presence in major U.S. cities
- Limited but growing international presence

---

### 2️⃣ Monthly Sales Trend
- Noticeable seasonal growth
- Significant spike in November and December
- Lowest sales observed in February

📌 Indicates strong year-end demand (holiday effect)

---

### 3️⃣ Sales Growth Over Years
- Consistent upward trend from 2014 to 2017
- Strong growth observed in 2016 and 2017

📌 Business demonstrates steady expansion

---

### 4️⃣ Sales by Category
- Technology generates the highest revenue
- Furniture and Office Supplies contribute moderate sales

📌 Technology is the primary revenue driver

---

### 5️⃣ Profit by Region
- West region generates highest profit
- East follows closely
- Central and South underperform comparatively

📌 Regional strategy optimization opportunity

---

### 6️⃣ Profit Margin by Category
- Technology and Office Supplies maintain healthy margins
- Furniture shows lower profit margin

📌 Cost optimization required in Furniture category

---

### 7️⃣ High Profit Products
Top contributors:
- Canon imageCLASS series
- Fellowes Electronics
- Hewlett Packard products

📌 These products should be prioritized in marketing campaigns

---

### 8️⃣ Low Profit Products
Certain products generate negative profit:
- Cubify CubeX 3D Printer
- Lexmark printers
- Some furniture items

📌 Recommendation:
- Reevaluate pricing strategy
- Reduce discount levels
- Consider discontinuation

---

## 🖼 Dashboard Preview

![Dashboard Preview](images/dashboard_preview.png)

---
## 💡 Business Recommendations

1. Increase marketing spend on Technology products
2. Review pricing strategy for low-margin Furniture products
3. Focus expansion in high-performing West region
4. Optimize supply chain to reduce shipping duration
5. Investigate loss-making SKUs
---

## 📌 Conclusion

This analysis demonstrates how data-driven decision-making can improve revenue growth, optimize profitability, and identify operational inefficiencies.

The dashboard provides actionable insights that can support strategic planning and business expansion.

---

## 👨‍💻 Author

**Gaurav Singh Rathore**  
Engineering Student | Aspiring Data Analyst | Entrepreneur  


