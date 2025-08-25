import folium
from flask import Flask, render_template_string

app = Flask(__name__)

# Coordinates for landmarks
ceddi_plaza = [9.0586, 7.4898]
nnpc_towers = [9.0582, 7.4891]
national_mosque = [9.0579, 7.4899]

# Create map
m = folium.Map(location=ceddi_plaza, zoom_start=16)

# Add custom markers
folium.Marker(
    ceddi_plaza,
    popup='Ceddi Plaza',
    icon=folium.Icon(color='blue', icon='shopping-cart', prefix='fa')
).add_to(m)

folium.Marker(
    nnpc_towers,
    popup='NNPC Towers',
    icon=folium.Icon(color='green', icon='building', prefix='fa')
).add_to(m)

folium.Marker(
    national_mosque,
    popup='National Mosque',
    icon=folium.Icon(color='red', icon='star', prefix='fa')
).add_to(m)

# Add a layer control
folium.LayerControl().add_to(m)

# Render map as HTML string
map_html = m._repr_html_()

@app.route('/')
def index():
    return render_template_string("""
    <html>
    <head>
        <title>Ceddi Plaza & Landmarks Map</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h2>Ceddi Plaza and Nearby Landmarks, Abuja</h2>
        {{ map_html|safe }}
    </body>
    </html>
    """, map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)