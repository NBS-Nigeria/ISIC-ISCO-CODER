#Loading necessary libraries
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


# Reading the underemployment CSV file data
df_under = pd.read_csv('data/underemployment.csv')  

# Reading the Nigeria states GeoJSON
gdf_states = gpd.read_file('data/nigeria_geo.json')

## Inspecting dataset
print(df_under.head())
print(gdf_states.head())

# Check for matching naming conventions
print(set(df_under['statename']) - set(gdf_states['state']))
print(set(gdf_states['state']) - set(df_under['statename']))

#Cleaning spelling mismatch statename to state
df_under['state'] = df_under['statename'].str.title().str.strip()
gdf_states['state'] = gdf_states['state'].str.title().str.strip()


#Merging datasets using state join
gdf_merged = gdf_states.merge(df_under, on='state', how='left')
# Check for missing values post-merge
print(gdf_merged[gdf_merged['rate'].isnull()])

#Inspect merged dataset
gdf_merged.head()

#Creating choropleth map
fig, ax = plt.subplots(1, 1, figsize=(12, 10))
gdf_merged.plot(
    column='rate',
    cmap='OrRd',              # Color palette
    scheme='Quantiles',       # Or 'Equal_interval'
    k=5,
    legend=True,
    edgecolor='black',
    linewidth=0.4,
    ax=ax
)
ax.set_title('Underemployment Rate by State – Nigeria (2023)', fontsize=16)
ax.axis('off')

# Get legend and reposition
legend = ax.get_legend()
legend.set_bbox_to_anchor((0, 1))  # (x, y) coordinates relative to plot
legend.set_frame_on(True)          # Show frame around legend

# Save before plt.show()
plt.savefig('underemployment_map.jpg', dpi=300, bbox_inches='tight')  
plt.show()