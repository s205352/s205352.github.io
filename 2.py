import pandas as pd
import urllib.request
import io
from bokeh.plotting import figure, show, output_file
from bokeh.transform import cumsum
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category20c, Turbo256
from bokeh.layouts import gridplot
from math import pi

# Specify the URL of your CSV data
url = "https://data.sfgov.org/resource/tmnf-yvry.csv?$limit=3000000"

# Use urllib to load the CSV data from the URL
with urllib.request.urlopen(url) as response:
    csv_data = response.read().decode('utf-8')

# Load the data into a DataFrame and convert column names to lowercase
df = pd.read_csv(io.StringIO(csv_data))
df.columns = df.columns.str.lower()

# Convert 'date' to datetime and filter the data for 'prostitution' between 2008 and 2017
df['date'] = pd.to_datetime(df['date'])
filtered_df = df[(df['category'] == 'PROSTITUTION') & (df['date'].dt.year >= 2008) & (df['date'].dt.year <= 2017)]

# Identify all unique districts and create a consistent color mapping
unique_districts = sorted(filtered_df['pddistrict'].unique())
max_colors = len(Turbo256)  # Using a larger palette if there are more than 20 districts
palette_size = min(len(unique_districts), max_colors)
color_map = {district: Turbo256[i * int(max_colors / palette_size)] for i, district in enumerate(unique_districts)}

# Function to prepare data for a given year
def prepare_data(year):
    year_df = filtered_df[filtered_df['date'].dt.year == year]
    counts = year_df['pddistrict'].value_counts().reset_index(name='incidents')
    counts.columns = ['pddistrict', 'incidents']
    counts['angle'] = counts['incidents']/counts['incidents'].sum() * 2*pi
    # Apply the consistent color mapping
    counts['color'] = counts['pddistrict'].map(color_map)
    return counts

# Create the grid of pie charts
pie_charts = []
for year in range(2008, 2018):
    data = prepare_data(year)
    source = ColumnDataSource(data=data)
    p = figure(height=350, width=350, title=f"Prostitution Incidents by District {year}", 
               tools="", tooltips="@pddistrict: @incidents", x_range=(-0.5, 1.0))
    p.wedge(x=0, y=1, radius=0.4, 
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='pddistrict', source=source)
    p.axis.axis_label=None
    p.axis.visible=False
    p.grid.grid_line_color=None
    pie_charts.append(p)

# Configure the output file (adjust the filename as necessary)
output_file("2.html")

# Create the grid layout of pie charts
grid = gridplot(pie_charts, ncols=2)  # Adjust the number of columns as needed

# Show the grid layout
show(grid)