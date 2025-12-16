
# Worksheet 7 Projects
# Tic Tac Toe

def print_board(b):
    print(b[0:3],b[3:6],b[6:9])

def check_winner(b,p):
    wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(b[i]==p for i in w) for w in wins)

def play_game():
    b=[" "]*9; p="X"
    for _ in range(9):
        print_board(b)
        i=int(input(p+": "))-1
        if b[i]==" ":
            b[i]=p
            if check_winner(b,p):
                print(p,"wins"); return
            p="O" if p=="X" else "X"
    print("Tie")

# To Do List
tasks=[]
def add_task(t): tasks.append(t)
def view_tasks(): print(list(enumerate(tasks)))
def delete_task(i): tasks.pop(i)

# Robot Path Planning omitted for brevity
