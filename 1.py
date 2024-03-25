import pandas as pd
import matplotlib.pyplot as plt
from bokeh.io import output_file, show

output_file("1.html")

#Load the data
data = pd.read_csv("Police_Department_Incident_Reports__Historical_2003_to_May_2018_20240130.csv")

#Filter data for 'LARCENY/THEFT' incidents only
data = data[data['Category'] == 'PROSTITUTION']

#Convert "Date" column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

#Filter data to include only the dates from November 20th to December 31st for each year from 2012 to 2017
data = data[(data['Date'].dt.month == 11) & (data['Date'].dt.day >= 20) | (data['Date'].dt.month == 12)]
data = data[(data['Date'].dt.year >= 2007) & (data['Date'].dt.year <= 2017)]

#Extract year from "Date" and create a new column
data['Year'] = data['Date'].dt.year

#Group data by year and count incidents
grouped_data = data.groupby('Year').count()['IncidntNum']

#Plotting
fig, ax = plt.subplots(figsize=(10, 6))
grouped_data.plot(kind='bar', color='skyblue', edgecolor='darkblue', ax=ax)
ax.set_title('Prostitution Incidents from 2007 to 2017 in San Francisco', fontsize=16)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Incidents', fontsize=12)
plt.xticks(rotation=45)
plt.show()