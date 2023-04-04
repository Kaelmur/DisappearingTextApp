import tkinter as tk

screen = tk.Tk()
screen.title("Disappearing text App")
is_on = True
second_passed = 0
text = tk.Label()


def start():
    if is_on:
        label = tk.Label(screen, text="Don't stop writing! After 5 second text will disappear!")
        label.grid(column=1, row=0)
        global text
        text = tk.Label(screen, text="")
        text.grid(column=1, rows=1)
        screen.bind("<Key>", pressed)
        screen.after(1000, second)


def pressed(event):
    global is_on
    is_on = True
    try:
        if event.char.lower:
            global second_passed
            text.configure(text=text.cget("text") + event.char.lower())
            second_passed = 0
    except tk.TclError:
        pass


def second():
    global second_passed
    global is_on
    second_passed += 1
    if is_on:
        screen.after(1000, second)
        if second_passed == 5:
            words = len(text.cget("text").split(" "))
            result = tk.Label(screen, text=f"Record: {words} words.", fg="black")
            result.grid(column=1, row=3)
            vanish()


def vanish():
    global text
    text.configure(text="")


start()
screen.mainloop()
