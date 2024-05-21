import customtkinter
from tkinter import *

app = customtkinter.CTk()
app.geometry("1920x1080")
app.title("Student Management")
app.resizable(True, False)
app.config(bg="white")
app.iconbitmap("hii.ico")

font = customtkinter.CTkFont(family='Helvetica', size=56)
font1 = customtkinter.CTkFont(family='Helvetica', size=18)
font2 = customtkinter.CTkFont(family='Helvetica', size=48)

img1 = PhotoImage(file="hhhiii.png")
Label(app, image=img1).pack()


img4 = PhotoImage(file="p1.png")
Label(app, image=img4).pack()

def exit():
    app.destroy()

def open_new_student_():
    app.destroy()
    import new
    print("successful!")
   

a_0 = customtkinter.CTkLabel(app,
                             text="New Student",
                             text_color="black",
                             bg_color='white',
                             font=font)
a_0.pack()

a_1 = customtkinter.CTkButton(app,
                               text='New Admission',
                               bg_color="white",
                               text_color="white",
                               font=font1,
                               command=open_new_student_)  # Assign the function to the button command
a_1.pack()


d_0 = customtkinter.CTkButton(app,
                               text="EXIT",
                               command=exit,
                               fg_color="red",
                               hover_color="black",
                               bg_color="white",
                               text_color="white",
                               font=font2,
                               width=8,
                               height=3,
                               border_width=3,
                               corner_radius=3,
                               border_color="black")
d_0.place(x=1400, y=700)

app.mainloop()
