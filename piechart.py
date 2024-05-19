import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned data
cleaned_file_path = r'C:\Users\Tarun\Desktop\cleaned_data.csv'
df = pd.read_csv(cleaned_file_path)

# Group the data by rural and urban areas
area_population = df.groupby('Total/ Rural/Urban')['Total disabled population - Persons'].sum()

# Plotting the pie chart
plt.figure(figsize=(8, 8))

# Define labels for the pie chart
labels = area_population.index

# Define sizes for each slice
sizes = area_population.values

# Define colors for each slice
colors = ['red', 'yellow', 'pink']

# Explode the slices (for highlighting)
explode = (0.01, 0.01, 0.01)

# Plot the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Add a title
plt.title('Proportion of Disabled Population in Rural and Urban Areas')

# Show the plot
plt.show()
