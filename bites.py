import pandas as pd

# Load the data
df = pd.read_csv('DOHMH_Dog_Bite_Data.csv')

# Count total bites per breed
breed_bite_counts = df['Breed'].value_counts()

# Show the top 10 breeds with the most bites
top_10_breeds = breed_bite_counts.head(10)
print(top_10_breeds)

