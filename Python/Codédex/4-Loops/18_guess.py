num_to_guess = "7"


def guess():
    guess = "0"

    while guess != num_to_guess:
        if not guess.isdigit() or len(guess) != 1:
            guess = input("Wrong format. Guess the number:  ")
        else:
            guess = input("Guess the number:  ")

    print("You got it!")


if __name__ == "__main__":
    guess()
