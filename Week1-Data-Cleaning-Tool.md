# Week 1 - Data Cleaning Tool

## Project Overview

This project is an automated client data cleaning tool developed using Python and Pandas.

The purpose of the project is to clean messy client data by removing unnecessary spaces, standardizing text, validating email addresses, handling missing values, and removing duplicate records.

## Dataset

Input dataset: `clients_messy.csv`

Output dataset: `clients_cleaned.csv`

## Tools Used

- Python
- Pandas
- Google Colab
- GitHub

## Data Cleaning Process

1. Loaded the CSV file using Pandas.
2. Inspected the dataset.
3. Cleaned the column names.
4. Removed unnecessary spaces.
5. Standardized names and cities.
6. Converted email addresses to lowercase.
7. Validated email addresses.
8. Standardized the Review column.
9. Checked missing values.
10. Exported the cleaned data to a new CSV file.

## Data Cleaning Logic

### Names and Cities

Names and cities were standardized using title case.

Example:

`KHIMA IRENe` → `Khima Irene`

### Email Addresses

Email addresses were converted to lowercase and unnecessary spaces were removed.

Invalid email addresses were identified and changed to missing values.

### Reviews

Inconsistent review values were standardized.

Example:

`Ba` → `Bad`

### Duplicate Records

Duplicate rows were removed using Pandas `drop_duplicates()`.

## Python Code

```python
import pandas as pd

df = pd.read_csv("clients_messy.csv")

df.columns = df.columns.str.strip().str.title()

for col in ["Name", "Email", "City", "Review"]:
    df[col] = (
        df[col]
        .astype("string")
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

df["Name"] = df["Name"].str.title()
df["City"] = df["City"].str.title()

df["Email"] = df["Email"].str.lower()
df["Email"] = df["Email"].str.replace(r"\s+", "", regex=True)

email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

valid_email = df["Email"].str.match(email_pattern, na=False)

df.loc[~valid_email, "Email"] = pd.NA

df["Review"] = df["Review"].replace({
    "Ba": "Bad"
})

df["Review"] = df["Review"].str.title()


df.to_csv("clients_cleaned.csv", index=False)
