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
    print(f"{row['ilots']}, {row['adresse']}")

fermette = geolocator.geocode("1900, rue Le Ber, Montreal, Quebec")
folium.Marker([fermette.latitude, fermette.longitude], popup=f"{fermette.address}", tooltip='Click Me!').add_to(map)

goupillier = geolocator.geocode("4161, 54e Rue, Montreal, Quebec")
folium.Marker([goupillier.latitude, goupillier.longitude], popup=f"{goupillier.address}", tooltip='Click Me!').add_to(map)

plaza = geolocator.geocode("Metro Jean-Talon, Montreal, Quebec")
folium.Marker([plaza.latitude, plaza.longitude], popup=f"{plaza.address}", tooltip='Click Me!').add_to(map)

ecopivot = geolocator.geocode("400, Avenue Atlantic, Montreal, Quebec")
folium.Marker([ecopivot.latitude, ecopivot.longitude], popup=f"{ecopivot.address}", tooltip='Click Me!', icon=folium.Icon(color="red", icon="info-sign")).add_to(map)

#map
map.save('index.html')
print('\nDone!\n')