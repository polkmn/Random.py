from Tkinter import *
import random
""" test = like_a_boss pro kak noob inwza"""
def random_choice():
        list_t = t.get()
        listt = list_t.split()
        if listt == []:
                ress = ''
        else:
                ress = random.choice(listt)
                get_new_win(ress)

def get_new_win(ress):

        newwin = Toplevel(root)
        res = Label(newwin)
        res.config(text=">>> %s" %ress)
        res.pack()
        def quit_win():
                newwin.destroy()
        Button(newwin,text='Quit',command=quit_win).pack()
        newwin.after(5000, func=newwin.destroy)                
        
        
def clear_text():
    ran_choice.delete(0, END)
    
root = Tk()
t = StringVar()
root.geometry('400x200')
title_t = Label(root, text="input box").pack()
ran_choice = Entry(root, textvariable=t)
ran_choice.pack()
random_b = Button(root, text="random", command=random_choice).pack()
clear_b = Button(root, text="Clear", command=clear_text).pack()
Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()
