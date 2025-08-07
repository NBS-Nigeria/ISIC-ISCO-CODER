### For Loop

for i in range(2):  # Repeat 2 times
    print("Happy birthday to you")

print("Happy birthday dear Ose")
print("Happy birthday to you")

### while Loop

count = 0

while count < 4:
    if count == 2:
        print("Happy birthday dear Ose")
    else:
        print("Happy birthday to you")
    
    count += 1
    
    ### If, Elif, and Else

language = input("Choose a language (english / spanish): ").lower()

if language == "english":
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday dear Ose")
    print("Happy birthday to you")

elif language == "spanish":
    print("Cumpleaños feliz")
    print("Cumpleaños feliz")
    print("Te deseamos, Ose")
    print("Cumpleaños feliz")

else:
    print("No birthday song for you!")

### Function

def sing_birthday(language):
    if language == "english":
        print("Happy birthday to you")
    elif language == "spanish":
        print("Cumpleaños feliz")
    else:
        print("No song for you 😶")

# Run the function
sing_birthday("spanish")  

## Load and Filter Gapminder Data

import pandas as pd

# Load dataset and filter for Nigeria

df = pd.read_csv("C:/Users/TEKIYAT ADEBISI/Documents/ISIC-ISCO/data/gapminder.csv")
nigeria = df[df['country'] == 'Nigeria']
nigeria.head()

## Using Conditional Statements Check if GDP per capita was ever below $1,500.

low_gdp_years = 0

for index, row in nigeria.iterrows():
    if row['gdpPercap'] < 1500:
        print(f"In {row['year']}, GDP per capita was low: ${row['gdpPercap']:.2f}")
        low_gdp_years += 1

print(f"\nTotal years with GDP per capita under $1,000: {low_gdp_years}")

## Classifying GDP Levels with a Function

##Define a function to label GDP as **low**, **medium**, or **high**.

def classify_gdp(gdp):
    if gdp < 1500:
        return "low"
    elif gdp < 3000:
        return "medium"
    else:
        return "high"

## Apply it to Nigeria data:

nigeria['gdp_level'] = nigeria['gdpPercap'].apply(classify_gdp)
nigeria[['year', 'gdpPercap', 'gdp_level']]

## Loop with Function: Print Yearly GDP Category

for index, row in nigeria.iterrows():
    category = classify_gdp(row['gdpPercap'])
    print(f"{row['year']}: GDP was {category}")


## Comparing Two Years with a Function Create a function to compare GDP between two years.

def compare_gdp(year1, year2, data):
    gdp1 = data[data['year'] == year1]['gdpPercap'].values[0]
    gdp2 = data[data['year'] == year2]['gdpPercap'].values[0]

    if gdp2 > gdp1:
        return f"GDP increased from {year1} to {year2} by ${gdp2 - gdp1:.2f}"
    elif gdp2 < gdp1:
        return f"GDP decreased from {year1} to {year2} by ${gdp1 - gdp2:.2f}"
    else:
        return f"GDP stayed the same between {year1} and {year2}"

##Try the function:

compare_gdp(1982, 2002, nigeria)

## Add a Summary Table with Changes Add GDP change and growth labels:

nigeria['gdp_change'] = nigeria['gdpPercap'].diff().round(2)
nigeria['growth'] = nigeria['gdp_change'].apply(
    lambda x: "increase" if x > 0 else ("decrease" if x < 0 else "no change")
)
nigeria[['year', 'gdpPercap', 'gdp_level', 'gdp_change', 'growth']]

##Exercise

import pandas as pd

# Load dataset and filter for Afghanistan

df = pd.read_csv("C:/Users/TEKIYAT ADEBISI/Documents/ISIC-ISCO/data/gapminder.csv")
afghanistan = df[df['country'] == 'Afghanistan']
afghanistan .head()
print(afghanistan.head())

#Convert `year` to integer
#country_data = df[df['country'] == country].copy()     #for all the country
#country_data['year'] = country_data['year'].astype(int)

afghanistan["year"] = afghanistan["year"].astype(int)

## Creating a New Column

#Calculate approximate total GDP: `population × gdp_per_capita`.
afghanistan["total_gdp"] = afghanistan["gdpPercap"] * afghanistan["pop"] 
afghanistan[["year", "gdpPercap", "pop", "total_gdp"]].head()

##Use a loop to calculate and print the average life expectancy for each country
countries = df['country'].unique()

for country in countries:
    country_data = df[df['country'] == country]
    avg_life_exp = country_data['lifeExp' ].mean()
    print(f"{country}: Average Life Expectancy = {avg_life_exp:.2f}")
    
##Use a loop to identify and print the country with the highest total_gdp for each year.

#Calculate approximate total GDP: `population × gdp_per_capita` for each row.

df['total_gdp'] = df['gdpPercap'] * df['pop']

years = df['year'].unique()

for year in sorted(years):
    year_data = df[df['year'] == year]
    top_country = year_data.loc[year_data['total_gdp'].idxmax()]
    print(f"{year}: {top_country['country']} had the highest GDP: ${top_country['total_gdp']:.2f}")
    
##Handle possible errors using try-except when country names are not found.
        
def safe_filter_country(data, country):
    try:
        filtered = data[data['country'] == country]
        if filtered.empty:
            raise ValueError("Country not found")
        return filtered
    except Exception as e:
        print(f"Error: {e}")
        return None

country_data = safe_filter_country(df, "Nigeria")
if country_data is not None:
    print(country_data.head())

##check for the country not in the list
country_data = safe_filter_country(df, "South Sudan")
if country_data is not None:
    print(country_data.head())
 
##Save the final dataframe with total_gdp column to gapminder_final.csv.   
df.to_csv("C:/Users/TEKIYAT ADEBISI/Documents/ISIC-ISCO/data/tekiyat_gapminder_final.csv", index=False)
