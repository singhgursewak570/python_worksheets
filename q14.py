# Q14
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def peri(self):
        return 2 * 3.14 * self.r

c = Circle(5)
print("AREA:", c.area())
print("PERI:", c.peri())
