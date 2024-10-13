# Zadanie 2. [1] <abc> {~}
import sys

try:
    x = input("Provide int..{0}".format("\n"))
    x = int(x)
    if x % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")
except (TypeError, ValueError):
    print("Provide int!")
    sys.exit()
