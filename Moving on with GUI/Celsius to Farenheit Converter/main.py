import tkinter
window = tkinter.Tk()
window.title("Celsius to Fahrenheit Converter")
window.minsize(width = 50, height =100)
window.config(padx = 20, pady = 20)

def calculate():
    display_farenheit.config(text = (int(enter_celsius.get()) * (9/5) + 32 ))


equal_to_label = tkinter.Label(text = "is equal to")
equal_to_label.grid(column = 0, row = 1)

enter_celsius = tkinter.Entry()
enter_celsius.config(width = 5)
enter_celsius.grid(column = 1, row = 0)

display_farenheit = tkinter.Label(text = "0")
display_farenheit.grid(column = 1, row = 1)

celsius_label = tkinter.Label(text = "\u00b0 Celsius")
celsius_label.grid(column = 2, row = 0)

farenheit_label = tkinter.Label(text = "\u00b0 Fahrenheit")
farenheit_label.grid(column = 2, row = 1 )

calculate_button = tkinter.Button(text = "Calculate", command = calculate)
calculate_button.grid(column = 1, row = 2)



window.mainloop()