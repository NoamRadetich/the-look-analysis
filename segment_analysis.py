import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load and Clean Data
df_rfm = pd.read_csv('rfm_results.csv')

if df_rfm['total_spend'].dtype == 'object':
    df_rfm['total_spend'] = df_rfm['total_spend'].str.replace(',', '').astype(float)

# Define the order of segments 
segment_order = ['Champions', 'Loyal Customers', 'At Risk', 'Lost']

# 2. Visual 1: Distribution of Segments (Volume)
plt.figure(figsize=(10, 6))
sns.countplot(data=df_rfm, x='customer_segment', order=segment_order, palette='viridis')
plt.title('Distribution of Customer Segments', fontsize=15)
plt.ylabel('Number of Adventurers (Users)')
plt.show()

# 3. Visual 2: Average Total Spend per Segment (Value)
plt.figure(figsize=(10, 6))
sns.barplot(data=df_rfm, x='customer_segment', y='total_spend', order=segment_order, palette='magma')
plt.title('Average Total Spend per Segment', fontsize=15)
plt.ylabel('Average Spend ($)')
plt.show()

# 4. Visual 3: Recency vs Frequency (Behavior)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_rfm, x='recency', y='frequency', hue='customer_segment', 
                hue_order=segment_order, palette='viridis', alpha=0.5)
plt.title('Recency vs Frequency by Segment', fontsize=15)
plt.xlabel('Days Since Last Order (Recency)')
plt.ylabel('Total Orders (Frequency)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
