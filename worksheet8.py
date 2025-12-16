
# Worksheet 8 Geometry
import numpy as np, math

class Point:
    def __init__(self,x,y): self.x=x; self.y=y

def distance(A,B): return math.hypot(A.x-B.x,A.y-B.y)
def midpoint(A,B): return ((A.x+B.x)/2,(A.y+B.y)/2)

def line_eq(A,B):
    m=(B.y-A.y)/(B.x-A.x)
    c=A.y-m*A.x
    return m,c

def reflect(C,A,B):
    m,c=line_eq(A,B)
    d=(C.x+(C.y-c)*m)/(1+m*m)
    xr=2*d-C.x
    yr=2*d*m-C.y+2*c
    return xr,yr

A=Point(1,2); B=Point(4,6)
print(distance(A,B), midpoint(A,B), line_eq(A,B))

A=np.array([1,2]); B=np.array([3,4]); C=np.array([5,6])
print(A+B+C, np.linalg.norm(A), np.dot(A,B))

S=np.array([0,0]); E=np.array([4,0]); P=np.array([2,3])
t=np.dot(P-S,E-S)/np.dot(E-S,E-S)
closest=S+t*(E-S)
print(np.linalg.norm(E-S),closest,np.linalg.norm(P-closest))

a1,b1,c1=1,1,4
a2,b2,c2=1,-1,0
det=a1*b2-a2*b1
if det!=0:
    x=(c1*b2-c2*b1)/det
    y=(a1*c2-a2*c1)/det
    print(x,y)
else:
    print("Parallel")
