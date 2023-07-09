import random

answers = [
    "Yes - definitely.",
    "It is decidedly so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
]


def eight_ball():
    print("Welcome to the Magic 8 Ball!")
    while True:
        question = input("Ask me a question: ")
        if question == "":
            print("Please enter a question!")
            continue
        elif question == "quit":
            print("Thanks for playing!")
            break
        else:
            print(random.choice(answers))


if __name__ == "__main__":
    eight_ball()
