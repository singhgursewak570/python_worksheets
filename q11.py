# Q11
def is_goal_reached(path):
    x = 0
    y = 0
    for p in path:
        if p == "up":
            y = y + 1
        elif p == "down":
            y = y - 1
        elif p == "left":
            x = x - 1
        elif p == "right":
            x = x + 1
    if x == 2 and y == 0:
        return True
    else:
        return False

print(is_goal_reached(["up","right","right","down"]))
print(is_goal_reached(["right","right"]))

