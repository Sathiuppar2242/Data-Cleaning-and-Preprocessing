import pandas as pd

# Path to the raw dataset
RAW_DATA_PATH = "data/raw/marketing_campaign.csv"

# Load the raw dataset
df = pd.read_csv(RAW_DATA_PATH, sep="\t")

print("Dataset loaded successfully.")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)