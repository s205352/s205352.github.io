from bokeh.io import output_file, show
from bokeh.layouts import row
from bokeh.plotting import figure

import urllib.request
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("Police_Department_Incident_Reports__Historical_2003_to_May_2018_20240130.csv")

df.head()

focuscrimes = set(['WEAPON LAWS', 'PROSTITUTION', 'DRIVING UNDER THE INFLUENCE', 
                   'ROBBERY', 'BURGLARY', 'ASSAULT', 'DRUNKENNESS', 
                   'DRUG/NARCOTIC', 'TRESPASS', 'LARCENY/THEFT', 'VANDALISM', 
                   'VEHICLE THEFT', 'STOLEN PROPERTY', 'DISORDERLY CONDUCT'])

# Filter the DataFrame for focus crimes only
df = df[df['Category'].isin(focuscrimes)]

# Convert Date column to datetime if not already
df['Date'] = pd.to_datetime(df['Date'])

# Filter for years 2010-2017
df = df[(df['Date'].dt.year >= 2010) & (df['Date'].dt.year <= 2017)]

# Assume Time is in HH:MM format; extract hour
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour

# Group by Category and Hour, then count incidents
grouped = df.groupby(['Category', 'Hour']).size().reset_index(name='Count')

# Calculate total incidents per category
total_counts = df.groupby('Category').size().reset_index(name='TotalCount')

# Merge back to get total counts per category
grouped = grouped.merge(total_counts, on='Category')

# Normalize counts
grouped['NormalizedCount'] = grouped['Count'] / grouped['TotalCount']

from bokeh.models import ColumnDataSource

# Ensure the hour column is of type string for Bokeh's x_range
grouped['Hour'] = grouped['Hour'].astype(str)

# Pivot the DataFrame for easier plotting with Bokeh
pivot_df = grouped.pivot(index='Hour', columns='Category', values='NormalizedCount').reset_index()

# Convert pivoted DataFrame to ColumnDataSource
source = ColumnDataSource(pivot_df)

from bokeh.plotting import figure
from bokeh.models import FactorRange
from bokeh.io import output_file, show

# Create a list of hours as strings
hours = [str(hour) for hour in range(24)]

# Initialize the figure
p = figure(title="Normalized Crime Distribution by Hour",
           x_axis_label='Hour of Day',
           y_axis_label='Normalized Crime Count',
           x_range=FactorRange(factors=hours),
           height=400,  # Changed from plot_height to height
           width=800,   # Changed from plot_width to width
           tools="pan,wheel_zoom,box_zoom,reset")

# Ensure the x-axis labels are readable
p.xaxis.major_label_orientation = 1

from bokeh.models import Legend, LegendItem
from bokeh.layouts import layout

# Assuming p is your figure and bar is your dictionary of vbars

# Create an empty list for legend items
legend_items = []

# Loop through the bars dictionary to populate legend_items
for category, glyph in bar.items():
    legend_items.append((category, [glyph]))

# Remove the old legend, if it exists
if p.legend:
    p.legend.items = []

# Create a new legend with the legend items
new_legend = Legend(items=legend_items, location=(10, 0))

# Assign the legend to the outside of the plot
new_legend.orientation = "vertical"

# Add the legend to the plot, but ensure it does not overlap the plot
p.add_layout(new_legend, 'left')

# Make the legend interactive
p.legend.click_policy = "mute"

# Set up the layout with the plot and place the legend next to it
# Note: we don't need to create a new layout since we added the legend to the plot
output_file("periodic1.html")
save(p)