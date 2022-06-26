from tkinter import *
from tkinter import messagebox
import random, pyperclip
import string

FONT_NAME = "Courier"
CAPS_LETTER = list(string.ascii_uppercase)
LOWER_LETTER = list(string.ascii_lowercase)
SYMBOLS = list(string.punctuation)
NUMBERS = list(string.digits)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # print(caps_letters)
    # print(lower_letter)
    # print(symbols)
    # print(numbers)
    delete_password_textbox()
    password = []
    # password=[val for val in range(4) if ]
    for _ in range(4):
        password.append(random.choice(CAPS_LETTER))
        password.append(random.choice(LOWER_LETTER))
        password.append(random.choice(SYMBOLS))
        password.append(random.choice(NUMBERS))
    # print(password)
    random.shuffle(password)
    final_password = ""
    # for val in password:
    #     final_password += val
    final_password = "".join(password)
    # print(final_password)

    password_txtbox.insert(0, final_password)
    pyperclip.copy(final_password)

def delete_password_textbox():
    val = password_txtbox.get()
    for _ in range(len(val)):
        password_txtbox.delete(0)


def delete_website_textbox():
    val = website_textbox.get()
    for _ in range(len(val)):
        website_textbox.delete(0)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_textbox.get()
    username = username_textbox.get()
    password = password_txtbox.get()

    error_msg = ""
    if website_name == "" or username == "" or password == "":
        error_msg = "Please dont leave Empty"
    else:
        error_msg = ""
        user_option = messagebox.askokcancel(title=f"{website_name} ",
                                             message=f"Username: {username}\n Password: {password}\n Do you want to Save? ")
        if user_option:  # true
            with open("password.txt", "a") as my_file:
                my_file.write(f"{website_name} | {username} | {password} \n")
            delete_website_textbox()
            delete_password_textbox()
            website_textbox.focus()

    error_label.config(text=error_msg, font=(FONT_NAME, 15, "bold"))


# ---------------------------- UI SETUP ------------------------------- #

my_window = Tk()
my_window.title("Password Manager")
my_window.config(pady=50, padx=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(50, 100, image=logo_img)
# canvas.pack()
canvas.grid(row=0, column=1, columnspan=2)
# website
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
# text box for website
website_textbox = Entry()
website_textbox.grid(row=1, column=1, columnspan=2)
website_textbox.config(width=50)
website_textbox.focus()

# email
email_label = Label(text="Email/ Username: ")
email_label.grid(row=2, column=0)
# username
username_textbox = Entry()
username_textbox.insert(0, "sharath@example.com")  # start from 0th index
# username_textbox.config(show="sharath@example.com")
username_textbox.config(width=50)
username_textbox.grid(row=2, column=1, columnspan=2)

# password
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

password_txtbox = Entry()
password_txtbox.config(width=31, )
password_txtbox.grid(row=3, column=1)
# generate password button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, )
# show errors
error_label = Label()
error_label.grid(row=4, column=1)
# add button
add_button = Button(text="Add")
add_button.config(width=20, bg="blue", fg="white", command=save_password)
add_button.grid(row=5, column=1)

my_window.mainloop()
