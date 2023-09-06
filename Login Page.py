from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import Toplevel
import ast

root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)


def signin():
    username = user.get()
    password = code.get()

    file = open('datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    # print(r.keys())
    # print(r.values())

    if username in r.keys() and password == r[username]:
        screen = Toplevel(root)
        screen.title("Login Sucessfull")
        screen.geometry("925x500+300+200")
        screen.configure(bg="white")

        Label(screen, text="Hello Everyone!", bg="#fff", font=(
            "Calibri(Body)", 50, "bold")).pack(expand=True)

        screen.mainloop()

    else:
        messagebox.showerror("ERROR", 'Invalid Credentials')


def signup_command():
    window = Toplevel(root)
    window.title("SignUp")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False)

    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()

        if password == confirm_password:
            try:
                # Open the file in read mode
                with open('datasheet.txt', 'r') as file:
                    d = file.read()
                    # Convert the file content to a dictionary
                    r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)

                # Open the file in write mode
                with open('datasheet.txt', 'w') as file:
                    file.write(str(r))

                messagebox.showinfo("Success", "Signup Successful!")
                window.destroy()
            except FileNotFoundError:
                messagebox.showerror(
                    "Error", "File 'datasheet.txt' not found.")
            except SyntaxError:
                messagebox.showerror(
                    "Error", "Invalid data in 'datasheet.txt'.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Error", "Passwords do not match!")

    def sign():
        window.destroy()

    img = PhotoImage(file="login2.png")
    Label(window, image=img, bg="white", border=0).place(x=50, y=90)

    frame = Frame(window, bg="#fff", width=350, height=390)
    frame.place(x=480, y=50)

    heading = Label(frame, text="Sign Up", fg="#57a1f8", bg="#fff",
                    font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, font=("Microsoft YaHei UI Light", 11),
                 fg="black", border=0, bg="white")
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, font=("Microsoft YaHei UI Light", 11),
                 fg="black", border=0, bg="white")
    code.place(x=30, y=150)
    code.insert(0, "Password")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    def on_enter(e):
        confirm_code.delete(0, 'end')

    def on_leave(e):
        name = confirm_code.get()
        if name == '':
            confirm_code.insert(0, 'Confirm Password')

    confirm_code = Entry(frame, width=25, font=("Microsoft YaHei UI Light", 11),
                         fg="black", border=0, bg="white")
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, "Password")
    confirm_code.bind('<FocusIn>', on_enter)
    confirm_code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

    Button(frame, width=39, pady=7, text="Sign up",
           bg="#57a1f8", fg="white", border=0, command=signup).place(x=35, y=280)
    label = Label(frame, text="I have an account", fg="black", bg="white",
                  font=("Microsoft YaHei UI Light", 9))
    label.place(x=90, y=340)

    sign_up = Button(frame, text="Sign in", bg="white",
                     fg="#57a1f8", cursor='hand2', border=0, width=6, command=sign)
    sign_up.place(x=200, y=340)

    window.mainloop()


img = PhotoImage(file="login.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, bg="white", width=350, height=350)
frame.place(x=480, y=70)

heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white",
                font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, font=("Microsoft YaHei UI Light", 11),
             fg="black", border=0, bg="white")
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


code = Entry(frame, width=25, font=("Microsoft YaHei UI Light", 11),
             fg="black", border=0, bg="white")
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, width=39, pady=7, text="Sign in",
       bg="#57a1f8", fg="white", border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account? ", fg="black", bg="white",
              font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=270)

sign_up = Button(frame, text="Sign up", bg="white",
                 fg="#57a1f8", cursor='hand2', border=0, width=6, command=signup_command)
sign_up.place(x=215, y=270)


root.mainloop()
