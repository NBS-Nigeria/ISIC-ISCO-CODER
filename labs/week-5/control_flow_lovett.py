import pandas as pd
df = pd.read_csv("data/gapminder.csv")
def filter_country_year(data, country, year):
    try:
        result = data[(data['country'] == country) & (data['year'] == year)]
        if result.empty:
            raise ValueError("No data found for that country and year.")
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

def calculate_gdp(data):
    data['total_gdp'] = data['gdpPercap'] * data['pop']
    return data


def average_life_expectancy(data):
    countries = data['country'].unique()
    for country in countries:
        avg_life = data[data['country'] == country]['lifeExp'].mean()
        print(f"{country}: {avg_life:.2f}")



def highest_gdp_per_year(data):
    years = data['year'].unique()
    for year in years:
        yearly_data = data[data['year'] == year]
        max_row = yearly_data.loc[yearly_data['total_gdp'].idxmax()]
        print(f"{year}: {max_row['country']} with GDP {max_row['total_gdp']:.2f}")


# step 6
df = calculate_gdp(df)
average_life_expectancy(df)
highest_gdp_per_year(df)

# Save to CSV
df.to_csv('data/gapminder_final.csv', index=False)
