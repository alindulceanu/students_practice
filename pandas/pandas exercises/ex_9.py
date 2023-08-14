'''From ser, keep the top 2 most frequent items as it is and replace everything else as ‘Other’.'''

import pandas as pd
import numpy as np

np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'

print(ser)
