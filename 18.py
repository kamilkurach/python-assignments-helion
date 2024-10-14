# Zadanie 18. [2:1,1] <abc
import sys

try:
    x = int(input("Provide int..{0}".format("\n")))
    x2 = x*2
    print("result: {0}".format(x2))
    total = 0

    while x2 not in list(range(1, 11)):
        total += x2
        x = int(input("Provide next int..{0}".format("\n")))
        x2 = x*2
        print("result: {0}".format(x2))

    print("Sum of omitted: {0}".format(total))

except (TypeError, ValueError):
    print("Provide int!")
    sys.exit()
