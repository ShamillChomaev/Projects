from tkinter import *
from tkinter import messagebox
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def time_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="TIMER", fg=GREEN)
    galka.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_time():
    global rep
    rep +=1
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60

    if rep % 8 == 0:
        huru_time(long)
        label.config(text="RELAX", fg=RED)
        messagebox.showinfo(message="TIME TO REST!")
    elif rep % 2 == 0:
        huru_time(short)
        label.config(text="BREAK", fg=PINK)
        messagebox.showinfo(message="TIME TO TAKE A BREAK!")
    else:
        huru_time(work)
        label.config(text="WORK", fg=GREEN)
        messagebox.showinfo(message="IT'S TIME TO WORK!")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def huru_time(count):
    count_min = math.floor(count // 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, huru_time, count - 1)
    else:
        start_time()
        mark = ""
        repetitions = math.floor(rep/2)
        for _ in range(repetitions):
            mark += "✔"
        galka.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

label = Label(text="TIMER", font=(FONT_NAME,30,"bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

reset_button = Button(text="Reset", font=(FONT_NAME), command=time_reset)
reset_button.grid(column=0,row=2)

start_button = Button(text="Start", font=(FONT_NAME), command=start_time)
start_button.grid(column=2,row=2)


galka = Label(font=(FONT_NAME), fg=GREEN, bg=YELLOW)
galka.grid(column=1,row=3)


window.mainloop()
