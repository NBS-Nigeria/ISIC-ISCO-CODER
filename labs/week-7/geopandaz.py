# Exercise: Which state had the highest underemployment rate in 2023?
# Your task is to create a choropleth map showing the underemployment rate for each state using data from the 2023 Labour Force Survey (Table 13).

# Load the necessary libraries
# Read the underemployment CSV file
# Read the nigeria GeoJSON file
# Merge the datasets using the state joining variable
# Create a choropleth map


import pandas as pd
import geopandas as gpd
from matplotlib import pyplot as plt
import seaborn
from mapclassify import EqualInterval, Quantiles, FisherJenks
import folium



# Read in the underemployment CSV file
uemp = pd.read_csv('data/underemployment.csv')
uemp.head()

# Read in the nigeria GeoJSON file
nigeria = gpd.read_file('data/nigeria_2.geojson')
nigeria.plot()

# Merge the datasets using the state joining variable
uemp['state'] = uemp['statename'].str.lower()
nigeria['state'] = nigeria['state'].str.lower()
uemp_data = pd.merge(nigeria, uemp, on = 'state', how = 'left')


print(uemp.head())
print(nigeria.head())
print(uemp_data.head())

# save to file
uemp_data.to_file('data/nigeria_underemployment.geojson')

# check distribution
ax = seaborn.histplot(uemp_data['rate'], bins=5)
seaborn.rugplot(uemp_data['rate'], height=0.05, color="red", ax=ax)
uemp_data['rate'].describe()

# Explore different classification schemes
EqualInterval(uemp_data["rate"], k=5) # Equal intervals
Quantiles(uemp_data["rate"], k=5) # Quintiles
FisherJenks(uemp_data["rate"], k=5) # Natural Breaks

# state with highest underemployment rate
huemp = uemp.loc[uemp['rate'].idxmax()]
print(f"{huemp['statename']} has the highest der rate of {huemp['rate']}% in 2023.")

# Create a choropleth map
fig, ax = plt.subplots(1, 1, figsize=(20, 10))
uemp_data.plot(column='rate', 
               cmap='OrRd', 
               linewidth=0.8, 
               ax=ax, 
               edgecolor='0.8', 
               legend=True,)
ax.set_title('Underemployment Rate by State in Nigeria (2023)', fontsize=22)
cbar = ax.get_figure().get_axes()[-1]
cbar.set_position([0.85, 0.15, 0.10, 0.7]) 
cbar.set_title('Underemployment Rate (%)')
plt.axis('off')
plt.show()

# save choropleth map to file
fig.savefig('data/lucky_choropleth_map.png', dpi=300, bbox_inches='tight')
