# Zadanie 7. [1] <abc> {~}

x = input("Provide key.. {0}".format("\n"))
count = 0
while x != "x":
    x = input()
    count+=1

print("Total keys before 'x': {0}".format(count))
