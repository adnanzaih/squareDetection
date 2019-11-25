from tkinter import *


def backgroundStyle(root):
    image1 = PhotoImage(file="bg.gif")
    label_for_image = Label(root, image=image1)
    label_for_image.place(x=0, y=0, relwidth=1, relheight=1, )
    label_for_image.pack(side='top', fill='both', expand='yes')
    root.mainloop()