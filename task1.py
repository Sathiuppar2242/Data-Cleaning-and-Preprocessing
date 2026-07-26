import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
# Load Dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Display first 5 rows
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df['Cabin'].fillna("Unknown", inplace=True)

# Verify missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Encode categorical columns
encoder = LabelEncoder()

df['Sex'] = encoder.fit_transform(df['Sex'])
df['Embarked'] = encoder.fit_transform(df['Embarked'])
df['Cabin'] = encoder.fit_transform(df['Cabin'])

print("\nEncoded Data:")
print(df.head())

# Standardize numerical columns
scaler = StandardScaler()

numerical_columns = ['Age', 'Fare']

df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

print("\nStandardized Data:")
print(df[['Age', 'Fare']].head())

# Visualize outliers
plt.figure(figsize=(8,5))
sns.boxplot(data=df[['Age', 'Fare']])
plt.title("Boxplot of Age and Fare")
plt.show()

# Remove outliers using IQR for Age

Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

df = df[(df['Age'] >= lower_limit) & (df['Age'] <= upper_limit)]

print("\nDataset Shape After Removing Outliers:")
print(df.shape)

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as 'cleaned_dataset.csv'")