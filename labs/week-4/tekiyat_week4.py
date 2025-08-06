# Importing libraries

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("C:/Users/TEKIYAT ADEBISI/Documents/ISIC-ISCO/gapminder.csv")
print(df)  #to check dataset

# Preview the dataset
df.head()

df.shape  # number of rows and columns
print(df.shape)

df.sample(5)  # random sample
print(df.sample(5)) 
# Inspecting the Data
df.info()
df.describe()
df.columns

# Filtering for Nigeria
nigeria = df[df["country"] == "Nigeria"].copy()
nigeria.head()

# Checking for Missing Data
nigeria.isnull().sum()

# Checking and Converting Data Types
nigeria.dtypes

#Convert `year` to integer
nigeria["year"] = nigeria["year"].astype(int)

## Creating a New Column

#Calculate approximate total GDP: `population × gdp_per_capita`.
nigeria["total_gdp"] = nigeria["pop"] * nigeria["gdpPercap"]
nigeria[["year", "gdpPercap", "pop", "total_gdp"]].head()

## Visualizing GDP per Capita Over Time
nigeria.plot(x="year", y="gdpPercap", kind="line", title="GDP per capita in Nigeria")
plt.ylabel("gdpPercap")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()

## Saving the Cleaned Dataset

#Export the cleaned data for future use.
nigeria.to_csv("C:/Users/TEKIYAT ADEBISI/Documents/ISIC-ISCO/data/gapminder_tekiyat_nigeria_cleaned.csv", index=False)

import os
os.path.exists("C:/Users/TEKIYAT ADEBISI/Documents/ISIC-ISCO/data/gapminder_tekiyat_nigeria_cleaned.csv")
#print("Script ran successfully")