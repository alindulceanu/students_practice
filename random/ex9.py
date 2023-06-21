import random
import secrets

for i in range(5):
    random.seed(99)
    print(random.choice(range(1, 7)))