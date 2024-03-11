import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("1000x1000")

player = "1"

default_image1 = Image.open("1080 copy 2.png")
img1 = ImageTk.PhotoImage(default_image1)
default_image2 = Image.open("joe.jpeg")
img2 = ImageTk.PhotoImage(default_image2)
default_image3 = Image.open("walmart.png")
img3 = ImageTk.PhotoImage(default_image3)






a00 = 0
a01 = 0
a02 = 0
a10 = 0
a11 = 0
a12 = 0
a20 = 0
a21 = 0
a22 = 0

def reset():
    global player, a00, a01, a02, a10, a11, a12, a20, a21, a22
    a00 = 0
    a01 = 0
    a02 = 0
    a10 = 0
    a11 = 0
    a12 = 0
    a20 = 0
    a21 = 0
    a22 = 0
    player = "1"
    button00.config(state="normal")
    button01.config(state="normal")
    button02.config(state="normal")
    button10.config(state="normal")
    button11.config(state="normal")
    button12.config(state="normal")
    button20.config(state="normal")
    button21.config(state="normal")
    button22.config(state="normal")
    button00.config(image=img3)
    button01.config(image=img3)
    button02.config(image=img3)
    button10.config(image=img3)
    button11.config(image=img3)
    button12.config(image=img3)
    button20.config(image=img3)
    button21.config(image=img3)
    button22.config(image=img3)



def tictactoe():
    global player, a00, a01, a02, a10, a11, a12, a20, a21, a22

    if a00 == 1 and a01 == 1 and a02 == 1:
        winner.config(text="Player 1 wins!")
        reset()
    if a10 == 1 and a11 == 1 and a12 == 1:
        winner.config(text="Player 1 wins!")
        reset()
    if a20 == 1 and a21 == 1 and a22 == 1:
        winner.config(text="Player 1 wins!")
        reset()
    if a00 == 1 and a10 == 1 and a20 == 1:
        winner.config(text="Player 1 wins!")
        reset()
    if a01 == 1 and a11 == 1 and a21 == 1:
        winner.config(text="Player 1 wins!")
        reset()
    if a02 == 1 and a12 == 1 and a22 == 1:
        winner.config(text="Player 1 wins!")
        reset()
    if a00 == 1 and a11 == 1 and a22 == 1:
        winner.config(text="Player 1 wins!")
        reset()
    if a02 == 1 and a11 == 1 and a20 == 1:
        winner.config(text="Player 1 wins!")
        reset()

    if a00 == 2 and a01 == 2 and a02 == 2:
        winner.config(text="Player 2 wins!")
        reset()
    if a10 == 2 and a11 == 2 and a12 == 2:
        winner.config(text="Player 2 wins!")
        reset()
    if a20 == 2 and a21 == 2 and a22 == 2:
        winner.config(text="Player 2 wins!")
        reset()
    if a00 == 2 and a10 == 2 and a20 == 2:
        winner.config(text="Player 2 wins!")
        reset()
    if a01 == 2 and a11 == 2 and a21 == 2:
        winner.config(text="Player 2 wins!")
        reset()
    if a02 == 2 and a12 == 2 and a22 == 2:
        winner.config(text="Player 2 wins!")
        reset()
    if a00 == 2 and a11 == 2 and a22 == 2:
        winner.config(text="Player 2 wins!")
        reset()
    if a02 == 2 and a11 == 2 and a20 == 2:
        winner.config(text="Player 2 wins!")
        reset()



def bottom(button):
    global player, a00, a01, a02, a10, a11, a12, a20, a21, a22

    if button == 0 and button20.cget("image") is not img3:
        if player == "1":
            button20.config(image=img1)
            player = "2"
            button20.config(state="disabled")
            a20 = 1
            tictactoe()
        elif player == "2":
            button20.config(image=img2)
            player = "1"
            button20.config(state="disabled")
            a20 = 2
            tictactoe()
    elif button == 1 and button21.cget("image") is not img3:
        if player == "1":
            button21.config(image=img1)
            player = "2"
            button21.config(state="disabled")
            a21 = 1
            tictactoe()
        elif player == "2":
            button21.config(image=img2)
            player = "1"
            button21.config(state="disabled")
            a21 = 2
            tictactoe()
    elif button == 2 and button22.cget("image") is not img3:
        if player == "1":
            button22.config(image=img1)
            player = "2"
            button22.config(state="disabled")
            a22 = 1
            tictactoe()
        elif player == "2":
            button22.config(image=img2)
            player = "1"
            button22.config(state="disabled")
            a22 = 2
            tictactoe()


