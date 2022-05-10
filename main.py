#!/usr/bin/env python3

import pandas as pd
import folium
from geopy.geocoders import Nominatim

def get_locations(file):
    pass

geolocator = Nominatim(user_agent="hien_foo")
montreal = geolocator.geocode("Montreal, Quebec, Canada")
map = folium.Map(location=[montreal.latitude, montreal.longitude], tiles='Stamen Terrain', zoom_start=12)

# Define some locations
get_locations("ilots.csv")

df = pd.read_csv("ilots.csv")
for index, row in df.iterrows():
    print(f"Add marker to map: {row['ilot']} -at- {row['adresse']}")
    marker = geolocator.geocode(row['adresse'])
    folium.Marker([marker.latitude, marker.longitude], 
        popup=f"<strong>{row['ilot']}</strong><br>{row['adresse']}", 
        tooltip=f"{row['ilot']}"
    ).add_to(map)

#fermette = geolocator.geocode("1900, rue Le Ber, Montreal, Quebec")
#folium.Marker([fermette.latitude, fermette.longitude], popup=f"{fermette.address}", tooltip='Click Me!').add_to(map)
#goupillier = geolocator.geocode("4161, 54e Rue, Montreal, Quebec")
#folium.Marker([goupillier.latitude, goupillier.longitude], popup=f"{goupillier.address}", tooltip='Click Me!').add_to(map)
#plaza = geolocator.geocode("Metro Jean-Talon, Montreal, Quebec")
#folium.Marker([plaza.latitude, plaza.longitude], popup=f"{plaza.address}", tooltip='Click Me!').add_to(map)
#ecopivot = geolocator.geocode("400, Avenue Atlantic, Montreal, Quebec")
#map
map.save('index.html')
print('\nDone!\n')