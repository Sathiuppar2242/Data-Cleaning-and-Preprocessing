# Data Cleaning and Preprocessing Summary

## Dataset

Customer Personality Analysis (`marketing_campaign.csv`)

## Cleaning Operations

- Loaded the raw dataset using Pandas.
- Checked the dataset shape, columns, and data types.
- Identified missing values in the `Income` column.
- Replaced missing `Income` values with the median income.
- Checked for duplicate rows and removed duplicates.
- Standardized text values in `Education` and `Marital_Status`.
- Cleaned column names by converting them to lowercase and replacing spaces with underscores.
- Converted `Dt_Customer` from text format to a datetime data type.
- Performed final checks for missing values and duplicate rows.
- Exported the cleaned dataset to the `data/cleaned/` directory.