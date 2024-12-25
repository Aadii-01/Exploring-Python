import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Celsius to Fahrenheit Converter")
window.minsize(width = 50, height =100)
window.config(padx = 20, pady = 20)

# \u00b0  --> Degree symbol

def calculate():
    """Convert temperature based on selected mode """
    try:
        temp = float(enter_value.get())
        if conversion_mode.get() == "C_to_F":
            result = (temp * 9 / 5) + 32  # Celsius to Fahrenheit
            display_down.config(text=f"{result:.2f} \u00b0F")
        elif conversion_mode.get() == "F_to_C":
            result = (temp - 32) * 5 / 9  # Fahrenheit to Celsius
            display_down.config(text=f"{result:.2f} \u00b0C")
        else:
            messagebox.showerror("Error", "Select a conversion mode!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

#Equal to value
equal_to_label = tkinter.Label(text = "is equal to     ")
equal_to_label.grid(column = 0, row = 1, padx=0, pady=10)

#Entry component for celsius
enter_value = tkinter.Entry()
enter_value.config(width = 3)
enter_value.grid(column = 0, row = 1, padx=0, pady=10, sticky="w")

#Farenheit label value display
display_down = tkinter.Label(text = "0.00")
display_down.grid(column = 0, row = 1, padx=0, pady=10, sticky="e")

# Conversion mode selection (radio buttons)
conversion_mode = tkinter.StringVar(value="C_to_F")  # Default mode
radio_c_to_f = tkinter.Radiobutton(window, text="Celsius to Fahrenheit", variable=conversion_mode, value="C_to_F")
radio_c_to_f.grid(column = 0, row = 2)
radio_f_to_c = tkinter.Radiobutton(window, text="Fahrenheit to Celsius", variable=conversion_mode, value="F_to_C")
radio_f_to_c.grid(column = 0, row = 3 )

#Click button to calculate
calculate_button = tkinter.Button(text = "Calculate", command = calculate)
calculate_button.grid(column = 0, row = 4, padx = 10, pady = 10)

window.mainloop()