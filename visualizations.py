import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# MARKETING CAMPAIGN ROI ANALYSIS
# MATPLOTLIB DASHBOARD
# ============================================================

# ============================================================
# 1. LOAD DATA
# ============================================================

df = pd.read_csv(
    "dataset/processed/marketing_clean.csv"
)

df["start_date"] = pd.to_datetime(
    df["start_date"],
    errors="coerce"
)

print("=" * 80)
print("MARKETING CAMPAIGN ROI ANALYSIS")
print("=" * 80)

print("\nDataset Shape:", df.shape)


# ============================================================
# 2. KPI CALCULATIONS
# ============================================================

total_spend = df["ad_spend"].sum()

total_revenue = df["revenue"].sum()

total_profit = df["profit"].sum()

overall_roi = (
    (total_revenue - total_spend)
    / total_spend
)

total_campaigns = df["campaign_id"].nunique()

total_impressions = df["impressions"].sum()

total_clicks = df["clicks"].sum()

total_conversions = df["conversions"].sum()

overall_ctr = (
    total_clicks
    / total_impressions
)

overall_conversion_rate = (
    total_conversions
    / total_clicks
)

cost_per_conversion = (
    total_spend
    / total_conversions
)


# ============================================================
# 3. GROUPED DATA
# ============================================================

