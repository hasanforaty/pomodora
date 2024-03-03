import tkinter as tk

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
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

windows = tk.Tk()
windows.title("Pomodoro App")
windows.config(padx=100, pady=50, bg=YELLOW)

# Timer
timer = tk.Label(text='Timer', font=(FONT_NAME, 80, 'bold'), fg=GREEN, bg=YELLOW)
timer.grid(row=0, column=1)

# Canvas (Potato)
canvas = tk.Canvas(windows, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


# start and reset Button
def start_timer():
    pass


def stop_timer():
    pass


start_button = tk.Button(text="Start", command=start_timer, font=(FONT_NAME, 10, 'bold'), highlightthickness=0)
start_button.grid(row=2, column=0)
stop_button = tk.Button(text="Stop", command=stop_timer, font=(FONT_NAME, 10, 'bold'), highlightthickness=0)
stop_button.grid(row=2, column=2)

# add checkmark
checkmark_text = tk.Label(text=CHECK_MARK, font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW)
checkmark_text.grid(row=3, column=1)

windows.mainloop()
