#creating a dataframe
# SELECTION AND INDEXING OF COLUMNS
# CREATING NEW COLUMNS
# REMOVING COLUMNS 
# SELECTING ROWS
# SELECTING SUBSET OF ROWS AND COLUMNS
# CONDITIONAL SELECTION

import numpy as np
import pandas as pd


#creating dataframes using dictonary

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}

print(pd.DataFrame(data))

#creating a dataframe from a list
list = [
    ['John', 28, 'New York', 65000],
    ['Anna', 34, 'Paris', 70000],
    ['Peter', 29, 'Berlin', 62000],
    ['Linda', 42, 'London', 85000]
]
print("WITHOUT INDEXING \n",pd.DataFrame(list))

columns = ["Name", "Age", "City", "Salary"]

df = pd.DataFrame(list,columns=columns)
print('WITH INDEXING\n',df)


#SELECTION AND INDEXING OF COLUMNS
print(df['Name'])  # Selecting a single column
print(df[['Name', 'City']])# Selecting multiple columns
print('\n',df.Name)  # Another way to select a single column
# CREATING NEW COLUMNS
df['Experience'] = [5, 10, 3, 15]  # Adding a new column
print('\n',df) 
print(df.drop('Experience', axis=1 ,inplace =True))  # Removing a column permanently
# print(df.drop('Experience', axis=1))  # Removing a column (note: use drop() method, not drop[])
print('\n',df) # experience is still there if you need to remove it permanently use keyword INPLACE = True

#for removing rows u just do axis = 0

#rows

print(df.loc[0])  # Selecting a single row by index
