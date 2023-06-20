def ph_levels():
    while True:
        try:
            ph = int(input("Enter a value between 0 and 14: "))
            if 0 <= ph <= 14:
                break
            else:
                print("Invalid input. Please enter a value between 0 and 14.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    if ph > 7:
        print("Basic")
    elif ph < 7:
        print("Acidic")
    else:
        print("Neutral")


if __name__ == "__main__":
    ph_levels()
