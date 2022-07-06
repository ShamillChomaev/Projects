BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
from random import randint, choice
current_card = {}

try:
    data = pandas.read_csv("data/unknown_word.csv")
except FileNotFoundError:
    origin_data = pandas.read_csv("data/french_words.csv")
    to_learn = origin_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def new_card():
    global current_card, the_timer
    window.after_cancel(the_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(learn_word, text=current_card["French"], fill="black")
    canvas.itemconfig(titel_text, text="French", fill="black")
    canvas.itemconfig(set_img, image=image)
    the_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(titel_text, text="English", fill="white")
    canvas.itemconfig(learn_word, text=current_card["English"], fill="white")
    canvas.itemconfig(set_img, image=bach_image)


def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/unknown_word.csv", index=False)
    new_card()









window = Tk()
window.title("Flash cards")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
the_timer = window.after(3000, func=flip_card)



#canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="images/card_front.png")
bach_image = PhotoImage(file="images/card_back.png")
set_img = canvas.create_image(400,263, image=image)
titel_text = canvas.create_text(400,150, text="Title", fill="black", font=("Arial",40,"italic"))
learn_word = canvas.create_text(400,263, text="word", fill="black", font=("Arial",60,"bold"))
canvas.grid(row=0, column=0, columnspan=2)



#button
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=new_card)
unknown_button.grid(row=1,column=0)

correct_img = PhotoImage(file="images/right.png")
known_button = Button(image=correct_img, highlightthickness=0, command=is_known)
known_button.grid(row=1,column=1)





new_card()

window.mainloop()