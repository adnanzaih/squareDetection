from tkinter import *


def backgroundStyle(root):

    background_image = PhotoImage("bg.jpg")
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.pack(side="bottom", fill="both", expand="yes")