def sorting_hat():
    houses = {
        "🦁 Gryffindor": 0,
        "🦅 Ravenclaw": 0,
        "🦡 Hufflepuff": 0,
        "🐍 Slytherin": 0,
    }

    def get_input(prompt, options):
        while True:
            print(prompt)
            for i, option in enumerate(options, start=1):
                print(f"  {i}) {option}")
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return choice
            print("Wrong input.\n")

    q1_options = ["Dawn", "Dusk"]
    q1 = get_input("Q1) Do you like Dawn or Dusk?", q1_options)
    if q1 == 1:
        houses["🦁 Gryffindor"] += 1
        houses["🦅 Ravenclaw"] += 1
    else:
        houses["🦡 Hufflepuff"] += 1
        houses["🐍 Slytherin"] += 1

    q2_options = ["The Good", "The Great", "The Wise", "The Bold"]
    q2 = get_input("Q2) When I'm dead, I want people to remember me as:", q2_options)
    if q2 == 1:
        houses["🦡 Hufflepuff"] += 2
    elif q2 == 2:
        houses["🐍 Slytherin"] += 2
    elif q2 == 3:
        houses["🦅 Ravenclaw"] += 2
    else:
        houses["🦁 Gryffindor"] += 2

    q3_options = ["The violin", "The trumpet", "The piano", "The drum"]
    q3 = get_input("Q3) Which kind of instrument most pleases your ear?", q3_options)
    if q3 == 1:
        houses["🐍 Slytherin"] += 4
    elif q3 == 2:
        houses["🦡 Hufflepuff"] += 4
    elif q3 == 3:
        houses["🦅 Ravenclaw"] += 4
    else:
        houses["🦁 Gryffindor"] += 4

    your_house = max(houses, key=houses.get)
    print(f"You are a...\n  {your_house}!")


if __name__ == "__main__":
    sorting_hat()
