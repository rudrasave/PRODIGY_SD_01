import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result.set(f"{temp:.2f}°C = {f:.2f}°F, {k:.2f}K")

        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result.set(f"{temp:.2f}°F = {c:.2f}°C, {k:.2f}K")

        elif unit == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result.set(f"{temp:.2f}K = {c:.2f}°C, {f:.2f}°F")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

# GUI Window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")
root.resizable(False, False)

# Heading
tk.Label(root, text="Temperature Converter", font=("Arial", 16)).pack(pady=10)

# Input
tk.Label(root, text="Enter Temperature:").pack()
entry_temp = tk.Entry(root, width=30)
entry_temp.pack(pady=5)

# Unit Selection
unit_var = tk.StringVar(value="Celsius")
tk.Label(root, text="Select Unit:").pack()
tk.OptionMenu(root, unit_var, "Celsius", "Fahrenheit", "Kelvin").pack(pady=5)

# Convert Button
tk.Button(root, text="Convert", command=convert_temperature).pack(pady=10)

# Result Display
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12), fg="blue").pack(pady=10)

# Start GUI loop
root.mainloop()
