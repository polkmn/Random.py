from Tkinter import *
import random
""" test = like_a_boss pro kak noob inwza"""
def random_choice():
    list_t = t.get()
    listt = list_t.split(' ')
    ress = random.choice(listt)
    res = Label(root, text="here : %s" % ress)
    res.pack()
root = Tk()
t = StringVar()
root.geometry('400x200')
title_t = Label(root, text="input each choice with ' ' ")
title_t.pack()
ran_choice = Entry(root, textvariable=t)
ran_choice.pack()
random_b = Button(root, text="random", command=random_choice)
random_b.pack()                  
root.mainloop()
