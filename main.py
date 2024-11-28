from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window= Tk()
window.title("Flash Card")
window.config(bg = BACKGROUND_COLOR, padx = 50, pady = 50)
right_image = PhotoImage(file ="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_front_image = PhotoImage(file = "images/card_front.png")
card_back_image = PhotoImage(file = "images/card_back.png")

#The buttons
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column =1)
wrong_Button = Button(image=wrong_image, highlightthickness=0)
wrong_Button.grid(row=1, column =0)

#The middle card as canvas
canvas = Canvas(width = 800, height = 526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400,263,image = card_front_image)
canvas.create_text(400, 150, text="Title", font=("Arial", 40,"italic"))
canvas.create_text(400,263,text = "Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0,column = 0, columnspan=2)









window.mainloop()