import tkinter
window = tkinter.Tk()  #from tkingter import Tk
window.title("My first GUI program") #Give title
window.minsize(width = 500, height =300) #Window size adjustments

"""Labels"""
my_label = tkinter.Label(text = "I am a label", font=("Times New Roman", 20, "bold"))
my_label.pack()

#Ways to change the key values
my_label["text"] = "I am a LABEL"
my_label.config(text = "I am a laBEL")

"""Buttons"""
def button_clicked():
    my_label.config(text = "I AM CLICKED!")
button = tkinter.Button(text = "Click Me", command = button_clicked)
button.pack()

#Challenge -> Button clicked, changes the label text by the input text
inputt = tkinter.Entry()
inputt.pack()
def get_input():
    my_label.config(text = inputt.get() )
button1 = tkinter.Button(text = "Enter!" , command = get_input)
button1.pack()


window.mainloop() #Keeps the window on running state