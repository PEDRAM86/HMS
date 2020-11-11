from tkinter import *
import webbrowser as wb

root = Tk()


e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    wb.open("www.google.com")
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

mybutton = Button(root, text="CLICK", command=myClick, fg="white", bg="black")
mybutton.pack()

root.mainloop()
