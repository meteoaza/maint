from datetime import datetime
from datetime import timedelta
import os
class Sens():
    def __init__(self, iram, lt, cl, wt, dur):
        self.iram = iram
        self.cl = cl
        self.lt = lt
        self.wt = wt
        self.dur = int(dur)
    def checkTime(self):
        #Check time and write time difference to dift
        now = datetime.now()
        stat = os.stat(self.f)
        t_f = datetime.fromtimestamp(stat.st_mtime)
        self.dift = now - t_f
    def ltInit(self):
        try:
            #File in DAT_SENS define
            self.f = (self.iram + self.lt + ".DAT")
            self.checkTime()
            #Check time of file
            if self.dift > timedelta(minutes=self.dur):
                self.lt_status = str(self.lt + ' Тревога!!! Нет данных!!!')
                self.lt_error = 1
                self.lt_val = "ERROR"
            else:
            #Чтение файла и запись данных в переменные
                f = open(self.f, 'r', encoding='utf-8', errors='ignore')
                tek_f = f.read()
                f.close()
                lt_stat = tek_f.split()[6]
                self.lt_val = str(float(tek_f.split()[4][:5]))[:-2]
                lt_batt = lt_stat[2]
            #Проверка ошибок и вывод результата
                if lt_batt == '1' and lt_stat[0] == '0' or lt_batt == '2' and lt_stat[0] == '0':
                    self.lt_status = str(self.lt + ' Внимание!!! Работа от батареи!!!')
                    self.lt_error = 2
                elif lt_stat[0] == 'I':
                    self.lt_status = str(self.lt + ' Ненормальная ситуация !!! ' + lt_stat)
                    self.lt_error = 1
                elif lt_stat[0] == 'W':
                    self.lt_status = str(self.lt + ' Предупреждение !!! ' + lt_stat)
                    self.lt_error = 1
                elif lt_stat[0] == 'A':
                    self.lt_status = str(self.lt + ' Авария  !!! ' + lt_stat)
                    self.lt_error = 1
                elif lt_stat[0] == 'E':
                    self.lt_status = str(self.lt + ' Ошибка !!! ' + lt_stat)
                    self.lt_error = 1
                elif lt_stat[0] == 'S':
                    self.lt_status = str(self.lt + ' Открыт интерфейс !!! ' + lt_stat)
                    self.lt_error = 1
                else:
                    self.lt_status = str(self.lt + ' OK ' + lt_stat)
                    self.lt_error = 0
            if self.lt_error != 0:
                self.repWrite(self.lt_status, "" )
        except (FileNotFoundError, PermissionError):
            self.lt_status = str(self.lt + " Ошибка чтения файла с данными!!!")
            self.lt_error = 3
            self.lt_val = "ERROR"
            pass
    def clInit(self):
        try:
            #File in DAT_SENS define
            self.f = (self.iram + self.cl + ".DAT")
            self.checkTime()
            if self.dift > timedelta(minutes=self.dur):
                self.cl_status = str(self.cl + ' Тревога!!! Нет данных!!!')
                self.cl_error = 1
                self.cl_val = "ERROR"
            else:
            #Чтение файла и запись данных в переменные
                f = open(self.f, 'r', encoding='utf-8', errors='ignore')
                tek_f = f.read()
                f.close()
                cl_stat = tek_f.split()[7]
                self.cl_val = tek_f.split()[4]
                if self.cl_val != '/////':
                    self.cl_val = str(float(self.cl_val))[:-2]
                cl_batt = cl_stat[5::3]
                cl_norm = '0000'
            #Проверка ошибок и вывод результата
                if cl_batt == '4' and cl_stat[:4] == (cl_norm):
                    self.cl_status = str(self.cl + ' Внимание!!! Работа от батареи!!!')
                    self.cl_error = 2
                elif cl_stat[:4] == (cl_norm):
                    self.cl_status = str(self.cl + ' OK ' + cl_stat)
                    self.cl_error = 0
                else:
                    self.cl_status = str(self.cl + ' Внимание!!! СБОЙ!!! ' + cl_stat)
                    self.cl_error = 1
            if self.cl_error != 0:
                self.repWrite("", self.cl_status)
        except (FileNotFoundError, PermissionError):
            self.cl_status = str(self.cl + " Ошибка чтения файла !!!")
            self.cl_error = 3
            self.cl_val = "ERROR"
            pass
    def wtInit(self):
        try:
            #File in DAT_SENS define
            self.f = (self.iram + self.wt + ".DAT")
            self.checkTime()
            if self.dift > timedelta(minutes=self.dur):
                self.wt_status = str(self.wt + ' Тревога!!! Нет данных!!!')
                self.wt_error = 1
                self.wt_val = "ERROR"
            else:
            #Чтение файла и запись данных в переменные
                f = open(self.f, 'r', encoding='utf-8', errors='ignore')
                tek_f = f.read()
                f.close()
                wt_stat = "OK"
                dd = str(float(tek_f.split()[3][:3]))[:-2]
                ff = str(float(tek_f.split()[4]))
                self.wt_val = (dd + " / " + ff)
            #Проверка ошибок и вывод результата
                self.wt_status = (self.wt + " " + wt_stat)
                self.wt_error = 0
        except (FileNotFoundError, PermissionError):
            self.wt_status = str(self.wt + " Ошибка чтения файла с данными!!!")
            self.wt_error = 3
            self.wt_val = "ERROR"
            pass
    def repWrite(self, l, c):
        t = datetime.strftime(datetime.now(), "%d-%m-%y %H:%M:%S")
        f_rep = open('maintLog.txt', 'a', encoding='utf-8')
        f_rep.write(t + " " + l + c + "\n")
        f_rep.close()

#s = Sens('d:\iram\TEK\DAT_SENS\\', 'LT311', 'CL311', 'WIND29', '1')
#s.clInit()
#print(s.cl_status + ' ' + s.cl_val)
#s.ltInit()
#print(s.lt_status + ' ' + s.lt_val)
