from tkinter import *
from tkinter import messagebox
import random
import string
import json
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
    new_data = {
        website.get(): {
            'email': user_id,
            'password': secret
        }
    }

    if len(resource) == 0 or len(secret) == 0 or len(user_id) == 0:
        messagebox.showinfo(message='Please fill all fields')
    else:
        is_ok = messagebox.askyesno(title=resource,
                                    message=f'Those are entered: \nEmail: {user_id}\nPassword: {secret}\n is it OK'
                                            f' to save?')
        if is_ok:
            try:
                with open('this_is_not_a_password.json', 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open('this_is_not_a_password.json', 'w') as f:
                    json.dump(new_data, f, indent=4)
            else:
                data.update(new_data)

                with open('this_is_not_a_password.json', 'w') as f:
                    json.dump(data, f, indent=4)

            entry_password.clipboard_clear()
            entry_password.clipboard_append(string=entry_password.get())

            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()


def search_password():
    try:
        with open('this_is_not_a_password.json', 'r') as f:
            data = json.load(f)
            if website.get().casefold() in data:
                searched_password = data[website.get().casefold()]['password']
                searched_email = data[website.get().casefold()]['email']
                messagebox.showinfo(message=f'{website.get()}:\nemail: {searched_email}\npassword: {searched_password}')
            else:
                messagebox.showinfo(message=f'No password for {website.get()} found')
    except FileNotFoundError:
        messagebox.showinfo(message='There is no any saved password')


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
entry_website = Entry(width=21, textvariable=website)
entry_website.grid(column=1, row=1)
entry_website.focus()

username = StringVar()
entry_username = Entry(width=39, textvariable=username)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, 'some@email.com')

password = StringVar()
entry_password = Entry(width=21, textvariable=password)
entry_password.grid(column=1, row=3)

button_search = Button(text='Search', width='13', command=search_password)
button_search.grid(column=2, row=1)

button_generate_password = Button(text='Generate Password', command=generate_password)
button_generate_password.grid(column=2, row=3)

button_add = Button(text='Add', width=36, command=add_password)
button_add.grid(column=1, row=4, columnspan=3)

window.mainloop()
