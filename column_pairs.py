import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv('cleaned.csv')

# Select the columns we want to plot
columns_to_plot = ['Printer Requested', 'Material 1 Qty', 'User Type', 
                  'Print Time (Hours)', 'Material_Category1', 'Cluster']

# Create a grid of scatter plots
n_cols = len(columns_to_plot)
plt.figure(figsize=(20, 20))

for i, col1 in enumerate(columns_to_plot):
    for j, col2 in enumerate(columns_to_plot):
        if i != j:  # Don't plot columns against themselves
            plt.subplot(n_cols, n_cols, i * n_cols + j + 1)
            
            # Check if both columns are numeric
            if pd.api.types.is_numeric_dtype(df[col1]) and pd.api.types.is_numeric_dtype(df[col2]):
                scatter = plt.scatter(df[col2], df[col1], 
                                    c=df['Cluster'], cmap='viridis', alpha=0.6)
            else:
                # For categorical columns, use a different plot type
                if pd.api.types.is_numeric_dtype(df[col1]):
                    sns.boxplot(x=df[col2], y=df[col1])
                elif pd.api.types.is_numeric_dtype(df[col2]):
                    sns.boxplot(x=df[col1], y=df[col2])
                else:
                    # For two categorical columns, use a count plot
                    sns.countplot(x=df[col1], hue=df[col2])
            
            plt.xlabel(col2)
            plt.ylabel(col1)
            plt.xticks(rotation=45, ha='right')

# Add a colorbar for the scatter plots
plt.subplot(n_cols, n_cols, n_cols * n_cols)
plt.colorbar(scatter, label='Cluster')
plt.axis('off')

plt.tight_layout()
plt.savefig('column_pairs.png', dpi=300, bbox_inches='tight')
plt.show() 