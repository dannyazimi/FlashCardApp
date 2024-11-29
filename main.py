from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():

    random_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French")
    canvas.itemconfig(card_word, text = random_word["French"])


window= Tk()
window.title("Flash Card")
window.config(bg = BACKGROUND_COLOR, padx = 50, pady = 50)
right_image = PhotoImage(file ="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_front_image = PhotoImage(file = "images/card_front.png")
card_back_image = PhotoImage(file = "images/card_back.png")

#The buttons
right_button = Button(image=right_image, highlightthickness=0,command=next_card)
right_button.grid(row=1, column =1)
wrong_Button = Button(image=wrong_image, highlightthickness=0,command=next_card)
wrong_Button.grid(row=1, column =0)

#The middle card as canvas
canvas = Canvas(width = 800, height = 526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400,263,image = card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40,"italic"))
card_word = canvas.create_text(400,263,text = "", font=("Ariel", 60, "bold"))
canvas.grid(row=0,column = 0, columnspan=2)

next_card()







window.mainloop()