from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

my_window=Tk()
my_window.title("Password Manager")
my_window.config(pady=50,padx=50)

logo_img=PhotoImage(file="logo.png")
canvas=Canvas(height=300,width=300, highlightthickness=0)
canvas.create_image(150,150,image=logo_img )
# canvas.pack()
canvas.grid(row=1,column=1)

my_window.mainloop()