from datetime import datetime
from datetime import timedelta
import os
class Sens():
    def __init__(self, iram, lt, cl, wt, dur, repW, logW):
        self.iram = iram
        self.cl = cl
        self.lt = lt
        self.wt = wt
        self.dur = int(dur)
        self.repW = int(repW)
        self.logW = int(logW)
        self.LOGs = "0"
        self.tempInit()
    def checkTime(self):
        #Check time and write time difference to dift
        now = datetime.now()
        stat = os.stat(self.f)
        t_f = datetime.fromtimestamp(stat.st_mtime)
        self.dift = now - t_f
    def ltInit(self):
        try:
            #File in DAT_SENS define
            self.f = (self.iram + "\\TEK\\DAT_SENS\\" + self.lt + ".DAT")
            self.checkTime()
            #Check time of file
            if self.dift > timedelta(minutes=self.dur):
                self.lt_status = str(self.lt + ' Тревога!!! Нет данных!!!')
                self.lt_error = 1
                self.lt_val = "ERROR"
            else:
            #Чтение файла и запись данных в переменные
                f = open(self.f, 'r', encoding='ANSI', errors='ignore')
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
                self.repWrite(self.lt_status, "", "" )
        except (FileNotFoundError, PermissionError, ValueError)as e:
            self.lt_status = str(self.lt + " Ошибка чтения файла с данными!!!")
            self.lt_error = 3
            self.lt_val = "ERROR"
            self.progBug(e)
            pass
    def clInit(self):
        try:
            #File in DAT_SENS define
            self.f = (self.iram + "\\TEK\\DAT_SENS\\" + self.cl + ".DAT")
            self.checkTime()
            if self.dift > timedelta(minutes=self.dur):
                self.cl_status = str(self.cl + ' Тревога!!! Нет данных!!!')
                self.cl_error = 1
                self.cl_val = "ERROR"
            else:
            #Чтение файла и запись данных в переменные
                f = open(self.f, 'r', encoding='ANSI', errors='ignore')
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
                self.repWrite("", self.cl_status, "")
        except (FileNotFoundError, PermissionError, ValueError)as e:
            self.cl_status = str(self.cl + " Ошибка чтения файла !!!")
            self.cl_error = 3
            self.cl_val = "ERROR"
            self.progBug(e)
            pass
    def wtInit(self):
        try:
            #File in DAT_SENS define
            self.f = (self.iram + "\\TEK\\DAT_SENS\\" + self.wt + ".DAT")
            self.checkTime()
            if self.dift > timedelta(minutes=self.dur):
                self.wt_status = str(self.wt + ' Тревога!!! Нет данных!!!')
                self.wt_error = 1
                self.wt_val = "ERROR"
            else:
            #Чтение файла и запись данных в переменные
                f = open(self.f, 'r', encoding='ANSI', errors='ignore')
                tek_f = f.read()
                f.close()
                wt_stat = "OK"
                self.dd = tek_f.split()[3][:3]
                self.ff = tek_f.split()[4]
                if self.ff != '\x01' or self.ff != '\x00':
                    self.dd = float(self.dd)
                    self.ff = float(self.ff)
                self.wt_val = (str(self.dd)[:-2] + " / " + str(self.ff))
            #Проверка ошибок и вывод результата
                self.wt_status = (self.wt + " " + wt_stat)
                self.wt_error = 0
            if self.wt_error != 0:
                self.repWrite("", "", self.wt_status)
        except (FileNotFoundError, PermissionError, ValueError)as e:
            self.wt_status = str(self.wt + " Ошибка чтения файла с данными!!!")
            self.wt_error = 3
            self.wt_val = "ERROR"
            print(self.dd + " " + self.ff)
            self.progBug(e)
            pass
    def tempInit(self):
        try:
            with open(self.iram + "\\TEK\\DAT_AVRG\\TTT45.DAT", 'r', encoding='ANSI') as f_t1, \
                 open(self.iram + "\\TEK\\DAT_AVRG\\TTT46.DAT", 'r', encoding='ANSI') as f_t2, \
                 open(self.iram + "\\TEK\\DAT_AVRG\\PPP41.DAT", 'r', encoding='ANSI') as f_p1, \
                 open(self.iram + "\\TEK\\DAT_AVRG\\PPP42.DAT", 'r', encoding='ANSI') as f_p2:
                self.temp1 = int(f_t1.readline().split()[3])
                self.temp1 = float(self.temp1/10)
                self.temp2 = int(f_t2.readline().split()[3])
                self.temp2 = float(self.temp2/10)
                self.pres1 = int(f_p1.readline().split()[3])
                self.pres1 = float(self.pres1/10)
                self.pres2 = int(f_p2.readline().split()[3])
                self.pres2 = float(self.pres2/10)
        except (FileNotFoundError, PermissionError, ValueError) as e:
            self.temp1 = "0"
            self.temp2 = "0"
            self.pres1 = "0"
            self.pres2 = "0"
            self.progBug(e)
            pass
    def repWrite(self, l, c, w):
        if self.repW != 0:
            try:
                t = datetime.strftime(datetime.now(), "%d-%m-%y %H:%M:%S")
                with open(r'LOGs\\maintLog.txt', 'a', encoding='utf-8') as f_rep:
                    f_rep.write(t + " " + l + c + w + "\n")
                    f_rep.close()
            except FileNotFoundError as e:
                self.LOGs = str(e)
                pass
    def progBug(self, e):
        if self.logW != 0:
            try:
                t = datetime.strftime(datetime.now(), "%d-%m-%y %H:%M:%S")
                with open(r'LOGs\\bugLog.txt', 'a', encoding='utf-8') as f_bug:
                    f_bug.write(t + " " + str(e) + "\n")
                    f_bug.close()
            except FileNotFoundError as e:
                self.LOGs = str(e)
                pass
