import pandas as pd
#load gapminder dataset
df = pd.read_csv('data/gapminder.csv')

# Write a function filter_country_year() that returns data for a specified country and year.
def filter_country_year(country, year):
    try:
        # Ensure country and year are of correct type
        if not isinstance(country, str):
            raise TypeError("Country must be a string")
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        
        # Check if the country and year exists in the dataset
        if country not in df['country'].unique():
            raise ValueError(f"Country '{country}' not found in dataset.")
        if year not in df['year'].unique():
            raise ValueError(f"Year '{year}' not found in dataset.")
        
        # Filter the dataframe
        filtered_df = df[(df['country'] == country) & (df['year'] == year)]

        # Check if filtered dataframe is empty
        if filtered_df.empty:
            raise ValueError("No data found for the given country and year")

        return filtered_df

    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



# Write a function calculate_gdp() that adds a new column total_gdp by multiplying gdpPercap and pop.
def calculate_gdp():
        df['total_gdp'] = df['gdpPercap'] * df['pop']


# Use a loop to calculate and print the average lifeExp for each country.
def avg_lifeExp():
    countries = df['country'].unique()
    for country in countries:
        avg_life = df[df['country'] == country]['lifeExp'].mean()
        print(f"{country}, Average Life Expectancy is {avg_life:.2f}")


# Use a loop to identify and print the country with the highest total_gdp for each year.
def highest_gdp_by_year():   
    # Ensure total_gdp is calculated
    calculate_gdp()
    # Sort the data by year and total_gdp
    df.sort_values(by=['year', 'total_gdp'], ascending=[True, False], inplace=True)
    # Get unique years
    years = df['year'].unique()
    print("Country with highest GDP by year:")
    # Loop through each year
    for year in years:
        gdp_df = df[df['year'] == year]
        hgdp = gdp_df.loc[gdp_df['total_gdp'].idxmax()]
        print(f"In {year}, {hgdp['country']} has highest total GDP of {hgdp['total_gdp']:.2f}")



# test functions 
print(filter_country_year("Nigeria", 2007))
avg_lifeExp()
highest_gdp_by_year()

# Save the final dataframe with total_gdp column to gapminder_final.csv.
df.to_csv("data/Lucky_gapminder_final.csv", index=False)



    


    
    
