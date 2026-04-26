from pathlib import Path
import json

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
    

print(mags[:10])
print(lons[:5])
print(lats[:5])