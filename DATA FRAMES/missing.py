import numpy as np
import pandas as pd

#finding missing data

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan],
    'D': [1, np.nan, np.nan, np.nan, 5]
}

df = pd.DataFrame(data)
print("Original DataFrame:",df)

# Check for missing values
print(df.isnull())
# Count missing values in each column
print(df.isnull().sum())
# Count total missing values
print(df.isnull().sum().sum())
# Percentage of missing values in each column
print(df.isnull().mean() * 100)     
#Check any null value
print(df.isnull().any())


#fill missing values with a specific value
df_filled = df.fillna(0)
print("DataFrame after filling missing values with 0:", df_filled)
#removing null value
df_dropped = df.dropna()
print("DataFrame after dropping rows with missing values:", df_dropped)