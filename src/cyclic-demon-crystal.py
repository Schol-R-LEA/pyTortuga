#!/usr/bin/env python

import sys
import numpy as np
import tkinter as tk
from chalkboard import Chalkboard
from indexed_colors import indexed_colors

class CyclicDemonCrystal(tk.Frame):
    def __init__(self, width, height, color_set, cycle_time, master=None):
        super().__init__(master)
        self.master = master
        self.board = Chalkboard(self, width=w, height=h)
        self.width = width
        self.height = height
        self.color_set = color_set
        self.cycle_time = cycle_time
        self.current = np.ndarray(shape=(self.width, self.height), dtype=np.uint16)
        self.target = np.ndarray(shape=(self.width, self.height), dtype=np.uint16)
        self.populate()
        self.refresh()
        self.cycle()
        self.pack()
        self.mainloop()
    
    def populate(self):
        from random import randint
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.current[x,y] = randint(0, len(self.color_set) - 1)
        self.target = self.current.copy()
    

    def refresh(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.board.plot(x, y, self.color_set[self.current[x,y]])


    def advance_target_value(self, x, y):
        neighbors = (
            # self.current[(x-1) % self.width, (y-1) % self.height],
            self.current[x, (y-1) % self.height],
            # self.current[(x + 1) % self.width, (y-1) % self.height],
            self.current[(x-1) % self.width, y],
            self.current[(x + 1) % self.width, y-1],
            # self.current[(x-1) % self.width, (y+1) % self.height],
            self.current[x, (y+1) % self.height],
            # self.current[(x + 1) % self.width, (y+1) % self.height]
        )
        advance = (self.current[x,y] + 1) % (len(self.color_set) - 1)
        if advance in neighbors:
             self.target[x,y] = advance
        else:
             self.target[x,y] = self.current[x,y]


    def cycle(self):
        for y in range(self.height):
            for x in range(self.width):
                self.advance_target_value(x, y)
        self.current = self.target.copy()
        self.refresh()
        self.after(self.cycle_time, self.cycle)

if __name__ == "__main__":
    w, h = 200, 200
    roygbiv = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    root = tk.Tk()
    cdc = CyclicDemonCrystal(w, h, roygbiv, 1, master=root)
 
