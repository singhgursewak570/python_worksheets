a = []
for i in range(3):
    b = []
    for j in range(4):
        c = []
        for k in range(6):
            c.append("*")
        b.append(c)
    a.append(b)

print(a)
