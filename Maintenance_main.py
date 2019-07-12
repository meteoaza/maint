from shutil import copyfile as cp
from datetime import datetime
from datetime import timedelta
import os

class Sens():
    def __init__(self, iram, lt, cl, wt, dur, repW, logW, tm):
        self.iram = iram
        self.cl = cl
        self.lt = lt
        self.wt = wt
        self.tm = tm
        self.dur = int(dur)
        self.repW = repW
        self.logW = logW
        self.LOGs = "0"
    def checkTime(self):
        #Check time and write time difference to dift
        now = datetime.now()
        stat = os.stat(self.f)
        t_f = datetime.fromtimestamp(stat.st_mtime)
        self.dift = now - t_f
    def ltInit(self):
        try:
            #File in DAT_SENS define
            self.f = (self.iram + r"\TEK\DAT_SENS\\" + self.lt + ".DAT")
            self.checkTime()
            #Check time of file
            if self.dift > timedelta(minutes=self.dur):
                self.lt_status = str(self.lt + ' Тревога!!! Нет данных!!!')
                self.lt_error = 1
                self.lt_val = "ERROR"
            else:
            #Чтение файла и запись данных в переменные
                with open(self.f, 'r', encoding='UTF-8', errors='ignore') as f:
                    tek_f = f.read()
                try:
                    lt_stat = tek_f.split()[6]
                    self.lt_val = tek_f.split()[4]
                    if self.lt_val != '///////':
                        self.lt_val = str(float(tek_f.split()[4]))[:-2]
                except ValueError as e:
                    lt_stat = tek_f.split()[6]
                    self.lt_val = tek_f.split()[4]
                    self.logWrite(self.lt + " ValueError " + str(e) + " " + self.lt_val)
                    pass
                lt_batt = lt_stat[2]
            #Проверка ошибок и вывод результата
                if lt_batt == '1' and lt_stat[0] == 'I' or lt_batt == '2' and lt_stat[0] == 'I':
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
        except FileNotFoundError as e:
            self.lt_status = str(self.lt + " Не найден файл с данными!!!")
            self.lt_error = 3
            self.lt_val = "ERROR"
            self.logWrite(self.lt + " FileNotFoundError " + str(e))
        except PermissionError as e:
            self.lt_status = str(self.lt + " Обработка....")
            self.lt_error = 0
            self.lt_val = "-----"
            self.logWrite(self.lt + " PermissionError " + str(e))
        except Exception as e:
            self.lt_status = str(self.lt + " Ошибка !!!")
            self.lt_error = 0
            self.lt_val = "-----"
            self.logWrite(self.lt + " Exception " + str(e) + " " + tek_f)
            pass
    def clInit(self):
        try:
            #File in DAT_SENS define
            self.f = (self.iram + r"\TEK\DAT_SENS\\" + self.cl + ".DAT")
            self.checkTime()
            if self.dift > timedelta(minutes=self.dur):
                self.cl_status = str(self.cl + ' Тревога!!! Нет данных!!!')
                self.cl_error = 1
                self.cl_val = "ERROR"
            else:
            #Чтение файла и запись данных в переменные
                with open(self.f, 'r', encoding='UTF-8', errors='ignore') as f:
                    tek_f = f.read()
                try:
                    cl_stat = tek_f.split()[7]
                    self.cl_val = tek_f.split()[4]
                    if self.cl_val != '/////':
                        self.cl_val = str(float(self.cl_val))[:-2]
                except ValueError as e:
                    cl_stat = tek_f.split()[7]
                    self.cl_val = tek_f.split()[4]
                    self.logWrite(self.cl + " ValueError " + str(e) + self.cl_val)
                    pass
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
        except FileNotFoundError as e:
            self.cl_status = str(self.cl + " Не найден файл с данными !!!")
            self.cl_error = 3
            self.cl_val = "ERROR"
            self.logWrite(self.cl + " FileNotFoundError " + str(e))
        except PermissionError as e:
            self.cl_status = str(self.cl + " Обработка....")
            self.cl_error = 0
            self.cl_val = "-----"
            self.logWrite(self.cl + " PermissionError " + str(e))
        except Exception as e:
            self.cl_status = str(self.cl + " Ошибка !!!")
            self.cl_error = 0
            self.cl_val = "-----"
            self.logWrite(self.cl + " Exception " + str(e) + " " + tek_f)
            pass
    def wtInit(self):
        try:
            #File in DAT_SENS define
            self.f = (self.iram + r"\TEK\DAT_SENS\\" + self.wt + ".DAT")
            self.checkTime()
            if self.dift > timedelta(minutes=self.dur):
                self.wt_status = str(self.wt + ' Тревога!!! Нет данных!!!')
                self.wt_error = 1
                self.wt_val = "ERROR"
            else:
            #Чтение файла и запись данных в переменные
                with open(self.f, 'r', encoding='UTF-8', errors='ignore') as f:
                    tek_f = f.read()
                try:
                    self.dd = float(tek_f.split()[3][:3])
                    self.ff = float(tek_f.split()[4])
                    self.wt_val = (str(self.dd)[:-2] + " / " + str(self.ff))
                except ValueError as e:
                    self.dd = float(tek_f.split()[4][:3])
                    self.ff = float(tek_f.split()[5])
                    self.wt_val = (str(self.dd)[:-2] + " / " + str(self.ff))
                    self.logWrite(self.wt + " ValueError " + str(e) + " " + self.wt_val)
                    pass
                wt_stat = "OK"
            #Проверка ошибок и вывод результата
                self.wt_status = (self.wt + " " + wt_stat)
                self.wt_error = 0
            if self.wt_error != 0:
                self.repWrite("", "", self.wt_status)
        except FileNotFoundError as e:
            self.wt_status = str(self.wt + " Не найден файл с данными !!!")
            self.wt_error = 3
            self.wt_val = "ERROR"
            self.logWrite(self.wt + " FileNotFoundError " + str(e))
        except PermissionError as e:
            self.wt_status = str(self.wt + " Обработка.... ")
            self.wt_error = 0
            self.wt_val = "-----"
            self.logWrite(self.wt + " PermissionError " + str(e))
        except Exception as e:
            self.wt_status = str(self.wt + " Ошибка !!!")
            self.wt_error = 0
            self.wt_val = "-----"
            self.logWrite(self.wt + " Exception " + str(e) + " " + tek_f)
            pass
    def tempInit(self):
        try:
            with open(self.iram + r"\TEK\\DAT_AVRG\\" + self.tm + ".DAT", 'r', encoding='utf-8') as f:
                self.tm_val = int(f.readline().split()[3])
                self.tm_val = float(self.tm_val/10)
        except Exception as e:
            self.tm_val = "0"
            self.logWrite(e)
            pass

    def repWrite(self, l, c, w):
        if self.repW != "0":
            try:
                if not os.path.exists('LOGs'):
                    os.mkdir('LOGs')
                t = datetime.strftime(datetime.now(), "%d-%m-%y %H:%M:%S")
                with open(r'LOGs\maintReport.txt', 'a', encoding='utf-8') as f_rep:
                    f_rep.write(t + " " + l + c + w + "\n")
            except Exception as e:
                self.LOGs = str(e)
                pass

    def logWrite(self, e):
        if self.logW != "0":
            try:
                if not os.path.exists('LOGs'):
                    os.mkdir('LOGs')
                t = datetime.strftime(datetime.now(), "%d-%m-%y %H:%M:%S")
                with open(r'LOGs\maintLog.txt', 'a', encoding='utf-8') as f_bug:
                    f_bug.write(t + " " + str(e) + "\n")
            except Exception as e:
                self.LOGs = str(e)
                pass
