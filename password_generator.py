import secrets
import string

# Combine letters and numbers into a single pool
pool = string.ascii_letters + string.digits

# Securely generate a 12-character random password
password = "".join(secrets.choice(pool) for _ in range(12))

print("Your password is:", password)