import pandas as pd

# Load the messy CSV file
df = pd.read_csv("clients_messy.csv")

# Clean column names
df.columns = df.columns.str.strip().str.title()

# Remove unnecessary spaces
for col in ["Name", "Email", "City", "Review"]:
    df[col] = (
        df[col]
        .astype("string")
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

# Standardize names and cities
df["Name"] = df["Name"].str.title()
df["City"] = df["City"].str.title()

# Clean email addresses
df["Email"] = df["Email"].str.lower()
df["Email"] = df["Email"].str.replace(r"\s+", "", regex=True)

# Validate email addresses
email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

valid_email = df["Email"].str.match(email_pattern, na=False)

df.loc[~valid_email, "Email"] = pd.NA

# Standardize review values
df["Review"] = df["Review"].replace({
    "Ba": "Bad"
})

df["Review"] = df["Review"].str.title()


# Save cleaned data
df.to_csv("clients_cleaned.csv", index=False)

print("Data cleaning completed successfully!")
print("Cleaned file saved as clients_cleaned.csv")
