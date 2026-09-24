import pandas as pd

# ============================================================
# 1. DATA LOADING
# ============================================================

# Load the dataset

df = pd.read_csv("dataset/raw/tech_advertising_campaigns_dataset.csv")


# ============================================================
# 2. BASIC DATA EXPLORATION
# ============================================================

# First 5 rows

print("=" * 70)
print("FIRST 5 ROWS")
print("=" * 70)

print(df.head())


# Last 5 rows

print("\n" + "=" * 70)
print("LAST 5 ROWS")
print("=" * 70)

print(df.tail())


# Dataset shape

print("\n" + "=" * 70)
print("DATASET SHAPE")
print("=" * 70)

print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])


# Column names

print("\n" + "=" * 70)
print("COLUMN NAMES")
print("=" * 70)

print(df.columns.tolist())


# Data types

print("\n" + "=" * 70)
print("DATA TYPES")
print("=" * 70)

print(df.dtypes)


# ============================================================
# 3. DATA QUALITY CHECK
# ============================================================

# Missing values

print("\n" + "=" * 70)
print("MISSING VALUES")
print("=" * 70)

print(df.isnull().sum())


# Missing value percentage

print("\n" + "=" * 70)
print("MISSING VALUE PERCENTAGE")
print("=" * 70)

print((df.isnull().sum() / len(df) * 100).round(2))


# Duplicate rows

print("\n" + "=" * 70)
print("DUPLICATE ROWS")
print("=" * 70)

print(df.duplicated().sum())


# ============================================================
# 4. STATISTICAL EXPLORATION
# ============================================================

# Numerical columns summary

print("\n" + "=" * 70)
print("NUMERICAL SUMMARY")
print("=" * 70)

print(df.describe())


# Categorical columns summary

print("\n" + "=" * 70)
print("CATEGORICAL SUMMARY")
print("=" * 70)

print(df.describe(include="str"))


# ============================================================
# 5. UNIQUE VALUES
# ============================================================

print("\n" + "=" * 70)
print("UNIQUE VALUES COUNT")
print("=" * 70)

print(df.nunique())


# ============================================================
# 6. IMPORTANT MARKETING COLUMNS
# ============================================================

print("\n" + "=" * 70)
print("CHANNELS")
print("=" * 70)

print(df["platform"].unique())


print("\n" + "=" * 70)
print("CAMPAIGN OBJECTIVES")
print("=" * 70)

print(df["campaign_objective"].unique())


# ============================================================
# 7. DATE EXPLORATION
# ============================================================

print("\n" + "=" * 70)
print("DATE INFORMATION")
print("=" * 70)

print("Minimum Date :", df["start_date"].min())
print("Maximum Date :", df["start_date"].max())


# ============================================================
# 8. IMPORTANT NUMERICAL COLUMNS
# ============================================================

print("\n" + "=" * 70)
print("MARKETING METRICS")
print("=" * 70)

print(
    df[
        [
            "impressions",
            "clicks",
            "conversions",
            "ad_spend",
            "revenue"
        ]
    ].describe()
)


# ============================================================
# 9. SAMPLE OF IMPORTANT COLUMNS
# ============================================================

print("\n" + "=" * 70)
print("IMPORTANT COLUMNS SAMPLE")
print("=" * 70)

print(
    df[
        [
            "campaign_id",
            "platform",
            "start_date",
            "impressions",
            "clicks",
            "conversions",
            "ad_spend",
            "revenue"
        ]
    ].head(10)
)


# ============================================================
# 10. DATA CLEANING
# ============================================================

print("\n" + "=" * 70)
print("DATA CLEANING")
print("=" * 70)


# Create a copy of the original dataframe

df_clean = df.copy()


# ------------------------------------------------------------
# 10.1 Check duplicate Campaign IDs
# ------------------------------------------------------------

print("\nDuplicate Campaign IDs Before Cleaning:")

duplicate_campaign_ids = df_clean["campaign_id"].duplicated().sum()

print(duplicate_campaign_ids)


# Remove duplicate Campaign IDs

