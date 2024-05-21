import customtkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="big"
)

app = customtkinter.CTk()
app.geometry("300x400")
app.title("LOGIN")
app.resizable(False, False)
app.config(bg="white")
font = customtkinter.CTkFont(family='Helvetica', size=26)  # for username and password
font1 = customtkinter.CTkFont(family='Helvetica', size=18)
app.iconbitmap("hii.ico")

def exit():
    app.destroy()

def login():
    username = user_name_entry.get()  # Get username from entry
    password = password_entry.get()  # Get password from entry

    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        print("Login successful!")
        app.destroy()  # Destroy the current login window
        # Import and initialize main window
        import main
    else:
        print("Invalid username or password!")
        messagebox.showerror("Error", "Invalid username or password!")
        # Show error message or perform any action for failed login

img1 = PhotoImage(file="hhii1.png")
Label(app, image=img1).pack()

user_name = customtkinter.CTkLabel(app, 
                                   text="UserName",
                                   text_color="black",
                                   bg_color='white',
                                   font=font)
user_name.place(x=90, y=120)

user_name_entry = customtkinter.CTkEntry(app,
                                         bg_color="white",
                                         border_color="black",
                                         border_width=3,
                                         fg_color="black",
                                         text_color="white")
user_name_entry.place(x=80, y=160)

password = customtkinter.CTkLabel(app,
                                  text="Password",
                                  text_color="black",
                                  bg_color='white',
                                  font=font)
password.place(x=90, y=220)

password_entry = customtkinter.CTkEntry(app,
                                        show='*',
                                        bg_color="white",
                                        border_color="black",
                                        border_width=3,
                                        fg_color="black",
                                        text_color="white")
password_entry.place(x=80, y=260)

submit = customtkinter.CTkButton(app,
                                 text='Submit',
                                 command=login,
                                 bg_color="white",
                                 text_color="white",
                                 font=font1)
submit.place(x=80, y=330)

exit_btn = customtkinter.CTkButton(app,
                                   text="Exit",
                                   command=exit,
                                   fg_color="red",
                                   hover_color="black",
                                   bg_color="white",
                                   text_color="white",
                                   font=font1,
                                   width=8,
                                   height=3,
                                   border_width=3,
                                   corner_radius=3,
                                   border_color="black")
exit_btn.place(x=255, y=360)

error_label = Label(app, text="",
                    bg="white",
                    font=("Helvetica", 12)
                    )
error_label.place(x=80, y=300)

app.mainloop()
