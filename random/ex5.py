from string import ascii_letters
import secrets

secret = secrets.SystemRandom()

seq = ''

for i in range(5):
    seq += secret.choice(ascii_letters)

print(seq)