def middle(button):
    global player, a00, a01, a02, a10, a11, a12, a20, a21, a22

    if button == 0 and button10.cget("image") is not img3:
        if player == "1":
            button10.config(image=img1)
            player = "2"
            button10.config(state="disabled")
            a10 = 1
            tictactoe()
        elif player == "2":
            button10.config(image=img2)
            player = "1"
            button10.config(state="disabled")
            a10 = 2
            tictactoe()
    elif button == 1 and button11.cget("image") is not img3:
        if player == "1":
            button11.config(image=img1)
            player = "2"
            button11.config(state="disabled")
            a11 = 1
            tictactoe()
        elif player == "2":
            button11.config(image=img2)
            player = "1"
            button11.config(state="disabled")
            a11 = 2
            tictactoe()
    elif button == 2 and button12.cget("image") is not img3:
        if player == "1":
            button12.config(image=img1)
            player = "2"
            button12.config(state="disabled")
            a12 = 1
            tictactoe()
        elif player == "2":
            button12.config(image=img2)
            player = "1"
            button12.config(state="disabled")
            a12 = 2
            tictactoe()


def top(button):
    global player, a00, a01, a02, a10, a11, a12, a20, a21, a22

    if button == 0 and button00.cget("image") is not img3:
        if player == "1":
            button00.config(image=img1)
            player = "2"
            button00.config(state="disabled")
            a00 = 1
            tictactoe()
        elif player == "2":
            button00.config(image=img2)
            player = "1"
            button00.config(state="disabled")
            a00 = 2
            tictactoe()
    elif button == 1 and button01.cget("image") is not img3:
        if player == "1":
            button01.config(image=img1)
            player = "2"
            button01.config(state="disabled")
            a01 = 1
            tictactoe()
        elif player == "2":
            button01.config(image=img2)
            player = "1"
            button01.config(state="disabled")
            a01 = 2
            tictactoe()
    elif button == 2 and button02.cget("image") is not img3:
        if player == "1":
            button02.config(image=img1)
            player = "2"
            button02.config(state="disabled")
            a02 = 1
            tictactoe()
        elif player == "2":
            button02.config(image=img2)
            player = "1"
            button02.config(state="disabled")
            a02 = 2
            tictactoe()


button00 = tk.Button(root, image=img3, command=lambda: top(0))
button01 = tk.Button(root, image=img3, command=lambda: top(1))
button02 = tk.Button(root, image=img3, command=lambda: top(2))
button10 = tk.Button(root, image=img3, command=lambda: middle(0))
button11 = tk.Button(root, image=img3, command=lambda: middle(1))
button12 = tk.Button(root, image=img3, command=lambda: middle(2))
button20 = tk.Button(root, image=img3, command=lambda: bottom(0))
button21 = tk.Button(root, image=img3, command=lambda: bottom(1))
button22 = tk.Button(root, image=img3, command=lambda: bottom(2))
reset_button = tk.Button(root, text="Reset", command=lambda: reset())
winner = tk.Label(root, text="")


button00.grid(row=0, column=0, ipadx=0, ipady=0)
button01.grid(row=0, column=1, ipadx=0, ipady=0)
button02.grid(row=0, column=2, ipadx=0, ipady=0)
button10.grid(row=1, column=0, ipadx=0, ipady=0)
button11.grid(row=1, column=1, ipadx=0, ipady=0)
button12.grid(row=1, column=2, ipadx=0, ipady=0)
button20.grid(row=2, column=0, ipadx=0, ipady=0)
button21.grid(row=2, column=1, ipadx=0, ipady=0)
button22.grid(row=2, column=2, ipadx=0, ipady=0)
reset_button.grid(row=3, column=1, ipadx=0, ipady=0)
winner.grid(row=4, column=1)


root.mainloop()
