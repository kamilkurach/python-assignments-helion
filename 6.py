# Zadanie 6. [1] <abc> {~}

import sys

try:
    count = 1
    odd = 0
    even = 0
    while True:
        x = input("Provide int.. {0}".format("\n"))
        x = int(x)
        if count <= 5:
            if x % 2 == 0:
                even += 1
            else:
                odd += 1
            count += 1
        else:
            print("Total even: {0} and odd: {1}".format(even, odd))
            sys.exit()

except (TypeError, ValueError):
    print("Provide int.")
    sys.exit()
