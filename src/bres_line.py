
import tkinter as tk
import Chalkboard as ch
from math import tan

def draw_line(start, end):
    x0, y0 = start
    x1, y1 = end
    dx = x1 - x0
    dy = y1 - y0
    D = 2*dy - dx
    y = y0
    
    for x in range(x0, x1):
        plot(x, y)
        if D > 0:
            y = y + 1
            D = D - 2 * dx

         D = D + 2 * dy



root = tk.Tk()
board = ch.Chalkboard(root)




