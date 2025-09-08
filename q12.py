# Q12
class Student:
    def __init__(self, sid, sname, sclass):
        self.student_id = sid
        self.student_name = sname
        self.student_class = sclass

    def show(self):
        print("ID:", self.student_id)
        print("NAME:", self.student_name)
        print("CLASS:", self.student_class)

s = Student(1,"Ram","CSE")
s.show()