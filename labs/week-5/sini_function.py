# Load Gapminder data
import pandas as pd

df = pd.read_csv("data/gapminder.csv")

# Function to filter by country and year
def filter_country_year(data, country, year):
    try:
        filtered = data[(data['country'] == country) & (data['year'] == year)]
        if filtered.empty:
            raise ValueError(f"No data for {country} in {year}")
        return filtered
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()

# Function to calculate total_gdp
def calculate_gdp(data):
    data['total_gdp'] = data['gdpPercap'] * data['pop']
    return data

# Add total_gdp column
df = calculate_gdp(df)

# Print average lifeExp for each country
countries = df['country'].unique()
for country in countries:
    try:
        avg_life = df[df['country'] == country]['lifeExp'].mean()
        print(f"{country}: Average lifeExp = {avg_life:.2f}")
    except Exception as e:
        print(f"Error for {country}: {e}")

# Print country with highest total_gdp for each year
for year in sorted(df['year'].unique()):
    year_data = df[df['year'] == year]
    if not year_data.empty:
        max_row = year_data.loc[year_data['total_gdp'].idxmax()]
        print(f"{year}: {max_row['country']} has highest total_gdp = {max_row['total_gdp']:.2f}")

# Save final dataframe
df.to_csv("data/sini_gapminder_final.csv", index=False)
