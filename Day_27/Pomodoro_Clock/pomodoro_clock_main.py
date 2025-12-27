import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_secs = 5
    short_break_secs = 5
    long_break_secs = 5

    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text='BREAK', font=(FONT_NAME, 50), fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        timer_label.config(text='BREAK', font=(FONT_NAME, 50), fg=PINK)
    else:
        count_down(work_secs)
        timer_label.config(text='WORK', font=(FONT_NAME, 50), fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_mins = count // 60
    count_secs = count % 60
    canvas.itemconfig(timer_text, text=f"{count_mins:02d}:{count_secs:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        ticks_amount = math.floor(reps/2)
        ticks=''
        for _ in range(ticks_amount):
            ticks += '✅'
        tick_label.config(text=ticks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 30, 'bold'))

canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text='Start', highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

tick_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
tick_label.grid(row=3, column=1)

window.mainloop()