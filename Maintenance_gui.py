import Maintenance_main
#import time
from tkinter import *
from pygame import mixer
from datetime import datetime
from Maintenance_main import Sens

class Window:
    def __init__(self, parent):
        # Variables
        self.cl_list = ["CL311", "CL312", "CT25K1", "CT25K2"]
        self.lt_list = ["LT311", "LT312", "LT313", "LT314", "LT315", "LT316"]
        self.fontsize = 10
        self.myfont = ("Helvetica", self.fontsize, "bold")
        self.snd = "d:\IRAM\KRAMS_DAT\WAV\srok1M.wav"
        self.dur = 0
        self.c_list = 0
        self.l_list = 0
        # Text label for CL
        self.txtC = Label(bg='black', fg='lightgreen', width=40)
        self.txtC.pack(fill=BOTH, expand = True)
        # Text entry
        self.path1 = StringVar()
        self.settings = Entry(parent, font = self.myfont, textvariable = self.path1, width=20)
        self.settings.pack(fill=BOTH, expand = True)
        # Text label for LT
        self.txtL = Label(bg='darkblue', fg='lightgreen', width=40)
        self.txtL.pack(fill=BOTH, expand = True)
        # Buttons
        self.button = Button(parent, bg='red', text="EXIT", command=parent.destroy)
        self.button1 = Button(parent, bg='green', text="GO", command=self.combine_func(self.clearSettings, self.setStatCl, self.setStatLt))
        self.button2 = Button(parent, text='1min', command=self.durbut1)
        self.button3 = Button(parent, text='5min', command=self.durbut2)
        self.button4 = Button(parent, text='10min', command=self.durbut3)
        self.button5 = Button(parent, text='+', command=self.fontSizeInc)
        self.button6 = Button(parent, text='-', command=self.fontSizeDec)
        self.button.pack(side=RIGHT)
        self.button1.pack(side=LEFT)
        self.button2.pack(side=LEFT)
        self.button3.pack(side=LEFT)
        self.button4.pack(side=LEFT)
        self.button5.pack(side=RIGHT)
        self.button6.pack(side=RIGHT)
        self.txtC.configure(font = self.myfont, text = 'Input path to IRAM')
        self.txtL.configure(font = self.myfont, text = 'Choose time for file check')

    # Function combine
    def combine_func(self, *func):
        def combined_func(*args, **kwargs):
            for f in func:
                f(*args, **kwargs)
        return combined_func
    # Set settings func
    def setSettings(self):
        self.iram = self.path1.get() + '\\TEK\\DAT_SENS\\'
        self.clearSettings()
    def durbut1(self):
        self.dur = 1
        self.setSettings()
        self.settings.insert(0, '1 minute')
    def durbut2(self):
        self.dur = 5
        self.setSettings()
        self.settings.insert(0, '5 minutes')
    def durbut3(self):
        self.dur = 10
        self.setSettings()
        self.settings.insert(0, '10 minutes')
    def fontSizeInc(self):
        self.fontsize += 5
        self.myfont = ("Helvetica", self.fontsize, "bold")
        self.clearSettings()
        self.settings.insert(0, self.fontsize)
    def fontSizeDec(self):
        self.fontsize -= 5
        self.myfont = ("Helvetica", self.fontsize, "bold")
        self.clearSettings()
        self.settings.insert(0, self.fontsize)
    def clearSettings(self):
        self.settings.delete(0, END)

    # Check CL status and write to text labels
    def setStatCl(self):
        try:
                try:
                    try:
                        self.c = self.cl_list[self.c_list]
                        Sens(self.iram, self.c, "", self.snd, self.dur ).cl()
                    except FileNotFoundError:
                        Maintenance_sub.status_cl = (self.c + ' Не найден файл с данными!!!\n' )
                        log = open(self.iram + "maintenance.log", "a+")
                        log.write(str(datetime.now()) + " " + self.c + ' Не найден файл с данными!!!\n' )
                        log.close()
                        mixer.music.load(self.snd)
                        mixer.music.play(0)
                except PermissionError:
                    Maintenance_sub.status_cl = ('Ошибка чтения файла ' + self.c )
                    log = open(self.iram + "maintenance.log", "a+")
                    log.write(str(datetime.now()) + " " + self.c + ' Ошибка чтения файла\n' )
                    log.close()
                    mixer.music.load(self.snd)
                    mixer.music.play(0)
                    pass
                self.txtC.configure(font=self.myfont, text = Maintenance_sub.status_cl)
                self.txtC.after(3000, self.setIcl)
        except (FileNotFoundError, AttributeError):
            self.clearSettings()
            self.settings.configure(bg='red', font=self.myfont)
            self.settings.insert(0, 'ERROR SETTINGS')
            root.destroy
    # Rotate CL sensors numbers
    def setIcl(self):
        if self.c_list < 3:
            self.c_list += 1
            self.setStatCl()
        else:
            self.c_list = 0
            self.setStatCl()
    # Check CL status and write to text labels
    def setStatLt(self):
        try:
            try:
                try:
                    self.l = self.lt_list[self.l_list]
                    Sens(self.iram, "", self.l, self.snd, self.dur ).lt()
                except FileNotFoundError:
                    Maintenance_sub.status_lt = (self.l + ' Не найден файл с данными!!!\n' )
                    log = open(self.iram + "maintenance.log", "a+")
                    log.write(str(datetime.now()) + " " + self.l + ' Не найден файл с данными!!!\n' )
                    log.close()
                    mixer.music.load(self.snd)
                    mixer.music.play(0)
            except PermissionError:
                Maintenance_sub.status_lt = ('Ошибка чтения файла ' + self.l )
                log = open(self.iram + "maintenance.log", "a+")
                log.write(str(datetime.now()) + " " + self.l + ' Ошибка чтения файла\n' )
                log.close()
                mixer.music.load(self.snd)
                mixer.music.play(0)
                pass
            self.txtL.configure(font=self.myfont, text = Maintenance_sub.status_lt)
            self.txtL.after(3000, self.setIlt)
        except (FileNotFoundError, AttributeError):
            self.clearSettings()
            self.settings.configure(bg='red', font=self.myfont)
            self.settings.insert(0, 'ERROR SETTINGS')
            root.destroy
    # Rotate LT sensors numbers
    def setIlt(self):
        if self.l_list < 5:
            self.l_list += 1
            self.setStatLt()
        else:
            self.l_list = 0
            self.setStatLt()

root = Tk()
root.title("Maintenance")
#root.geometry("300x100")
window = Window(root)
root.mainloop()
