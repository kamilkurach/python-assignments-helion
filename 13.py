# Zadanie 13. [1] <abc> {!}

tab = []
count_accepted = 0
count_omitted = 0
for i in range(1, 121):
    if i % 11 == 0 and i % 5 == 0:
        count_omitted += 1
    else:
        count_accepted += 1
        tab.append(i)

print(tab)
print("Accepted: {0} Omitted: {1}".format(count_accepted, count_omitted))

