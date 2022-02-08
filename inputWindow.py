import tkinter
from tkinter import *
import imageSort

wdth = 20
hght = 20
mheight = 2
mwidth = 2
basewidth = 400

def input_window():
    from uploadJSON import parameter_length
    from uploadJSON import parameter_names

    global wdth
    global hght

    #Initial Search Window
    root = tkinter.Tk()
    entry_dict = {}

    def display():
        # Triggered by Submit
        global mheight
        global mwidth
        global basewidth

        inputlist = [0]*parameter_length

        # Create Search Array Containing:
        # Parameter Values
        # Matrix Height & Width
        # Image Width

        for i in range(parameter_length):
            inputlist[i]=entry_dict[i].get()
        if mheightentry.get() != '':
            mheight = int(mheightentry.get())
        if mwidthentry.get() != '':
            mwidth = int(mwidthentry.get())
        if bwidthentry.get()!='':
            basewidth = int(bwidthentry.get())

        # Close Window
        root.destroy()

        # Search for Corresponding Images
        imageSort.imagesort(inputlist)

    root.title("Input")
    root.config(bg="#0b3d91")

    # Create Input Labels for Each Parameter

    for i in range(parameter_length):
        label = Label(root,width=wdth,text=parameter_names[i])
        label.grid(row=i,column=0)
        label.config(bd=5, bg="#0b3d91",fg='white')
        entry_dict[i] = Entry(root,width=wdth)
        entry_dict[i].config(highlightbackground="#FC3D21")
        entry_dict[i].grid(row=i,column=1)

    # Matrix Height Label, Entry, Current
    mheightentry = Entry(root,width=wdth)
    mheightentry.grid(row=parameter_length,column=1)
    mheightentry.config(highlightbackground="#FC3D21")

    hlabel=Label(root, width=wdth,text = "Matrix Height:",bd=5, bg="#0b3d91",fg='white')
    hlabel.grid(row=parameter_length,column=0)

    # Matrix Width Label, Entry, Current
    mwidthentry = Entry(root,width=wdth)
    mwidthentry.config(highlightbackground="#FC3D21")
    mwidthentry.grid(row=parameter_length+1,column=1)

    wlabel = Label(root, width=wdth, text="Matrix Width:",bd=5, bg="#0b3d91",fg='white')
    wlabel.grid(row=parameter_length+1, column=0)


    # Image Width Label, Entry, Current
    bwidthentry = Entry(root, width=wdth)
    bwidthentry.config(highlightbackground="#FC3D21")
    bwidthentry.grid(row=parameter_length + 2, column=1)

    blabel = Label(root, width=wdth, text="Image Size:",bd=5, bg="#0b3d91",fg='white')
    blabel.grid(row=parameter_length + 2, column=0)

    # Submit Button
    submit = Button(root,width=20,text="Submit Parameters",bg="#FC3D21",command=display)
    submit.config(highlightbackground="#FC3D21")
    submit.grid(row=parameter_length+3,column=1)

    root.mainloop()