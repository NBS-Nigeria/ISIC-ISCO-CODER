import pandas as pd

# Loading dataset
df = pd.read_csv("./data/gapminder.csv")

# 1. Filter function that returns data for a specified country and year.
def filter_country_year(country, year):
    try:
        filtered_country = df[(df['country'] == country) & (df['year'] == year)]
        if filtered_country.empty:
            raise ValueError(f"No data found for {country} in {year}")
        return filtered_country
    except Exception as e:
        print(f"Error: {e}")
        return None


# Testing filter_country_year function
filter_country_year('Nigeria', 2007)

# Function calculate_gdp() that adds a new column total_gdp by multiplying gdpPercap and pop.
def calculate_gdp():
    df['total_gdp'] = df['gdpPercap'] * df['pop']
    return df

#Testing calculate_gdp function
df = calculate_gdp()

# Loop to calculate and print the average lifeExp for each country.
print("\nAverage Life Expectancy per Country:")
for country in df['country'].unique():
    avg_life_exp = df[df['country'] == country]['lifeExp'].mean()
    print(f"{country}: {avg_life_exp:.2f}")


# Loop to identify and print the country with the highest total_gdp for each year.
print("\nCountry with Highest Total GDP per Year:")
for year in df['year'].unique():
    year_df = df[df['year'] == year]
    top_country = year_df.loc[year_df['total_gdp'].idxmax()]
    print(f"{year}: {top_country['country']} with GDP {top_country['total_gdp']:.2f}")


# Saving the final dataframe with total_gdp column to gapminder_final_siyudi.csv.
df.to_csv("./data/gapminder_final_siyudi.csv", index=False)
print("Final dataset saved to gapminder_final_siyudi.csv")
