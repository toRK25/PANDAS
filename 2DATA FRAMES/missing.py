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



#removing null value
df_dropped = df.dropna()
print("DataFrame after dropping rows with missing values:", df_dropped)

#remove a particular column
df_dropped_col = df.drop(columns=['B'])
print("DataFrame after dropping column 'B':", df_dropped_col)

dg= df.dropna(thresh=3)  # Drop rows with at least 2 non-NA values
print("DataFrame after dropping rows with at least 2 non-NA values:", dg)

# Selecting rows where COLUMN A is greater than 2
print('Selecting rows where COLUMN A is greater than 2',df[df['A'] > 2])  # Conditional selection based on a column value


#fill missing values with a specific value
df_filled = df.fillna(0) #columnwise fill with 0
print("DataFrame after filling missing values with 0:", df_filled)

#fill with particular values
value={'A': 0, 'B': 81, 'C': 22, 'D': 45}
df_filled_specific = df.fillna(value)  # Fill with specific values for each column
print("DataFrame after filling missing values with specific values:", df_filled_specific)