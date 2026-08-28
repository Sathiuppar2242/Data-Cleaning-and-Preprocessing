import pandas as pd

# -----------------------------------------
# 1. File Paths
# -----------------------------------------

RAW_DATA_PATH = "data/raw/marketing_campaign.csv"
CLEANED_DATA_PATH = "data/cleaned/marketing_campaign_cleaned.csv"


# -----------------------------------------
# 2. Load Raw Dataset
# -----------------------------------------

df = pd.read_csv(RAW_DATA_PATH, sep="\t")

print("Dataset loaded successfully.")

print("\nFirst 5 rows:")
print(df.head())


# -----------------------------------------
# 3. Initial Dataset Information
# -----------------------------------------

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)


# -----------------------------------------
# 4. Check Missing Values
# -----------------------------------------

print("\nMissing values before cleaning:")
print(df.isnull().sum())

missing_income = df["Income"].isnull().sum()

print("\nMissing Income values:", missing_income)


# -----------------------------------------
# 5. Handle Missing Values
# -----------------------------------------

df["Income"] = df["Income"].fillna(df["Income"].median())

print("\nMissing values after handling:")
print(df.isnull().sum())


# -----------------------------------------
# 6. Check Duplicate Rows
# -----------------------------------------

duplicate_count = df.duplicated().sum()

print("\nDuplicate rows before cleaning:", duplicate_count)


# -----------------------------------------
# 7. Remove Duplicate Rows
# -----------------------------------------

df = df.drop_duplicates()

print("\nDataset shape after removing duplicates:")
print(df.shape)

print("\nDuplicate rows after cleaning:", df.duplicated().sum())


# -----------------------------------------
# 8. Standardize Text Values
# -----------------------------------------

df["Education"] = (
    df["Education"]
    .str.strip()
    .str.title()
)

df["Marital_Status"] = (
    df["Marital_Status"]
    .str.strip()
    .str.title()
)

print("\nStandardized Education values:")
print(df["Education"].unique())

print("\nStandardized Marital Status values:")
print(df["Marital_Status"].unique())


# -----------------------------------------
# 9. Clean Column Names
# -----------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCleaned column names:")
print(df.columns.tolist())


# -----------------------------------------
# 10. Convert Date Column
# -----------------------------------------

df["dt_customer"] = pd.to_datetime(
    df["dt_customer"],
    format="%d-%m-%Y"
)

print("\nDate column data type:")
print(df["dt_customer"].dtype)


# -----------------------------------------
# 11. Check Data Types
# -----------------------------------------

print("\nFinal data types:")
print(df.dtypes)


# -----------------------------------------
# 12. Final Missing Value Check
# -----------------------------------------

print("\nFinal missing values:")
print(df.isnull().sum())


# -----------------------------------------
# 13. Final Duplicate Check
# -----------------------------------------

print("\nFinal duplicate count:")
print(df.duplicated().sum())


# -----------------------------------------
# 14. Save Cleaned Dataset
# -----------------------------------------

df.to_csv(CLEANED_DATA_PATH, index=False)

print("\nCleaned dataset saved successfully.")
print("Output file:", CLEANED_DATA_PATH)