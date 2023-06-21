import secrets
import string

secret = secrets.SystemRandom()

seq = input('seq:')

print(secret.choice(seq))