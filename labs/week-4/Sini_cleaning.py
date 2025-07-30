# import library
import pandas as pd

# load the dataset
df = pd.read_csv('data/gapminder.csv')

# inspecting and exploring data
print(df.head())  
print(df.info())
df.describe() 

# renaming Rename gdpPercap
df.rename(columns={'gdpPercap': 'GDP_per_capita'}, inplace=True)

# checking for missing values
print(df.isnull().sum())

# Drop rows where lifeExp is missing.
df.dropna(subset=['lifeExp'], inplace=True)

# Fill missing pop values with median population. 
df['pop'] = df['pop'].fillna(df['pop'].median())

# Filter the dataset
df_africa = df[(df['country'].isin(['Nigeria', 'Ghana', 'Kenya', 'South Africa'])) & (df['year'] >= 2000)].copy()
print(df_africa.head())

# Save the cleaned dataset
df_africa.to_csv('data/Sini_gapminder_cleaned.csv', index=False)