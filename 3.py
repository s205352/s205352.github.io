import pandas as pd
import plotly.express as px
import urllib.request
import json  # For loading GeoJSON content
import io

# URL of the CSV data for incidents
data_url = "https://data.sfgov.org/resource/tmnf-yvry.csv?$limit=3000000"

# URL of the GeoJSON data for police districts
geojson_url = "https://raw.githubusercontent.com/suneman/socialdata2022/main/files/sfpd.geojson"

# Use urllib to load the CSV data from the data_url
with urllib.request.urlopen(data_url) as response:
    csv_data = response.read().decode('utf-8')

# Load the data into a DataFrame and convert column names to lowercase
data = pd.read_csv(io.StringIO(csv_data))
data.columns = data.columns.str.lower()

# Convert 'date' to datetime, then extract year, filtering for 'prostitution' between 2008 and 2017
data['date'] = pd.to_datetime(data['date'])
data['year'] = data['date'].dt.year
filtered_df = data[(data['category'].str.upper() == 'PROSTITUTION') & 
                   (data['year'] >= 2008) & 
                   (data['year'] <= 2017)]

# Aggregate data by Year and Police District, converting all relevant references to lowercase
prostitution_counts_by_year = filtered_df.groupby(['year', 'pddistrict']).size().reset_index(name='counts')

# Use urllib to load the GeoJSON data from the geojson_url
with urllib.request.urlopen(geojson_url) as response:
    geojson = json.load(response)

# Create the choropleth map with a slider for each year
fig = px.choropleth_mapbox(prostitution_counts_by_year, geojson=geojson, locations='pddistrict', color='counts',
                           color_continuous_scale="Viridis", range_color=[0, prostitution_counts_by_year['counts'].max()],
                           mapbox_style="carto-positron", zoom=11, center={"lat": 37.7749, "lon": -122.4194},
                           animation_frame='year', opacity=0.5, labels={'counts': 'Prostitution Counts'})

fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
# Save the plot to an HTML file named "3.html"
fig.write_html("3.html")
