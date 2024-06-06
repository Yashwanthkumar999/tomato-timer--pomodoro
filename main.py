from tkinter import *

# TIME mechanism
import time
import math


def start_count():
    count_down(300)

def reset_count():
    canvas.itemconfig(screen_text, text=f"00:00")



def count_down(count):
    min_count = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(screen_text, text=f"{min_count}:{sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


window = Tk()
window.config(bg="yellow")
window.title("POMODORO")
window.config(padx=50, pady=50)

timer_label = Label(text="Timer", fg="green")
timer_label.config(bg="yellow", font=("arial", 35, "bold"))
timer_label.grid(row=1, column=2)

canvas = Canvas(width=280, height=270, highlightthickness=0, bg="yellow")
photo_img = PhotoImage(file="tomato12.png")
canvas.create_image(150, 130, image=photo_img)
screen_text = canvas.create_text(150, 150, text="00:00", fill="white", font=("arial", 25, "bold"))
canvas.grid(row=2, column=2)

start_button = Button(text="Start", highlightthickness=0, command=start_count)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_count)
reset_button.grid(row=3, column=3)

check_box = Label(text="√", bg="yellow", fg="green")
check_box.grid(row=4, column=2)

window.mainloop()
