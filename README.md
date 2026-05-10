# The Look E-Commerce Analysis

A comprehensive data analysis project using Google BigQuery to extract actionable business insights from The Look—a fictional e-commerce platform. This portfolio project demonstrates end-to-end analytics across three core models: cohort retention, conversion funnel, and customer segmentation (RFM).

## 📊 Project Overview

This project analyzes e-commerce user behavior and business performance using BigQuery's public dataset (`bigquery-public-data.thelook_ecommerce`). The analysis focuses on three core analytical models:

1. **Cohort Analysis** — User retention trends across monthly cohorts
2. **Funnel Analysis** — Conversion rates through the customer journey
3. **RFM Segmentation** — Customer value and risk profiling

## 🎯 Key Insights

### Cohort Analysis: Monthly User Retention

![Cohort Retention Heatmap](https://github.com/NoamRadetich/the-look-analysis/blob/main/cohort_retention_heatmap.png)

**What it shows:**
- Each row represents a cohort (users who made their first purchase in that month)
- Each column represents months elapsed since first purchase (Month 0 through Month 3)
- Cell values show the percentage of users who returned to purchase in each subsequent month

**Key takeaway:**
The retention heatmap reveals user stickiness patterns and helps identify if newer cohorts have stronger or weaker retention compared to historical cohorts. This metric is critical for understanding customer lifecycle dynamics and predicting long-term business viability.

---

### RFM Analysis: Customer Segmentation

#### Executive Summary

The RFM model categorizes the customer base into four distinct segments based on purchasing behavior (Recency, Frequency, Monetary value). This segmentation enables targeted marketing strategies and optimized resource allocation across 66,030 unique customers.

#### 1. Segment Distribution & Volume

![Customer Segment Distribution](https://github.com/NoamRadetich/the-look-analysis/blob/main/segment_distribution.png)

The analysis reveals a healthy distribution with clear business implications:

- **Champions**: A small but elite group of high-value, recently-active users
- **Loyal Customers**: Represent the core of the active user base, providing consistent transaction volume
- **At Risk**: A significant portion of the database that has not engaged in over 6–12 months, requiring immediate attention
- **Lost**: Users with minimal recent activity, representing natural churn

#### 2. Monetary Value Analysis

![Average Spend by Segment](https://github.com/NoamRadetich/the-look-analysis/blob/main/spend_by_segment.png)

There is a stark contrast in lifetime value (LTV) across segments:

- **High-Value Contribution**: The "Champions" segment accounts for a disproportionately high percentage of total revenue, with a single customer spending nearly **3x more** than a "Loyal Customer"
- **Revenue Growth Opportunity**: Moving "Loyal Customers" into the "Champions" tier through upselling and retention initiatives could significantly impact the bottom line
- **Cost-Benefit Reality**: The "Lost" segment has minimal value recovery potential; resources are better directed elsewhere

#### 3. Behavioral Insights: Recency vs. Frequency

![Recency vs. Frequency by Segment](https://github.com/NoamRadetich/the-look-analysis/blob/main/recency_frequency_scatter.png)

The scatter plot analysis highlights clear behavioral boundaries:

- **Engagement Decay**: The "At Risk" and "Lost" segments show a clear drift toward high recency values (1,000+ days since last purchase). Once a user stops engaging for more than a year, the likelihood of spontaneous return is near zero.
- **Purchase Velocity**: "Champions" are characterized not just by high spend, but by a high frequency of orders within a short time window (low recency <30 days)
- **Frequency Ceiling**: "Lost" customers averaged 3–5 purchases before disengaging, suggesting either product-market fit issues or external lifecycle factors

#### Strategic Recommendations

| Segment | Strategic Action | Objective | Expected Impact |
|---------|-----------------|-----------|-----------------|
| **Champions** | Exclusive Rewards / Early Access / VIP Program | Maintain high engagement and reward brand advocacy | Retain top 5% of revenue |
| **Loyal Customers** | Cross-selling / Tiered Loyalty Programs / Exclusive Discounts | Increase average order value (AOV) and purchase frequency | Move 10–20% into Champions tier |
| **At Risk** | Re-engagement Campaigns / "Win-back" Discounts / Personalized Offers | Prevent churn by providing high-incentive reasons to return | Recover 5–10% of revenue from lapsed customers |
| **Lost** | Minimal Spend / Re-activation Research / Automated Email | Accept as natural churn; focus on low-cost outreach | Reduce acquisition cost; focus on new CAC |

---

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
- **Strategic Planning**: Translating data insights into actionable business recommendations
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
├── main_script.sql                  # Core SQL queries (Cohort, Funnel, RFM analysis)
├── cohort_analysis.py               # Python script for cohort heatmap visualization
├── segment_analysis.py              # Python script for RFM segment visualizations
├── cohort_results.csv               # Cohort analysis output data
├── rfm_results.csv                  # RFM analysis output data
├── cohort_retention_heatmap.png     # Visualization of monthly retention trends
├── segment_distribution.png         # Visualization of customer segment volume
├── spend_by_segment.png             # Visualization of average spend per segment
├── recency_frequency_scatter.png    # Scatter plot of behavior patterns
└── README.md                        # This file
```

## 🚀 How to Use

### Prerequisites
- Google BigQuery access (with `bigquery-public-data.thelook_ecommerce` dataset)
- Python 3.7+
- Required libraries: `pandas`, `matplotlib`, `seaborn`

### Step 1: Run SQL Queries
Execute `main_script.sql` in BigQuery to generate the analytical tables:
- Export cohort analysis results as `cohort_results.csv`
- Export RFM analysis results as `rfm_results.csv`

### Step 2: Generate Cohort Visualizations
```bash
python cohort_analysis.py
```
This creates `cohort_retention_heatmap.png` showing retention trends across monthly cohorts.

### Step 3: Generate RFM Segment Visualizations
```bash
python segment_analysis.py
```
This creates three visualizations:
- `segment_distribution.png` — Distribution of customer segments by volume
- `spend_by_segment.png` — Average lifetime value per segment
- `recency_frequency_scatter.png` — Behavioral analysis of recency vs. frequency

## 📈 Key Metrics Explained

### Cohort Analysis
- **Cohort Size**: Number of unique users making their first purchase in a given month
- **M0 Retention %**: Baseline cohort (100%)
- **M1 Retention %**: % of cohort users who returned in Month 1
- **M2 Retention %**: % of cohort users who returned in Month 2
- **M3 Retention %**: % of cohort users who returned in Month 3

### Funnel Analysis
- **View to Cart Conversion**: % of product viewers who add items to cart
- **Cart to Purchase Conversion**: % of cart users who complete a purchase
- **Overall Conversion Rate**: % of sessions resulting in a purchase

### RFM Segmentation
- **Recency (R)**: Days since last purchase (lower is better; 4 is best, 1 is worst)
- **Frequency (F)**: Total number of purchases (higher is better; 4 is best, 1 is worst)
- **Monetary (M)**: Total lifetime spend in dollars (higher is better; 4 is best, 1 is worst)
- **RFM Score**: Sum of R, F, M quartile scores (range: 3–12)
- **Segments**:
  - **Champions** (RFM Score ≥ 10): Elite customers, high recent activity, high spend
  - **Loyal Customers** (RFM Score 7–9): Core user base, consistent activity
  - **At Risk** (RFM Score 4–6): Declining engagement, churned in 6–12 months
  - **Lost** (RFM Score ≤ 3): Minimal recent activity, low recovery potential

## 💡 Business Applications

- **Retention Strategy**: Identify weak cohorts and implement targeted engagement campaigns
- **Funnel Optimization**: Detect conversion bottlenecks and prioritize improvements
- **Marketing Allocation**: Focus resources on high-value customer segments based on RFM scores
- **Customer Lifetime Value**: Predict future revenue contributions by segment
- **Campaign Personalization**: Tailor messaging and offers based on segment behavior
- **Product Development**: Use cohort and funnel insights to inform feature decisions
- **Risk Management**: Proactively identify at-risk customers and deploy win-back strategies

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
