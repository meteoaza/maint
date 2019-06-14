from datetime import datetime
from datetime import timedelta
import os
class Sens():
    def __init__(self, iram, cl, lt, wt, dur):
        self.iram = iram
        self.cl = cl
        self.lt = lt
        self.wt = wt
        self.dur = int(dur)
    def clInit(self):
        try:
            global cl_status, cl_error, cl_val
            f_cl = (self.iram + self.cl + ".DAT")
            #Check time and write time difference to dift
            now = datetime.now()
            stat = os.stat(f_cl)
            t_cl = datetime.fromtimestamp(stat.st_mtime)
            dift = now - t_cl
            if dift > timedelta(minutes=self.dur):
                cl_status = str(self.cl + ' Тревога!!! Нет данных!!!')
                cl_error = 1
                cl_val = "ERROR"
            else:
            #Чтение файла и запись данных в переменные
                f = open(f_cl, 'r', encoding='utf-8', errors='ignore')
                tek_f = f.read()
                f.close()
                cl_stat = tek_f.split()[7]
                cl_val = tek_f.split()[4][1:]
                cl_batt = cl_stat[5::3]
                cl_norm = '0000'
            #Проверка ошибок и вывод результата
                if cl_batt == '4' and cl_stat[:4] == (cl_norm):
                    cl_status = str(self.cl + ' Внимание!!! Работа от батареи!!!')
                    cl_error = 2
                elif cl_stat[:4] == (cl_norm):
                    cl_status = str(self.cl + ' OK ' + cl_stat)
                    cl_error = 0
                else:
                    cl_status = str(self.cl + ' Внимание!!! СБОЙ!!! ' + cl_stat)
                    cl_error = 1
            if cl_error != 0:
                self.repWrite("", cl_status)
        except (FileNotFoundError, PermissionError):
            cl_status = str(self.cl + " Ошибка чтения файла !!!")
            cl_error = 3
            cl_val = "ERROR"
            pass
    def ltInit(self):
        try:
            global lt_status, lt_error, lt_val
            f_lt = (self.iram + self.lt + ".DAT")
            #Check time and write time difference to dift
            now = datetime.now()
            stat = os.stat(f_lt)
            t_lt = datetime.fromtimestamp(stat.st_mtime)
            dift = now - t_lt
            #Check time of file
            if dift > timedelta(minutes=self.dur):
                lt_status = str(self.lt + ' Тревога!!! Нет данных!!!')
                lt_error = 1
                lt_val = "ERROR"
            else:
            #Чтение файла и запись данных в переменные
                f = open(f_lt, 'r', encoding='utf-8', errors='ignore')
                tek_f = f.read()
                f.close()
                lt_stat = tek_f.split()[6]
                lt_val = tek_f.split()[4][:5]
                lt_batt = lt_stat[2]
            #Проверка ошибок и вывод результата
                if lt_batt == '1' and lt_stat[0] == '0' or lt_batt == '2' and lt_stat[0] == '0':
                    lt_status = str(self.lt + ' Внимание!!! Работа от батареи!!!')
                    lt_error = 2
                elif lt_stat[0] == 'I':
                    lt_status = str(self.lt + ' Ненормальная ситуация !!! ' + lt_stat)
                    lt_error = 1
                elif lt_stat[0] == 'W':
                    lt_status = str(self.lt + ' Предупреждение !!! ' + lt_stat)
                    lt_error = 1
                elif lt_stat[0] == 'A':
                    lt_status = str(self.lt + ' Авария  !!! ' + lt_stat)
                    lt_error = 1
                elif lt_stat[0] == 'E':
                    lt_status = str(self.lt + ' Ошибка !!! ' + lt_stat)
                    lt_error = 1
                elif lt_stat[0] == 'S':
                    lt_status = str(self.lt + ' Открыт интерфейс !!! ' + lt_stat)
                    lt_error = 1
                else:
                    lt_status = str(self.lt + ' OK ' + lt_stat)
                    lt_error = 0
            if lt_error != 0:
                self.repWrite(lt_status, "" )
        except (FileNotFoundError, PermissionError):
            lt_status = str(self.lt + " Ошибка чтения файла с данными!!!")
            lt_error = 3
            lt_val = "ERROR"
            pass
    def wtInit(self):
        try:
            global wt_status, wt_error, wt_val
            f_wt = (self.iram + self.wt + ".DAT")
            #Check time and write time difference to dift
            now = datetime.now()
            stat = os.stat(f_wt)
            t_wt = datetime.fromtimestamp(stat.st_mtime)
            dift = now - t_wt
            if dift > timedelta(minutes=self.dur):
                wt_status = str(self.wt + ' Тревога!!! Нет данных!!!')
                wt_error = 1
                wt_val = "ERROR"
            else:
            #Чтение файла и запись данных в переменные
                f = open(f_wt, 'r', encoding='utf-8', errors='ignore')
                tek_f = f.read()
                f.close()
                wt_stat = "OK"
                wt_val = tek_f.split()[3][:3] + " / " + tek_f.split()[4]
            #Проверка ошибок и вывод результата
                wt_status = (self.wt + " " + wt_stat)
                wt_error = 0
        except (FileNotFoundError, PermissionError):
            wt_status = str(self.wt + " Ошибка чтения файла с данными!!!")
            wt_error = 3
            wt_val = "ERROR"
            pass
    def repWrite(self, l, c):
        t = datetime.strftime(datetime.now(), "%d-%m-%y %H:%M:%S")
        f_rep = open('maintLog.txt', 'a', encoding='utf-8')
        f_rep.write(t + " " + l + c + "\n")
        f_rep.close()
