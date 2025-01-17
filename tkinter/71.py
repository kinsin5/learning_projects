import tkinter as tk
from tkinter import ttk
from dpi import set_dpi_awareness

set_dpi_awareness()

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        UserInputFrame(self).pack()

class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.user_input = tk.StringVar()

        label = ttk.Label(self, text="Enter your name:")
        entry = ttk.Entry(self, textvariable=self.user_input)
        button = ttk.Button(self, command=self.greet)

        label.pack(side="left")
        entry.pack(side="left")
        button.pack(side="left")

    def greet(self):
        print(f"Hello, {self.user_input.get()}!")



root = App()


root.mainloop()