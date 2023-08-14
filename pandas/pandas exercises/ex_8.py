'''Calculte the frequency counts of each unique value ser.'''

import pandas as pd
import numpy as np

x = np.random.randint(8, size=30)

ser = pd.Series(np.take(list('abcdefgh'), x))

print(ser)

print(x)

print(ser.value_counts())