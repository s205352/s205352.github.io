import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Category20c
from math import pi

# Load the data (Ensure your path to the CSV file is correct)
df = pd.read_csv("Police_Department_Incident_Reports__Historical_2003_to_May_2018_20240130.csv")

# Convert 'Date' to datetime and filter the data
df['Date'] = pd.to_datetime(df['Date'])
filtered_df = df[(df['Category'] == 'PROSTITUTION') &
                 (df['Date'].dt.year >= 2007) & (df['Date'].dt.year <= 2017)]

# Function to prepare data for a given year
def prepare_data(year):
    year_df = filtered_df[filtered_df['Date'].dt.year == year]
    counts = year_df['PdDistrict'].value_counts().reset_index(name='Incidents')
    counts.columns = ['PdDistrict', 'Incidents']
    counts['Angle'] = counts['Incidents']/counts['Incidents'].sum() * 2*pi
    counts['Color'] = Category20c[len(counts) % 20]
    return counts

# Initial data preparation
initial_year = 2007
data = prepare_data(initial_year)

source = ColumnDataSource(data=data)

# Configure the output file (adjust the filename as necessary)
output_file("2.html")

# Create the pie chart
p = figure(height=350, title="Prostitution Incidents by District", toolbar_location=None,
           tools="", tooltips="@PdDistrict: @Incidents", x_range=(-0.5, 1.0))

p.add_tools(HoverTool(tooltips=[("District", "@PdDistrict"), ("Incidents", "@Incidents")]))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('Angle', include_zero=True), end_angle=cumsum('Angle'),
        line_color="white", fill_color='Color', legend_field='PdDistrict', source=source)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

# Show or save the plot
show(p)  # Opens the plot in a browser
# or use save(p) to save the plot to a file
