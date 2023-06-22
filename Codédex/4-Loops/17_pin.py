correct_pin = "1234"


def pin():
    pin = "0000"

    while pin != correct_pin:
        if not pin.isdigit() or len(pin) != 4:
            pin = input("Wrong format. Enter PIN:  ")
        else:
            pin = input("Enter PIN:  ")

    print("PIN entered correctly!")


if __name__ == "__main__":
    pin()
