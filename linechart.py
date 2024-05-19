import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned data
cleaned_file_path = r'C:\Users\Tarun\Desktop\cleaned_data.csv'
df = pd.read_csv(cleaned_file_path)

# Group the data by age group and calculate the sum of disabled population for each category
age_group_population = df.groupby('Age-group').agg({
    'Total disabled population - Persons': 'sum',
    'Total disabled population - Males': 'sum',
    'Total disabled population - Females': 'sum'
}).reset_index()

# Plotting the line chart
plt.figure(figsize=(10, 6))

# Plot the line for total disabled population
plt.plot(age_group_population['Age-group'], age_group_population['Total disabled population - Persons'],
         marker='o', color='blue', label='Total')

# Plot the line for male disabled population
plt.plot(age_group_population['Age-group'], age_group_population['Total disabled population - Males'],
         marker='o', color='green', label='Male')

# Plot the line for female disabled population
plt.plot(age_group_population['Age-group'], age_group_population['Total disabled population - Females'],
         marker='o', color='red', label='Female')

# Add labels and title
plt.xlabel('Age Group')
plt.ylabel('Total Disabled Population')
plt.title('Trend of Disabled Population over Age Groups')

# Add legend
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Show grid
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
