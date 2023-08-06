'''Combine ser1 and ser2 to form a dataframe.'''

import pandas as pd
import numpy as np

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df = pd.concat([ser1, ser2], axis = 1)

print(df)

