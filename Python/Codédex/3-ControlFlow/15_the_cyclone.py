def cyclone_checker():
    height = int(input("Enter your height(cm): "))
    credits = int(input("Enter your credits: "))

    if height >= 137 and credits >= 10:
        print("Enjoy the ride!")
    elif height <= 137:
        print("You are not tall enough to ride.")
    elif credits <= 10:
        print("You don't have enough credits to ride.")
    else:
        print("Invalid data.")


if __name__ == "__main__":
    cyclone_checker()
