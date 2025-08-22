import numpy as np  
import pandas as pd 
import re

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
print("\nDataFrame after cleaning Episodes column:\n", df)


# print(type(df["Episodes"]))

def extract_time(txt):
    match = re.search(r"[A-Za-z]{3}\s\d{4}\s*[-–]\s*[A-Za-z]{3}\s\d{4}", str(txt))
    if match:
        return match.group(0)   # return the matched timestamp
    return None
