from tkinter import *
from tkinter import messagebox
import random
import string


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    secret = StringVar(value=''.join(random.choice(alphabet) for i in range(18)))
    entry_password.config(textvariable=secret)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    resource = entry_website.get()
    user_id = entry_username.get()
    secret = entry_password.get()

    if len(resource) == 0 or len(secret) == 0 or len(user_id) == 0:
        messagebox.showinfo(message='Please fill all fields')
    else:
        is_ok = messagebox.askyesno(title=resource,
                                    message=f'Those are entered: \nEmail: {resource}\nPassword: {secret}\n is it OK'
                                            f' to save?')
        if is_ok:
            with open('this_is_not_a_password.txt', 'a') as f:
                f.write(f'{resource}  |  {user_id}  |  {secret}\n')

            entry_password.clipboard_clear()
            entry_password.clipboard_append(string=entry_password.get())

            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title('Password Manager')

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


label_website = Label(text='Website:')
label_website.grid(column=0, row=1)

label_username = Label(text='Email/Username:')
label_username.grid(column=0, row=2)

label_password = Label(text='Password:')
label_password.grid(column=0, row=3)

website = StringVar()
entry_website = Entry(width=39, textvariable=website)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

username = StringVar()
entry_username = Entry(width=39, textvariable=username)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, 'some@email.com')

password = StringVar()
entry_password = Entry(width=21, textvariable=password)
entry_password.grid(column=1, row=3)


button_generate_password = Button(text='Generate Password', command=generate_password)
button_generate_password.grid(column=2, row=3)

button_add = Button(text='Add', width=36, command=add_password)
button_add.grid(column=1, row=4, columnspan=3)

window.mainloop()
