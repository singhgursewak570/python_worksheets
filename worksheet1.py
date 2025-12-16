
# Worksheet 1 Solutions
import math

print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")

fname = input("First name: ")
lname = input("Last name: ")
print(lname, fname)

r = float(input("Radius: "))
print("Area:", math.pi*r*r)

colors = ["Red","Green","White","Black"]
print(colors[0], colors[-1])

n = int(input("Enter n: "))
print(n + int(str(n)*2) + int(str(n)*3))

nums = input("Numbers: ").split(",")
lst = list(nums)
tup = tuple(nums)
print(lst, tup)

c = float(input("Celsius: "))
print("Fahrenheit:", (c*9/5)+32)

a,b = map(int,input("Two numbers: ").split())
a = a + b
b = a - b
a = a - b
print(a,b)

num = int(input("Number: "))
print("Even" if num%2==0 else "Odd")

year = int(input("Year: "))
print("Leap" if (year%400==0 or (year%4==0 and year%100!=0)) else "Not Leap")

x1,y1,x2,y2 = map(float,input("x1 y1 x2 y2: ").split())
print("Distance:", math.dist((x1,y1),(x2,y2)))

a1,a2,a3 = map(int,input("Angles: ").split())
print("Triangle" if a1+a2+a3==180 else "Not Triangle")

p,r,t = map(float,input("P R T: ").split())
print("CI:", p*(1+r/100)**t - p)

N = int(input("N: "))
print("Prime" if N>1 and all(N%i for i in range(2,int(N**0.5)+1)) else "Not Prime")

N = int(input("N for sum squares: "))
print(sum(i*i for i in range(1,N+1)))
