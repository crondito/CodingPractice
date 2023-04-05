# Rock, Paper, Scissors
import random

rock = '''
Rock
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
            ______)
            _______)
            _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
            ______)
        __________)
        (____)
---.__(___)
'''

player_choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = random.randint(0, 2)

if player_choice == "0":
    print(rock)
elif player_choice == "1":
    print(paper)
elif player_choice == "2":
    print(scissors)
else:
    print("Invalid input. You lose!\n")

print("Computer chose:")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if int(player_choice) == computer_choice:
    print("It's a draw.")
elif player_choice == "1" and computer_choice == 0:
    print("You win!")

elif player_choice == "2" and computer_choice == 1:
    print("You win!")
elif player_choice == "0" and computer_choice == 2:
    print("You win!")
else:
    print("You lose!")
