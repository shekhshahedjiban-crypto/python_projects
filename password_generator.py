import secrets #secrets module is imported to generate random secure passwords
import string #string module for the string constants like ascii_letters and digits

# Combine letters and numbers into a single pool
pool = string.ascii_letters + string.digits #pool variable is created for the combuination of letters and numbers to generate a secure password

# Securely generate a 12-character random password
password = "".join(secrets.choice(pool) for _ in range(12))#it is used for generating a random password of length 12 by selecting random characters from the pool of letters and numbers

print("Your password is:", password) #print the generated password as output to user