import pandas as pd

# Load the data
df = pd.read_csv('DOHMH_Dog_Bite_Data.csv')

# Count total bites per breed
breed_bite_counts = df['Breed'].value_counts()

# Show the top 15 breeds with the most bites
top_15_breeds = breed_bite_counts.head(15)
print(top_15_breeds)

