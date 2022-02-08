import tkinter
from tkinter import *
from PIL import Image,ImageTk
import imageSort

nextindex = 0

def image_display(data_array,mheight,mwidth,basewidth):
    from findJSON import filename

    matrix_height = mheight
    matrix_height = matrix_height*4
    matrix_width = mwidth
    filename = filename.replace('index.json', '')
    root = tkinter.Tk()
    root.title("Matrix Display")
    root.config(bd=10)
    root.config(background="#0b3d91")
    k = 0

    button_dict={}
    next_dict={}
    image_dict={}
    reset_label_dict = {}
    reset_entry_dict = {}
    current_label_dict = {}

    def reset():
        from uploadJSON import parameter_length

        inputlist = [0] * parameter_length

        for i in range(parameter_length):
            if reset_entry_dict[i].get()!='':
                inputlist[i]=int(reset_entry_dict[i].get())
            else:
                inputlist[i]=''
        root.destroy()
        imageSort.imagesort(inputlist)

    def settings():

        from imageSort import current_parameters
        from uploadJSON import parameter_length
        from uploadJSON import parameter_names
        from inputWindow import mheight
        from inputWindow import mwidth
        from inputWindow import basewidth

        settingslevel = tkinter.Toplevel()
        settingslevel.title("New Search")
        settingslevel.config(bg='#0B3D91')

        Label(settingslevel, text="Parameter(s)", fg='white', bg='#0B3D91', width=20).grid(column=0, row=0)
        Label(settingslevel, text="Current", fg='white', bg='#0B3D91', width=20).grid(column=1,row=0)
        Label(settingslevel, text="Input", fg='white', bg='#0B3D91', width=20).grid(column=2,row=0)

        for i in range(parameter_length):
            reset_label_dict[i] = Label(settingslevel, text=parameter_names[i] + ":",fg='white',bg='#0B3D91', width=20)
            reset_label_dict[i].grid(column=0,row=i+1)

            pvalue = current_parameters[i]
            if(pvalue == ''):
                pvalue="No Entry"
            current_label_dict[i] = Label(settingslevel, text=pvalue,fg='white',bg='#0B3D91', width=20).grid(column=1,row=i+1)

            reset_entry_dict[i] = Entry(settingslevel, width=20)
            reset_entry_dict[i].config(highlightbackground="#FC3D21")
            reset_entry_dict[i].grid(column=2, row=i+1)

        def action():

            global basewidth
            global mheight
            global mwidth

            if(bwidthentry.get()!=''):
                basewidth=int(bwidthentry.get())
            if (mheightentry.get() != ''):
                mheight = int(mheightentry.get())
            if (mwidthentry.get() != ''):
                mwidth = int(mwidthentry.get())

            return reset()

        from inputWindow import wdth

        Label(settingslevel, text="Matrix Height:", fg='white',bg='#0B3D91',width=20).grid(column=0, row=parameter_length+1)
        mheightentry = Entry(settingslevel, width=20)
        mheightentry.config(highlightbackground="#FC3D21")
        mheightentry.grid(column=2, row=parameter_length+1)

        Label(settingslevel, text=str(mheight), fg='white', bg='#0B3D91', width=20).grid(column=1, row=parameter_length + 1)

        Label(settingslevel, text="Matrix Width:", fg='white',bg='#0B3D91',width=20).grid(column=0, row=parameter_length + 2)
        mwidthentry = Entry(settingslevel, width=20)
        mwidthentry.config(highlightbackground="#FC3D21")
        mwidthentry.grid(column=2, row=parameter_length + 2)

        Label(settingslevel, text=str(mwidth), fg='white', bg='#0B3D91', width=20).grid(column=1, row=parameter_length + 2)

        Label(settingslevel, width=wdth, text="Image Size:",bg='#0B3D91',fg='white').grid(row=parameter_length + 3, column=0)
        bwidthentry = Entry(settingslevel, width=wdth)
        bwidthentry.config(highlightbackground="#FC3D21")
        bwidthentry.grid(row=parameter_length + 3, column=2)

        Label(settingslevel, text=str(basewidth), fg='white', bg='#0B3D91', width=20).grid(column=1, row=parameter_length + 3)

        Button(settingslevel, text="Submit Parameters", command=action, width=20).grid(column=2,row=parameter_length + 4)
        settingslevel.mainloop()

    def expand(k_input):
        from uploadJSON import data
        newlevel = tkinter.Toplevel(root)
        newlevel.title('Expansion')

        def close():
            newlevel.destroy()

        basewidth = 800
        newlevel.title("Expanded")
        index = data_array[k_input][0]
        image_extension = data[index]['filename']
        imagepath = str(filename + image_extension)
        img = Image.open(imagepath)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(img)
        currentlabel = tkinter.Label(newlevel, image=test)
        currentlabel.image = test
        currentlabel.grid(row=0, column=0)
        closebutton = tkinter.Button(newlevel,text="Close",width = 20,command=close)
        closebutton.grid(row=1,column=0)

        newlevel.mainloop()

    def next(i_input, j_input):

        from inputWindow import mheight
        from inputWindow import mwidth
        from inputWindow import basewidth

        global basewidth
        global nextindex
        global mheight
        global mwidth

        k_input = mheight+mwidth

        index = data_array[k_input+nextindex][0]
        image_extension = data[index]['filename']
        imagepath = str(filename + image_extension)
        img = Image.open(imagepath)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(img)

        image_dict[k] = tkinter.Label(root,
                                      image=test)
        image_dict[k].image = test
        image_dict[k].grid(row=i_input, column=j_input)
        image_dict[k].config(bd = 5,bg="#0b3d91")

        nextindex=nextindex+1

    def back(i_input, j_input):
        from uploadJSON import data
        from inputWindow import mheight
        from inputWindow import mwidth
        from inputWindow import basewidth

        global basewidth
        global nextindex
        global mheight
        global mwidth

        nextindex = nextindex - 1

        k_input = mheight+mwidth

        index = data_array[k_input+nextindex][0]
        image_extension = data[index]['filename']
        imagepath = str(filename + image_extension)

        img = Image.open(imagepath)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(img)

        image_dict[k] = tkinter.Label(root,image=test)
        image_dict[k].config(bd=5, bg="#0b3d91")
        image_dict[k].image = test
        image_dict[k].grid(row=i_input,column=j_input)

    from uploadJSON import data

    for i in range(0,matrix_height,4):
        for j in range(0,matrix_width):
            index = data_array[k][0]
            image_extension =data[index]['filename']

            imagepath = str(filename+image_extension)
            img = Image.open(imagepath)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(img)

            image_dict[k] = tkinter.Label(root,
                                         image=test)
            image_dict[k].image = test
            image_dict[k].grid(row=i, column=j)
            image_dict[k].config(bd = 5,bg="#0b3d91")

            def action1(k_input = k):
                return expand(k_input)
            def action2(i_input = i,j_input = j):
                return next(i_input,j_input)
            def action3(i_input = i,j_input = j):
                return back(i_input,j_input)

            button_dict[k] = Button(root,width = 20,
                                    text = "Expand",
                                    highlightbackground='#FC3D21',
                                    command = action1)

            button_dict[k].grid(row=i+1,column=j)

            next_dict[k] = Button(root, width=20,
                                    text="Next",
                                    highlightbackground='#FC3D21',
                                    command=action2)

            next_dict[k].grid(row=i + 2, column=j)

            next_dict[k] = Button(root, width=20,
                                  text="Back",
                                  highlightbackground='#FC3D21',
                                  command=action3)

            next_dict[k].grid(row=i + 3, column=j)
            k += 1


    button_dict[k]=Button(root, width=20,
                                  text="Settings",
                                  highlightbackground='#FC3D21',
                                  command=settings)

    button_dict[k].place(relx=0.5, rely=0.0, anchor=CENTER)

    root.mainloop()