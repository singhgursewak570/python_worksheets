import random
import string

for i in range(100):
    ln = random.randint(6,8)
    st = ""
    for j in range(ln):
        st = st + random.choice(string.ascii_letters)
    print(st)
for x in range(600,801):
    f = 0
    for j in range(2,x):
        if x % j == 0:
            f = 1
            break
    if f == 0:
        print(x)
for x in range(100,1001):
    if x % 7 == 0 and x % 9 == 0:
        print(x)
