import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {user_name.get() or 'Nothing'}!")


root = tk.Tk()
root.geometry("600x400")

root.columnconfigure(0, weight=1)

frame1 = ttk.Frame(root, padding=(10, 20, 20, 10))
frame1.grid(sticky="EW")

frame2 = ttk.Frame(root)
frame2.grid(sticky="EW")

frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1)

user_name = tk.StringVar()

name_lable = ttk.Label(frame1, text="Name: ")
name_lable.grid(row=0, column=0, padx=(0,10))
name_entry = ttk.Entry(frame1, width=20, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()



greet_button = ttk.Button(frame2, text="Greet", command=greet)
greet_button.grid(row=0, column=0, sticky="EW")

quit_button = ttk.Button(frame2, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")

root.mainloop()