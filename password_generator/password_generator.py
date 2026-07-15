import secrets #secrets module is imported to generate random secure passwords
import string #string module for the string constants like ascii_letters and digits

# Combine letters and numbers into a single pool
pool = string.ascii_letters + string.digits #pool variable is created for the combination of letters and numbers to generate a secure password
password ="" #password variable is initialized as an empty string to store the generated password
for i in range(12): #loop is used to generate a password of length 12 characters
    password += secrets.choice(pool) #secrets.choice() is used to select a random character from the pool and add it to the password variable

print("Your password is:", password) #print the generated password as output to user
