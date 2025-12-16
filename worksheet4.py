
# Worksheet 4 NumPy
import numpy as np

a=np.arange(5,26)
b=np.random.randint(10,51,(3,4))

print(a.shape,a.size,a.dtype)
print(b.shape,b.size,b.dtype)

A=np.array([2,4,6,8,10])
B=np.array([1,3,5,7,9])
print(A+B,A-B,A*B,A/B)

c=np.arange(1,10).reshape(3,3)
print(c*5)

d=np.arange(10,26).reshape(4,4)
print(d[1], d[:,-1])
d[0]=0

e=np.random.randint(20,41,10)
print(e[e>30])

f=np.arange(11,23).reshape(3,4)
print(f)

M1=np.array([[1,2],[3,4]])
M2=np.array([[5,6],[7,8]])
print(M1@M2, M1.T)

stats=np.random.randint(10,61,15)
print(stats.mean(),np.median(stats),stats.std())

A=np.array([[2,1,3],[0,5,6],[7,8,9]])
print(np.linalg.det(A))
print(np.linalg.inv(A))
print(np.linalg.eig(A))

pos=np.array([[0,0],[2,3],[4,7],[7,10],[10,15]])
print(np.linalg.norm(pos[-1]-pos[0]))
print(np.sum(np.linalg.norm(np.diff(pos,axis=0),axis=1)))
