import tkinter as tk

root = tk.Tk()

root.geometry("600x400")

rectangle_3 = tk.Label(root, text="Rectangle 3", bg="black", fg="white")
rectangle_3.pack(ipadx=10, ipady=10, side="bottom", fill="x")

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.pack(ipadx=10, ipady=10, side="left", fill="both",expand=True)

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(ipadx=10, ipady=10, side="right", fill="both",expand=True)



root.mainloop()

