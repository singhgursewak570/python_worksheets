
# Worksheet 2 Solutions
import random, string, math

L=[11,12,13,14]
L.extend([50,60])
L.remove(11); L.remove(13)
print(sorted(L))
print(sorted(L,reverse=True))
print(13 in L)
print(len(L))
print(sum(L))
print(sum(i for i in L if i%2))
print(sum(i for i in L if i%2==0))

def isprime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True

print(sum(i for i in L if isprime(i)))
L.clear()

lst=[1,2,3,4]
s=0
for i in lst: s+=i
print(s)

m=1
for i in lst: m*=i
print(m)

arr=[[["*"]*6 for _ in range(4)] for _ in range(3)]
print(arr)

D={1:5.6,2:7.8,3:6.6,4:8.7,5:7.7}
D[8]=8.8
D.pop(2)
print(6 in D)
print(len(D))
print(sum(D.values()))
D[3]=7.1
D.clear()

S1={10,20,30,40,50,60}
S2={40,50,60,70,80,90}
S1.update([55,66])
S1.discard(10); S1.discard(30)
print(40 in S1)
print(S1|S2)
print(S1&S2)
print(S1-S2)

for _ in range(100):
    print(''.join(random.choice(string.ascii_letters) for _ in range(random.randint(6,8))))

print([i for i in range(600,801) if isprime(i)])
print([i for i in range(100,1001) if i%7==0 and i%9==0])
