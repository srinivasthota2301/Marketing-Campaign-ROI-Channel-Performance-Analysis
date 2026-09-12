# Marketing Campaign ROI & Channel Performance Analysis

## 📌 Project Overview

This project analyzes digital marketing campaign performance to understand how advertising spend translates into clicks, conversions, revenue, profit, and return on investment (ROI).

The project uses Python and Matplotlib for data exploration, data cleaning, feature engineering, and visualization.

The analysis focuses on identifying:

- Overall marketing performance
- Campaign ROI
- Channel performance
- Conversion efficiency
- Cost per conversion
- Revenue and profit performance
- High-performing and low-performing campaigns
- Monthly advertising performance

## 🎯 Project Objectives

The main objectives of this project are:

1. Explore the marketing campaign dataset.
2. Identify and validate data quality issues.
3. Clean and prepare the dataset for analysis.
4. Create meaningful marketing performance features.
5. Analyze campaign and channel-level performance.
6. Visualize important business KPIs.
7. Identify high-performing campaigns and marketing channels.
8. Support data-driven marketing decisions.

## 📊 Dataset

### Dataset Name

**Digital Advertising Campaign Performance Dataset**

### Source

Kaggle:

Digital Advertising Campaign Performance Dataset

### Dataset Size

- Original Rows: **10,000**
- Original Columns: **41**
- Final Rows: **10,000**
- Final Columns: **44**
- Primary Key: `campaign_id`
- Date Column: `start_date`
- Date Range: **01-01-2024 to 31-12-2025**

The dataset contains campaign-level information including:

- Campaign objective
- Platform
- Ad placement
- Device type
- Operating system
- Creative format
- Target audience
- Campaign date
- Impressions
- Clicks
- Conversions
- Advertising spend
- Revenue
- CTR
- CPC
- Conversion rate
- CPA
- ROAS
- Profit


## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Excel **
- **Power BI**
- **Git & GitHub**

## 📁 Project Structure

DA_PROJECT/
│
├── dataset/
│   ├── raw/
│   │   └── tech_advertising_campaigns_dataset.csv
│   │
│   └── processed/
│       └── marketing_clean.csv
│
├── source_code/
│   ├── cleaning.py
│   ├── feature_engineering.py
│   └── visualizations.py
│
├── reports/
│   ├── data_quality_report.docx
│   └── cleaning_log.xlsx
│
├── .venv/
│
├── requirements.txt
│
└── README.md