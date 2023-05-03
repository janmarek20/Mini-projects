import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Analiza struktury danych.
filename = 'eq_data_30_day_m1.geojson'
with open(filename, encoding='utf8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

print(mags[:10])
print(lons[:5])
print(lats[:5])

#Mapa trzęsień ziemi.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': { 'title': "Siła" },
    },
}]
my_layout = Layout(title='Trzęsienia ziemi na świecie')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')