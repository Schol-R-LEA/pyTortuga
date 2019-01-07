#! /usr/python3 

import tkinter as tk
from enum import Enum

class Line_Method(Enum):
    primitive = 0
    bresenham = 1
    wu = 2

class Chalkboard(tk.Canvas):
    def __init__(self, master=None, height=600, width=800, background="black"):
        super().__init__(master, height=height, width=width, background=background)
        self.color = background
        self.right  = width
        self.bottom = height
        self.x_center = width // 2
        self.y_center = height // 2
        self.pack()
            
    def translate(self, x, y, origin_x, origin_y):
        return x + origin_x, origin_y - y

    def normalize(self, x, y):
        return self.translate(x, y, self.x_center, self.y_center)

    def denormalize(self, x, y):
        return self.translate(x, y, -self.x_center, -self.y_center)

    def plot(self, x, y, color="white"):
        """ Draw a single pixel at (x,y) relative to the upper left corner of the canvas."""
        if type(x) is int and type(y) is int:
            self.create_line(x-1, y-1, x, y, fill=color, width=0)

    def plot_centered(self, x=0, y=0, color="white"):
        """ Draw a single pixel at (x,y) relative to the midpoint of the canvas. """
        if type(x) is int and type(y) is int:
            norm_x, norm_y = self.normalize(x, y)
            self.plot(norm_x, norm_y, color=color)

    def draw_line(self, start, end, color="white", method=Line_Method.primitive):
        if method == Line_Method.primitive:
            x0, y0 = start
            x1, y1 = end
            norm_x0, norm_y0 = self.normalize(x0, y0)
            norm_x1, norm_y1 = self.normalize(x1, y1)
            self.create_line(norm_x0, norm_y0, norm_x1, norm_y1, fill=color)
        elif method == Line_Method.bresenham:
            self.bres_line(start, end, color)
        elif method == Line_Method.wu:
            self.wu_line(start, end, color)
        else:
            pass


    def bres_line(self, start, end, color="white"):
        x0, y0 = start
        x1, y1 = end
        dx = x1 - x0
        dy = y1 - y0
        
        # Determine how steep the line is
        is_steep = abs(dy) > abs(dx)
        
        # Rotate line
        if is_steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        
        # Swap start and end points if necessary and store swap state
        swapped = False
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
            swapped = True
        
        # Recalculate differentials
        dx = x1 - x0
        dy = y1 - y0
        
        # Calculate error
        error = int(dx / 2.0)
        y_step = 1 if y0 < y1 else -1
        
        y = y0
        for x in range(x0, x1 + 1):
            coord = (y, x) if is_steep else (x, y) 
            self.plot_centered(coord[0], coord[1], color=color)
            error -= abs(dy)
            if error < 0:
                y += y_step
                error += dx


    def wu_line(self, start, end, color="white"):
        pass


if __name__ == "__main__":
    w, h = 900, 300
    columns = 3
    max_x, max_y = w // columns, (h - 50)
    mid_x, mid_y = max_x // 2 , max_y // 2
    test = tk.Frame(master=None, width=w, height=h)
    board = []

    off_x, off_y = 0, 0
    for alg in Line_Method:
        board = Chalkboard(test, width=max_x, height=max_y)
        for x in [-mid_x, mid_x]:
            for y in range(-mid_y, mid_y + 1, 10):
                board.draw_line([0, 0], [x, y], method=alg, color="blue")
        for y in [-mid_y, mid_y]:
            for x in range(-mid_x, mid_x + 1, 10):
                board.draw_line([0, 0], [x, y], method=alg,color="red")
    
    test.grid()
    test.mainloop()

