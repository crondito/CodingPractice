import random

# RNGesus will give us a random number that is either 0 or 1
grade = random.randint(1, 100)

if grade >= 55:
    print(f'----> You passed with {grade}')
else:
    print(f'----> You failed with {grade}')
