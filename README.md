# 📊 Sales Intelligence Dashboard

> **End-to-end Python Data Analytics Pipeline with Power BI Integration**  
> Built for enterprise-grade sales analysis, forecasting, and customer segmentation.

---

## 🚀 Project Highlights

| Feature | Technology |
|---|---|
| Synthetic Data Generation | `Faker`, `NumPy`, `Pandas` |
| Static Dashboards (5 charts) | `Matplotlib`, `Seaborn` |
| Interactive Dashboard | `Plotly` (HTML export) |
| Revenue Forecasting | `Scikit-learn` Linear Regression |
| Customer Segmentation | `K-Means Clustering` |
| Power BI Ready Export | Multi-sheet `.xlsx` data model |

---

## 📁 Project Structure

```
sales-intelligence-dashboard/
│
├── main.py                        # ← Run this first
├── requirements.txt
│
├── src/
│   ├── data_generator.py          # Generates 2000 sales + 500 customer records
│   ├── visualizations.py          # Matplotlib + Plotly dashboards
│   └── ml_analytics.py            # Forecasting + K-Means segmentation
│
├── data/                          # Auto-generated CSVs + Excel
│   ├── sales_data.csv
│   ├── customer_data.csv
│   ├── kpi_summary.csv
│   └── customer_segments.csv
│
├── reports/                       # Auto-generated charts
│   ├── 01_executive_dashboard.png
│   ├── 02_sales_deepdive.png
│   ├── 03_interactive_dashboard.html  ← Open in browser
│   ├── 04_revenue_forecast.png
│   └── 05_customer_segmentation.png
│
└── powerbi_exports/
    └── PowerBI_DataModel.xlsx     # 6-sheet data model for Power BI
```

---

## ⚙️ Setup & Run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/sales-intelligence-dashboard.git
cd sales-intelligence-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the full pipeline
python main.py
```

---

## 📈 Dashboards Generated

### 1. Executive KPI Overview
![Executive Dashboard](reports/01_executive_dashboard.png)

Key metrics: Revenue, Profit, Margin %, Win Rate, Monthly Trend, Category Heatmap, Channel Mix.

---

### 2. Sales Deep Dive
![Sales Deep Dive](reports/02_sales_deepdive.png)

Quarterly revenue, Revenue vs Profit scatter, Segment stacked bars, Discount impact analysis.

---

### 3. Interactive Plotly Dashboard
Open `reports/03_interactive_dashboard.html` in any browser for fully interactive charts with hover, zoom, and filter capabilities.

---

### 4. Revenue Forecasting (ML)
![Forecast](reports/04_revenue_forecast.png)

Linear regression trend with 6-month forward forecast and ±8% confidence bands.

---

### 5. Customer Segmentation (K-Means)
![Segmentation](reports/05_customer_segmentation.png)

4 distinct clusters: **Champions**, **Loyal**, **At Risk**, **New Prospects** — using Lifetime Value, Order Frequency, and Margin features.

---

## 🗂️ Power BI Integration

Import `powerbi_exports/PowerBI_DataModel.xlsx` directly into Power BI Desktop:

1. **Open Power BI Desktop**
2. **Get Data → Excel Workbook**
3. Select `PowerBI_DataModel.xlsx`
4. Load all 6 sheets: `fact_sales`, `dim_customer`, `agg_monthly`, `agg_category`, `agg_salesperson`, `kpi_summary`
5. Create relationships and build your custom visuals

### Suggested Power BI Visuals:
- Revenue KPI cards → `kpi_summary`
- Monthly line chart → `agg_monthly`
- Category matrix → `agg_category`
- Salesperson leaderboard → `agg_salesperson`
- Customer map → `dim_customer` (city field)

---

## 🧠 ML Models

### Revenue Forecasting
- Algorithm: Linear Regression
- Features: Time index (monthly)
- Output: 6-month revenue forecast with confidence band
- Metric: R², MAE

### Customer Segmentation
- Algorithm: K-Means (k=4, elbow-method validated)
- Features: Lifetime Value, Total Orders, Avg Order Value, Avg Margin, Returns
- Segments: Champions · Loyal · At Risk · New Prospects

---

## 🛠️ Tech Stack

```
Python 3.10+
├── Data       → Pandas, NumPy, Faker
├── Viz        → Matplotlib, Seaborn, Plotly
├── ML         → Scikit-learn
└── Export     → OpenPyXL, XlsxWriter
```

---

## 👤 Author

**[Your Name]**  
B.Tech — [Your Branch]  
[Your College Name]

---

*Built as part of the Celebal Technologies campus hiring process.*
