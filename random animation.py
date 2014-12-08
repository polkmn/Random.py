from Tkinter import *
import random
list_in = ['a', 'b', 'c', 'd', 'e']
i = 1
def pre_random(i):
    i += 3
    label.config(text=random.choice(list_in))
    test = label.after(i, pre_random, i)
    if i > 200:
        label.after_cancel(test)
    print i

root = Tk()
label = Label(root, fg="red")
label.pack()
Button(root, text='Quit', width=30, command=root.destroy).pack()
pre_random(i)
root.mainloop()
