import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation
new_password = ''.join(secrets.choice(characters) for x in range(18))

print(new_password)
