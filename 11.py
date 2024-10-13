# Zadanie 11. [1] <abc> {!}

#1
result = []
for i in range(100, 10, -1):
    if i % 7 != 0:
        result.append(i)

print(result)

#2
result = []
for i in sorted(list(range(11, 101)), reverse=True):
    if i % 7 != 0:
        result.append(i)

print(result)
