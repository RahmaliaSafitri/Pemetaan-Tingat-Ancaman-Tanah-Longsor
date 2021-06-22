import pandas as pd
import geopandas as gpd

from sklearn.cluster import KMeans
import folium
import pickle

import warnings
warnings.filterwarnings('ignore')

path = './KAB. SINJAI/ADMINISTRASIKECAMATAN_AR_50K.shp'
data_kota = gpd.read_file(path)

data = pd.read_excel('Data Skripsi Anwar.xlsx')
df = data[['Kecamatan', 'Botot_Kelurusan', 'Bobot_Elevasi', 'Bobot_Geologi', 'Bobot_jalan',
    'Bobot_Kel', 'Bobot_Lahan', 'Bobot_Sungai', 'Bobot_tanah', 'Bobot_hujan','Bobot_Aspek']]

kmeans = KMeans(n_clusters=3).fit(df.iloc[: , 1:])
df['Clusters'] = kmeans.labels_
shp_file_json_str = data_kota.to_json()


sinjai_map = folium.Map(location=[-5.217196, 120.112735] , zoom_start=11, tiles='cartodbpositron')

# generate choropleth map 
choropleth = folium.Choropleth(
    geo_data=shp_file_json_str,
    data=df,
    columns=['Kecamatan', 'Clusters'],
    key_on='feature.properties.NAMOBJ',
    fill_color="YlGn",
    bins=[0, 1, 2, 3],
    line_opacity=0,
    nan_fill_color='gray'
).add_to(sinjai_map)

# add labels indicating the name of the community
style_function = "font-size: 15px; font-weight: bold"
choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['NAMOBJ'], style=style_function, labels=False))

# create a layer control
folium.LayerControl().add_to(sinjai_map)
sinjai_map.save('map.html')

pickle.dump(kmeans, open('kmeans.pkl', 'wb'))

