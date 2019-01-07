import tkinter as tk

root = tk.Tk()

a = tk.Frame(master=root, height=600, width=800)
a.pack(fill=tk.BOTH)

board = tk.Canvas(a, background="black", height=600, width=800)

board.create_line(0, 0, 800, 600, fill="white")  
board.pack(fill=tk.BOTH, expand=1)


root.geometry("800x800")
root.mainloop()
