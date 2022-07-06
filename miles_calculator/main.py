from tkinter import *

window = Tk()
window.title("Text")
window.minsize(250,130)
window.config(padx=20, pady=20)


label = Label(text="is equal to", font=("Arial", 14))
label.grid(column=1, row=2)

miles = Label(text="Miles", font=("Arial", 14))
miles.grid(column=3, row=1)

km = Label(text="Km", font=("Arial", 14))
km.grid(column=3, row=2)

score = Label(text=0, font=("Arial", 14))
score.grid(column=2, row=2)

def cliced():
    a = int(int(iut.get()) * 1.6)
    score["text"] = a

button = Button(text="Calculate", font=("Arial", 12), command=cliced)
button.grid(column=2, row=3)


iut = Entry(width=10)
iut.grid(column=2, row=1)


window.mainloop()