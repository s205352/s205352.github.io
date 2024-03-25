import pandas as pd
import urllib.request
import io
from bokeh.io import curdoc
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.models import ColumnDataSource, HoverTool, Slider
from bokeh.palettes import Category20c
from bokeh.layouts import layout
from math import pi

# Specify the URL of your CSV data
url = "https://data.sfgov.org/resource/tmnf-yvry.csv?$limit=3000000"

# Use urllib to load the CSV data from the URL
with urllib.request.urlopen(url) as response:
    csv_data = response.read().decode('utf-8')

# Load the data into a DataFrame and convert column names to lowercase
df = pd.read_csv(io.StringIO(csv_data))
df.columns = df.columns.str.lower()

# Convert 'date' to datetime and filter the data for 'prostitution' between 2007 and 2017
df['date'] = pd.to_datetime(df['date'])
filtered_df = df[(df['category'] == 'PROSTITUTION') & (df['date'].dt.year >= 2007) & (df['date'].dt.year <= 2017)]

# Function to prepare data for a given year
def prepare_data(year):
    year_df = filtered_df[filtered_df['date'].dt.year == year]
    counts = year_df['pddistrict'].value_counts().reset_index(name='incidents')
    counts.columns = ['pddistrict', 'incidents']
    counts['angle'] = counts['incidents']/counts['incidents'].sum() * 2*pi
    counts['color'] = Category20c[len(counts) % 20]
    return counts

# Initial data preparation
initial_year = 2007
data = prepare_data(initial_year)

source = ColumnDataSource(data=data)

# Configure the output file (adjust the filename as necessary)
output_file("2.html")

# Create the pie chart
p = figure(height=350, title="Prostitution Incidents by District", toolbar_location=None,
           tools="", tooltips="@pddistrict: @incidents", x_range=(-0.5, 1.0))

p.add_tools(HoverTool(tooltips=[("District", "@pddistrict"), ("Incidents", "@incidents")]))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='pddistrict', source=source)

p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color=None

# Slider callback function
def update_chart(attr, old, new):
    year = slider.value
    new_source = ColumnDataSource(data=prepare_data(year))
    source.data = new_source.data

# Year slider
slider = Slider(start=2007, end=2017, value=initial_year, step=1, title="Year")
slider.on_change('value', update_chart)

# Add layout
lay = layout([[slider], [p]])

# Add the layout to the current document
curdoc().add_root(lay)

# Show or save the plot
show(p)  # Opens the plot in a browser
