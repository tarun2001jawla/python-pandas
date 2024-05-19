import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned data
cleaned_file_path = r'C:\Users\Tarun\Desktop\cleaned_data.csv'
df = pd.read_csv(cleaned_file_path)

# Plotting the data
# Group the data by area name and sum the total disabled population
area_population = df.groupby('Area Name')['Total disabled population - Persons'].sum().reset_index()

# Plotting the bar chart
plt.figure(figsize=(12, 6))
plt.bar(area_population['Area Name'], area_population['Total disabled population - Persons'], color='blue')
plt.xlabel('Area')
plt.ylabel('Total Disabled Population')
plt.title('Total Disabled Population by Area')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
