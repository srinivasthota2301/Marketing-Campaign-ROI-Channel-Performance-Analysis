import pandas as pd
import numpy as np

# ============================================================
# 1. LOAD CLEANED DATASET
# ============================================================

df = pd.read_csv(
    "dataset/processed/marketing_clean.csv"
)

print("=" * 70)
print("FEATURE ENGINEERING")
print("=" * 70)

print("\nDataset Shape:")
print(df.shape)

# ============================================================
# 2. CONVERT DATE COLUMN
# ============================================================

df["start_date"] = pd.to_datetime(
    df["start_date"],
    errors="coerce"
)

print("\nstart_date datatype:")
print(df["start_date"].dtype)

# ============================================================
# 3. CTR
# Formula:
# CTR = Clicks / Impressions
# ============================================================

df["CTR"] = np.where(
    df["impressions"] > 0,
    df["clicks"] / df["impressions"],
    np.nan
)

# ============================================================
# 4. CONVERSION RATE
# Formula:
# Conversion Rate = Conversions / Clicks
# ============================================================

df["conversion_rate"] = np.where(
    df["clicks"] > 0,
    df["conversions"] / df["clicks"],
    np.nan
)

# ============================================================
# 5. ROI
# Formula:
# ROI = (Revenue - Ad Spend) / Ad Spend
# ============================================================

df["ROI"] = np.where(
    df["ad_spend"] > 0,
    (df["revenue"] - df["ad_spend"]) / df["ad_spend"],
    np.nan
)

# ============================================================
# 6. COST PER CONVERSION
# Formula:
# Cost Per Conversion = Ad Spend / Conversions
# ============================================================

df["Cost_Per_Conversion"] = np.where(
    df["conversions"] > 0,
    df["ad_spend"] / df["conversions"],
    np.nan
)

# ============================================================
# 7. CAMPAIGN MONTH
# ============================================================

df["campaign_month"] = (
    df["start_date"]
    .dt.to_period("M")
    .astype(str)
)

# ============================================================
# 8. DISPLAY CALCULATED COLUMNS
# ============================================================

print("\n" + "=" * 70)
print("CALCULATED FEATURES")
print("=" * 70)

print(
    df[
        [
            "campaign_id",
            "impressions",
            "clicks",
            "conversions",
            "ad_spend",
            "revenue",
            "CTR",
            "conversion_rate",
            "ROI",
            "Cost_Per_Conversion",
            "campaign_month"
        ]
    ].head(10)
)

# ============================================================
# 9. FEATURE SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("FEATURE SUMMARY")
print("=" * 70)

print(
    df[
        [
            "CTR",
            "conversion_rate",
            "ROI",
            "Cost_Per_Conversion"
        ]
    ].describe()
)

# ============================================================
# 10. CHECK MISSING VALUES IN NEW FEATURES
# ============================================================

print("\n" + "=" * 70)
print("MISSING VALUES IN NEW FEATURES")
print("=" * 70)

print(
    df[
        [
            "CTR",
            "conversion_rate",
            "ROI",
            "Cost_Per_Conversion",
            "campaign_month"
        ]
    ].isnull().sum()
)

# ============================================================
# 11. CHECK INFINITE VALUES
# ============================================================

print("\n" + "=" * 70)
print("INFINITE VALUES")
print("=" * 70)

print(
    np.isinf(
        df[
            [
                "CTR",
                "conversion_rate",
                "ROI",
                "Cost_Per_Conversion"
            ]
        ]
    ).sum()
)

# ============================================================
# 12. FINAL DATASET INFORMATION
# ============================================================

print("\n" + "=" * 70)
print("FINAL DATASET")
print("=" * 70)

print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])

print("\nNew Columns:")
print([
    "CTR",
    "conversion_rate",
    "ROI",
    "Cost_Per_Conversion",
    "campaign_month"
])

# ============================================================
# 13. SAVE FINAL DATASET
# ============================================================

df.to_csv(
    "dataset/processed/marketing_clean.csv",
    index=False
)

print("\n" + "=" * 70)
print("FEATURE ENGINEERING COMPLETED")
print("=" * 70)

print(
    "Final dataset saved to: "
    "dataset/processed/marketing_clean.csv"
)