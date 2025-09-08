S1 = {10,20,30,40,50,60}
S2 = {40,50,60,70,80,90}

# (i)
S1.add(55)
S1.add(66)
print(S1)

# (ii)
S1.remove(10)
S1.remove(30)
print(S1)

# (iii)
if 40 in S1:
    print("YES")
else:
    print("NO")

# (iv)
print(S1 | S2)

# (v)
print(S1 & S2)

# (vi)
print(S1 - S2)