class Av6():

    def __init__(self, arh, av6W):
        self.arh = arh
        self.av6W = av6W
        if self.av6W != "0":
            self.arhDirDef()


    def arhDirDef(self):
        t = datetime.strftime(datetime.now(), "%d %m %Y %H%M")
        t = t.split(' ')
        self.day = ('D' + t[0])
        self.month = ('M' + t[1])
        self.year = ('G' + t[2])
        self.hour = t[3]
        self.arh_src_dir = self.arh + '\\ARX__AB6' + '\\' + self.year + '\\' + self.month + '\\' + self.day
        self.arh_dst_dir = 'AV6_ARH' + '\\' + self.year + '\\' + self.month + '\\' + self.day
        self.arhCopy()

    def mkDir(self):
        try:
            if not os.path.exists(self.arh_dst_dir):
                os.makedirs(self.arh_dst_dir)
        except Exception as e:
            Sens.logWrite(self, e)
            pass

    def arhCopy(self):
        if os.path.exists(self.arh_src_dir):
            self.mkDir()
            self.arh_src = self.arh_src_dir + '\\' + 'AB6.DAT'
            self.arh_dst = self.arh_dst_dir + '\\' + 'AB6_' + self.hour + '.DAT'
            try:
                cp(self.arh_src, self.arh_dst)
                self.av6_rep = self.hour + ' Файл АВ-6 успешно записан!'
            except Exception as e:
                Sens.logWrite(self, e)
                pass
        else: self.av6_rep = self.hour + ' Файл АВ-6 не записан!'
