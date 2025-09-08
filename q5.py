D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

# (i)
D[8] = 8.8
print(D)

# (ii)
del D[2]
print(D)

# (iii)
if 6 in D:
    print("YES")
else:
    print("NO")

# (iv)
c = 0
for k in D:
    c = c + 1
print("COUNT:", c)

# (v)
s = 0
for k in D:
    s = s + D[k]
print("SUM:", s)

# (vi)
D[3] = 7.1
print(D)

# (vii)
D.clear()
print(D)
