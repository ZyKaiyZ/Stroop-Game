# pylint: disable=C0114, W0603
from tkinter import Tk, Label, Button, PhotoImage
import random
from functools import partial

CORRECT = FAIL = 0
COUNTER = NUMBER = 6

def game_over():
    """
    Update the text and hide the score label
    """
    label.config(text="Time's Up\n\nClick button to restart", fg="black")
    time_label.config(text="Time's Up")

def game_restart():
    """
    Update the text and score label
    """
    label.config(text="黑色", fg="black")
    correct_label.config(text="Correct : 0")
    fail_label.config(text="Fail : 0")
    time_label.config(text="Time : 3")
    global COUNTER, FAIL, CORRECT
    COUNTER = NUMBER
    CORRECT = FAIL = 0
    restart_btn.forget()
    update_counter()

def update_counter():
    """
    Set the time and show game over
    """
    global COUNTER
    COUNTER -= 1
    time_label.config(text="Time : " + str(COUNTER))
    if COUNTER > 0:
        window.after(1000, update_counter)
    else:
        game_over()
        restart_btn.pack(side='left', padx='50', fill='x')

def button_clicked(index):
    """
    Updates the score and the text with a random color 
    Restart the game when time is over
    """
    if COUNTER > 0:
        color_array = ['紅色', '藍色', '綠色', '黑色', '黃色']
        if index == label['fg']:
            global CORRECT
            CORRECT = CORRECT + 1
            correct_label.config(text="Correct : " + str(CORRECT))
        else:
            global FAIL
            FAIL = FAIL+1
            fail_label.config(text="Fail : " + str(FAIL))

        random_color = random.choice(color_array)
        label.config(text=random_color,
                    fg=random.choice(['red', 'blue', 'green', 'black', 'yellow']))

def creat_buttons():
    """
    Create and display buttons with different background colors
    """
    seq = ["red", "blue", "green", "black", "yellow"]
    for color in seq:
        Button(width=10, height=5, padx=5, bg=color,
            command=partial(button_clicked, color)).pack(side='left', padx='20', fill='x')

window = Tk()
window.title("Stroop Game")
window.iconphoto(False, PhotoImage(file="./img/favicon.png"))
window.configure(bg="#7AFEC6")
window.minsize(width=500, height=500)
window.resizable(width=False, height=False)

correct_label = Label(text="Correct : 0", font=("Arial", 10, "bold"), bg="#7AFEC6", fg="black")
fail_label = Label(text="Fail : 0", font=("Arial", 10, "bold"), bg="#7AFEC6", fg="black")
time_label = Label(text="Time : 0", font=("Arial", 10, "bold"), bg="#7AFEC6", fg="black")
label = Label(text="黑色", font=("Arial", 30, "bold"), padx=5, bg="#7AFEC6", fg="black")

correct_label.pack(anchor='n', side='left', padx='30')
fail_label.pack(anchor='n', side='right', padx='30')
time_label.pack(anchor='n', side='top', padx='30')
label.pack(pady='100')

restart_btn = Button(text="R E S T A R T", font=("Arial", 10, "bold"),
                     width=15, height=2, padx=5, bg="black", fg="white", command=game_restart)

creat_buttons()
update_counter()

window.mainloop()
