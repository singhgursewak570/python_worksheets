# Q16
class Robot:
    def __init__(self, name, task, battery_level):
        self.name = name
        self.task = task
        self.battery_level = battery_level

    def perform_task(self):
        print(self.name, "performing", self.task)
        self.battery_level = self.battery_level - 10

    def recharge(self):
        self.battery_level = 100

    def status(self):
        print("NAME:", self.name)
        print("TASK:", self.task)
        print("BATTERY:", self.battery_level)

r = Robot("R2D2","cleaning",100)
r.perform_task()
r.status()
r.recharge()
r.status()
