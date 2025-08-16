#a series is a one dimensional array-like object that can hold any data type
import numpy as np
import pandas as pd 

label = ['a','b','c','d']
list = [12,21,43,22]
arr=np.array([3,5,2,4])
dic={'a':2,'b':1,'c':3,'d':7}

#creating a series from a list
print(pd.Series(list))
print(pd.Series(list,index=label))
print(pd.Series(dic))

