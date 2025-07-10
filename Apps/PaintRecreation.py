import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Paint")
root.geometry('1000x1000')
root.resizable(False, False)
root.configure(borderwidth=5, bg='black', highlightthickness=0)

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="black", width=1000, height=1000, highlightthickness=0)
canvas.pack()

cursor_size = [20, 20]
last_cursor_pos = [0, 0]
def cursor(x, y):
    canvas.delete("cursor")
    canvas.create_oval(x-cursor_size[0]/2, y-cursor_size[1]/2, x+cursor_size[0]/2, y+cursor_size[1]/2, fill="red", tag="cursor")

def motion(event):
    x, y = event.x, event.y
    last_cursor_pos[0] = x
    last_cursor_pos[1] = y
    cursor(x, y)
    print('{}, {}'.format(x, y))

def cursor_size_increase(e):
    cursor_size[0]+=2
    cursor_size[1]+=2
    cursor(last_cursor_pos[0], last_cursor_pos[1])

def cursor_size_decrease(e):
    cursor_size[0]-=2
    cursor_size[1]-=2
    cursor(last_cursor_pos[0], last_cursor_pos[1])

def cursor_paint(event):
    x, y = event.x, event.y
    canvas.create_oval(x-cursor_size[0]/2, y-cursor_size[1]/2,
                       x+cursor_size[0]/2, y+cursor_size[1]/2,
                       fill="red", outline='')
    print("cursor down")

root.bind("<Up>", cursor_size_increase)
root.bind("<Down>", cursor_size_decrease)
canvas.bind("<B1-Motion>", cursor_paint)
root.bind('<Motion>', motion)

root.mainloop()