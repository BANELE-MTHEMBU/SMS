from mysql import connector
from config import config
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from commands import *
from state import GlobalState
import constants
# connecting to the database
conn = connector.connect(**config)
cursor = conn.cursor()
state = GlobalState()
# cursor.execute("SELECT * FROM admin;")
# rows = [i for i in cursor]
# print(rows)

window = Tk()
windowWidth = 670
windowHeight = 650
positionTop = int(window.winfo_screenheight()/2 - windowHeight/2)
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
window.title(constants.TITLE)
window.geometry('{}x{}+{}+{}'.format(windowWidth, windowHeight, positionRight ,positionTop))
window.resizable(False, False)
# https://icon-icons.com/download/34003/ICO/512/
window.iconbitmap('./main.ico')



# ------------------- 
logo = ImageTk.PhotoImage(Image.open(r"./main.ico"))
Label(window, text=constants.TITLE, 
      font=("Arial",20,  "bold"), 
      image=logo,compound=TOP).grid(row=0, column=0, columnspan=3, ipadx=20)

# -------------- Auth Frame
pass_ey = BooleanVar()
def hide_show():
    eye.config(bg="cornflowerblue")
    if pass_ey.get() == True:
        password_entry.config(show="")
        eye.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        eye.config(text="Show Password")
        
def login():
    password = password_entry.get()
    username = username_entry.get()
    if state.getAuthenticated():
        messagebox.showinfo(constants.TITLE, "You are already authenticated.")
    else:
        cursor.execute(AuthCommands.LOGIN, [username, password])
        user = [i for i in cursor]
        if len(user) == 0:
            messagebox.showerror(constants.TITLE, "Invalid login credentials.")
        else:
            state.setAuthenticated(True)
    password_entry.delete(0, END)
    username_entry.delete(0, END)
    
def logout():
    password_entry.delete(0, END)
    username_entry.delete(0, END)
    if state.getAuthenticated() == False:
        messagebox.showerror(constants.TITLE, "There's no authenticated admin.")
        return
    state.setAuthenticated(False)
    messagebox.showinfo(constants.TITLE, "The admin is logged out.")
    
            
authFrame = Frame(window, bg="cornflowerblue", bd=1)
Label(authFrame, text="Admin Authentication", bg="cornflowerblue", 
      font=("Arial",15,  "bold")).grid(row=0, column=0, sticky=W, pady=10, 
                                       columnspan=2)

ttk.Separator(authFrame, orient=HORIZONTAL).grid(row=0, 
                                                 column=2,
                                                 ipadx=180, 
                                                 sticky=W, 
                                                 columnspan=3)
Label(authFrame, text="Username", 
      font=("Arial",10,  "bold"), bg="cornflowerblue").grid(row=1, column=0, sticky=W)
username_entry = ttk.Entry(authFrame)
username_entry.grid(row=1, column=1, sticky=W)

Label(authFrame, text="Password", 
      font=("Arial",10,  "bold"), bg="cornflowerblue").grid(row=1, column=2, sticky=W)
password_entry = ttk.Entry(authFrame, show='*')
password_entry.grid(row=1, column=3, sticky=W)

eye = Checkbutton(authFrame, text="Show Password",
                      font=("Arial", 10),
                      variable=pass_ey, 
                      bg="cornflowerblue",
                      width=15,
                      activebackground="cornflowerblue",
                      command=hide_show, onvalue=True, offvalue=False)
eye.grid(row=1, column=4, sticky=W)

Button(authFrame, text="Login", font=("Arial", 12), 
            width=10, bd=1, bg="black",
            fg="white",
            command=login,
            activebackground="white",
            activeforeground="black"
           ).grid(row=2, column=0, sticky=W, pady=10)

Button(authFrame, text="Logout", font=("Arial", 12), 
            width=10, bd=1, bg="black",
            fg="white",
            command= logout,
            activebackground="white",
            activeforeground="black"
           ).grid(row=2, column=1, sticky=W, pady=10, padx=5)


authFrame.grid(row=1, column=0, columnspan=3, ipadx=10, sticky=W, ipady=10)

# -------- Details Frame
detailsFrame = Frame(window, bg="white")

Label(detailsFrame, text="Student Registration", bg="white", 
      font=("Arial",15,  "bold")).grid(row=0, column=0, sticky=W, pady=10, 
                                       columnspan=2)

ttk.Separator(detailsFrame, orient=HORIZONTAL).grid(row=0, 
                                                 column=2,
                                                 ipadx=180, 
                                                 sticky=W, 
                                                 columnspan=3)
Label(detailsFrame, text="Student Name", 
      font=("Arial",10,  "bold"), bg="white").grid(row=1, column=0, sticky=W)
student_name_entry = ttk.Entry(detailsFrame)
student_name_entry.grid(row=1, column=1, sticky=W)


# Buttons [clear, register]

detailsFrame.grid(row=2, column=0,
                  columnspan=3, ipadx=10, sticky=W, ipady=10)

window.mainloop(0)
# closing the connection
conn.close()