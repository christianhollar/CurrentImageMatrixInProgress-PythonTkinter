import tkinter
from tkinter import *
from tkinter import filedialog
import uploadJSON

filename = ''

def findjson():
    # 1. Tkinter Upload Window Created
    root = tkinter.Tk()
    # 2. Tkinter Upload Window Background Set to Black
    root.configure(background="black")

    def click():
        # 5. User Defines Filename
        global filename
        filename = filedialog.askopenfilename(master=root, initialdir='/Desktop')
        root.destroy()
        uploadJSON.uploadjson()

    # 3. Tkinter Upload Window Title Set to Upload Window
    root.title("Upload Window")
    # 4. File Dialog Button
    button = Button(root,text="Click to Select JSON File",width=20,command=click)
    button.pack(side=TOP)
    button.pack()
    root.mainloop()