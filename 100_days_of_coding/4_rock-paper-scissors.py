# Rock, Paper, Scissors
import random

ROCK = '''
Rock
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
'''

PAPER = '''
Paper
    _______
---'   ____)____
            ______)
            _______)
            _______)
---.__________)
'''

SCISSORS = '''
Scissors
    _______
---'   ____)____
            ______)
        __________)
        (____)
---.__(___)
'''

WIN_TEXT = "You win!"

player_choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = random.randint(0, 2)

if player_choice == "0":
    print(ROCK)
elif player_choice == "1":
    print(PAPER)
elif player_choice == "2":
    print(SCISSORS)
else:
    print("Invalid input. You lose!\n")

print("Computer chose:")
if computer_choice == 0:
    print(ROCK)
elif computer_choice == 1:
    print(PAPER)
elif computer_choice == 2:
    print(SCISSORS)

if int(player_choice) == computer_choice:
    print("It's a draw.")
elif player_choice == "1" and computer_choice == 0:
    print(WIN_TEXT)
elif player_choice == "2" and computer_choice == 1:
    print(WIN_TEXT)
elif player_choice == "0" and computer_choice == 2:
    print(WIN_TEXT)
else:
    print("You lose!")
