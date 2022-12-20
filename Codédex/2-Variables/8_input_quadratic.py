import math

# User Input

username = input("Enter your name: ")
age = int(input("What's your age:"))

print(username + " " + str(age))

# Quadratic formula

print("Quadratic formula")
a = int(input("Enter a: "))             # 2
b = int(input("Enter b: "))             # 3
c = int(input("Enter c: "))             # 1

root1 = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
root2 = (-b-math.sqrt((b**2)-(4*a*c)))/(2*a)

print("root1: " + str(root1))           # -0.5
print("root2: " + str(root2))           # -1.0
