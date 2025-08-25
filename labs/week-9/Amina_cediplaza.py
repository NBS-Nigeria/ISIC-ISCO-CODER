import folium

# Coordinates for Ceddi Plaza, Abuja
ceddi_plaza_coords = [9.0586, 7.4898]  # Latitude, Longitude
nnpc_towers = [9.0582, 7.4891]
national_mosque = [9.0579, 7.4899]

# Use a direct image URL of Ceddi Plaza
ceddi_image_url = 'https://www.mecsr.org/directory-shopping-centres/ceddi-plaza'

# Add a marker for Ceddi Plaza with an image and a link in the popup
ceddi_popup_html = f"""
<b>Ceddi Plaza, Central Business District, Abuja</b><br>
<img src="{ceddi_image_url}" alt="ceddiplaza3" style="width:300px; border:2px solid #555; margin:5px 0;"><br>
<a href="{ceddi_image_url}" target="_blank">View Larger Image</a><br>
<a href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStMmidOEUlAsvmJS2LJK4Ti3vvJxtDDrtCsA&s" target="_blank">Visit Ceddi Plaza Website</a>
"""

# Create a map centered around Ceddi Plaza
map_abuja = folium.Map(location=ceddi_plaza_coords, zoom_start=16)

folium.Marker(
    location=ceddi_plaza_coords,
    popup=folium.Popup(ceddi_popup_html, max_width=250),
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(map_abuja)

folium.Marker(
    nnpc_towers,
    popup='NNPC Towers',
    icon=folium.Icon(color='green', icon='building', prefix='fa')
).add_to(map_abuja)

folium.Marker(
    national_mosque,
    popup='National Mosque',
    icon=folium.Icon(color='red', icon='star', prefix='fa')
).add_to(map_abuja)

# Save the map to an HTML file
map_abuja.save('ceddi_plaza_map.html')
