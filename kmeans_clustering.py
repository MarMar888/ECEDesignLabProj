import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer

# Read the data
df = pd.read_csv('3D_Print_Jobs_cleaned.csv')

# Define categorical and numerical columns
categorical_cols = ['User Type', 'Material 1', 'Material 2', 'Select Printer', 'Printer Requested']
numerical_cols = ['Material 1 Qty', 'Material 2 Qty', 'Print Time (Hours)', 'Print Cost']

# Create preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]), numerical_cols),
        ('cat', Pipeline([
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ]), categorical_cols)
    ])

# Create full pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('clusterer', KMeans(n_clusters=5, random_state=42))
])

# Fit the pipeline
pipeline.fit(df)

# Get cluster labels
cluster_labels = pipeline.named_steps['clusterer'].labels_

# Add cluster labels to original dataframe
df['Cluster'] = cluster_labels

# Print cluster sizes
print("\nCluster Sizes:")
print(df['Cluster'].value_counts().sort_index())

# Print characteristics of each cluster
print("\nCluster Characteristics:")
for cluster in range(5):
    print(f"\nCluster {cluster}:")
    cluster_data = df[df['Cluster'] == cluster]
    
    # Print most common values for categorical columns
    for col in categorical_cols:
        print(f"\nMost common {col}:")
        print(cluster_data[col].value_counts().head(3))
    
    # Print statistics for numerical columns
    print("\nNumerical Statistics:")
    print(cluster_data[numerical_cols].describe().round(2))

# Save results
df.to_csv('3D_Print_Jobs_clustered.csv', index=False) 