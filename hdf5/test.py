#!/usr/bin/env python3

import h5py
import numpy as np

d1 = np.random.random(size = (1000,20))
d2 = np.random.random(size = (1000,200))

hf = h5py.File('data.h5', 'r, w')

g1 = hf.create_group('group1')
g2 = hf.create_group('group2/subfolder')

g2.create_dataset('ds_1', data = d1)
g2.create_dataset('ds_2', data = d2)

g3 = hf.get('group2/subfolder')

print(g3.items())

n1 = g1.get('ds_1')

n1 = np.array(n1)

hf.close()

print(n1.shape)



