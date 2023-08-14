'''Compute the minimum, 25th percentile, median, 75th, and maximum of ser.
'''

import pandas as pd
import numpy as np

ser = pd.Series(np.random.normal(10, 5, 25))

print(ser.to_string)

print(np.percentile(ser, q = [0, 25, 50, 75, 100]))