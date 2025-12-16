
# Worksheet 5 SciPy & Matplotlib
import numpy as np
from scipy import stats,fftpack,interpolate,signal,linalg,optimize
import matplotlib.pyplot as plt

data=np.random.rand(10)
print(stats.describe(data))

arr=np.random.rand(4,4)
print(fftpack.fft2(arr))

A=np.array([[1,2],[3,4]])
print(linalg.det(A),linalg.inv(A),linalg.eig(A))

x=np.linspace(0,10,10)
y=np.sin(x)
f=interpolate.interp1d(x,y,kind='cubic')

t=np.linspace(0,1,100)
sig=np.sin(2*np.pi*5*t)
filtered=signal.medfilt(sig,5)

sales=np.random.randint(100,500,(12,4))
print(sales.sum(axis=0),sales.mean())

names=["Arin","Aditya","Chirag","Gurleen","Kunal"]
marks=np.array([[85,78,92,88],[79,82,74,90],[90,85,89,92],[66,75,80,78],[70,68,75,85]])
print(marks.sum(axis=1))

time=np.array([0,1,2,3,4,5])
vel=np.array([2,3.1,7.9,18.2,34.3,56.2])
def quad(t,a,b,c): return a*t*t+b*t+c
params,_=optimize.curve_fit(quad,time,vel)
print(params)
