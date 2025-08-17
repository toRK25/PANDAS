#merging , joining and concatenating dataframes
import numpy as np
import pandas as pd     

# Create two DataFrames

# DataFrame 1: Employee information
employees = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Anna', 'Peter', 'Linda', 'Bob'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR']
})

print("Employees DataFrame:\n", employees)

# DataFrame 2: Salary information
salaries = pd.DataFrame({
    'employee_id': [1, 2, 3, 6, 7],
    'salary': [60000, 80000, 65000, 70000, 90000],
    'bonus': [5000, 10000, 7000, 8000, 12000]
})

print("\nSalaries DataFrame:\n", salaries)

df = pd.merge (employees, salaries)
print("\nMerged DataFrame:\n", df)
# #merge all dataframes rows
df_all = pd.merge(employees, salaries, how='outer')
print("\nMerged DataFrame with all rows:\n", df_all)

# Merge with salaries
df2 = pd.merge(employees, salaries, how='left')
print("\nLeft Join DataFrame:\n", df2)

#merge with employee id
df3 = pd.merge(employees, salaries, how='right')
print("\nRight Join DataFrame:\n", df3)