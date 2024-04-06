from tkinter import *
import os
import random
import string

# ---------------------------- CONSTANTS ------------------------------- #
GREY = "#d3d4d3"
file_name = 'Data.txt'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_strong_password(length=12):
    # Define the characters to use in the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()-_=+"

    # Combine all characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password contains at least one character of each type
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to randomize the order of characters
    random.shuffle(password)

    # Convert the list of characters into a string
    result = ''.join(password)

    print(result)
    password_entry.insert(1, result)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    credentials = f"{web_entry.get()}  | {username_entry.get()} | {password_entry.get()} \n"
    if os.path.isfile(file_name):
        with open(file_name, 'a') as file:
            file.write(credentials)
    else:
        with open(file_name, 'w') as file:
            file.write(credentials)
    clear()
    print('Operation completed !')


def clear():
    web_entry.delete(0, 10)
    username_entry.delete(0, 10)
    password_entry.delete(0, 50)


# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# labels
web_label = Label(text='Website')
web_label.grid(column=0, row=1)

username_label = Label(text='Email/UserName')
username_label.grid(column=0, row=2)

password_label = Label(text='Password')
password_label.grid(column=0, row=3)

# Entries
web_entry = Entry(width=30)
web_entry.grid(column=1, row=1)

username_entry = Entry(width=25)
username_entry.grid(column=1, row=2)

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text='Generate', width=7, command=create_strong_password)
generate_button.grid(column=1, row=4)

save_button = Button(text='Save', width=7, command=save_password)
save_button.grid(column=2, row=4)
window.mainloop()
