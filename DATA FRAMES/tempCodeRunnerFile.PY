df_all = pd.merge(employees, salaries, how='outer')
print("\nMerged DataFrame with all rows:\n", df_all)
