# Asks the user for the amount they have in yuan, yen, and won
# and calculate the total in USD.

if __name__ == '__main__':

    yuan = int(input("What do you have left in yuan? "))
    yen = int(input("What do you have left in yen? "))
    won = int(input("What do you have left in won? "))

    # 1 dollar = 6.98 yuan
    a = yuan / 6.98

    # 1 dollar = 136 yen
    b = yen / 136

    # 1 dollar = 1298 won
    c = won / 1298

    print(f'Your total in USD is: ${round(a + b + c, 2)}')
