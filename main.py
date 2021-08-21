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


def timer_reset():
    window.after_cancel(timer)
    label1.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label2.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer_start():
    global reps

    reps += 1

    if reps % 8 == 0:
        count_down(20*60)
        label1.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(5*60)
        label1.config(text='Break', fg=PINK)
    else:
        count_down(25*60)
        label1.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    count_min = count//60
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        timer_start()
        label2.config(text=reps//2*'✔')

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

label1 = Label(text='Timer', font=(FONT_NAME, 50, 'normal'), fg=GREEN, bg=YELLOW)
label1.grid(column=1, row=0)

start = Button(text='Start', highlightthickness=0, command=timer_start)
start.grid(column=0, row=2)

reset = Button(text='Reset', highlightthickness=0, command=timer_reset)
reset.grid(column=2, row=2)

label2 = Label(fg=GREEN, bg=YELLOW)
label2.grid(column=1, row=3)

window.mainloop()
