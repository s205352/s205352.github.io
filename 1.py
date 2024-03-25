import pandas as pd
import io
import urllib.request
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

# URL of the CSV data
url = "https://data.sfgov.org/resource/tmnf-yvry.csv?$limit=3000000"

# Use urllib to load the CSV data from the URL
with urllib.request.urlopen(url) as response:
    csv_data = response.read().decode('utf-8')

# Convert the string data to a pandas DataFrame
data = pd.read_csv(io.StringIO(csv_data))

# Ensure the category matches your dataset. Adjust 'category' to the correct column name if needed.
# Filter data for 'PROSTITUTION' incidents only
data = data[data['category'] == 'PROSTITUTION']

# Assuming 'date' is the correct column, if it's different adjust accordingly.
# Convert "Date" column to datetime format
data['date'] = pd.to_datetime(data['date'])

# Filter data to include only the dates from 2008 to 2017
data = data[(data['date'].dt.year >= 2008) & (data['date'].dt.year <= 2017)]

# Extract year from "Date" and create a new column
data['year'] = data['date'].dt.year

# Group data by year and count incidents
# Adjust 'incidntnum' to the column that uniquely identifies incidents, if different.
grouped_data = data.groupby('year').count()['incidntnum']

# Setting up the output file (this will save the plot as HTML)
output_file("1.html")

# Preparing data for Bokeh plotting
source = ColumnDataSource(data=dict(years=[str(x) for x in grouped_data.index], counts=grouped_data.values))

# Creating a new plot with a title and axis labels
p = figure(x_range=source.data['years'], title="Prostitution Incidents from 2007 to 2017 in San Francisco",
           x_axis_label='Year', y_axis_label='Number of Incidents', height=400, tools="")

# Adding a bar renderer to the plot
p.vbar(x='years', top='counts', width=0.9, source=source, legend_label="Incidents")

# Customize the plot
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.xaxis.major_label_orientation = 1.2  # Rotate the x-axis labels for better readability

# Display the plot
show(p)
