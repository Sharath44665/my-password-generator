from tkinter import *
from tkinter import messagebox
import random, pyperclip, json
import string

FONT_NAME = "Courier"
CAPS_LETTER = list(string.ascii_uppercase)
LOWER_LETTER = list(string.ascii_lowercase)
SYMBOLS = list(string.punctuation)
NUMBERS = list(string.digits)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_txtbox.delete(0, 50)
    numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    smallLetters = list(string.ascii_lowercase)
    capsLetters = list(string.ascii_uppercase)
    specialChars = ['_', '$', '.']
    passWordList = []
    passWordText = ""

    for i in range(random.randint(1, 9)):
        passWordList.append(random.choice(numberList))
    for i in range(random.randint(5, 9)):
        passWordList.append(random.choice(smallLetters))
    for i in range(random.randint(5, 9)):
        passWordList.append(random.choice(capsLetters))
    for i in range(random.randint(1, 5)):
        passWordList.append(random.choice(specialChars))
    random.shuffle(passWordList)

    for letter in passWordList:
        passWordText = passWordText + str(letter)
    # return passWordText
    password_txtbox.insert(0, passWordText)


def delete_website_textbox():
    val = website_textbox.get()
    for _ in range(len(val)):
        website_textbox.delete(0)


def deletePassTextBox():
    val = password_txtbox.get()
    for _ in range(len(val)):
        password_txtbox.delete(0)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_textbox.get()
    username = username_textbox.get()
    password = password_txtbox.get()
    newData = {
        website_name: {
            "username": username,
            "password": password
        }
    }
    error_msg = ""
    if website_name == "" or username == "" or password == "":
        error_msg = "Please dont leave Empty"
    else:
        error_msg = ""
        # user_option = messagebox.askokcancel(title=f"{website_name} ",
        #                                      message=f"Username: {username}\n Password: {password}\n Do you want to Save? ")
        # if user_option:  # true
        #     write to json file
        #     with open("data.json", "w") as my_file:
        #         # json.load(newData,my_file,indent=4)
        #         json.dump(newData, my_file,indent=4)
        #         my_file.write(f"{website_name} | {username} | {password} \n")
        #     update to json file
        try:
            with open("data.json", "r") as myFile:
                data = json.load(myFile)
                if data.get(website_name) != None:
                    myData = data[website_name]
                    # print(myData["username"])
                    if myData["username"] == username:
                        print(f"{username} found, please change the username")
        except FileNotFoundError:

            with open("data.json", "w") as myFile:
                json.dump(newData, myFile, indent=4)
        else:
            data.update(newData)
            with open("data.json", "w") as myFile:
                json.dump(data, myFile, indent=4)

            delete_website_textbox()
            deletePassTextBox()
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
