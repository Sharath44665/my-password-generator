from tkinter import *
import random
import string
FONT_NAME = "Courier"
CAPS_LETTER=list(string.ascii_uppercase)
LOWER_LETTER=list(string.ascii_lowercase)
SYMBOLS=list(string.punctuation)
NUMBERS=list(string.digits)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passowrd():
    # print(caps_letters)
    # print(lower_letter)
    # print(symbols)
    # print(numbers)
    delete_val()
    password=[]
    for _ in range(4):
        password.append(random.choice(CAPS_LETTER))
        password.append(random.choice(LOWER_LETTER))
        password.append(random.choice(SYMBOLS))
        password.append(random.choice(NUMBERS))
    # print(password)
    random.shuffle(password)
    final_password=""
    for val in password:
        final_password+=val
    # print(final_password)
    password_txtbox.insert(1,final_password)

def delete_val():
    val=password_txtbox.get()
    for _ in range(len(val)):
        password_txtbox.delete(0)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

my_window=Tk()
my_window.title("Password Manager")
my_window.config(pady=50,padx=50)

logo_img=PhotoImage(file="logo.png")
canvas=Canvas(height=200,width=200, highlightthickness=0)
canvas.create_image(50,100,image=logo_img )
# canvas.pack()
canvas.grid(row=0,column=1)
# website
website_label= Label(text="Website: ", font=(FONT_NAME,20,"bold"))
website_label.grid(row=1,column=0)
# text box for website
website_textbox=Entry()
website_textbox.grid(row=1,column=1)
website_textbox.config(width=50)

# email
email_label=Label(text="Email/ Username: ")
email_label.grid(row=2, column=0)
# username
username_textbox=Entry()
username_textbox.insert(1, "sharath@example.com")
# username_textbox.config(show="sharath@example.com")
username_textbox.config(width=50)
username_textbox.grid(row=2,column=1)

# password
password_label=Label(text="Password: ")
password_label.grid(row=3,column=0)

password_txtbox=Entry()
password_txtbox.config(width=50)
password_txtbox.grid(row=3,column=1)
# generate password button
generate_password_button=Button(text="Generate Password", command=generate_passowrd)
generate_password_button.grid(row=3,column=2)
# add button
add_button=Button(text="Add")
add_button.config(width=20, bg="blue", fg="white",)
add_button.grid(row=4,column=1)






my_window.mainloop()