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
