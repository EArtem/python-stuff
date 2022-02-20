from tkinter import *


#Creating a new window and configurations
window = Tk()
window.title("km to miles")

#Labels
is_equal_to = Label(text="Is equal to")
is_equal_to.grid(column=0, row=1)

mi_label = Label(text='mi')
mi_label.grid(column=2, row=1)


#Buttons
def insert_miles():
    mi_to_km = round(int(miles.get()) * 1.609344, 3)
    kilometers.config(text=mi_to_km)


#calls action() when pressed
btn_calculate = Button(text="Calculate", command=insert_miles)
btn_calculate.grid(column=1, row=2)


#Entries
miles = Entry(width=5, takefocus=True)
#Add some text to begin with
#Gets text in entry
print(miles.get())
miles.grid(column=1, row=0)

kilometers = Label()
kilometers.grid(column=1, row=1)

km_label = Label()
km_label.config(text='km')
km_label.grid(column=2, row=0)

window.mainloop()