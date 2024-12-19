import tkinter
window = tkinter.Tk()  #from tkingter import Tk
window.title("My first GUI program") #Give title
window.minsize(width = 500, height =300) #Window size adjustments
window.config(padx = 20, pady = 20)  #Add padding to the window

"""Labels"""
my_label = tkinter.Label(text = "I am a label", font=("Times New Roman", 20, "bold"))
#Ways to change the key values
my_label["text"] = "I am a LABEL"
my_label.config(text = "I am a laBEL")
my_label.config(padx= 20, pady= 20)
my_label.pack()

def get_input():
    my_label.config(text = inputt.get() )

"""Buttons"""
#Challenge -> Button clicked, changes the label text by the input text
inputt = tkinter.Entry()
inputt.pack()
button1 = tkinter.Button(text = "Enter!" , command = get_input)
button1.pack()


"""Challenge -> Create a screen consisiting of two buttons a label  and an entry in form of grid"""
# my_label = tkinter.Label(text = "My label")
# my_label.grid(column = 0, row = 0)
#
# b1 = tkinter.Button(text = "Click me")
# b1.grid(column = 1, row = 1)
#
# b2 = tkinter.Button(text = "Dont click me")
# b2.grid(column = 2, row = 0)
#
# inputt = tkinter.Entry()
# inputt.grid(column = 3, row = 2)



window.mainloop() #Keeps the window on running state