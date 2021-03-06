from tkinter import *
import game

root = Tk()

root.geometry("800x600")
root.title('Impostor detector')
root.configure(background='black')
img = PhotoImage(file="among-us-logo.png")
lbl_img = Label(root, image=img, borderwidth=0).pack()

def color(color, name):
    print(name)
    game.main(color, name)

Label(root, text='Custom name:\n', fg="white", background='black').pack()
text_field = Text(root, height=1, width=12, insertbackground='white', bg='black', fg='white')
text_field.pack()
Label(root, text="\n", background='black').pack()
text1 = Label(root, text="Select the character:", fg="white", background='black').pack()
button1 = Button(root, text="  red   ", fg="red", background='black', borderwidth=0, command=lambda: color('red', text_field.get("1.0", 'end-1c')))
button2 = Button(root, text="yellow", fg="yellow", background='black', borderwidth=0, command=lambda: color('yellow', text_field.get("1.0", 'end-1c')))
button3 = Button(root, text=" green ", fg="lightgreen", background='black', borderwidth=0, command=lambda: color('green', text_field.get("1.0", 'end-1c')))
button4 = Button(root, text="  cyan  ", fg="cyan", background='black', borderwidth=0, command=lambda: color('cyan', text_field.get("1.0", 'end-1c')))

button1.pack()
button2.pack()
button3.pack()
button4.pack()

"""
muito gamer
"""

root.mainloop()
