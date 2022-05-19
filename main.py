from tkinter import *
from PIL import Image
import requests


def get_quote():
    response = requests.get(url='https://api.whatdoestrumpthink.com/api/v1/quotes/random/')
    response.raise_for_status()
    phrase = response.json()['message']
    canvas.itemconfig(quote_text, text=phrase)



window = Tk()
window.title("Trump Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text='Trump Says...', width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

image = Image.open("trump.png")
image = image.resize((200, 200), Image.Resampling.LANCZOS)
image.save("new_trump.png")
kanye_img = PhotoImage(file="new_trump.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()