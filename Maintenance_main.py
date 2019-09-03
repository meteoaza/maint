from shutil import copyfile as cp
from datetime import datetime
from datetime import timedelta
import os

class Sens():

    def __init__(self, iram, sens, dur, repW, logW):
        self.iram = iram
        self.sens = sens
        self.dur = int(dur)
        self.repW = repW
        self.logW = logW
        self.LOGs = "0"

    def checkTime(self, f):
        #Check time and write time difference to dift
        now = datetime.now()
        stat = os.stat(f)
        t_f = datetime.fromtimestamp(stat.st_mtime)
        self.dift = now - t_f

    def ltInit(self):
        if self.sens != 'OFF':
            try:
                #File in DAT_SENS define
                self.f = (self.iram + r"\TEK\DAT_SENS\\" + self.sens + ".DAT")
                #Check time of file
                self.checkTime(self.f)
                if self.dift > timedelta(minutes=self.dur):
                    self.lt_status = str(self.sens + ' Тревога!!! Нет данных!!!')
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
                        self.logWrite(self.sens + " ValueError " + str(e) + " " + self.lt_val)
                        pass
                    lt_batt = lt_stat[2]
                #Проверка ошибок и вывод результата
                    if lt_batt == '1' and lt_stat[0] == 'I' or lt_batt == '2' and lt_stat[0] == 'I':
                        self.lt_status = str(self.sens + ' Внимание!!! Работа от батареи!!!')
                        self.lt_error = 2
                    elif lt_stat[0] == 'I':
                        self.lt_status = str(self.sens + ' Ненормальная ситуация !!! ' + lt_stat)
                        self.lt_error = 1
                    elif lt_stat[0] == 'W':
                        self.lt_status = str(self.sens + ' Предупреждение !!! ' + lt_stat)
                        self.lt_error = 1
                    elif lt_stat[0] == 'A':
                        self.lt_status = str(self.sens + ' Авария  !!! ' + lt_stat)
                        self.lt_error = 1
                    elif lt_stat[0] == 'E':
                        self.lt_status = str(self.sens + ' Ошибка !!! ' + lt_stat)
                        self.lt_error = 1
                    elif lt_stat[0] == 'S':
                        self.lt_status = str(self.sens + ' Открыт интерфейс !!! ' + lt_stat)
                        self.lt_error = 1
                    else:
                        self.lt_status = str(self.sens + ' OK ' + lt_stat)
                        self.lt_error = 0
                if self.lt_error != 0:
                    self.repWrite(self.lt_status)
            except FileNotFoundError as e:
                self.lt_status = str(self.sens + " Не найден файл с данными!!!")
                self.lt_error = 3
                self.lt_val = "ERROR"
                self.logWrite(self.sens + " FileNotFoundError " + str(e))
            except PermissionError as e:
                self.lt_status = str(self.sens + " Обработка....")
                self.lt_error = 0
                self.lt_val = "-----"
                self.logWrite(self.sens + " PermissionError " + str(e))
            except Exception as e:
                self.lt_status = str(self.sens + " Ошибка !!!")
                self.lt_error = 0
                self.lt_val = "-----"
                self.logWrite(self.sens + " Exception " + str(e))
                pass
        else:
            self.lt_status = self.lt_error = self.lt_val = ' OFF'

    def clInit(self):
        if self.sens != 'OFF':
            try:
                #File in DAT_SENS define
                self.f = (self.iram + r"\TEK\DAT_SENS\\" + self.sens + ".DAT")
                #Check time of file
                self.checkTime(self.f)
                if self.dift > timedelta(minutes=self.dur):
                    self.cl_status = str(self.sens + ' Тревога!!! Нет данных!!!')
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
                        self.logWrite(self.sens + " ValueError " + str(e) + self.cl_val)
                        pass
                    cl_batt = cl_stat[5::3]
                    cl_norm = '0000'
                #Проверка ошибок и вывод результата
                    if cl_batt == '4' and cl_stat[:4] == (cl_norm):
                        self.cl_status = str(self.sens + ' Внимание!!! Работа от батареи!!!')
                        self.cl_error = 2
                    elif cl_stat[:4] == (cl_norm):
                        self.cl_status = str(self.sens + ' OK ' + cl_stat)
                        self.cl_error = 0
                    else:
                        self.cl_status = str(self.sens + ' Внимание!!! СБОЙ!!! ' + cl_stat)
                        self.cl_error = 1
                if self.cl_error != 0:
                    self.repWrite(self.cl_status)
            except FileNotFoundError as e:
                self.cl_status = str(self.sens + " Не найден файл с данными !!!")
                self.cl_error = 3
                self.cl_val = "ERROR"
                self.logWrite(self.sens + " FileNotFoundError " + str(e))
            except PermissionError as e:
                self.cl_status = str(self.sens + " Обработка....")
                self.cl_error = 0
                self.cl_val = "-----"
                self.logWrite(self.sens + " PermissionError " + str(e))
            except Exception as e:
                self.cl_status = str(self.sens + " Ошибка !!!")
                self.cl_error = 0
                self.cl_val = "-----"
                self.logWrite(self.sens + " Exception " + str(e))
                pass
        else:
            self.cl_status = self.cl_error = self.cl_val = 'OFF'

    def wtInit(self):
        if self.sens != "OFF":
            try:
                #File in DAT_SENS define
                self.f = (self.iram + r"\TEK\DAT_SENS\\" + self.sens + ".DAT")
                #Check time of file
                self.checkTime(self.f)
                if self.dift > timedelta(minutes=self.dur):
                    self.wt_status = str(self.sens + ' Тревога!!! Нет данных!!!')
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
                        self.logWrite(self.sens + " ValueError " + str(e) + " " + self.wt_val)
                        pass
                    wt_stat = "OK"
                #Проверка ошибок и вывод результата
                    self.wt_status = (self.sens + " " + wt_stat)
                    self.wt_error = 0
                if self.wt_error != 0:
                    self.repWrite(self.wt_status)
            except FileNotFoundError as e:
                self.wt_status = str(self.sens + " Не найден файл с данными !!!")
                self.wt_error = 3
                self.wt_val = "ERROR"
                self.logWrite(self.sens + " FileNotFoundError " + str(e))
            except PermissionError as e:
                self.wt_status = str(self.sens + " Обработка.... ")
                self.wt_error = 0
                self.wt_val = "-----"
                self.logWrite(self.sens + " PermissionError " + str(e))
            except Exception as e:
                self.wt_status = str(self.sens + " Ошибка !!!")
                self.wt_error = 0
                self.wt_val = "-----"
                self.logWrite(self.sens + " Exception " + str(e))
                pass
        else:
            self.wt_status = self.wt_error = self.wt_val = 'OFF'

    def tempInit(self):
        if self.sens != 'OFF':
            try:
                with open(self.iram + r"\TEK\DAT_AVRG\\" + self.sens + ".DAT", 'r', encoding='utf-8') as f:
                    self.tm_val = int(f.readline().split()[3])
                    self.tm_val = float(self.tm_val/10)
            except Exception as e:
                self.tm_val = "0"
                self.logWrite(self.sens + " Exception" + str(e))
                pass
        else:
            self.tm_val = 'OFF'

    def repWrite(self, r):
        if self.repW != "0":
            try:
                if not os.path.exists('LOGs'):
                    os.mkdir('LOGs')
                t = datetime.strftime(datetime.now(), "%d-%m-%y %H:%M:%S")
                with open(r'LOGs\maintReport.txt', 'a', encoding='utf-8') as f_rep:
                    f_rep.write(t + " " + r + "\n")
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

    def __init__(self, arh_path, av6W):
        self.arh = arh_path
        self.av6W = av6W
        if self.av6W != "0":
            self.repW = self.logW = self.av6W
            self.arhDirDef()

    def arhDirDef(self):
        self.t = datetime.strftime(datetime.now(), "%d %m %Y %H%M")
        t = self.t.split(' ')
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
                self.av6_rep = self.hour[:2] + ':' + self.hour[2:] + ' Файл АВ-6 успешно записан!'
                Sens.repWrite(self, " Файл АВ-6 успешно записан!")
            except Exception as e:
                self.av6_rep = self.hour[:2] + ':' + self.hour[2:] + ' Файл АВ-6 не записан!'
                Sens.logWrite(self, e)
                pass
        else:
            self.av6_rep = self.hour[:2] + ':' + self.hour[2:] + ' Файл АВ-6 не записан!'
            Sens.repWrite(self, " Файл АВ-6 не записан!")
