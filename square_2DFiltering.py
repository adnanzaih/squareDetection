from tkinter import *
import os
from utils import backgroundStyle

root = Tk()
root.title("Dropdown Menu")
root.configure(background="black")
file_list = []
file_dir = "N:/MedicalPhysics/Quality Control Program/Treatment/Weekly/Winston-Lutz/Unit 08 SN3864/2019_11_18/QA Winston-Lutz U8/"

for file in os.listdir(file_dir):
    if file.endswith(".dcm"):
        file_list.append(file)

print(file_list[:])


# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

#backgroundStyle(mainframe)
# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
tkvar.set(file_list[0]) # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *file_list)
Label(mainframe, text="Choose a file").grid(row = 1, column = 1)
popupMenu.grid(row=2, column=1)

# on change dropdown value
def change_dropdown(*args):
    print(tkvar.get())

# link function to change dropdown
tkvar.trace('w', change_dropdown)
root.mainloop()
