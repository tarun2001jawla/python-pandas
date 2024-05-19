import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned data
cleaned_file_path = r'C:\Users\Tarun\Desktop\cleaned_data.csv'
df = pd.read_csv(cleaned_file_path)

# Extract age and total disabled population columns
age_population = df[['Age-group', 'Total disabled population - Persons']]

# Rename the columns for simplicity
age_population.columns = ['Age', 'Total Disabled Population']

# Plotting the scatter plot
plt.figure(figsize=(10, 6))

# Scatter plot of age vs total disabled population
plt.scatter(age_population['Age'], age_population['Total Disabled Population'], color='blue', alpha=1)

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Total Disabled Population')
plt.title('Relationship between Age and Disabled Population')

# Show grid
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
