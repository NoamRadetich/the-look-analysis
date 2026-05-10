import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
df = pd.read_csv('cohort_results.csv')

# 2. Data Preparation
df['cohort_month'] = pd.to_datetime(df['cohort_month'])
df = df.sort_values('cohort_month')

# Standard cohort charts usually start with a 'Month 0' (100% retention)
df['m0_retention_pct'] = 100.0

# We'll take the most recent 15 months to keep the heatmap clean and readable
plot_df = df.tail(15).copy()

# 3. Pivot/Prepare for Heatmap
# We select Month 0 through Month 3 retention percentages
heatmap_data = plot_df.set_index('cohort_month')[['m0_retention_pct', 'm1_retention_pct', 'm2_retention_pct', 'm3_retention_pct']]
heatmap_data.columns = ['Month 0', 'Month 1', 'Month 2', 'Month 3']
heatmap_data.index = heatmap_data.index.strftime('%Y-%m')

# 4. Plot
plt.figure(figsize=(12, 8))
sns.set_theme(style="white")

ax = sns.heatmap(heatmap_data, 
                 annot=True,     
                 fmt=".1f",     
                 cmap="YlGnBu",  
                 linewidths=.5, 
                 cbar_kws={'label': 'Retention Rate (%)'})

# 5. Polishing
plt.title('Cohort Analysis: Monthly User Retention (%)', fontsize=16, pad=20)
plt.xlabel('Months Since First Purchase', fontsize=12)
plt.ylabel('Cohort Birth Month', fontsize=12)

plt.tight_layout()
plt.savefig('cohort_retention_heatmap.png', dpi=300)
