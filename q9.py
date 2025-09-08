# Q9
def move_robot(x, y, d):
    if d == "up":
        y = y + 1
    elif d == "down":
        y = y - 1
    elif d == "left":
        x = x - 1
    elif d == "right":
        x = x + 1
    return (x,y)

print(move_robot(0,0,"up"))
print(move_robot(0,0,"right"))
