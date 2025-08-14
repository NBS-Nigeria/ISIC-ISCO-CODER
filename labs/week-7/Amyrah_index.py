import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Read the underemployment CSV file
underemployment_df = pd.read_csv(r"C:\Users\user\Documents\ISIC-ISCO-CODER\labs\week-7\data\underemployment.csv")

# Read the Nigeria GeoJSON file
nigeria = gpd.read_file(r"C:\Users\user\Documents\ISIC-ISCO-CODER\labs\week-7\data\Nigerian_states.geojson.geojson")

print(nigeria.columns)
print(underemployment_df.columns)

# Merge datasets
merge = nigeria.merge(underemployment_df, left_on='state', right_on='statename')
merge.head()

# Rename 'rate' to 'Underemployment_rate'
merge = merge.rename(columns={'rate': 'Underemployment_rate'})
merge.head()

# Create a choropleth map
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
merge.plot(column='Underemployment_rate', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title('Underemployment Rate by State in Nigeria')
ax.axis('off')
plt.savefig(r"C:\Users\user\Documents\ISIC-ISCO-CODER\data\Amyrah_Choropleth_Map.png", bbox_inches='tight')
plt.show()

# Save the merged DataFrame
merge.to_csv(r"C:\Users\user\Documents\ISIC-ISCO-CODER\data\Amyrah_Merged_Nigeria_underemployment.csv", index=False)