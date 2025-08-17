#concatate two dataframes
import numpy as np
import pandas as pd
# First DataFrame
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2'],
    'C': ['C0', 'C1', 'C2']
})

print("First DataFrame:\n", df1)

# Second DataFrame
df2 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5'],
    'C': ['C3', 'C4', 'C5']
})

print("\nSecond DataFrame:\n", df2)

con = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenated DataFrame:\n", con)