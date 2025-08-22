import pandas as pd
import numpy as np  

data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D', 'E'] * 4,
    'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 
               'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South',
               'East', 'West', 'North', 'South'],
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np.random.randint(10, 100, 20),
    'Rep': ['John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 
            'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice',
            'John', 'Mary', 'Bob', 'Alice']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

fog = pd.pivot_table(df,values = ['Sales', 'Units'],
                    index = ['Region'],
                    columns = ['Product'])
print("\nPivot Table:\n", fog)

dop = pd.crosstab(df['Region'], df['Product'])
print("\nCrosstab:\n", dop)