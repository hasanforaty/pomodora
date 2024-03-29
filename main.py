import tkinter as tk
from pygame import mixer
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
mixer.init()


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
timer_is_running = False


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    if timer_is_running:
        minutes = count // 60
        seconds = count % 60
        canvas.itemconfig(count_down_text, text=f"{minutes:02d}:{seconds:02d}")
        if count > 0:
            windows.after(1000, count_down, count - 1)
        else:
            start_timer()
            checkmark = ''
            number = reps // 2
            while number > 0:
                checkmark += CHECK_MARK
                number -= 1
            checkmark_text.config(text=checkmark)


# ---------------------------- UI SETUP ------------------------------- #

windows = tk.Tk()
windows.title("Pomodoro App")
windows.config(padx=100, pady=50, bg=YELLOW)

# Timer
timer_label = tk.Label(text='Timer', font=(FONT_NAME, 80, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Canvas (Potato)
canvas = tk.Canvas(windows, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
count_down_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


# start and reset Button
def start_timer():
    global timer_is_running
    global reps
    timer_is_running = True
    reps += 1
    start_button.config(text='stop', command=stop_timer)
    if reps % 8 == 0:
        mixer.music.load('Hope_study.mp3')
        time = LONG_BREAK_MIN
        timer_label.config(text='Long break', fg=RED)
    elif reps % 2 == 0:
        mixer.music.load('Tic_Tac.mp3')
        time = SHORT_BREAK_MIN
        timer_label.config(text='Short break', fg=PINK)
    else:
        mixer.music.load('river-stream.mp3')
        time = WORK_MIN
        timer_label.config(text='Work time', fg=GREEN)
    mixer.music.set_volume(0.1)
    mixer.music.play(loops=-1)
    count_down(time * 60)


def reset_timer():
    global timer_is_running
    global reps
    timer_is_running = False
    timer_label['text'] = ''
    canvas.itemconfig(count_down_text, text='00:00')
    timer_label.config(text='Timer')
    reps = 0
    mixer.music.stop()
    mixer.music.unload()
    start_button.config(text='start', command=start_timer)


def stop_timer():
    start_button.config(text='resume', command=resume_timer)
    global timer_is_running
    timer_is_running = False
    mixer.music.pause()


def resume_timer():
    global reps
    global timer_is_running
    mixer.music.unpause()
    reps = 0
    timer_is_running = True
    start_button.config(text='start', command=stop_timer)
    text = canvas.itemcget(count_down_text, 'text').split(":")
    minute = int(text[0])
    second = int(text[1])
    count = minute*60 + second
    count_down(count)


start_button = tk.Button(text="Start", command=start_timer, font=(FONT_NAME, 10, 'bold'), highlightthickness=1)
start_button.grid(row=2, column=0)
reset_button = tk.Button(text="reset", command=reset_timer, font=(FONT_NAME, 10, 'bold'), highlightthickness=1)
reset_button.grid(row=2, column=2)

# add checkmark
checkmark_text = tk.Label(text="", font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW)
checkmark_text.grid(row=3, column=1)

windows.mainloop()
