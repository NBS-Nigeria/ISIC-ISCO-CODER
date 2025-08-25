import folium

# Coordinates for Ceddi Plaza, Abuja
ceddi_plaza_coords = [9.0586, 7.4898]  # Latitude, Longitude

# Create a map centered around Ceddi Plaza
map_abuja = folium.Map(location=ceddi_plaza_coords, zoom_start=16)

# Add a marker for Ceddi Plaza
folium.Marker(
    location=ceddi_plaza_coords,
    popup='Ceddi Plaza, Central Business District, Abuja',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(map_abuja)

# Save the map to an HTML file
map_abuja.save('ceddi_plaza_map.html')