df_clean = df_clean.drop_duplicates(
    subset="campaign_id",
    keep="first"
)


print("Duplicate Campaign IDs After Cleaning:")
print(df_clean["campaign_id"].duplicated().sum())


# ------------------------------------------------------------
# 10.2 Convert Date Column
# ------------------------------------------------------------

print("\nConverting start_date to datetime...")

df_clean["start_date"] = pd.to_datetime(
    df_clean["start_date"],
    format="%d-%m-%Y",
    errors="coerce"
)

print("start_date datatype:")
print(df_clean["start_date"].dtype)


# ------------------------------------------------------------
# 10.3 Convert Important Numeric Columns
# ------------------------------------------------------------

print("\nConverting important numeric columns...")

df_clean["impressions"] = pd.to_numeric(
    df_clean["impressions"],
    errors="coerce"
)

df_clean["clicks"] = pd.to_numeric(
    df_clean["clicks"],
    errors="coerce"
)

df_clean["conversions"] = pd.to_numeric(
    df_clean["conversions"],
    errors="coerce"
)

df_clean["ad_spend"] = pd.to_numeric(
    df_clean["ad_spend"],
    errors="coerce"
)

df_clean["revenue"] = pd.to_numeric(
    df_clean["revenue"],
    errors="coerce"
)


# ------------------------------------------------------------
# 10.4 Check Missing Values After Conversion
# ------------------------------------------------------------

print("\nMissing Values After Data Type Conversion:")

print(
    df_clean[
        [
            "start_date",
            "impressions",
            "clicks",
            "conversions",
            "ad_spend",
            "revenue"
        ]
    ].isnull().sum()
)


# ------------------------------------------------------------
# 10.5 Check Negative Spend
# ------------------------------------------------------------

print("\nNegative Ad Spend Records:")

negative_spend = (df_clean["ad_spend"] < 0).sum()

print(negative_spend)


# ------------------------------------------------------------
# 10.6 Check Negative Revenue
# ------------------------------------------------------------

print("\nNegative Revenue Records:")

negative_revenue = (df_clean["revenue"] < 0).sum()

print(negative_revenue)


# ------------------------------------------------------------
# 10.7 Check Clicks Greater Than Impressions
# ------------------------------------------------------------

print("\nClicks Greater Than Impressions:")

invalid_clicks = (
    df_clean["clicks"] > df_clean["impressions"]
).sum()

print(invalid_clicks)


# ------------------------------------------------------------
# 10.8 Check Conversions Greater Than Clicks
# ------------------------------------------------------------

print("\nConversions Greater Than Clicks:")

invalid_conversions = (
    df_clean["conversions"] > df_clean["clicks"]
).sum()

print(invalid_conversions)


# ============================================================
# 11. FINAL CLEANING VALIDATION
# ============================================================

print("\n" + "=" * 70)
print("FINAL CLEANING VALIDATION")
print("=" * 70)


print("\nOriginal Rows :", len(df))
print("Cleaned Rows  :", len(df_clean))

print("\nOriginal Columns :", df.shape[1])
print("Cleaned Columns  :", df_clean.shape[1])


print("\nDuplicate Rows After Cleaning:")
print(df_clean.duplicated().sum())


print("\nDuplicate Campaign IDs After Cleaning:")
print(df_clean["campaign_id"].duplicated().sum())


print("\nMissing Values After Cleaning:")
print(df_clean.isnull().sum().sum())


print("\nNegative Ad Spend After Cleaning:")
print((df_clean["ad_spend"] < 0).sum())


print("\nNegative Revenue After Cleaning:")
print((df_clean["revenue"] < 0).sum())


# ============================================================
# 12. SAVE CLEANED DATASET
# ============================================================

df_clean.to_csv(
    "dataset/processed/marketing_clean.csv",
    index=False
)


print("\n" + "=" * 70)
print("CLEANING COMPLETED")
print("=" * 70)

print(
    "Cleaned dataset saved to: "
    "dataset/processed/marketing_clean.csv"
)