#!/usr/bin/env python

import sys
import tkinter as tk
from chalkboard import Chalkboard
from indexed_colors import indexed_colors

w, h = 850, 850
rows = 2
columns = 2

wall = tk.Frame(master=None, width=w, height=h)

board = Chalkboard(wall, width=w, height=h)

a = int(sys.argv[1])
b = int(sys.argv[2])

side = int(sys.argv[3])

side_w = float(side) / float(w)
side_h = float(side) / float(h)

for i in range(w):
    for j in range(h):
        x = a + (i * side_w)  
        y = b + (j * side_h)
        c = int((x ** 2) + (y ** 2))
        board.plot(i, j, color=indexed_colors[c % len(indexed_colors)])

wall.grid()
wall.mainloop()