channel_revenue = (
    df.groupby("platform")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

channel_spend = (
    df.groupby("platform")["ad_spend"]
    .sum()
    .sort_values(ascending=False)
)

channel_roi = (
    df.groupby("platform")["ROI"]
    .mean()
    .sort_values(ascending=False)
)

channel_conversion = (
    df.groupby("platform")["conversion_rate"]
    .mean()
    .sort_values(ascending=False)
)

channel_ctr = (
    df.groupby("platform")["CTR"]
    .mean()
    .sort_values(ascending=False)
)

channel_profit = (
    df.groupby("platform")["profit"]
    .sum()
    .sort_values(ascending=False)
)


# ============================================================
# 4. MONTHLY PERFORMANCE
# ============================================================

monthly_performance = (
    df.groupby("campaign_month")[
        ["ad_spend", "revenue", "profit"]
    ]
    .sum()
)


# ============================================================
# 5. TOP CAMPAIGNS
# ============================================================

top_5_roi = (
    df[
        [
            "campaign_id",
            "platform",
            "ad_spend",
            "revenue",
            "ROI",
            "conversion_rate",
            "Cost_Per_Conversion"
        ]
    ]
    .sort_values(
        "ROI",
        ascending=False
    )
    .head(5)
)


# ============================================================
# 6. WORST CAMPAIGNS
# ============================================================

bottom_5_roi = (
    df[
        [
            "campaign_id",
            "platform",
            "ad_spend",
            "revenue",
            "ROI"
        ]
    ]
    .sort_values(
        "ROI",
        ascending=True
    )
    .head(5)
)


# ============================================================
# ============================================================
# PAGE 1 — EXECUTIVE OVERVIEW
# ============================================================
# ============================================================

fig = plt.figure(
    figsize=(18, 11)
)

fig.suptitle(
    "MARKETING CAMPAIGN — EXECUTIVE OVERVIEW",
    fontsize=20,
    fontweight="bold"
)


# ------------------------------------------------------------
# KPI 1 — TOTAL SPEND
# ------------------------------------------------------------

ax1 = plt.subplot2grid(
    (4, 4),
    (0, 0)
)

ax1.text(
    0.5,
    0.55,
    f"${total_spend:,.0f}",
    ha="center",
    va="center",
    fontsize=22,
    fontweight="bold"
)

ax1.text(
    0.5,
    0.20,
    "TOTAL AD SPEND",
    ha="center",
    va="center",
    fontsize=11
)

ax1.axis("off")


# ------------------------------------------------------------
# KPI 2 — TOTAL REVENUE
# ------------------------------------------------------------

ax2 = plt.subplot2grid(
    (4, 4),
    (0, 1)
)

ax2.text(
    0.5,
    0.55,
    f"${total_revenue:,.0f}",
    ha="center",
    va="center",
    fontsize=22,
    fontweight="bold"
)

ax2.text(
    0.5,
    0.20,
    "TOTAL REVENUE",
    ha="center",
    va="center",
    fontsize=11
)

ax2.axis("off")


# ------------------------------------------------------------
# KPI 3 — OVERALL ROI
# ------------------------------------------------------------

ax3 = plt.subplot2grid(
    (4, 4),
    (0, 2)
)

ax3.text(
    0.5,
    0.55,
    f"{overall_roi:.2f}x",
    ha="center",
    va="center",
    fontsize=22,
    fontweight="bold"
)

ax3.text(
    0.5,
    0.20,
    "OVERALL ROI",
    ha="center",
    va="center",
    fontsize=11
)

ax3.axis("off")


# ------------------------------------------------------------
# KPI 4 — CAMPAIGNS
# ------------------------------------------------------------

ax4 = plt.subplot2grid(
    (4, 4),
    (0, 3)
)

ax4.text(
    0.5,
    0.55,
    f"{total_campaigns:,}",
    ha="center",
    va="center",
    fontsize=22,
    fontweight="bold"
)

ax4.text(
    0.5,
    0.20,
    "TOTAL CAMPAIGNS",
    ha="center",
    va="center",
    fontsize=11
)

ax4.axis("off")


# ------------------------------------------------------------
# MONTHLY SPEND VS REVENUE
# ------------------------------------------------------------

ax5 = plt.subplot2grid(
    (4, 4),
    (1, 0),
    colspan=4,
    rowspan=2
)

ax5.plot(
    monthly_performance.index,
    monthly_performance["ad_spend"],
    marker="o",
    label="Ad Spend"
)

ax5.plot(
    monthly_performance.index,
    monthly_performance["revenue"],
    marker="o",
    label="Revenue"
)

ax5.set_title(
    "Monthly Ad Spend vs Revenue",
    fontsize=14,
    fontweight="bold"
)

ax5.set_xlabel("Campaign Month")

ax5.set_ylabel("Amount")

ax5.tick_params(
    axis="x",
    rotation=45
)

ax5.legend()

ax5.grid(
    alpha=0.3
)


# ------------------------------------------------------------
# REVENUE BY CHANNEL
# ------------------------------------------------------------

ax6 = plt.subplot2grid(
    (4, 4),
    (3, 0),
    colspan=2
)

ax6.bar(
    channel_revenue.index,
    channel_revenue.values
)

ax6.set_title(
    "Revenue by Channel",
    fontweight="bold"
)

ax6.set_ylabel("Revenue")

ax6.tick_params(
    axis="x",
    rotation=45
)


# ------------------------------------------------------------
# ROI BY CHANNEL
# ------------------------------------------------------------

ax7 = plt.subplot2grid(
    (4, 4),
    (3, 2),
    colspan=2
)

ax7.bar(
    channel_roi.index,
    channel_roi.values
)

ax7.set_title(
    "Average ROI by Channel",
    fontweight="bold"
)

ax7.set_ylabel("ROI")

ax7.tick_params(
    axis="x",
    rotation=45
)


plt.tight_layout(
    rect=[0, 0, 1, 0.95]
)

plt.show()


# ============================================================
# ============================================================
# PAGE 2 — CHANNEL PERFORMANCE
# ============================================================
# ============================================================

fig = plt.figure(
    figsize=(18, 11)
)

fig.suptitle(
    "MARKETING CAMPAIGN — CHANNEL PERFORMANCE",
    fontsize=20,
    fontweight="bold"
)


# ------------------------------------------------------------
# REVENUE BY CHANNEL
# ------------------------------------------------------------

ax1 = plt.subplot2grid(
    (3, 4),
    (0, 0),
    colspan=2
)

ax1.bar(
    channel_revenue.index,
    channel_revenue.values
)

ax1.set_title(
    "Revenue by Channel",
    fontweight="bold"
)

ax1.set_ylabel("Revenue")

ax1.tick_params(
    axis="x",
    rotation=45
)


# ------------------------------------------------------------
# SPEND BY CHANNEL
# ------------------------------------------------------------

ax2 = plt.subplot2grid(
    (3, 4),
    (0, 2),
    colspan=2
)

ax2.bar(
    channel_spend.index,
    channel_spend.values
)

ax2.set_title(
    "Ad Spend by Channel",
    fontweight="bold"
)

ax2.set_ylabel("Ad Spend")

ax2.tick_params(
    axis="x",
    rotation=45
)


# ------------------------------------------------------------
# ROI BY CHANNEL
# ------------------------------------------------------------

ax3 = plt.subplot2grid(
    (3, 4),
    (1, 0),
    colspan=2
)

ax3.bar(
    channel_roi.index,
    channel_roi.values
)

ax3.set_title(
    "Average ROI by Channel",
    fontweight="bold"
)

ax3.set_ylabel("ROI")

ax3.tick_params(
    axis="x",
    rotation=45
)


# ------------------------------------------------------------
# CONVERSION RATE BY CHANNEL
# ------------------------------------------------------------

ax4 = plt.subplot2grid(
    (3, 4),
    (1, 2),
    colspan=2
)

ax4.bar(
    channel_conversion.index,
    channel_conversion.values
)

ax4.set_title(
    "Average Conversion Rate by Channel",
    fontweight="bold"
)

ax4.set_ylabel("Conversion Rate")

ax4.tick_params(
    axis="x",
    rotation=45
)


# ------------------------------------------------------------
# CTR BY CHANNEL
# ------------------------------------------------------------

ax5 = plt.subplot2grid(
    (3, 4),
    (2, 0),
    colspan=2
)

ax5.bar(
    channel_ctr.index,
    channel_ctr.values
)

ax5.set_title(
    "Average CTR by Channel",
    fontweight="bold"
)

ax5.set_ylabel("CTR")

ax5.tick_params(
    axis="x",
    rotation=45
)


# ------------------------------------------------------------
# PROFIT BY CHANNEL
# ------------------------------------------------------------

ax6 = plt.subplot2grid(
    (3, 4),
    (2, 2),
    colspan=2
)

ax6.bar(
    channel_profit.index,
    channel_profit.values
)

ax6.set_title(
    "Total Profit by Channel",
    fontweight="bold"
)

ax6.set_ylabel("Profit")

ax6.tick_params(
    axis="x",
    rotation=45
)


plt.tight_layout(
    rect=[0, 0, 1, 0.95]
)

plt.show()


# ============================================================
# ============================================================
# PAGE 3 — CAMPAIGN INSIGHTS
# ============================================================
# ============================================================

fig = plt.figure(
    figsize=(18, 11)
)

fig.suptitle(
    "MARKETING CAMPAIGN — CAMPAIGN INSIGHTS",
    fontsize=20,
    fontweight="bold"
)


# ------------------------------------------------------------
# TOP 5 CAMPAIGNS BY ROI
# ------------------------------------------------------------

ax1 = plt.subplot2grid(
    (3, 4),
    (0, 0),
    colspan=2
)

ax1.bar(
    top_5_roi["campaign_id"],
    top_5_roi["ROI"]
)

ax1.set_title(
    "Top 5 Campaigns by ROI",
    fontweight="bold"
)

ax1.set_xlabel("Campaign ID")

ax1.set_ylabel("ROI")

ax1.tick_params(
    axis="x",
    rotation=45
)


# ------------------------------------------------------------
# BOTTOM 5 CAMPAIGNS BY ROI
# ------------------------------------------------------------

ax2 = plt.subplot2grid(
    (3, 4),
    (0, 2),
    colspan=2
)

ax2.bar(
    bottom_5_roi["campaign_id"],
    bottom_5_roi["ROI"]
)

ax2.set_title(
    "Bottom 5 Campaigns by ROI",
    fontweight="bold"
)

ax2.set_xlabel("Campaign ID")

ax2.set_ylabel("ROI")

ax2.tick_params(
    axis="x",
    rotation=45
)


# ------------------------------------------------------------
# AD SPEND VS REVENUE
# ------------------------------------------------------------

ax3 = plt.subplot2grid(
    (3, 4),
    (1, 0),
    colspan=2
)

ax3.scatter(
    df["ad_spend"],
    df["revenue"],
    alpha=0.4
)

ax3.set_title(
    "Ad Spend vs Revenue",
    fontweight="bold"
)

ax3.set_xlabel("Ad Spend")

ax3.set_ylabel("Revenue")


# ------------------------------------------------------------
# CONVERSION RATE VS ROI
# ------------------------------------------------------------

ax4 = plt.subplot2grid(
    (3, 4),
    (1, 2),
    colspan=2
)

ax4.scatter(
    df["conversion_rate"],
    df["ROI"],
    alpha=0.4
)

ax4.set_title(
    "Conversion Rate vs ROI",
    fontweight="bold"
)

ax4.set_xlabel("Conversion Rate")

ax4.set_ylabel("ROI")


# ------------------------------------------------------------
# COST PER CONVERSION
# ------------------------------------------------------------

top_10_cpa = (
    df[
        [
            "campaign_id",
            "Cost_Per_Conversion"
        ]
    ]
    .dropna()
    .sort_values(
        "Cost_Per_Conversion",
        ascending=True
    )
    .head(10)
)

ax5 = plt.subplot2grid(
    (3, 4),
    (2, 0),
    colspan=2
)

ax5.bar(
    top_10_cpa["campaign_id"],
    top_10_cpa["Cost_Per_Conversion"]
)

ax5.set_title(
    "10 Lowest Cost-per-Conversion Campaigns",
    fontweight="bold"
)

ax5.set_xlabel("Campaign ID")

ax5.set_ylabel("Cost Per Conversion")

ax5.tick_params(
    axis="x",
    rotation=45
)


# ------------------------------------------------------------
# IMPRESSIONS VS CLICKS
# ------------------------------------------------------------

ax6 = plt.subplot2grid(
    (3, 4),
    (2, 2),
    colspan=2
)

ax6.scatter(
    df["impressions"],
    df["clicks"],
    alpha=0.4
)

ax6.set_title(
    "Impressions vs Clicks",
    fontweight="bold"
)

ax6.set_xlabel("Impressions")

ax6.set_ylabel("Clicks")


plt.tight_layout(
    rect=[0, 0, 1, 0.95]
)

plt.show()


# ============================================================
# 7. PRINT IMPORTANT KPI RESULTS
# ============================================================

print("\n" + "=" * 80)
print("KEY PERFORMANCE INDICATORS")
print("=" * 80)

print(f"Total Spend              : ${total_spend:,.2f}")
print(f"Total Revenue            : ${total_revenue:,.2f}")
print(f"Total Profit             : ${total_profit:,.2f}")
print(f"Overall ROI              : {overall_roi:.4f}x")
print(f"Total Campaigns          : {total_campaigns:,}")
print(f"Total Impressions        : {total_impressions:,}")
print(f"Total Clicks             : {total_clicks:,}")
print(f"Total Conversions        : {total_conversions:,}")
print(f"Overall CTR              : {overall_ctr:.4%}")
print(f"Overall Conversion Rate  : {overall_conversion_rate:.4%}")
print(f"Overall Cost/Conversion  : ${cost_per_conversion:,.2f}")


# ============================================================
# 8. CHANNEL INSIGHTS
# ============================================================

print("\n" + "=" * 80)
print("CHANNEL INSIGHTS")
print("=" * 80)

print(
    "\nHighest Revenue Channel :",
    channel_revenue.index[0]
)

print(
    "Highest ROI Channel     :",
    channel_roi.index[0]
)

print(
    "Highest Conversion Rate :",
    channel_conversion.index[0]
)

print(
    "Highest CTR Channel     :",
    channel_ctr.index[0]
)

print(
    "Highest Profit Channel  :",
    channel_profit.index[0]
)


# ============================================================
# 9. TOP CAMPAIGNS
# ============================================================

print("\n" + "=" * 80)
print("TOP 5 CAMPAIGNS BY ROI")
print("=" * 80)

print(top_5_roi)


# ============================================================
# 10. VISUALIZATION COMPLETED
# ============================================================

print("\n" + "=" * 80)
print("MATPLOTLIB DASHBOARD COMPLETED")
print("=" * 80)