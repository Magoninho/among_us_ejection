from tkinter import *
import game

root = Tk()

root.geometry("800x600")
root.configure(background='black')
img = PhotoImage(file="among-us-logo.png")
lbl_img = Label(root, image=img, borderwidth=0).pack()

def color(color):
    game.main(color)

test = 0
Label(root, text="\n\n", background='black').pack()
text1 = Label(root, text="Selecione o personagem:", fg="white", background='black').pack()
button1 = Button(root, text="  red   ", fg="red", background='black', borderwidth=0, command=lambda: color('red')).pack()
button2 = Button(root, text="yellow", fg="yellow", background='black', borderwidth=0, command=lambda: color('yellow')).pack()
button3 = Button(root, text=" green ", fg="lightgreen", background='black', borderwidth=0, command=lambda: color('green')).pack()
button4 = Button(root, text="  cyan  ", fg="cyan", background='black', borderwidth=0, command=lambda: color('cyan')).pack()

"""
muito gamer
"""

root.mainloop()