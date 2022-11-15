from random import randint
from tkinter import *
import tkinter.font as font
from playsound import playsound
from PIL import ImageTk, Image

secret_number = randint(0, 10)
max_tries = 3
attempts = 0
found = False
found_subs = -1


def close_window():
    playsound('\\python\\GUI\\Guess_the_number\\exit.mp3')  # sound by Camouflaged_Noob
    root.destroy()


def donut_destroy():
    playsound('\\python\\GUI\\Guess_the_number\\donut.mp3')  # sound by rj10328
    donut_button.destroy()


def show_hint():
    playsound('\\python\\GUI\\Guess_the_number\\click.mp3')  # sound by deadsillyrabbit
    hint = Label(root, text="The number is between 0 and 10", pady=5)
    hint.grid(row=5, column=0)


def open_message_box(x):
    top = Toplevel()
    guess_too_low_msg = Label(top, text=f"Your guess is too {x}.", width=20, height=2).pack()
    top.iconbitmap("icon.ico")
    ok_button = Button(top, text="OK", command=top.destroy).pack()


def game_won():
    global found
    message = Label(root, text="You found it!", padx=150, pady=20)
    message.grid(row=3, column=0)
    message2 = Label(root, text="Here's a donut for your reward:", pady=5)
    message2.grid(row=5, column=0)
    donut_bunny = Label(root, text="{\\__/}\n( • . •)\n/    >")
    donut_bunny.grid(row=6, column=0)
    donut_button.place(x=229, y=209, anchor=CENTER)
    found = True


def submit():
    global attempts
    global found_subs
    global found
    global secret_number

    playsound('\\python\\GUI\\Guess_the_number\\click.mp3')  # sound by deadsillyrabbit

    while not found:
        try:
            user_input = int(num_field.get())
        except ValueError:
            break

        attempts += 1

        if attempts < max_tries:
            if user_input == secret_number:
                hint_button.destroy()
                game_won()

            if user_input != secret_number:
                message = Label(root, text=f"Unfortunately {user_input} is not the hidden number. Try "
                                           f"again...", pady=5)
                message.grid(row=3, column=0)
                if user_input < secret_number:
                    open_message_box("low")
                else:
                    open_message_box("high")
                break

        elif attempts == max_tries:
            hint_button.destroy()
            if user_input == secret_number:
                game_won()
            else:
                message = Label(root, text=f" Well, {user_input} is not the hidden number and "
                                           f"you have no more tries left.\nYou lost.")
                message.grid(row=3, column=0)
                break

        elif attempts == max_tries + 1:
            message = Label(root, text="It's game over. You can leave now.")
            message.grid()
            break
        elif attempts == max_tries + 2:
            message = Label(root, text="You are out of tries. Please stop guessing.")
            message.grid()
            break
        elif attempts == max_tries + 3:
            message = Label(root, text="Why do you keep pressing the button?")
            message.grid()
            break
        elif attempts == max_tries + 4:
            message = Label(root, text="You are OUT OF TRIES. It's over!")
            message.grid()
            break
        elif attempts == max_tries + 5:
            submit_button = Button(root, text="Submit my guess!", bd=2, command=submit, state=DISABLED)
            submit_button.grid(row=2, column=0)
            exit_button = Button(root, text='Exit', command=close_window)
            exit_button.grid()
            break
    else:
        found_subs += 1
        if found_subs == 1:
            message = Label(root, text="You have already found the number. What more do you want?", width=55)
            message.grid()
        if found_subs == 2:
            message = Label(root, text="I already gave you a donut.", width=55)
            message.grid()
        if found_subs == 4:
            message = Label(root, text="Please stop pressing this button.")
            message.grid()
        if found_subs == 6:
            message = Label(root, text="See? It does nothing now.")
            message.grid()
        if found_subs == 7:
            donut_bunny = Label(root, text="{\\__/}\n( - . -)\n/    >")
            donut_bunny.grid(row=6, column=0)
        if found_subs == 8:
            submit_button = Button(root, text="Submit my guess!", bd=2, command=submit, state=DISABLED)
            submit_button.grid(row=2, column=0)
            exit_button = Button(root, text='Exit', command=close_window)
            exit_button.grid()


def next_func():
    playsound('\\python\\GUI\\Guess_the_number\\click.mp3')  # sound by deadsillyrabbit
    print(secret_number)
    # clear
    info_line0.destroy()
    info_line1.destroy()
    info_line2.destroy()
    next_button.destroy()

    # text field with prompt
    num_field_txt_prompt = Label(root, text="Type in your guess: ", width=55, bd=10)
    num_field_txt_prompt.grid(row=0, column=0)
    num_field.grid(row=1, column=0)

    # submit button
    submit_button = Button(root, text="Submit my guess!", bd=1, command=submit)
    submit_button.grid(row=2, column=0)

    # draw hint button
    hint_button.grid(row=5, column=0)


root = Tk()
root.title("Guess the number")
root.geometry("400x400")
root.iconbitmap("icon.ico")
root.config(cursor='@cursor.cur')

num_field = Entry(root, width=5)
hint_button = Button(root, text="Get Hint", command=show_hint)

# define font
small = font.Font(size=8)
bold_and_big = font.Font(size=10, weight='bold')

# donut
donut_img = ImageTk.PhotoImage(Image.open("donut.png"))
donut_button = Button(root, image=donut_img, borderwidth=0, command=donut_destroy)

# startup screen
info_line0 = Label(root, text="There is a number hidden inside this program", width=40, pady=15)
info_line0['font'] = bold_and_big
info_line0.grid(row=0, column=0)
info_line1 = Label(root, text="You have 3 tries to find it", width=55, pady=10)
info_line1.grid(row=1, column=0)
info_line2 = Label(root, text='Click on Next to begin', fg='gray', width=55, pady=5)
info_line2['font'] = small
info_line2.grid(row=3, column=0)
next_button = Button(root, text="Next", command=next_func)
next_button.grid(row=2, column=0)

root.mainloop()