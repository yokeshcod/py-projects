from tkinter import *
from tkinter import ttk
import mysql.connector
import customtkinter as ct
from tkinter import messagebox

app = ct.CTk()
app.geometry("1920x1080")
app.title("New Admission")
app.resizable(True, False)
app.config(bg="white")
app.iconbitmap("hii.ico")
font = ct.CTkFont(family='Helvetica', size=26)
font1 = ct.CTkFont(family='Helvetica', size=18)
font2 = ct.CTkFont(family='Bebas Neue', size=28)

img1 = PhotoImage(file="y1.png")
Label(app, image=img1).place(x=1550, y=750)

a = ct.CTkLabel(app, text="NEW ADMISSION", text_color="blue", bg_color="white", font=font2)
a.pack()

q = ct.CTkLabel(app, text="Name:", text_color="black", bg_color='white', font=font)
q.place(x=70, y=158)

w = ct.CTkEntry(app, bg_color="white", border_color="black", border_width=3, fg_color="black", text_color="white")
w.place(x=150, y=160)

e = ct.CTkLabel(app, text="Last Name:", text_color="black", bg_color='white', font=font)
e.place(x=15, y=200)

r = ct.CTkEntry(app, bg_color="white", border_color="black", border_width=3, fg_color="black", text_color="white")
r.place(x=150, y=200)

t = ct.CTkLabel(app, text="Phone No:", text_color="black", bg_color='white', font=font)
t.place(x=25, y=240)

# Validate function to allow only 10-digit numbers
def validate_phone_input(value):
    if len(value) <= 10 and value.isdigit():
        return True
    return False

vcmd_phone = app.register(validate_phone_input)

y = ct.CTkEntry(app, bg_color="white", border_color="black", border_width=3, fg_color="black", text_color="white", validate="key", validatecommand=(vcmd_phone, '%P'))
y.place(x=150, y=240)

u = ct.CTkLabel(app, text="Email:", text_color="black", bg_color='white', font=font)
u.place(x=70, y=280)

i = ct.CTkEntry(app, bg_color="white", border_color="black", border_width=3, fg_color="black", text_color="white")
i.place(x=150, y=280)

# Address
o = ct.CTkLabel(app, text="Address:", text_color="black", bg_color='white', font=font)
o.place(x=45, y=320)

p = ct.CTkEntry(app, bg_color="white", border_color="black", border_width=3, fg_color="black", text_color="white", width=300, height=70)
p.place(x=150, y=320)

# Standard ComboBox
std = ct.CTkLabel(app, text="Standard:", text_color="black", bg_color='white', font=font)
std.place(x=40, y=400)

std_options = [str(i) for i in range(1, 13)]
std_combobox = ct.CTkComboBox(app, values=std_options, bg_color="white")
std_combobox.place(x=150, y=400)

# Gender
g = ct.CTkLabel(app, text="Gender:", text_color="black", bg_color='white', font=font)
g.place(x=55, y=440)

gender_var = StringVar()
male_radio = ct.CTkRadioButton(app, text="Male", variable=gender_var, value="Male", text_color="black", bg_color='white', font=font1)
male_radio.place(x=150, y=445)
female_radio = ct.CTkRadioButton(app, text="Female", variable=gender_var, value="Female", text_color="black", bg_color='white', font=font1)
female_radio.place(x=250, y=445)

# Second Language
sl = ct.CTkLabel(app, text="Second Lang:", text_color="black", bg_color='white', font=font)
sl.place(x=5, y=480)

lang_var = StringVar()
hindi_radio = ct.CTkRadioButton(app, text="Hindi", variable=lang_var, value="Hindi", text_color="black", bg_color='white', font=font1)
hindi_radio.place(x=170, y=485)
tamil_radio = ct.CTkRadioButton(app, text="Tamil", variable=lang_var, value="Tamil", text_color="black", bg_color='white', font=font1)
tamil_radio.place(x=270, y=485)

