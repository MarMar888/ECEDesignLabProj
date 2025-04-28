import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Read the data
df = pd.read_csv('cleaned_dataset.csv')

# Select features for clustering
features = ['Print Time (Hours)', 'Material 1 Qty', 'Print Cost']

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[features])

# Perform K-means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# Calculate statistics for each cluster
cluster_stats = df.groupby('Cluster')['Print Time (Hours)'].agg(['mean', 'std', 'median', 'min', 'max']).round(2)

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Box plot
sns.boxplot(x='Cluster', y='Print Time (Hours)', data=df, ax=ax1)
ax1.set_title('Print Time Distribution by Cluster')
ax1.set_xlabel('Cluster')
ax1.set_ylabel('Print Time (Hours)')

# Bar plot of means with error bars
ax2.bar(cluster_stats.index, cluster_stats['mean'], 
        yerr=cluster_stats['std'], 
        capsize=5, 
        color='skyblue')
ax2.set_title('Average Print Time by Cluster')
ax2.set_xlabel('Cluster')
ax2.set_ylabel('Average Print Time (Hours)')

# Add text annotations for statistics
for i, (mean, std, median, min_val, max_val) in enumerate(zip(
    cluster_stats['mean'], 
    cluster_stats['std'], 
    cluster_stats['median'],
    cluster_stats['min'],
    cluster_stats['max']
)):
    stats_text = f'Mean: {mean:.2f}\nStd: {std:.2f}\nMedian: {median:.2f}\nMin: {min_val:.2f}\nMax: {max_val:.2f}'
    ax2.text(i, mean + std + 1, stats_text, ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig('print_time_by_cluster.png', dpi=300, bbox_inches='tight')
plt.show()

# Print cluster sizes
print("\nCluster Sizes:")
print(df['Cluster'].value_counts().sort_index()) 