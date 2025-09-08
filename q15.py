rec = {"MOVE","TURN_LEFT","TURN_RIGHT","STOP"}
exe = {"MOVE","TURN_LEFT","STOP"}

for x in rec:
    if x not in exe:
        print(x)
