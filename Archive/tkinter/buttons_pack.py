import tkinter as tk
from tkinter import ttk

def greet():
    print("siema eniu")


root = tk.Tk()

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="right", fil="y")

root.mainloop()

