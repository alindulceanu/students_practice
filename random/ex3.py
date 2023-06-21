import random as r
import secrets
from string import digits

secret = secrets.SystemRandom()
password = ''

for i in range(6):
    password += secret.choice(digits)

print(password)
