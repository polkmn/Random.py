from Tkinter import *
import random
def random_choice():
    t = ['a', 'b', 'c', 'd']
    print(random.choice(t))
root = Tk()
title_t = Label(root, text="Get Random")
title_t.pack()
random_b = Button(root, text="random", command=random_choice)
random_b.pack()                  
root.mainloop()
