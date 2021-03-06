"""
PSIT PROJECT: All Random
Language: Python 2.7.8
Author: Teerawat & Mongkol
GUI: Tkinter
Version: 1.0.0 Beta
Date: 30/11/57 - 17/12/57
"""
from Tkinter import *
import tkMessageBox as Msgbox
import os
import random
import string
class Start:
    def __init__(self):
        """part of main gui"""
        self.main = Tk()
        self.main.iconbitmap('favicon.ico')
        self.main.title('All Random')
        self.main.geometry('400x400')
        self.main.resizable(width=FALSE, height=FALSE)
        self.main.configure(background = '#000000')
    def run(self):
        """Run GUI"""
        canvas = Canvas(self.main, bd = 0, bg='#000000', width=400, height=180, highlightthickness=0, relief='ridge')
        canvas.pack()
        logo = PhotoImage(file = "BGF.gif")
        canvas.create_image(170, 95, image=logo)

        mainGUI = Program(self.main)
        mainGUI.guipack()
        self.main.mainloop()

class Program:
    def __init__(self, main):
        '''part of edit gui'''
        #edit gui here
         #Label
        self.text = self.textlabel(main, 'By Teerawat And Mongkol')
        self.text2 = self.textlabel(main, 'CAUTION : Fill "," between data for divide from group of data')
         #filltext
        self.fill = self.textfill(values.filltext)
        self.fill.config(width=30, font = ('', 14))
        self.restext = self.textfill(values.res)
        self.restext.config(width=20, state='readonly', readonlybackground='#FFFFFF', font = ('', 20))
        #Button
        self.button = Button(main, text = 'RANDOM!', command = self.random)
        self.button.config(height = 1, width = 9)
        self.button_content = Button(main, text = "More Option Random", command=self.open_other)
        self.button_content.config(height = 1, width = 55)
        #MenuBar
        self.menuBar = Menu(main)
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="EXIT", command=self.exit_window)

        self.optionMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Option', menu=self.optionMenu)
        self.optionMenu.add_command(label='Number', command=self.num_random)
        self.optionMenu.add_command(label='Colors', command=self.color_random)
        self.optionMenu.add_command(label='Other random', command=self.open_other)

        self.HelpMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Help", menu=self.HelpMenu)
        self.HelpMenu.add_command(label="Developer", command=self.author_window)
        main.config(menu=self.menuBar)

    def open_other(self):
        '''open content or option window'''
        other = Other()
    
    def author_window(self):
        '''open gui author window'''
        #Author Menu Window
        def thatOk():
          about.destroy()
        about = Toplevel(start.main, bg='#000000')
        about.geometry('200x100')
        about.iconbitmap('favicon.ico')
        about.resizable(width=FALSE, height=FALSE)
        about.title("Author")
        about_message = "  Developer:\nTeerawat 57070057\nMongkol 57070093"
        msg = Message(about, text=about_message, justify=CENTER, fg='white', bg='#000000', font = ('', 10))
        msg.pack()
        button = Button(about, text="Accept", command=thatOk)
        button.place(x = 155, y = 75)

    def num_random(self):
        '''part of anything randomizations'''
        #Random_number
        self.num_ran = Toplevel(start.main, bg='#000000')
        self.num_ran.geometry('300x300')
        self.num_ran.iconbitmap('favicon.ico')
        self.num_ran.resizable(width=FALSE, height=FALSE)
        self.num_ran.title("Random Number")
        #entries
        self.fillnum1 = self.numfill(values.fillnum1)
        self.fillnum1.config(width=5, font = ('', 14))
        self.fillnum2 = self.numfill(values.fillnum2)
        self.fillnum2.config(width=5, font = ('', 14))
        self.resnum = self.numfill(values.resnum)
        self.resnum.config(width=10, state='readonly', readonlybackground='#FFFFFF', font = ('', 16))
        #label
        self.label_start = self.numlabel(self.num_ran, 'Start')
        self.label_stop = self.numlabel(self.num_ran, 'Stop')
        #button
        self.button = Button(self.num_ran, text = 'RANDOM!', command = self.rannum)
        self.button.config(height = 1, width = 9)
        #pack
        self.fillnum1.place(x=33, y=125)
        self.button.place(x=112, y=125)
        self.fillnum2.place(x=203, y=125)
        self.resnum.place(x=85, y=200)
        self.label_start.place(x=30, y=80)
        self.label_stop.place(x=200, y=80)

    def color_random(self):
        '''part of color randomization'''
        #Random color
        self.color_ran = Toplevel(start.main, bg='#000000')
        self.color_ran.iconbitmap('favicon.ico')
        self.color_ran.resizable(width=FALSE, height=FALSE)
        self.color_ran.title("Random Colors")
        #entries
        self.resc = self.colorfill(values.rescl)
        self.resc.config(width=8, state='readonly', readonlybackground='#FFFFFF', font = ('', 20))
        #button
        self.buttonc = Button(self.color_ran, text = 'RANDOM!!', command = self.rancolor)
        self.buttonc.config(width=9, height=1)
        #pack
        self.buttonc.pack()
        self.resc.pack()
        
        
    
    def exit_window(self):
        '''exit program command'''
        self.quit = exit()
        return
    
    def textfill(self, var):
        '''method for entry text'''
        #create entry
        return Entry(start.main, textvariable = var, bg = '#FFFFFF')

    def numfill(self, var):
        '''method for entry number text fill'''
        #create entry for numran
        return Entry(self.num_ran, textvariable = var, bg = '#FFFFFF')

    def colorfill(self, var):
        '''method for entry show color's already random'''
        #create entry for numran
        return Entry(self.color_ran, textvariable = var, bg = '#FFFFFF')

    def textlabel(self, main, your_text, color = '#FFFFFF'):
        '''show text on gui'''
        #Create Label
        return Label(start.main, text = your_text, bg = 'black', fg = color)

    def numlabel(self, main, your_text, color = '#FFFFFF'):
        '''show the number on gui'''
        #Create Label
        return Label(self.num_ran, text = your_text, bg = 'black', fg = color, font = ('', 20))

    def random(self):
        '''list random processing'''
        fill1 = values.filltext.get()
        if fill1 == "":
            Msgbox.showerror('Error!', 'Fill some text in entry')
        else:
            res = random.choice(fill1.split(','))
            values.res.set('%s' % res)

    def rannum(self):
        '''number random processing'''
        fill1 = values.fillnum1.get()
        fill2 = values.fillnum2.get()
        data = range(fill1, fill2 + 1)
        if fill1 == '' and fill2 == '':
            Msgbox.showerror('Error!', 'Fill number in both of two entries')
        else:
            resn = random.choice(data)
            values.resnum.set('%s' % resn)

    def rancolor(self):
        '''random color processing'''
        res = random.choice(values.lst_data)
        values.rescl.set('%s' % res)
        
    def call_rancolor(self, event):
        '''start random colors'''
        self.rancolor()

    def call_random(self, event):
        '''start random anythings'''
        self.random()

    def call_rannum(self, event):
        '''start random number'''
        self.rannum()

    def guipack(self):
        '''pack GUI'''
        #place position
        self.fill.place(x = 32, y = 190)
        self.restext.place(x = 48, y = 270)
        self.button.place(x = 160, y = 240)
        self.text.place(x = 10, y = 355)
        self.text2.place(x = 31, y = 218)
        self.button_content.place(x = 3, y = 320)

