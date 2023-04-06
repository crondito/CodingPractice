# Password Generator Project

import random

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password? \n"))
symbols = int(input("How many symbols would you like? \n"))
numbers = int(input("How many numbers would you like? \n"))

password = ""

for i in range(letters):
    password += chr(random.randint(65, 122))

for i in range(symbols):
    password += chr(random.randint(33, 47))

for i in range(numbers):
    password += chr(random.randint(48, 57))

shuffled_password = list(password)
random.shuffle(shuffled_password)
print("Here is your password: " + ''.join(shuffled_password))
