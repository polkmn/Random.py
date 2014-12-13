from Tkinter import *
import random
""" test = like_a_boss pro kak noob inwza"""
def random_choice():
        list_t = t.get()
        listt = list_t.split()
        ress = random.choice(listt)
        res.config(text=">>> %s" %ress)
        
def clear_text():
    ran_choice.delete(0, END)

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def quit_p():
        exit()
        return

def author():
        aut = Tk()
        aut.configure(background='black')
        first = Label(aut, text='Mr.Teerawat Teerathumrongrak', fg='white', bg='black').grid(row=2, column=0)
        second = Label(aut, text='Mr.Mongkol GodChickenV2', fg='white', bg='black').grid(row=4, column=0)
        first_num = Label(aut, text='57070057', fg='white', bg='black').grid(row=3, column=0)
        second_num = Label(aut, text='57070093', fg='white', bg='black').grid(row=5, column=0)
        Programs_name = Label(aut, text='RANDOM FUCK arai suck yang?', fg='white', bg='black').grid(row=0, column=0)
        head = Label(aut, text='Authors:',fg='white', bg='black').grid(row=1, column=0)
        return
#---------------------------------------------------------------

root = Tk() #Create Tkinter GUI
root.configure(background='black')
root.title("GGWP RANDOM")
root.geometry('400x130')

t = StringVar() #Set variable
title_t = Label(root, text="input box").grid(row=0, column=0)
ran_choice = Entry(root, textvariable=t)
ran_choice.grid(row=0, column=1)


#Button
random_b = Button(root, text="random", command=random_choice).grid(row=1, column=0)
clear_b = Button(root, text="Clear", command=clear_text).grid(row=1, column=1)
quit_r = Button(root, text="Quit", command=quit_p).grid(row=1, column=2)
#END Button
#----------------------------------------------------------------------
#Result
res = Label(root, bg='black', fg='white')
res.grid(row=1, column=1)
#END Result
#----------------------------------------------------------------------
#Menu Bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=clear_text)
filemenu.add_command(label="Close", command=quit_p)

menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to use....?", command=donothing)
helpmenu.add_command(label="Authors", command=author)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
#End Menu Bar
#----------------------------------------------------------------------
root.mainloop()
