import pandas as pd
df = pd.read_csv("data/gapminder.csv")
print(df.head())       # View first few rows
print(df.info())       # Check data types and missing values
print(df.describe())   # Summary statistics
df.rename(columns={"gdpPercap": "GDP_per_capita"}, inplace=True)
df = df.dropna(subset=["lifeExp"])
median_pop = df["pop"].median()
df["pop"].fillna(median_pop, inplace=True)
# keep only data for nigeria, ghana, and kenya
countries = ["Nigeria", "Ghana", "Kenya", "South Africa"]
df_filtered = df[(df["country"].isin(countries)) & (df["year"] >= 2000)]

df_filtered.to_csv("data/gapminder_cleaned.csv", index=False)



