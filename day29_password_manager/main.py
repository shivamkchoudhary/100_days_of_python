from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any filed empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the detailed entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs is okay to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# website_label
website_label = Label(text="Website:  ")
website_label.grid(row=1, column=0)
# website_entry
website_input = Entry(width=55)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# Email_label
email_label = Label(text="Email/Username:  ")
email_label.grid(row=2, column=0)
# Email_entry
email_input = Entry(width=55)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "email@gmail.com")

# Password_label
password_label = Label(text="Password:  ")
password_label.grid(row=3, column=0)
# Password_entry
password_input = Entry(width=37)
password_input.grid(row=3, column=1)

# generate_password_button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
# add_password_button
add_password_button = Button(text="Add", width=46, command=save)
add_password_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
