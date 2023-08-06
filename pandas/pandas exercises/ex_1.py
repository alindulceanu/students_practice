#Create a pandas series from each of the items below: a list, numpy and a dictionary

import pandas as pd
import numpy as np

mylist = list('abcedfghijklmnopqrstuvwxyz')
df = pd.Series(mylist)
print(df)

myarr = np.arange(26)
df = pd.Series(myarr)
print(df)

mydict = dict(zip(mylist, myarr))
df = pd.Series(mydict)
print(df)