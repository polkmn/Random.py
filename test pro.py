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
    
root = Tk()
t = StringVar()
#root.geometry('400x200')
title_t = Label(root, text="input box").pack()
ran_choice = Entry(root, textvariable=t)
ran_choice.pack()
random_b = Button(root, text="random", command=random_choice).pack()
clear_b = Button(root, text="Clear", command=clear_text).pack()
res = Label(root)
res.pack()
Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()
