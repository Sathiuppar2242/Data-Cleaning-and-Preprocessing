# Data Cleaning and Preprocessing

## Overview

This project demonstrates the process of cleaning and preprocessing a raw customer dataset using Python and Pandas.

The objective is to identify and handle common data quality issues such as missing values, duplicate records, inconsistent text values, date formats, column names, and data types.

## Dataset

**Dataset:** Customer Personality Analysis

**Source:** Kaggle

**Original File:** `marketing_campaign.csv`

The raw dataset is stored separately in:

```text
data/raw/
The cleaned dataset is generated in:

data/cleaned/
Data Cleaning Operations

The project performs the following operations:

Load the raw dataset using Pandas.
Inspect the dataset structure and dimensions.
Check for missing values.
Handle missing values in the Income column.
Detect duplicate records.
Remove duplicate records.
Standardize text values.
Clean and standardize column names.
Convert the customer date column to datetime format.
Check and validate data types.
Perform final data-quality checks.
Export the cleaned dataset.
Project Structure
Data-Cleaning-and-Preprocessing/
│
├── data/
│   ├── raw/
│   │   └── marketing_campaign.csv
│   │
│   └── cleaned/
│       └── marketing_campaign_cleaned.csv
│
├── reports/
│   └── cleaning_summary.md
│
├── data_cleaning.py
├── requirements.txt
└── README.md
Technologies Used
Python
Pandas
Git
GitHub
VS Code
How to Run

Install the required dependency:

pip install -r requirements.txt

Run the data-cleaning script:

python data_cleaning.py

The cleaned dataset will be generated at:

data/cleaned/marketing_campaign_cleaned.csv
Output

The final cleaned dataset contains:

Handled missing values
Removed duplicate records
Standardized text values
Clean column names
Converted date values
Validated data types
Project Objective

The main objective of this project is to demonstrate a complete and reproducible data cleaning and preprocessing workflow using Pandas.