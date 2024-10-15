# Zadanie 22. [2:1,1] <list> {~}
import sys

try:
    x = int(input("Provide int.. {0}".format("\n")))
    tab = []
    tab.append(x)

    while True:
        if len(tab) > 1:
            if tab[-2] == x:
                sys.exit()
            else:
                x = int(input("Provide int.. {0}".format("\n")))
                tab.append(x)
        else:
            x = int(input("Provide int.. {0}".format("\n")))
            tab.append(x)
except (TypeError, ValueError):
    print("Provide int!")
    sys.exit()
