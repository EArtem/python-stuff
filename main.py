from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Ariel'
TEXT_BACKGROUND = 'FFFFFF'

try:
    french_words = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    french_words = pd.read_csv('data/french_words.csv')
to_learn = french_words.to_dict(orient='records')
current_card = {}


def next_card():
    global current_card, flip_timer, french_words
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(label_language, text='French', fill='black')
    canvas.itemconfig(tagOrId=label_word, text=current_card['French'], fill='black')
    canvas.itemconfig(canvas_background, image=card_image_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(label_language, text='English', fill='white')
    canvas.itemconfig(label_word, text=current_card['English'], fill='white')
    canvas.itemconfig(canvas_background, image=card_image_back)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
flip_timer = window.after(3000, flip_card)
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=25)
canvas = Canvas(width=800, height=526, borderwidth=0, background=BACKGROUND_COLOR, highlightthickness=0)
card_image_front = PhotoImage(file='images/card_front.png')
card_image_back = PhotoImage(file='images/card_back.png')
canvas_background = canvas.create_image(400, 263, image=card_image_front)
canvas.grid(column=0, row=0, columnspan=2, pady=25)

wrong_button_image = PhotoImage(file='images/wrong.png')
btn_wrong = Button(image=wrong_button_image, pady=25, borderwidth=0, command=next_card)
btn_wrong.grid(column=0, row=1)

rigth_button_image = PhotoImage(file='images/right.png')
btn_rigth = Button(image=rigth_button_image, pady=25, borderwidth=0, command=is_known)
btn_rigth.grid(column=1, row=1)

label_language = canvas.create_text(400, 150, text='', font=(FONT_NAME, 40, 'italic'))
label_word = canvas.create_text(400, 263, text='', font=(FONT_NAME, 60, 'bold'))

next_card()
window.mainloop()
