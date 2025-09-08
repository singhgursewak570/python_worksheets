# Q13
class Student:
    def __init__(self, sid, sname, sclass):
        self.sid = sid
        self.sname = sname
        self.sclass = sclass

st1 = Student(1,"Ram","CSE")
st2 = Student(2,"Shyam","ECE")

print("Student1:", st1.sid, st1.sname, st1.sclass)
print("Student2:", st2.sid, st2.sname, st2.sclass)
