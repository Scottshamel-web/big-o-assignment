import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------------------------
# Original messy data
# -------------------------------------------------

messy = pd.DataFrame({
    "product": [
        "Widget A", "Widget B", "widget a", "Widget C", "Widget B",
        "Widget A", " Widget C", "Widget D", None, "Widget A"
    ],
    "sales": [
        "150", "200", "175", "300", "200",
        "180", "250", "abc", "100", "-50"
    ],
    "date": [
        "2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02",
        "2025-01-03", "2025-01-03", "2025-01-04", "2025-01-04",
        "2025-01-05", "2025-01-05"
    ],
    "region": [
        "North", "South", "north", "East", "South",
        "West", "east", "North", "South", "West"
    ],
})


print("ORIGINAL DATA")
print(messy)


# -------------------------------------------------
# 1. Clean the data
# -------------------------------------------------

clean = messy.copy()


# Standardize product names
clean["product"] = (
    clean["product"]
    .str.strip()
    .str.title()
)


# Standardize regions
clean["region"] = (
    clean["region"]
    .str.strip()
    .str.title()
)


# Convert sales to numeric
# "abc" becomes NaN
clean["sales"] = pd.to_numeric(
    clean["sales"],
    errors="coerce"
)


# Treat negative sales as invalid
clean.loc[clean["sales"] < 0, "sales"] = pd.NA


# Convert date column to datetime
clean["date"] = pd.to_datetime(
    clean["date"],
    errors="coerce"
)


# Remove rows missing important values
clean = clean.dropna(
    subset=["product", "sales", "date", "region"]
)


# Remove duplicate rows
clean = clean.drop_duplicates()


# Reset row numbers
clean = clean.reset_index(drop=True)


print("\nCLEANED DATA")
print(clean)


# -------------------------------------------------
# Summary
# -------------------------------------------------

print("\nDATA SUMMARY")
print(clean.info())

print("\nDescriptive statistics:")
print(clean["sales"].describe())


# -------------------------------------------------
# 2. Total sales by product
# -------------------------------------------------

sales_by_product = (
    clean.groupby("product")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTOTAL SALES BY PRODUCT")
print(sales_by_product)


plt.figure(figsize=(8, 5))

sales_by_product.plot(
    kind="bar"
)

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "product_sales_bar.png",
    dpi=300
)

plt.close()


# -------------------------------------------------
# 3. Daily sales trend
# -------------------------------------------------

daily_sales = (
    clean.groupby("date")["sales"]
    .sum()
    .sort_index()
)

print("\nDAILY SALES")
print(daily_sales)


plt.figure(figsize=(8, 5))

daily_sales.plot(
    marker="o"
)

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "daily_sales_trend.png",
    dpi=300
)

plt.close()


# -------------------------------------------------
# 4. Sales distribution
# -------------------------------------------------

plt.figure(figsize=(8, 5))

clean["sales"].plot(
    kind="hist",
    bins=6,
    edgecolor="black"
)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig(
    "sales_distribution.png",
    dpi=300
)

plt.close()


# -------------------------------------------------
# Finished
# -------------------------------------------------

print("\nCharts saved successfully:")
print("product_sales_bar.png")
print("daily_sales_trend.png")
print("sales_distribution.png")