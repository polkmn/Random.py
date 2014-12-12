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
        self.aboutMenu = Menu(self.menuBar, tearoff=0)
        self.aboutMenu.add_command(label="Developer", command=self.about_window)
        self.aboutMenu.add_command(label="EXIT", command=self.exit_window)
        self.menuBar.add_cascade(label="Help", menu=self.aboutMenu)
        main.config(menu=self.menuBar)

    def about_window(self):
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
    
    def exit_window(self):
        self.quit = exit()
        return
    
    def textfill(self, var):
        #create entry
        return Entry(start.main, textvariable = var, bg = '#FFFFFF')

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

    def call_random(self, event):
        self.random()

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


start = Start()
values = Values()
start.run()
