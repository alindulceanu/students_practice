import secrets
import string 

password = secrets.token_hex(64)

print("password is:" + password)

url = secrets.token_urlsafe(64)

print(url)