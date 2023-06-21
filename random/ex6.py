import string
import secrets

secret = secrets.SystemRandom()

source = string.ascii_letters + string.digits + string.punctuation

seq = secret.choice(string.ascii_uppercase)
seq += secret.choice(string.ascii_uppercase)
seq += secret.choice(string.digits)
seq += secret.choice(string.punctuation)

for i in range(6):
    seq += secret.choice(source)

chars = list(seq)

secret.shuffle(chars)

seq = ''.join(chars)

print(seq)