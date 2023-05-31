import tkinter


window = tkinter.Tk()
window.title("Py jungle login")
window.geometry('340x440')
window.configure(bg='#291')

def login():
    username = "Axl Rose"
    password = "1234"
    if username_entry.get()==username and password_entry.get()==password:
        print("Succes loged in")
    else:
        print('invalid login')

frame = tkinter.Frame(bg='#291')

# Creating widgets

login_label = tkinter.Label(frame, text="Login", bg='#291', fg='#FFFFFF', font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg='#291', fg='#FFFFFF', font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password", bg='#291',fg='#FFFFFF', font=("Arial", 16))
login_button = tkinter .Button(frame, text="Login", bg="#246", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2,sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
