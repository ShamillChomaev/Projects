from tkinter import *
from tkinter import messagebox
import pyperclip
import json




# Password Generator Project
from random import choice, randint,shuffle


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for char in range(randint(8, 10))]
    password_sybmols = [choice(symbols) for c in range(randint(2, 4))]
    password_numbers = [choice(numbers) for k in range(randint(2, 4))]
    password_list = password_letter + password_sybmols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)




def save():
    website = website_entry.get()
    password = password_entry.get()
    username = email_entry.get()

    new_data = {
        website: {
            "email": username,
            "password": password,
        }

    }

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showerror(message="You did not write down required information")

    else:
        try:
            with open("data1.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data1.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data1.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def search():
    website = website_entry.get()
    try:
     with open("data1.json", "r") as data_file:
        data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(message="File not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(message=f"Ваша почта: {email}\n Ваш пароль: {password}")
            print(data[website]["email"])
        else:
            messagebox.showerror(message=f"The is no data about {website} website, please fill it in")


#______________UI______________
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons
generate_password_button = Button(text="Generate", command=password_generator)
generate_password_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=38, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_password = Button(text="  Search  ", command=search)
search_password.grid(row=1, column=2)

window.mainloop()