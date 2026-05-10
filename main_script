/* ============================================================================
   PROJECT: E-Commerce Data Analysis Portfolio
   DATASET: bigquery-public-data.thelook_ecommerce
   AUTHOR: Noam Emilio Radetich
   
   DESCRIPTION:
   This script contains three core analytical models used to understand 
   user behavior, platform performance, and customer value:
   1. Cohort Analysis (User Retention)
   2. Funnel Analysis (Conversion Rates)
   3. RFM Segmentation (Customer Value)
============================================================================ */

/* ----------------------------------------------------------------------------
   1. COHORT ANALYSIS: Monthly Retention
   Goal: Measure the percentage of users who return to purchase in the months 
   following their first order.
---------------------------------------------------------------------------- */

WITH user_first_purchase AS (
  SELECT
    user_id,
    MIN(DATE(DATE_TRUNC(created_at, MONTH))) AS cohort_month
  FROM `bigquery-public-data.thelook_ecommerce.orders`
  WHERE status != 'Cancelled'
  GROUP BY 1
),

order_activities AS (
  SELECT
    o.user_id,
    f.cohort_month,
    DATE_TRUNC(o.created_at, MONTH) AS order_month,
    DATE_DIFF(DATE_TRUNC(DATE(o.created_at), MONTH), DATE(f.cohort_month), MONTH) AS month_number
  FROM `bigquery-public-data.thelook_ecommerce.orders` AS o
  JOIN user_first_purchase AS f 
    ON o.user_id = f.user_id
  WHERE o.status != 'Cancelled'
),

cohort_counts AS (
  SELECT
    cohort_month,
    month_number,
    COUNT(DISTINCT user_id) AS active_users
  FROM order_activities
  GROUP BY 1, 2
)

SELECT
  cohort_month,
  MAX(IF(month_number = 0, active_users, 0)) AS cohort_size,
  ROUND(SAFE_DIVIDE(MAX(IF(month_number = 1, active_users, 0)), MAX(IF(month_number = 0, active_users, 0))) * 100, 2) AS m1_retention_pct,
  ROUND(SAFE_DIVIDE(MAX(IF(month_number = 2, active_users, 0)), MAX(IF(month_number = 0, active_users, 0))) * 100, 2) AS m2_retention_pct,
  ROUND(SAFE_DIVIDE(MAX(IF(month_number = 3, active_users, 0)), MAX(IF(month_number = 0, active_users, 0))) * 100, 2) AS m3_retention_pct
FROM cohort_counts
GROUP BY 1
ORDER BY 1 DESC;

/* ----------------------------------------------------------------------------
   2. FUNNEL ANALYSIS: Web Conversion
   Goal: Identify the drop-off rate across the primary user journey from 
   viewing a product to completing a purchase.
---------------------------------------------------------------------------- */

WITH event_steps AS (
  SELECT
    session_id,
    MAX(IF(event_type = 'product', 1, 0)) AS saw_product,
    MAX(IF(event_type = 'cart', 1, 0)) AS added_to_cart,
    MAX(IF(event_type = 'purchase', 1, 0)) AS completed_purchase
  FROM `bigquery-public-data.thelook_ecommerce.events`
  GROUP BY 1
)

SELECT
  COUNT(*) AS total_sessions,
  SUM(saw_product) AS product_views,
  SUM(added_to_cart) AS cart_adds,
  SUM(completed_purchase) AS purchases,
  -- Step-by-Step Conversion Rates
  ROUND(SAFE_DIVIDE(SUM(added_to_cart), SUM(saw_product)) * 100, 2) AS view_to_cart_pct,
  ROUND(SAFE_DIVIDE(SUM(completed_purchase), SUM(added_to_cart)) * 100, 2) AS cart_to_purchase_pct,
  -- Overall Conversion Rate
  ROUND(SAFE_DIVIDE(SUM(completed_purchase), COUNT(*)) * 100, 2) AS overall_conversion_pct
FROM event_steps;

/* ----------------------------------------------------------------------------
   3. SEGMENTATION: RFM Analysis (Recency, Frequency, Monetary)
   Goal: Categorize customers based on their purchasing habits to identify 
   high-value segments and at-risk users.
---------------------------------------------------------------------------- */

WITH user_metrics AS (
  SELECT
    user_id,
    DATE_DIFF(CURRENT_DATE(), MAX(DATE(created_at)), DAY) AS recency,
    COUNT(DISTINCT order_id) AS frequency,
    SUM(sale_price) AS monetary
  FROM `bigquery-public-data.thelook_ecommerce.order_items`
  WHERE status NOT IN ('Cancelled', 'Returned')
  GROUP BY 1
),

rfm_scores AS (
  SELECT
    user_id,
    recency,
    frequency,
    monetary,
    -- Quartile scoring: 4 is best, 1 is worst
    NTILE(4) OVER (ORDER BY recency DESC) AS r_score, 
    NTILE(4) OVER (ORDER BY frequency ASC) AS f_score,
    NTILE(4) OVER (ORDER BY monetary ASC) AS m_score
  FROM user_metrics
)

SELECT
  user_id,
  recency,
  frequency,
  ROUND(monetary, 2) AS total_spend,
  (r_score + f_score + m_score) AS total_rfm_score,
  CASE
    WHEN (r_score + f_score + m_score) >= 10 THEN 'Champions'
    WHEN (r_score + f_score + m_score) >= 7 THEN 'Loyal Customers'
    WHEN (r_score + f_score + m_score) >= 4 THEN 'At Risk'
    ELSE 'Lost'
  END AS customer_segment
FROM rfm_scores
ORDER BY total_rfm_score DESC;
