L1 = [1,2,3,4,5]
L2 = [6,7,8,9,10]
L3 = []

for x in L1:
    if x % 2 != 0:
        L3.append(x)

for x in L2:
    if x % 2 == 0:
        L3.append(x)

print(L3)
