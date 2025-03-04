import random
import string
password_len=12
chrvalue= string.ascii_letters+string.digits+string.punctuation
password=""
for num in range(password_len):
    password+=random.choice(chrvalue)
print("Your random password is:",password)