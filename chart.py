import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned data
cleaned_file_path = r'C:\Users\Tarun\Desktop\cleaned_data.csv'
df = pd.read_csv(cleaned_file_path)

# Group the data by state name
state_population = df.groupby('Area Name').sum()

# Plotting the grouped bar chart
plt.figure(figsize=(12, 6))

# Get the states and the number of states
states = state_population.index
num_states = len(states)

# Define the width of each bar
bar_width = 0.35

# Set the index for the x-axis
index = range(num_states)

# Plot the bars for males
plt.bar(index, state_population['Total disabled population - Males'], bar_width, label='Male')

# Plot the bars for females
plt.bar([i + bar_width for i in index], state_population['Total disabled population - Females'], bar_width, label='Female')

# Set the x-axis labels
plt.xlabel('State')
plt.ylabel('Total Disabled Population')
plt.title('Total Disabled Population by Gender and State')
plt.xticks([i + bar_width / 2 for i in index], states, rotation=90)
plt.legend()

plt.tight_layout()
plt.show()
