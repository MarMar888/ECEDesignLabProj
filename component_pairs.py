import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# Read the data
df = pd.read_csv('cleaned.csv')

# Select numeric columns for PCA
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
X = df[numeric_cols]

# Apply PCA
pca = PCA()
X_pca = pca.fit_transform(X)

# Create a DataFrame with PCA components
n_components = X_pca.shape[1]
pca_df = pd.DataFrame(X_pca, columns=[f'PC{i+1}' for i in range(n_components)])
pca_df['Cluster'] = df['Cluster']  # Add cluster information if available

# Create a grid of scatter plots
plt.figure(figsize=(20, 20))
for i in range(n_components):
    for j in range(n_components):
        if i != j:  # Don't plot components against themselves
            plt.subplot(n_components, n_components, i * n_components + j + 1)
            scatter = plt.scatter(pca_df[f'PC{j+1}'], pca_df[f'PC{i+1}'], 
                                c=pca_df['Cluster'], cmap='viridis', alpha=0.6)
            plt.xlabel(f'PC{j+1}')
            plt.ylabel(f'PC{i+1}')
            
            # Add variance explained in title
            var_explained = pca.explained_variance_ratio_
            plt.title(f'Var: {var_explained[j]:.2%}, {var_explained[i]:.2%}', fontsize=8)

# Add a colorbar
plt.subplot(n_components, n_components, n_components * n_components)
plt.colorbar(scatter, label='Cluster')
plt.axis('off')

plt.tight_layout()
plt.savefig('component_pairs.png', dpi=300, bbox_inches='tight')
plt.show()

# Print explained variance for each component
print("\nExplained Variance Ratio for each component:")
for i, ratio in enumerate(pca.explained_variance_ratio_):
    print(f"PC{i+1}: {ratio:.2%}") 