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
        if check == 0:
            ress = random.choice(string.ascii_lowercase)
        if check + check2 == 2:
            ress = random.choice(string.ascii_letters)

        get_new_win(ress, 5)
     
    Button(window, text="Submit", command=res_az).pack(fill=X)
    Button(window, text="Quit", command=window.destroy).pack(fill=X)
