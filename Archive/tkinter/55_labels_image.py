import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from dist_converter.dpi import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()

root.geometry("600x400")
root.resizable(False,False)
root.title("Widget Examples")

image = Image.open("widgets\\alfa_code.png").resize((300, 300))
photo = ImageTk.PhotoImage(image)



label = ttk.Label(root, image=photo, padding=5)
label.pack()



root.mainloop()


