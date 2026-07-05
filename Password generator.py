#password generator
import random
import string
letters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation
all=letters+numbers+symbols
password=""
length=int(input("Enter password length: "))
for i in range(len):
    password+=random.choice(all)
print(password)
