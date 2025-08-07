
import pandas as pd
 #load data set
df = pd.read_csv('data/gapminder.csv')

# 1. Create a function to filter by country and year
def filter_country_year(country, year):
    try:
# Check required columns
        if 'country' not in df.columns or 'year' not in df.columns:
            return "Error: Required columns 'country' and 'year' are missing."

        # Check if country exists
        if country not in df['country'].unique():
            return f"Error: Country '{country}' not found in dataset."

        # Filter by country and year
        filtered = df[(df['country'] == country) & (df['year'] == year)]

        if filtered.empty:
            return f"No data found for {country} in {year}."

        return filtered

    except FileNotFoundError:
        return "Error: gapminder.csv not found."


# 2. write a Function calculate_gdp
def calculate_gdp():
    # Calculate total GDP
        df['total_gdp'] = df['gdpPercap'] * df['pop']
        
        return df
df_with_gdp = calculate_gdp()
print(df_with_gdp[['country', 'year', 'total_gdp']].head())


# 3. 
def print_avg_life_expectancy():
        countries = df['country'].unique()
        for country in countries:
            avg_life = df[df['country'] == country]['lifeExp'].mean()
            print(f"{country}: {avg_life:.2f}")

print_avg_life_expectancy()

# 4. & 5
def print_highest_gdp_by_year():   

      # Calculate total_gdp
        df['total_gdp'] = df['gdpPercap'] * df['pop']

        # Get unique years
        years = sorted(df['year'].unique())

        # Loop through each year
        for year in years:
            year_data = df[df['year'] == year]
            max_row = year_data.loc[year_data['total_gdp'].idxmax()]
            print(f"{year}: {max_row['country']} with total GDP of {max_row['total_gdp']:.2f}")
print_highest_gdp_by_year()

# 5. 
print(filter_country_year("Mecury", 2007))
print(filter_country_year("Kenya", 1602))

# 6.
# Save the updated DataFrame to a new CSV file
df.to_csv("data/Amina_gapminder_final.csv", index=False)



    


    
    