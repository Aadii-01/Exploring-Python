import tkinter
window = tkinter.Tk()
window.title("Celsius to Fahrenheit Converter")
window.minsize(width = 50, height =100)
window.config(padx = 20, pady = 20)

def calculate():
    display_down.config(text = (int(enter_value.get()) * (9/5) + 32 ))

#Equal to value
equal_to_label = tkinter.Label(text = "is equal to")
equal_to_label.grid(column = 0, row = 1)

#Entry component for celsius
enter_value = tkinter.Entry()
enter_value.config(width = 5)
enter_value.grid(column = 1, row = 0)

#Farenheit label value display
display_down = tkinter.Label(text = "0")
display_down.grid(column = 1, row = 1)

#Celsius label display
up_label = tkinter.Label(text = "\u00b0 Celsius")
up_label.grid(column = 2, row = 0)

#Farenheit label display
down_label = tkinter.Label(text = "\u00b0 Fahrenheit")
down_label.grid(column = 2, row = 1 )

#Click button to calculate
calculate_button = tkinter.Button(text = "Calculate", command = calculate)
calculate_button.grid(column = 1, row = 2)


window.mainloop()