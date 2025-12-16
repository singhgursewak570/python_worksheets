
# Worksheet 9 Tkinter
import tkinter as tk

root=tk.Tk()
root.title("Robot Control Panel")
root.geometry("500x400")
root.configure(bg="yellow")

canvas=tk.Canvas(root,width=500,height=400)
canvas.pack()

pt=canvas.create_oval(95,95,105,105,fill="black")
path=[(20,50),(100,120),(180,90),(250,150)]
canvas.create_line(path,fill="blue",width=3)

def move():
    canvas.move(pt,5,0)
    root.after(50,move)
move()

root.mainloop()
