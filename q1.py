L = [11, 12, 13, 14]
L.append(50)
L.append(60)
print(L)

L.remove(11)
L.remove(13)
print(L)

L.sort()
print(L)

L.sort(reverse=True)
print(L)

# Search 13
flag = 0
for i in L:
    if i == 13:
        flag = 1
if flag == 1:
    print("NUMBER FOUND")
else:
    print("NUMBER NOT FOUND")

# Count
count = 0
for i in L:
    count += 1
print("COUNT : ", count)

# Even & Odd Sum
sumo = 0
sume = 0
for i in L:
    if i % 2 == 0:
        sume += i
    else:
        sumo += i
print("EVEN SUM : ", sume)
print("ODD SUM : ", sumo)

# Prime Sum
sump = 0
for i in L:
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0 and i > 1:
        sump += i
print("SUM PRIME : ", sump)

# Clear List
L.clear()
del(L)
