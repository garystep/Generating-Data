from pathlib import Path
import json

import plotly.express as px

# Read the data from the JSON file.
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
eq_data = json.loads(contents)

# create a more readable format of the data.
all_eq_dicts = eq_data['features']
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    
title = 'Global Earthquakes'    
fig = px.scatter_geo(lat=lats, lon=lons, color=mags, size=mags,
                         color_continuous_scale='Viridis',
                         range_color=(0, 10),
                         title=title)

fig.show()