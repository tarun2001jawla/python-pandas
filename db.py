import pandas as pd

# Specify the file path using a raw string literal (r'')
file_path = r'C:\Users\Tarun\Desktop\Office Work\India-disability-data.csv'

# Read the data
df = pd.read_csv(file_path)

# Drop NaN values
df = df.dropna()

# Fill NaN values with empty strings
df = df.fillna('')

# Remove duplicates
df = df.drop_duplicates()

# Remove rows with all 0 values
df = df[(df != 0).all(axis=1)]

# Save cleaned data to a new file
cleaned_file_path = r'C:\Users\Tarun\Desktop\cleaned_data.csv'
df.to_csv(cleaned_file_path, index=False)

# Print the first few rows of the cleaned DataFrame
print(df.head())

# Check for null values
print(df.isnull().sum())

# Check for duplicated rows
print(df.duplicated().sum())

# Check data types
print(df.dtypes)

# Basic statistics
print(df.describe())

# Plotting the data
import matplotlib.pyplot as plt

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