# Date
d = ct.CTkLabel(app, text="Date:", text_color="black", bg_color='white', font=font)
d.place(x=85, y=525)

date_entry = ct.CTkEntry(app, bg_color="white", border_color="black", border_width=3, fg_color="black", text_color="white")
date_entry.place(x=150, y=525)

# Time
tm = ct.CTkLabel(app, text="Time:", text_color="black", bg_color='white', font=font)
tm.place(x=85, y=565)

time_entry = ct.CTkEntry(app, bg_color="white", border_color="black", border_width=3, fg_color="black", text_color="white")
time_entry.place(x=150, y=565)

# Day
day = ct.CTkLabel(app, text="Day:", text_color="black", bg_color='white', font=font)
day.place(x=95, y=605)

day_entry = ct.CTkEntry(app, bg_color="white", border_color="black", border_width=3, fg_color="black", text_color="white")
day_entry.place(x=150, y=605)

def save_data():
    # Retrieve data from entry fields
    name = w.get()
    last_name = r.get()
    phone = y.get()
    email = i.get()
    address = p.get()
    standard = std_combobox.get()
    gender = gender_var.get()
    second_language = lang_var.get()
    date = date_entry.get()
    time = time_entry.get()
    day = day_entry.get()

    try:
        # Connect to MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your password
            database="big"
        )

        mycursor = mydb.cursor()

        # Insert data into the table
        sql = "INSERT INTO admissions (name, last_name, phone, email, address, standard, gender, second_language, date, time, day) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (name, last_name, phone, email, address, standard, gender, second_language, date, time, day)
        mycursor.execute(sql, val)

        # Commit changes and close connection
        mydb.commit()
        mydb.close()

        # Clear the entry fields after successful submission
        w.delete(0, END)
        r.delete(0, END)
        y.delete(0, END)
        i.delete(0, END)
        p.delete(0, END)
        date_entry.delete(0, END)
        time_entry.delete(0, END)
        day_entry.delete(0, END)

        # Optionally, you can display a message indicating successful submission
        messagebox.showinfo("Success", "Data submitted successfully!")

    except mysql.connector.Error as error:
        # Handle any errors that occur during database operations
        messagebox.showerror("Error", f"Error: {error}")

# Button for submitting data
submit = ct.CTkButton(app,
                      text='Submit',
                      bg_color="white",
                      text_color="black",
                      font=font1,
                      command=save_data)
submit.place(x=100, y=700)

# Treeview widget to display data
tree = ttk.Treeview(app, columns=("Name", "Last Name", "Phone", "Email", "Address", "Standard", "Gender", "Second Language", "Date", "Time", "Day"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Last Name", text="Last Name")
tree.heading("Phone", text="Phone")
tree.heading("Email", text="Email")
tree.heading("Address", text="Address")
tree.heading("Standard", text="Standard")
tree.heading("Gender", text="Gender")
tree.heading("Second Language", text="Second Language")
tree.heading("Date", text="Date")
tree.heading("Time", text="Time")
tree.heading("Day", text="Day")
tree.place(x=600, y=100, width=1200, height=600)  # Adjust these coordinates to position the Treeview widget

def fetch_data():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your password
            database="big"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM admissions")
        rows = mycursor.fetchall()

        for row in rows:
            tree.insert("", "end", values=row)

        mydb.close()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error: {error}")

# Button to fetch data from MySQL
fetch_button = ct.CTkButton(app,
                            text="Fetch Data",
                            bg_color="white",
                            text_color="black",
                            font=font1,
                            command=fetch_data)
fetch_button.place(x=100, y=750)

d_0 = ct.CTkButton(app,
                               text="EXIT",
                               command=exit,
                               fg_color="red",
                               hover_color="black",
                               bg_color="white",
                               text_color="white",
                               font=font2,
                               width=5,
                               height=3,
                               border_width=3,
                               corner_radius=10,
                               border_color="black")
d_0.place(x=330, y=740)

app.mainloop()
