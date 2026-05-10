# The Look E-Commerce Analysis

A comprehensive data analysis project using Google BigQuery to extract actionable business insights from The Look—a fictional e-commerce platform. This portfolio project demonstrates end-to-end analytics capabilities including cohort analysis, funnel analysis, and customer segmentation.

## 📊 Project Overview

This project analyzes e-commerce user behavior and business performance using BigQuery's public dataset (`bigquery-public-data.thelook_ecommerce`). The analysis focuses on three core analytical models:

1. **Cohort Analysis** — User retention trends across monthly cohorts
2. **Funnel Analysis** — Conversion rates through the customer journey
3. **RFM Segmentation** — Customer value and risk profiling

## 🎯 Key Insights

### Cohort Analysis: Monthly User Retention

![Cohort Retention Heatmap](cohort_retention_heatmap.png)

**What it shows:**
- Each row represents a cohort (users who made their first purchase in that month)
- Each column represents months elapsed since first purchase (Month 0 through Month 3)
- Cell values show the percentage of users who returned to purchase in each subsequent month

**Key takeaway:**
The retention heatmap reveals user stickiness patterns and helps identify if newer cohorts have stronger or weaker retention compared to historical cohorts. This metric is critical for understanding customer lifetime value and the effectiveness of customer retention strategies.

## 🛠️ Skills & Technical Value

### Analytics & SQL Expertise
- **Complex SQL Queries**: Window functions (NTILE), date manipulation, aggregations with CTEs
- **BigQuery Optimization**: Efficient query design for large-scale data processing
- **Data Modeling**: Creating meaningful metrics (cohort_month, retention_pct, RFM scores)

### Python Data Visualization
- **Pandas**: Data transformation, pivoting, and manipulation
- **Seaborn & Matplotlib**: Professional heatmap creation with customization
- **Reproducible Analytics**: Automated pipeline from SQL to visualization

### Business Acumen
- **Cohort Analysis**: Measure user retention and identify retention trends
- **Funnel Analysis**: Diagnose conversion bottlenecks in the customer journey
- **RFM Segmentation**: Classify customers by recency, frequency, and monetary value for targeted campaigns
- **Metrics Design**: Creating KPIs that drive business decisions

### Portfolio Perspective
This project demonstrates:
✅ **End-to-End Analytics**: From raw data to actionable insights  
✅ **Cross-Platform Proficiency**: SQL (BigQuery) + Python (Pandas, visualization)  
✅ **Business Impact**: Metrics designed to inform real business decisions  
✅ **Scalable Architecture**: Working with large datasets efficiently  
✅ **Professional Presentation**: Clear visualizations and documentation  

## 📁 Project Structure

```
the-look-analysis/
├── main_script.sql              # Core SQL queries (Cohort, Funnel, RFM analysis)
├── cohort_analysis.py           # Python script for cohort heatmap visualization
├── cohort_results.csv           # Cohort analysis output data
├── cohort_retention_heatmap.png # Visualization of monthly retention trends
└── README.md                    # This file
```

## 🚀 How to Use

### Prerequisites
- Google BigQuery access (with `bigquery-public-data.thelook_ecommerce` dataset)
- Python 3.7+
- Required libraries: `pandas`, `matplotlib`, `seaborn`

### Step 1: Run SQL Queries
Execute `main_script.sql` in BigQuery to generate the analytical tables. Export the cohort analysis results as `cohort_results.csv`.

### Step 2: Generate Visualizations
```bash
python cohort_analysis.py
```

This creates `cohort_retention_heatmap.png` showing retention trends across monthly cohorts.

## 📈 Key Metrics Explained

### Cohort Analysis
- **Cohort Size**: Number of unique users making their first purchase in a given month
- **M1 Retention %**: % of cohort users who returned in Month 1
- **M2 Retention %**: % of cohort users who returned in Month 2
- **M3 Retention %**: % of cohort users who returned in Month 3

### Funnel Analysis
- **View to Cart Conversion**: % of product viewers who add items to cart
- **Cart to Purchase Conversion**: % of cart users who complete a purchase
- **Overall Conversion**: % of sessions resulting in a purchase

### RFM Segmentation
- **Recency**: Days since last purchase (lower is better)
- **Frequency**: Total number of purchases
- **Monetary**: Total spend
- **Segments**: Champions, Loyal Customers, At Risk, Lost

## 💡 Business Applications

- **Retention Strategy**: Identify weak cohorts and implement targeted engagement campaigns
- **Funnel Optimization**: Detect conversion bottlenecks and prioritize improvements
- **Marketing Allocation**: Focus resources on high-value customer segments
- **Product Development**: Use cohort insights to inform feature decisions

## 🔗 Data Source

Dataset: `bigquery-public-data.thelook_ecommerce`  
Tables Used:
- `orders` — Transaction records
- `events` — Session-level user events
- `order_items` — Item-level purchase details

---

**Created by:** Noam Emilio Radetich  
**Last Updated:** 2026-05-10  
**Portfolio Project:** E-Commerce Analytics
