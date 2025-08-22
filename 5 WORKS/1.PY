import numpy as np  
import pandas as pd 
import re   

# re means Regular Expression module in Python.
# A regular expression (often written as regex) is like a special search pattern.It helps you find or extract parts of text (like years, dates, numbers, words, etc.) from a string.

df = pd.read_csv('anime.csv')
# print("Original DataFrame:\n", df)  #head shows first 5 rows

def extract_episodes(txt):
    check = False
    data = ""
    for i in txt:
        if i == ')':   # <-- यहाँ bug fix किया
            check = False
            break
        if i == '(':
            check = True
            continue
        if check:
            data += i
    return data

df["Episodes"] = df["Title"].apply(extract_episodes)
# print("\nDataFrame after extracting Episodes:\n", df)

df["Episodes"]= df["Episodes"].str.replace(" eps", "", regex=False).astype(int)
# print("\nDataFrame after cleaning Episodes column:\n", df)


# print(type(df["Episodes"]))

def extract_time(txt):
    match = re.search(r"[A-Za-z]{3}\s\d{4}\s*[-–]\s*[A-Za-z]{3}\s\d{4}", str(txt))
    if match:
        return match.group(0)   # return the matched timestamp
    return None

df['Total Time'] = df['Title'].apply(extract_time)

# print(df[['Title', 'Time']].head(10))
# print(df.drop('Time', axis=1, inplace=True))
# print("\nDataFrame after extracting Time column:\n", df)

# Overwrite the same CSV file
# df.to_csv("anime.csv", index=False)

print(df[df['Score'] == df['Score'].max()].head())
