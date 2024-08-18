import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('DOHMH_Dog_Bite_Data.csv')

# Show the first 100 unique 'Breed' values
unique_breeds = df['Breed'].unique()[:500]
for i, breed in enumerate(unique_breeds):
    print(f"{i}: {breed}")

# User input for selecting breeds
selected_breeds_indices = input("Enter the numbers of up to 4 breeds separated by spaces: ")
selected_breeds_indices = list(map(int, selected_breeds_indices.split()))
selected_breeds = [unique_breeds[i] for i in selected_breeds_indices]

# Filter data for selected breeds
filtered_df = df[df['Breed'].isin(selected_breeds)]

# Convert 'DateOfBite' to datetime
filtered_df['DateOfBite'] = pd.to_datetime(filtered_df['DateOfBite'])

# Group by month and breed
monthly_bites = filtered_df.groupby([filtered_df['DateOfBite'].dt.to_period('M'), 'Breed']).size().unstack(fill_value=0)

# Plot total bites for selected breeds
plt.figure(figsize=(12, 6))
linestyles = ['-', '--', '-.', ':']
for i, breed in enumerate(selected_breeds):
    plt.plot(monthly_bites.index.to_timestamp(), monthly_bites[breed], linestyle=linestyles[i], color='black', label=breed)
plt.legend()
plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Number of Bites')
plt.title('Monthly Dog Bites for Selected Breeds')

# Set 15 xticks
xticks = monthly_bites.index.to_timestamp()[::max(1, len(monthly_bites) // 15)]
plt.xticks(xticks, rotation=90)
plt.tight_layout()
safe_breeds = [breed.replace('/', '_') for breed in selected_breeds]
plt.savefig(str(safe_breeds)+'.png',dpi=300)
plt.show()

# Plot gender-specific bites for selected breeds
plt.figure(figsize=(12, 6))
for i, breed in enumerate(selected_breeds):
    breed_df = filtered_df[filtered_df['Breed'] == breed]
    gender_bites = breed_df.groupby([breed_df['DateOfBite'].dt.to_period('M'), 'Gender']).size().unstack(fill_value=0)
    if 'M' in gender_bites.columns:
        plt.plot(gender_bites.index.to_timestamp(), gender_bites['M'], linestyle=linestyles[i], linewidth=1, color='black', label=f'{breed} M')
    if 'F' in gender_bites.columns:
        plt.plot(gender_bites.index.to_timestamp(), gender_bites['F'], linestyle=linestyles[i], linewidth=2, color='black', label=f'{breed} F')
plt.legend()
plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Number of Bites')
plt.title('Monthly Dog Bites by Gender for Selected Breeds')

# Set 15 xticks
xticks = gender_bites.index.to_timestamp()[::max(1, len(gender_bites) // 15)]
plt.xticks(xticks, rotation=90)
plt.tight_layout()
plt.savefig(str(safe_breeds)+'-MF.png',dpi=300)
plt.show()

