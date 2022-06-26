from tkinter import *

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
generate_password_button=Button(text="Generate Password")
generate_password_button.grid(row=3,column=2)
# add button
add_button=Button(text="Add")
add_button.config(width=20, bg="blue", fg="white")
add_button.grid(row=4,column=1)






my_window.mainloop()