from Tkinter import *
import random
""" test = like_a_boss pro kak noob inwza"""
def random_choice():
    list_t = t.get()
    listt = list_t.split(' ')
    ress = random.choice(listt)
    res = Label(root, text="here : %s" % ress).grid(row=3, column=1)
root = Tk()
t = StringVar()
root.geometry('400x200')
title_t = Label(root, text="input each choice with ' ' ").grid(row=0, column=0)
ran_choice = Entry(root, textvariable=t).grid(row=0, column=1)
random_b = Button(root, text="random", command=random_choice).grid(row=0, column=2)            
root.mainloop()
