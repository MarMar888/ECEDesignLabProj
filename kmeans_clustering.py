import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Read the data
df = pd.read_csv('PCA_ready.csv')

# Define categorical columns
categorical_cols = ['User Type', 'Material 1', 'Material 2', 'Select Printer', 'Printer Requested']

# Convert categorical variables to numerical using Label Encoding
label_encoders = {}
for col in categorical_cols:
    # Create a label encoder for each categorical column
    label_encoders[col] = LabelEncoder()
    
    # Fill missing values with 'missing' before encoding
    df[col] = df[col].fillna('missing')
    
    # Fit and transform the column
    df[col] = label_encoders[col].fit_transform(df[col])

# Handle missing values in numerical columns using median imputation
numerical_cols = ['Material 1 Qty', 'Material 2 Qty', 'Print Time (Hours)', 'Print Cost']
imputer = SimpleImputer(strategy='median')
df[numerical_cols] = imputer.fit_transform(df[numerical_cols])

# Scale all numerical features
scaler = StandardScaler()
all_features = categorical_cols + numerical_cols
df[all_features] = scaler.fit_transform(df[all_features])

# Perform K-means clustering
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[all_features])

# Print cluster sizes
print("\nCluster Sizes:")
print(df['Cluster'].value_counts().sort_index())

# Print characteristics of each cluster
print("\nCluster Characteristics:")
for cluster in range(5):
    print(f"\nCluster {cluster}:")
    cluster_data = df[df['Cluster'] == cluster]
    
    # Print statistics for all features
    print("\nFeature Statistics:")
    print(cluster_data[all_features].describe().round(2))

# Save results
df.to_csv('3D_Print_Jobs_clustered.csv', index=False)

# Print the mapping of encoded values for reference
print("\nEncoded Value Mappings:")
for col in categorical_cols:
    print(f"\n{col} mapping:")
    for i, label in enumerate(label_encoders[col].classes_):
        print(f"{label}: {i}") 