import sys

x = input("Provide int: ")

try:
    x = int(x)
    if x < 0:
        x = x - 1
    elif x > 0:
        x = x + 1
    else:
        pass

    print("Your number is: {0}".format(x))

    if x % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")

except (TypeError, ValueError):
    print("Provide int!")
    sys.exit()
