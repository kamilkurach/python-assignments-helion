# Zadanie 6. [1] <abc> {~}

import sys

try:
    count = 0
    odd = 0
    even = 0
    while count <= 4:
        x = input("Provide int.. {0}".format("\n"))
        x = int(x)
        if x % 2 == 0:
            even += 1
            count += 1
        else:
            odd += 1
            count += 1

    print("Total even: {0} and odd: {1}".format(even, odd))

except (TypeError, ValueError):
    print("Provide int.")
    sys.exit()
