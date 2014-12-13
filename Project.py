from Tkinter import *
import tkMessageBox as Msgbox
import random
class Start:
    def __init__(self):
        self.main = Tk()
        self.main.iconbitmap('favicon.ico')
        self.main.title('All Random')
        self.main.geometry('400x400')
        self.main.resizable(width=FALSE, height=FALSE)
        self.main.configure(background = '#000000')
    def run(self):
        canvas = Canvas(self.main, bd = 0, bg='#000000', width=400, height=160, highlightthickness=0, relief='ridge')
        canvas.pack()
        logo = PhotoImage(file = "bg.gif")
        canvas.create_image(200, 80, image=logo)

        mainGUI = Program(self.main)
        mainGUI.guipack()
        self.main.mainloop()

class Program:
    def __init__(self, main):
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
        #MenuBar
        self.menuBar = Menu(main)
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="EXIT", command=self.exit_window)

        self.optionMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Option', menu=self.optionMenu)
        self.optionMenu.add_command(label='Number', command=self.num_random)
        self.optionMenu.add_command(label='Update..Soon', command='null')

        self.HelpMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Help", menu=self.HelpMenu)
        self.HelpMenu.add_command(label="Developer", command=self.author_window)
        main.config(menu=self.menuBar)

    def author_window(self):
        #Author Menu Window
        def thatOk():
          about.destroy()
        about = Toplevel(start.main, bg='#000000')
        about.geometry('200x100')
        about.resizable(width=FALSE, height=FALSE)
        about.title("Author")
        about_message = "  Developer:\nTeerawat 57070057\nMongkol 57070093"
        msg = Message(about, text=about_message, justify=CENTER, fg='white', bg='#000000', font = ('', 10))
        msg.pack()
        button = Button(about, text="Accept", command=thatOk)
        button.place(x = 155, y = 75)

    def num_random(self):
        #Random_number
        self.num_ran = Toplevel(start.main, bg='#000000')
        self.num_ran.geometry('300x300')
        self.num_ran.resizable(width=FALSE, height=FALSE)
        self.num_ran.title("Random Number")
        #entries
        self.fillnum1 = self.numfill(values.fillnum1)
        self.fillnum1.config(width=5, font = ('', 14))
        self.fillnum2 = self.numfill(values.fillnum2)
        self.fillnum2.config(width=5, font = ('', 14))
        self.resnum = self.numfill(values.resnum)
        self.resnum.config(width=10, state='readonly', readonlybackground='#FFFFFF', font = ('', 16))
        #button
        self.button = Button(self.num_ran, text = 'RANDOM!', command = self.rannum)
        self.button.config(height = 1, width = 9)
        #pack
        self.fillnum1.place(x=33, y=125)
        self.button.place(x=112, y=125)
        self.fillnum2.place(x=203, y=125)
        self.resnum.place(x=85, y=200)
        
        
    
    def exit_window(self):
        self.quit = exit()
        return
    
    def textfill(self, var):
        #create entry
        return Entry(start.main, textvariable = var, bg = '#FFFFFF')

    def numfill(self, var):
        #create entry for numran
        return Entry(self.num_ran, textvariable = var, bg = '#FFFFFF')

    def textlabel(self, main, your_text, color = '#FFFFFF'):
        #Create Label
        return Label(start.main, text = your_text, bg = 'black', fg = color)

    def random(self):
        fill1 = values.filltext.get()
        if fill1 == "":
            Msgbox.showerror('Error!', 'Fill some text in entry')
        else:
            res = random.choice(fill1.split(','))
            values.res.set('%s' % res)

    def rannum(self):
        fill1 = values.fillnum1.get()
        fill2 = values.fillnum2.get()
        data = range(fill1, fill2 + 1)
        if fill1 == '' and fill2 == '':
            Msgbox.showerror('Error!', 'Fill number in both of two entries')
        else:
            resn = random.choice(data)
            values.resnum.set('%s' % resn)
        

    def call_random(self, event):
        self.random()

    def call_rannum(self, event):
        self.rannum()

    def guipack(self):
        #place position
        self.fill.place(x = 32, y = 190)
        self.restext.place(x = 50, y = 290)
        self.button.place(x = 160, y = 240)
        self.text.place(x = 10, y = 355)
        self.text2.place(x = 31, y = 218)

class Values:
        def __init__(self):
            self.filltext = StringVar()
            self.res = StringVar()
            self.fillnum1 = IntVar()
            self.fillnum2 = IntVar()
            self.resnum = StringVar()
            


start = Start()
values = Values()
start.run()
