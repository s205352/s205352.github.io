import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_csv("Police_Department_Incident_Reports__Historical_2003_to_May_2018_20240130.csv")

# Convert 'Date' to datetime
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year

# Filter for PROSTITUTION crimes between 2007 and 2017
filtered_df = data[(data['Category'] == 'PROSTITUTION') & 
                   (data['Year'] >= 2007) & 
                   (data['Year'] <= 2017)]

# Aggregate data by Year and Police District
prostitution_counts_by_year = filtered_df.groupby(['Year', 'PdDistrict']).size().reset_index(name='counts')

# Load your GeoJSON file for the police districts
geojson = 'sfpd.geojson'

# Create the choropleth map with a slider for each year
fig = px.choropleth_mapbox(prostitution_counts_by_year, geojson=geojson, locations='PdDistrict', color='counts',
                           color_continuous_scale="Viridis", range_color=[0, prostitution_counts_by_year['counts'].max()],
                           mapbox_style="carto-positron", zoom=11, center={"lat": 37.7749, "lon": -122.4194},
                           animation_frame='Year', opacity=0.5, labels={'counts': 'Prostitution Counts'})

fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})

# Save the plot to an HTML file
fig.write_html("3.html")

# Alternatively, if you wish to display the plot in a browser directly from the script, you can use:
fig.show()