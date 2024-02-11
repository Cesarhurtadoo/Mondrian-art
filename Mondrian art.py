#  Draw random "art" in a Mondrian style
#
import tkinter as tk
import random

WIDTH = 1024
HEIGHT = 768

SPLIT_LOW = 120
SPLIT_PENALTY = 1.5

def randomColor():
    colors = ["red", "blue", "yellow", "white", "black"]
    return random.choice(colors)
    

def split_both(x, y, w, h, canvas):
    if w < SPLIT_LOW and h <SPLIT_LOW:
        return
    elif w < SPLIT_LOW:
        split_vertical(x,y,w,h,canvas)
    elif h < SPLIT_LOW:
        split_horizontal(x,y,w,h,canvas)
    else:
        if random.random() > 0.5:
            split_horizontal(x,y,w,h,canvas)
        else:
            split_vertical(x,y,w,h,canvas)

def split_horizontal(x, y, w, h, canvas):
    split_point = int(w/SPLIT_PENALTY)
    canvas.create_rectangle(x,y,x+w,y+h, fill = randomColor())
    split_both(x,y,split_point,h,canvas)
    split_both(x+split_point,y,w - split_point,h,canvas)


def split_vertical(x, y, w, h, canvas):
    split_point = int(h / SPLIT_PENALTY)
    canvas.create_rectangle(x, y, x + w, y + h, fill=randomColor())
    split_both(x, y, w, split_point, canvas)
    split_both(x, y + split_point, w, h - split_point, canvas)
    



def mondrian(x, y, w, h, canvas):
    if w < SPLIT_LOW and h < SPLIT_LOW:
        return
    elif w < SPLIT_LOW:
        split_vertical(x,y,w,h,canvas)
    elif h < SPLIT_LOW:
        split_horizontal(x,y,w,h,canvas)
    else:
        if random.random() > 0.5:
            split_horizontal(x,y,w,h,canvas)
        else:
            split_vertical(x,y,w,h,canvas)


# Main method - driver of the program

def main():
  # Create a window with a canvas
  master = tk.Tk()
  canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT)
  canvas.pack()

  # Draw the art
  mondrian(0, 0, WIDTH, HEIGHT, canvas)
  tk.mainloop()

main()