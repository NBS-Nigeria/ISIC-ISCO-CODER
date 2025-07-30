
import pandas as pd

#Load the gapminder.csv into a DataFrame.
df = pd.read_csv("./data/gapminder.csv")

# Inspect the data using: head() info() describe()
df.head()
df.info()
df.describe()

#Rename gdpPercap to GDP_per_capita. 
df.rename(columns={'gdpPercap': 'GDP_per_capita'}, inplace=True)

#Handle missing values: Check for missing values
df.isnull().sum()

#Drop rows where lifeExp is missing.
df = df.dropna(subset=['lifeExp'])

#Fill missing pop values with median population. 
df['pop'] = df['pop'].fillna(df['pop'].median())

#Filter the dataset to include only data for:Nigeria, Ghana, Kenya, and South Africa.
df = df[df['country'].isin(['Nigeria', 'Ghana', 'Kenya', 'South Africa' ])]

#Filter the dataset to include Years 2000 and above.
df = df[df['year']>= 2000]

#Export the cleaned dataset to gapminder_cleaned.csv.
df.to_csv('data/gapminder_amina.csv', index=False)

#Commit and push your work to GitHub.
