# Tip Calculator

print("Welcome to tip calculator!")
bill = input("What was the total bill? ")
percentage = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")
number = input("How many people to split the bill? ")
answer = "{:.2f}".format(
    (float(bill) * (1 + (float(percentage) / 100))) / float(number))
print(f"Each person should pay: ${answer}")
