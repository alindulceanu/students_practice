import random as r

x = r.sample(range(1000000000, 10000000000), 1000)
print(r.sample(x, 2))