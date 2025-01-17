import tkinter as tk
from tkinter import ttk
from dpi import set_dpi_awareness

set_dpi_awareness()

class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.title = "Distance Converter"

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        frame = Feet_to_Meters(container)
        frame.grid(row=0, column=0, sticky="NSEW")

        self.bind("<Return>", frame.calculate)
        

class Meters_to_Feet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        
        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        meter_label = ttk.Label(self, text="Meters:")
        meter_entry = ttk.Entry(self, textvariable=self.meters_value)

        feet_label = ttk.Label(self, text="Feet:")
        feet_calc = ttk.Label(self, textvariable=self.feet_value)

        calculate_butt = ttk.Button(self, text="Calculate", command=self.calculate)
        meter_label.grid(column=0, row=0, sticky="W")
        meter_entry.grid(column=1, row=0, sticky="EW")
        feet_label.grid(column=0, row=1, sticky="W")
        feet_calc.grid(column=1, row=1, sticky="EW")
        calculate_butt.grid(column=0, row=2, columnspan=2, sticky="EW")
    
        for child in self.winfo_children():
             child.grid_configure(padx=15, pady=15)
    

    def calculate(self, *args):
        try:
                m = float(self.meters_value.get())
                feet = m * 3.28084
                self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass

class Feet_to_Meters(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        
        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        feet_label = ttk.Label(self, text="Feet:")
        feet_entry = ttk.Entry(self, textvariable=self.feet_value)

        meter_label = ttk.Label(self, text="Meter:")
        meter_calc = ttk.Label(self, textvariable=self.meters_value)

        calculate_butt = ttk.Button(self, text="Calculate", command=self.calculate)
        feet_label.grid(column=0, row=0, sticky="W")
        feet_entry.grid(column=1, row=0, sticky="EW")
        meter_label.grid(column=0, row=1, sticky="W")
        meter_calc.grid(column=1, row=1, sticky="EW")
        calculate_butt.grid(column=0, row=2, columnspan=2, sticky="EW")
    
        for child in self.winfo_children():
             child.grid_configure(padx=15, pady=15)
    

    def calculate(self, *args):
        try:
                feet = float(self.feet_value.get())
                m = feet / 3.28084
                self.meters_value.set(f"{m:.3f}")
        except ValueError:
            pass


root = DistanceConverter()

root.columnconfigure(0, weight=0)

root.mainloop()


