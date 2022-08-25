from tkinter import *
from word_bank import WordBank
from tkinter import messagebox

LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
BUTTON_FONT = ("Arial", 16, "bold")
BACKGROUND_COLOR = "#B1DDC6"
card_state = "French"


def flip_card():
    global card_state
    if card_state == "French":
        canvas.itemconfig(language_text, text="English")
        canvas.itemconfig(word_text, text=word_bank.current_word["English"])
        canvas.itemconfig(card, image=card_back_img)
        card_state = "English"
    elif card_state == "English":
        canvas.itemconfig(language_text, text="French")
        canvas.itemconfig(word_text, text=word_bank.current_word["French"])
        canvas.itemconfig(card, image=card_front_img)
        card_state = "French"


def replace_card():
    new_word = word_bank.random_word()
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=new_word["French"])
    canvas.itemconfig(card, image=card_front_img)

    global card_state
    card_state = "French"


def right_button_press():
    if word_bank.check_out_of_cards():
        messagebox.showinfo(title="Congratulations", message="You have completed all flash cards!")
        return
    word_bank.remove_current_word()
    replace_card()


def wrong_button_press():
    replace_card()


def reset():
    confirmation = messagebox.askyesno(title="Reset",
                                       message=f"Would you like to place all flash cards back into the list?")
    if confirmation:
        word_bank.reset_bank()
        replace_card()


word_bank = WordBank()

window = Tk()
window.title("Flashcards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text=word_bank.current_word["French"], font=WORD_FONT)
canvas.grid(row=1, column=0, columnspan=5)

# Buttons
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=right_button_press)
right_button.grid(column=3, row=2)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=wrong_button_press)
wrong_button.grid(column=0, row=2)
flip_button = Button(text="FLIP", bg=BACKGROUND_COLOR, highlightthickness=0, font=BUTTON_FONT,
                     command=flip_card, width=6)
flip_button.grid(column=2, row=2)
reset_button = Button(text="RESET", bg=BACKGROUND_COLOR, highlightthickness=0, font=BUTTON_FONT, command=reset)
reset_button.grid(column=1, row=2)


window.mainloop()
