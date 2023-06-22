correct_pin = 1234


def pin():
    pin = input("Enter your PIN: ")

    while not pin.isdigit() or len(pin) != 4:
        pin = input("Incorrect PIN format. Enter your PIN again (4 digits only): ")

    pin = int(pin)

    while pin != correct_pin:
        pin = int(input("Incorrect PIN. Enter your PIN again: "))

    if pin == correct_pin:
        print("PIN accepted!")


if __name__ == "__main__":
    pin()
