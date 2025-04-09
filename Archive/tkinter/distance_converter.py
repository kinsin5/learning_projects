import tkinter as tk
from tkinter import ttk
from dpi import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.title("Distance Converter")

root.columnconfigure(0, weight=1)

meters = tk.StringVar()
feet_value = tk.StringVar()

def calc_feet(*args):
    try:
        m = float(meters.get())
        feet = m * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass


main = ttk.Frame(root, padding=(10,10))
main.grid()

meter_label = ttk.Label(main, text="Meteres:")

meter_input = ttk.Entry(main, width=10, textvariable=meters)
meter_input.focus()

feet_label = ttk.Label(main, text="Feet:")
feet_calc = ttk.Label(main, textvariable=feet_value)

calc_button = ttk.Button(main, text="Calculate", command=calc_feet)

meter_label.grid(row=0, column=0, sticky="W", padx=5, pady=5)
meter_input.grid(row=0, column=1, stick="EW", padx=5, pady=5)

feet_label.grid(row=1, column=0, sticky="W", padx=5, pady=5)
feet_calc.grid(row=1, column=1, stick="EW", padx=5, pady=5)

calc_button.grid(row=2, column=0, columnspan=2, sticky="EW", padx=5, pady=5)

root.bind("<Return>", calc_feet)
root.bind("<KP_Enter>", calc_feet)

root.mainloop()