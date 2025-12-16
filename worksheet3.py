
# Worksheet 3 Solutions

def diff17(n): return abs(n-17)*2 if n>17 else 17-n
def test_range(n): return 100<=n<=1000 or n==2000
def reverse(s): return s[::-1]

def count_case(s):
    return {"upper":sum(c.isupper() for c in s),
            "lower":sum(c.islower() for c in s)}

def distinct(lst): return list(set(lst))
def evens(lst): return [i for i in lst if i%2==0]

def robot():
    def move(): print("Robot moving")
    move()

def student(name,age,course): pass
print(student.__code__.co_varnames)

def move_robot(x,y,d):
    return {"up":(x,y+1),"down":(x,y-1),
            "left":(x-1,y),"right":(x+1,y)}[d]

def classify_temperature(t):
    if t<15: return "Cold"
    if t<=30: return "Moderate"
    return "Hot"

def is_goal_reached(path):
    x=y=0
    for p in path:
        x,y=move_robot(x,y,p)
    return (x,y)==(2,0)

class Student:
    def __init__(self,i,n,c=None):
        self.student_id=i; self.student_name=n; self.student_class=c
    def show(self): print(self.__dict__)

class Circle:
    def __init__(self,r): self.r=r
    def area(self): return 3.14*self.r*self.r
    def perimeter(self): return 2*3.14*self.r

class Robot:
    def __init__(self,n,t,b=100):
        self.name=n; self.task=t; self.battery=b
    def perform_task(self):
        print(self.task); self.battery-=10
    def recharge(self): self.battery=100
    def status(self): print(self.name,self.task,self.battery)
