from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = "✔"
timer = None


def reset_timer():
    global reps
    window.after_cancel(timer1)
    timeer_label.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timeer_label.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timeer_label.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timeer_label.config(text="WORK", fg=GREEN)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer1
        timer1 = window.after(1000, count_down, count - 1)
    else:
        global mark
        start_timer()
        if reps % 2 == 0:
            check_mark_label.config(text=mark)
            mark += "✔"


window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timeer_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 30, "bold"), fg=GREEN)
timeer_label.grid(column=1, row=0)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 8, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 8, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark_label = Label(bg=YELLOW, font=(FONT_NAME, 10, "bold"), fg=GREEN)
check_mark_label.grid(column=1, row=3)


window.mainloop()
