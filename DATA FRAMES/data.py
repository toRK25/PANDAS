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

print("WITH INDEXING \n",pd.DataFrame(list, columns=['Name', 'Age', 'City', 'Salary']))