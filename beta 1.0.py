from Tkinter import *
import random
import string
root = Tk()
def get_new_win(ress, defi):
    newwin = Toplevel(root)
    if defi == 1:
        for i in ress:
            Label(newwin, text=i).pack(fill=X)
    if defi in [2, 3, 4, 5]:
        Label(newwin, text=ress).pack(fill=X)

    Button(newwin,text='Again',command=lambda:again(defi)).pack(side=LEFT)
    Button(newwin,text='Quit',command=newwin.destroy).pack(side=RIGHT)
    def again(check):
        newwin.destroy()
        if check == 1:
            random_res()
        if check == 2:
            res_min_max()
        if check == 3:
            res_str()
        if check == 4:
            res_choice()
        if check == 5:
            res_az()
#------------------------------------------------
def ran_list():
    """random for n item"""
    window = Toplevel(root)
    get_in = StringVar()
    n1 = IntVar()
    Label(window, text="Insert Here (space for each").pack(fill=X)
    Entry(window, textvariable=get_in).pack()
    Label(window, text="Insert Ranking Number").pack(fill=X)
    Entry(window, textvariable=n1).pack()
    global random_res
    def random_res():
        get_input = get_in.get()
        req = str(get_input).split()
        n = n1.get()
        res = []
        for i in range(1, n+1):
            res.append(str(i)+':' + req[random.randint(0, len(req)-1)])
        get_new_win(res, 1)
    
    Button(window, text="Submit", command=random_res).pack(fill=X)
    Button(window, text="Quit", command=window.destroy).pack(fill=X)
#-------------------------------------------------
def ran_min_max():
    """random number min to max"""
    window = Toplevel(root)
    get1 = IntVar()
    get2 = IntVar()
    Label(window, text="Min").pack(fill=X)
    Entry(window, textvariable=get1).pack()
    Label(window, text="Max").pack(fill=X)
    Entry(window, textvariable=get2).pack()
    global res_min_max 
    def res_min_max():
        minn = get1.get()
        maxx = get2.get()
        get_new_win(random.randint(minn, maxx), 2)
    Button(window, text="Submit", command=res_min_max).pack(fill=X)
    Button(window, text="Quit", command=window.destroy).pack(fill=X)
#-------------------------------------------------
def ran_str():
    """random password"""
    window = Toplevel(root)
    n0 = IntVar()
    Label(window, text="Length Password").pack(fill=X)
    Entry(window, textvariable=n0).pack()
    global res_str
    def res_str():
        n = n0.get()/2
        digits = "".join([random.choice(string.digits) for i in range(n)])
        chars = "".join([random.choice(string.ascii_letters) for i in range(n)])
        result = digits + chars
        if len(result) != (n*2)+1:
            result += str(random.choice(string.ascii_letters))
        res = ''.join(random.sample(result, len(result)))
        get_new_win(res, 3)
    Button(window, text="Submit", command=res_str).pack(fill=X)
    Button(window, text="Quit", command=window.destroy).pack(fill=X)
#--------------------------------------------------
def random_choice():
    """ random simply """
    window = Toplevel(root)
    get_in = StringVar()
    Label(window, text="Insert Here (space for each").pack(fill=X)
    Entry(window, textvariable=get_in).pack()
    global res_choice
    def res_choice():
        list_t = get_in.get()
        listt = list_t.split()
        ress = random.choice(listt)
        get_new_win(ress, 4)
    Button(window, text="Submit", command=res_choice).pack(fill=X)
    Button(window, text="Quit", command=window.destroy).pack(fill=X)
#--------------------------------------------------
def random_a_to_z():
    window = Toplevel(root)
    upp = IntVar()
    low = IntVar()
    Checkbutton(window, text="Uppercase", variable=upp).pack(fill=X)
    Checkbutton(window, text="Lowercase", variable=low).pack(fill=X)
    global res_az
    def res_az():
        check = upp.get()
        check2 = low.get()
        if check == 1:
            ress = random.choice(string.ascii_uppercase)
        if check + check2 == 2:
            ress = random.choice(string.ascii_letters)
        else:
            ress = random.choice(string.ascii_lowercase)
        get_new_win(ress, 5)
     
    Button(window, text="Submit", command=res_az).pack(fill=X)
    Button(window, text="Quit", command=window.destroy).pack(fill=X)
#--------------------------------------------------

#--------------------------------------------------
    
Button(root, text="Ranking", command=ran_list).pack(fill=X)
Button(root, text="Random Number", command=ran_min_max).pack(fill=X)
Button(root, text="Random string", command=ran_str).pack(fill=X)
Button(root, text="Random from ur list", command=random_choice).pack(fill=X)
Button(root, text="Random A to Z", command=random_a_to_z).pack(fill=X)
Button(root, text="Quit", command=root.destroy).pack(fill=X)
root.mainloop()
