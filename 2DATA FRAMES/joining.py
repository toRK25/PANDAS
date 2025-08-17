#joining two data frames
import numpy as np      
import pandas as pd

grades = pd.DataFrame({
    'student': ['Alice', 'Bob', 'Charlie', 'David'],
    'math': [85, 90, 78, 92],
    'science': [88, 76, 95, 89]
})


sales = pd.DataFrame({
    'product': ['A', 'B', 'C', 'D'],
    'units_sold': [100, 150, 200, 130],
    'price': [10, 15, 20, 12]
})

df = grades.join(sales)
print("\nJoined DataFrame:\n", df)