class Values:
    '''part of intialization'''
    def __init__(self):
        self.filltext = StringVar()
        self.res = StringVar()
        self.rescl = StringVar()
        self.fillnum1 = IntVar()
        self.fillnum2 = IntVar()
        self.resnum = StringVar()
        self.color = open('color.txt')
        self.data = ''
        for line in self.color:
            self.data += line
        self.lst_data = self.data.split(',')
        self.color.close()

class Other:
    #----More Option part----
    def __init__(self):
        '''content window gui'''
        root = Toplevel(start.main, bg='#000000')
        root.title('Content Random')
        root.geometry('250x105')
        root.iconbitmap('favicon.ico')
        def get_new_win(ress, defi):
            '''new window first'''
            newwin = Toplevel(root)
            if defi == 1:
                for i in ress:
                    Label(newwin, text=i).pack(fill=X)
            if defi in [2, 3]:
                Label(newwin, text=ress).pack(fill=X)
            Button(newwin,text='Again',command=lambda:again(defi)).pack(side=LEFT)
            Button(newwin,text='Quit',command=newwin.destroy).pack(side=RIGHT)
            def again(check):
                newwin.destroy()
                if check == 1:
                    random_res()
                if check == 2:
                    res_str()
                if check == 3:
                    res_az()
        #------------------------------------------------
        def ran_list():
            '''new window second'''
            """random for n item"""
            window = Toplevel(root)
            window.iconbitmap('favicon.ico')
            window.title('Ranking')
            get_in = StringVar()
            n1 = IntVar()
            Label(window, text="Insert Here (space for each)").pack(fill=X)
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
        def ran_str():
            """random password"""
            window = Toplevel(root)
            window.iconbitmap('favicon.ico')
            window.title('Random Password')
            n0 = IntVar()
            Label(window, text="Length Password").pack(fill=X)
            Entry(window, textvariable=n0).pack()
            global res_str
            def res_str():
                n = n0.get()/2
                check = n0.get()
                digits = "".join([random.choice(string.digits) for i in range(n)])
                chars = "".join([random.choice(string.ascii_letters) for i in range(n)])
                result = digits + chars
                if check % 2 != 0:
                    result += str(random.choice(string.ascii_letters))
                res = ''.join(random.sample(result, len(result)))
                get_new_win(res, 2)
            Button(window, text="Submit", command=res_str).pack(fill=X)
            Button(window, text="Quit", command=window.destroy).pack(fill=X)

        #--------------------------------------------------
        def random_a_to_z():
            '''random character A-Z'''
            window = Toplevel(root)
            window.title('Random A-Z')
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

                get_new_win(ress, 3)
     
            Button(window, text="Submit", command=res_az).pack(fill=X)
            Button(window, text="Quit", command=window.destroy).pack(fill=X)

        #--------------------------------------------------
        
        #--------------------------------------------------
            
        Button(root, text="Ranking", command=ran_list).pack(fill=X)
        Button(root, text="Random Password", command=ran_str).pack(fill=X)
        Button(root, text="Random A to Z", command=random_a_to_z).pack(fill=X)
        Button(root, text="Quit", command=root.destroy).pack(fill=X)
        
    
#---------------------------------------------------------------------------------------------------------------

start = Start()
values = Values()
start.run()
