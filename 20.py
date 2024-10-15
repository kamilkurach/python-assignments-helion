# Zadanie 20. [2] <list> {~}

tab1 = [3,5,6,208,7,2,8,12,18,35]
tab2 = []
temp = []

for element in tab1:
    if element % 2 == 0:
        tab2.append(element)
    else:
        temp.append(element)
        
result = tab2 + temp

print(result)
