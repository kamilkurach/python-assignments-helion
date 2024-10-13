# Zadanie 1. [2:1,1] <abc
import sys

try:
    count = 0
    tab = []
    while count <= 2:
        x = input("Provide non-negative int..{0}".format("\n"))
        x = int(x)
        if x > 0:
            count += 1
            tab.append(x)

    max_tab = max(tab)
    print("Max from input: {0}".format(max_tab))
    
    for _ in range(max_tab):
        print(sum(tab) - max_tab)

except (TypeError, ValueError):
    print("Provide non-negative int.")
    sys.exit()
