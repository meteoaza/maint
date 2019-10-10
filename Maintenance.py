import subprocess, sys, os, time
from winreg import *
from pygame import mixer
from datetime import datetime
from datetime import timedelta
from shutil import copyfile as cp
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer, Qt
from Maintenance_design_manas import Ui_MainWindow as MainWindowManas
from Maintenance_design_osh import Ui_MainWindow as MainWindowOsh
from Settings_design import Ui_Settings
from About_design import Ui_AboutFrame


global ver
ver = '2.0'

class SettingsInit(QtWidgets.QFrame):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.stationSett = self.ui.boxStation
        self.stInd = self.ui.lineStation
        self.iram_Sett = self.ui.lineIRAM
        self.snd_Sett = self.ui.lineSND
        self.FileTSett = self.ui.lineFileT
        self.TimerSett = self.ui.lineTimer
        self.av_Sett = self.ui.lineAV6
        self.sensList = self.ui.boxSensors
        self.sensSett = self.ui.lineSensors
        self.sensAdd = self.ui.buttSensors
        self.serRun = self.ui.buttSerial
        self.sensView = self.ui.viewSensors
        self.checkSensW = self.ui.checkSensW
        self.checkLogW = self.ui.checkLogW
        self.checkRepW = self.ui.checkRepW
        self.checkAv6 = self.ui.checkAv6
        self.av_Time1 = self.ui.lineAVtime1
        self.av_Time2 = self.ui.lineAVtime2
        self.btnIramSett = self.ui.buttOK
        self.btnHelp = self.ui.buttHelp
        #Список станций в настройках
        self.stationSett.addItems([' ', 'UCFM', 'UCFO'])
        #Запускаем Чтение настроек
        self.settRead()

    def settRead(self):
        self.stationSett.activated[str].connect(self.stChange)
        self.set = {
        'STATION': 'UCFM', 'PATH': 'y:\\tek\\dat_sens\\',
        'SOUND': 'd:\\IRAM\\KRAMS_DAT\\WAV\\Srok1M.WAV',
        'DUR': '1', 'REFRESH': '3', 'AV_P': 'Y:\\', 'SENS_W': '0',
        'REP': '2', 'LOG': '0', 'AV_W': '2', 'AV_T1': '00', 'AV_T2': '30'
        }
        #Читаем настройки программы
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        try:
            rKey = OpenKey(aReg, r"Software\IRAM\MAINT\SETT")
            for k, v in self.set.items():
                v = QueryValueEx(rKey, k)[0]
                self.set[k] = v
        except (ValueError, FileNotFoundError)as e:
            Sens.logWrite(self, e)
            print(str(e))
            pass
        self.sens_list = [
        'LT1', 'LT2', 'LT3', 'LT4', 'LT5', 'LT6', 'CL1', 'CL2', 'CL3', 'CL4',
        'WT1', 'WT2', 'WT3', 'WT4', 'TEMP1', 'TEMP2', 'PRES1', 'PRES2'
        ]
        if  self.set['STATION'] == 'UCFM':
            self.sens_list.insert(14, 'WT5')
            self.sens_list.insert(15, 'WT6')
        self.sens = dict.fromkeys(self.sens_list)
        try:
            self.sensList.addItems([' ', *self.sens])
        except Exception as e:
            Sens.logWrite(self, e)
            self.set['STATION'] = '----'
        #Читаем настройки датчиков
        try:
            rKey = OpenKey(aReg, r"Software\IRAM\MAINT\SENS")
            for k, v in self.sens.items():
                v = QueryValueEx(rKey, k)[0]
                self.sens[k] = v
        except Exception as e:
            Sens.logWrite(self, e)
            pass
        #Выводим текст настроек в Settings
        self.stInd.setText(self.set['STATION'])
        self.iram_Sett.setText(self.set['PATH'])
        self.snd_Sett.setText(self.set['SOUND'])
        self.FileTSett.setText(self.set['DUR'])
        self.TimerSett.setText(self.set['REFRESH'])
        self.av_Sett.setText(self.set['AV_P'])
        self.checkSensW.setCheckState(int(self.set['SENS_W']))
        self.checkRepW.setCheckState(int(self.set['REP']))
        self.checkLogW.setCheckState(int(self.set['LOG']))
        self.checkAv6.setCheckState(int(self.set['AV_W']))
        self.av_Time1.setText(self.set['AV_T1'])
        self.av_Time2.setText(self.set['AV_T2'])
        #Привязка кнопок
        self.btnIramSett.accepted.connect(self.settWrite)
        self.btnIramSett.rejected.connect(lambda: self.close())
        self.btnHelp.clicked.connect(self.help)
        self.sensAdd.clicked.connect(self.settSens)
        self.serRun.clicked.connect(self.portInit)
        self.viewSens()
    #Привязка датчиков
    def settSens(self):
        text = self.sensList.currentText()
        for k, v in self.sens.items():
            if text == k: v = self.sensSett.text()
            self.sens[k] = v
        self.viewSens()
    #Просмотр привязки датчиков
    def viewSens(self):
        self.sensView.setText('')
        for k, v in self.sens.items():
            self.sensView.append(str(k) + '\t ---- \t '  + str(v))
    #Запись настроек в реестр
    def settWrite(self):
        #Читаем настройки программы из полей для записи в реестр
        self.set['STATION'] = self.stInd.text()
        self.set['PATH'] = self.iram_Sett.text()
        self.set['SOUND'] = self.snd_Sett.text()
        self.set['DUR'] = self.FileTSett.text()
        self.set['REFRESH'] = self.TimerSett.text()
        self.set['AV_P'] = self.av_Sett.text()
        self.set['SENS_W'] =str(self.checkSensW.checkState())
        self.set['REP'] = str(self.checkRepW.checkState())
        self.set['LOG'] = str(self.checkLogW.checkState())
        self.set['AV_W'] = str(self.checkAv6.checkState())
        self.set['AV_T1'] = self.av_Time1.text()
        self.set['AV_T2'] = self.av_Time2.text()
        #Пишем настройки программы в реестр
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        try:
            nKey = CreateKeyEx(aReg, r'Software\IRAM\MAINT\SETT', 0, KEY_ALL_ACCESS)
            for k, v in self.set.items():
                keyval = SetValueEx(nKey, k, 0, REG_SZ, v)
                self.set[k] = v
        except Exception as e:
            Sens.logWrite(self, e)
            pass
        #Пишем настройки датчиков в реестр
        try:
            aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
            nKey = CreateKeyEx(aReg, r'Software\IRAM\MAINT\SENS', 0, KEY_ALL_ACCESS)
            for k, v in self.sens.items():
                keyval = SetValueEx(nKey, k, 0, REG_SZ, v)
        except Exception as e:
            Sens.logWrite(self, e)
            pass
        except Exception as e:
            Sens.logWrite(self, e)
            pass
        aReg.Close()
        self.goWindow()
        self.stationSett.activated[str].disconnect()
        self.btnIramSett.accepted.disconnect()
        self.btnHelp.clicked.disconnect()
        self.sensAdd.clicked.disconnect()

    def stChange(self):
        self.set['STATION'] = self.stationSett.currentText()
        self.stationSett.activated[str].disconnect()
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        nKey = CreateKeyEx(aReg, r'Software\IRAM\MAINT\SETT', 0, KEY_ALL_ACCESS)
        keyval = SetValueEx(nKey, 'STATION', 0, REG_SZ, self.set['STATION'])
        aReg.Close()
        self.settRead()

    def help(self):
        self.w = QtWidgets.QMainWindow()
        if self.set['STATION'] == 'UCFM':
            self.win = MainWindowManas()
        else:
            self.win = MainWindowOsh()
        self.win.setupUi(self.w)
        self.w.show()
        self.win.exit.clicked.connect(self.w.close)

    def goWindow(self):
        self.close()
        Window().show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def portInit(self):
        subprocess.Popen(['Mserial.exe'])


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.set = SettingsInit()
        self.set.close()
        if self.set.set['STATION'] == 'UCFM':
            self.ui = MainWindowManas()
        elif self.set.set['STATION'] == 'UCFO':
            self.ui =MainWindowOsh()
        else:
            SettingsInit().show()
        try:
            self.ui.setupUi(self)
            self.show()
            self.About = QtWidgets.QFrame()
            self.ui_a = Ui_AboutFrame()
            self.ui_a.setupUi(self.About)
            #Привязка виджетов Window
            self.menuSett = self.ui.menu
            self.menuIram = self.ui.iram
            self.menuReport = self.ui.report
            self.menuLog = self.ui.log
            self.menuAbout = self.ui.about
            self.start = self.ui.start
            self.exit = self.ui.exit
            self.btn = self.ui.btn
            self.info = self.ui.lineInfo
            self.info2 = self.ui.lineInfo2
            self.dtime = self.ui.timedate
            self.bar = self.ui.statusBar
            self.term = self.ui.terminal
            self.menuSett.menuAction().setStatusTip("Настройки")
            #Привязка переменных из класса SettingsInit
            self.s = self.set.set #Prog settings
            self.sens_s = self.set.sens #Sensor settings
            self.sens_list = self.set.sens_list
            #Привязка датчиков к окнам
            self.sens_win_s = {
            'LT1': self.ui.lineLT1, 'LT2': self.ui.lineLT2, 'LT3': self.ui.lineLT3,
            'LT4': self.ui.lineLT4, 'LT5': self.ui.lineLT5, 'LT6': self.ui.lineLT6,
            'CL1': self.ui.lineCL1, 'CL2': self.ui.lineCL2, 'CL3': self.ui.lineCL3,
            'CL4': self.ui.lineCL4, 'WT1': self.ui.lineWT1, 'WT2': self.ui.lineWT2,
            'WT3': self.ui.lineWT3, 'WT4': self.ui.lineWT4
            }
            self.sens_win_v = {
            'LT1': self.ui.labelLT1, 'LT2': self.ui.labelLT2, 'LT3': self.ui.labelLT3,
            'LT4': self.ui.labelLT4, 'LT5': self.ui.labelLT5, 'LT6': self.ui.labelLT6,
            'CL1': self.ui.labelCL1, 'CL2': self.ui.labelCL2, 'CL3': self.ui.labelCL3,
            'CL4': self.ui.labelCL4,  'WT1': self.ui.labelWT1, 'WT2': self.ui.labelWT2,
            'WT3': self.ui.labelWT3, 'WT4': self.ui.labelWT4, 'TEMP1': self.ui.lcdTemp1,
            'TEMP2': self.ui.lcdTemp2, 'PRES1': self.ui.lcdPres1, 'PRES2': self.ui.lcdPres2
            }
            self.mute_but = {
            'LT1': self.ui.btnLT1, 'LT2': self.ui.btnLT2, 'LT3': self.ui.btnLT3,
            'LT4': self.ui.btnLT4, 'LT5': self.ui.btnLT5, 'LT6': self.ui.btnLT6,
            'CL1': self.ui.btnCL1, 'CL2': self.ui.btnCL2, 'CL3': self.ui.btnCL3,
            'CL4': self.ui.btnCL4, 'WT1': self.ui.btnWind1, 'WT2': self.ui.btnWind2,
            'WT3': self.ui.btnWind3, 'WT4': self.ui.btnWind4
            }
            if  self.set.set['STATION'] == 'UCFM':
                self.sens_win_s['WT5'] = self.ui.lineWT5
                self.sens_win_s['WT6'] = self.ui.lineWT6
                self.sens_win_v['WT5'] = self.ui.labelWT5
                self.sens_win_v['WT6'] = self.ui.labelWT6
                self.mute_but['WT5'] = self.ui.btnWind5
                self.mute_but['WT6'] = self.ui.btnWind6
            self.mute = dict.fromkeys(self.sens_list, 0)
            #Определение цветов
            self.red = "background-color: qconicalgradient(cx:1, cy:0.329773, \
                        angle:0, stop:0.3125 rgba(239, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"
            self.green = "background-color: qconicalgradient(cx:1, cy:0.529, angle:0,\
                        stop:0.215909 rgba(38, 174, 23, 255), stop:1 rgba(255, 255, 255, 255));"
            self.yellow = "background-color: qconicalgradient(cx:1, cy:0.329773, \
                        angle:0, stop:0.363636 rgba(219, 219, 0, 255), stop:1 rgba(255, 255, 255, 255));"
            self.blue = "background-color: qconicalgradient(cx:1, cy:0.529, angle:0,\
                        stop:0.215909 rgba(100, 200, 250, 200), stop:1 rgba(255, 255, 255, 255));"
            # Привязка кнопок к putty
            for k, v in self.sens_win_s.items():
                self.puttySett(v, k)
            # Привязка кнопок к unmute
            for k, v in self.mute_but.items():
                self.unmuteSens(v, k)
            self.btn.clicked.connect(self.muteALL)
            self.btn.setStyleSheet(self.green)
            #Привязка виджетов About
            self.about = self.ui_a.about
            #Версия программы
            self.ui_a.ver.setText('Version' + ver)
            #Привязка элементов МЕНЮ
            self.menuIram.triggered.connect(self.goSett)
            self.menuReport.triggered.connect(self.openRep)
            self.menuLog.triggered.connect(self.openLog)
            self.menuAbout.triggered.connect(self.About.show)
            #Привязка кнопок
            self.start.clicked.connect(self.goStart)
            self.exit.clicked.connect(self.close)
            self.term.clicked.connect(lambda: self.putty(""))
            #Активируем Shortcuts
            self.settShct = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self)
            self.settShct.activated.connect(self.goSett)
            self.repShct = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+R"), self)
            self.repShct.activated.connect(self.openRep)
            self.logShct = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+L"), self)
            self.logShct.activated.connect(self.openLog)
            self.pause = True
        except Exception as e:
            Sens.logWrite(self, e)
            pass

    def goStart(self):
        self.pause = False
        self.start.setText("Пауза")
        self.start.setStyleSheet("background-color: ")
        self.info.setStyleSheet("background-color: ")
        self.info2.setStyleSheet("background-color: ")
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.statPause)
        #заводим часы
        self.dtimeTick()
        #Запуск основного процесса
        self.statLT()

    def statPause(self):
        self.pause = True
        self.start.setText("Пуск")
        self.start.setStyleSheet(self.red)
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.goStart)

    def statLT(self):
        try:
            self.s_list = list()
            if self.pause == False:
                for i in self.sens_list:
                    if i[:2] == 'LT':
                        sensor = self.sens_s[i]
                        w_sta = self.sens_win_s[i]
                        w_val = self.sens_win_v[i]
                        mut = self.mute[i]
                        s = Sens(self.s['PATH'], sensor, self.s['DUR'], self.s['REP'], self.s['LOG'], mut)
                        s.ltInit()
                        w_sta.setText(s.lt_status)
                        w_val.setText(s.lt_val)
                        self.info2.setText("Идет процесс... LT" )
                        self.info2.setStyleSheet(self.blue)
                        if s.lt_error == 1:
                            w_sta.setStyleSheet(self.red)
                            w_val.setStyleSheet(self.red)
                            if mut == 0:
                                self.sndplay()
                        elif s.lt_error == 2:
                            w_sta.setStyleSheet(self.yellow)
                            w_val.setStyleSheet(self.yellow)
                            if mut == 0:
                                self.sndplay()
                        elif s.lt_error == 3:
                            w_sta.setStyleSheet(self.red)
                            w_val.setStyleSheet(self.red)
                        else:
                            w_sta.setStyleSheet(self.green)
                            w_val.setStyleSheet(self.green)
                            pass
                        self.s_list.append(s.lt_status + ' ' + s.lt_val)
                        if s.LOGs == "0":
                            pass
                        else:
                            self.info.setText(s.LOGs)
                QTimer().singleShot(int(self.s['REFRESH']), self.statCL)
            else:
                self.info2.setText("Остановлено")
                self.info2.setStyleSheet(self.red)
                pass
        except Exception as e:
            log = 'StatLT ' + sensor + str(e)
            Sens.logWrite(self, log)
            pass

    def statCL(self):
        try:
            self.s_list = list()
            if self.pause == False:
                for i in self.sens_list:
                    if i[:2] == 'CL':
                        sensor = self.sens_s[i]
                        w_sta = self.sens_win_s[i]
                        w_val = self.sens_win_v[i]
                        mut = self.mute[i]
                        s = Sens(self.s['PATH'], sensor, self.s['DUR'], self.s['REP'], self.s['LOG'], mut)
                        s.clInit()
                        w_sta.setText(s.cl_status)
                        w_val.setText(s.cl_val)
                        self.info2.setText("Идет процесс... CL ")
                        self.info2.setStyleSheet(self.blue)
                        if s.cl_error == 1:
                            w_sta.setStyleSheet(self.red)
                            w_val.setStyleSheet(self.red)
                            if mut == 0:
                                self.sndplay()
                        elif s.cl_error == 2:
                            w_sta.setStyleSheet(self.yellow)
                            w_val.setStyleSheet(self.yellow)
                            if mut == 0:
                                self.sndplay()
                        elif s.cl_error == 3:
                            w_sta.setStyleSheet(self.red)
                            w_val.setStyleSheet(self.red)
                        else:
                            w_sta.setStyleSheet(self.green)
                            w_val.setStyleSheet(self.green)
                            pass
                        self.s_list.append(s.cl_status + ' ' + s.cl_val)
                        if s.LOGs == "0":
                            pass
                        else:
                            self.info.setText(s.LOGs)
                QTimer().singleShot(int(self.s['REFRESH']), self.statWT)
            else:
                self.info2.setText("Остановлено")
                self.info2.setStyleSheet(self.red)
                pass
        except Exception as e:
            log = 'StatCL ' + sensor + str(e)
            Sens.logWrite(self, log)
            pass

    def statWT(self):
        try:
            self.s_list = list()
            if self.pause == False:
                for i in self.sens_list:
                    if i[:2] == 'WT':
                        sensor = self.sens_s[i]
                        w_sta = self.sens_win_s[i]
                        w_val = self.sens_win_v[i]
                        mut = self.mute[i]
                        s = Sens(self.s['PATH'], sensor, self.s['DUR'], self.s['REP'], self.s['LOG'], mut)
                        s.wtInit()
                        w_sta.setText(s.wt_status)
                        w_val.setText(s.wt_val)
                        self.info2.setText("Идет процесс... WIND")
                        self.info2.setStyleSheet(self.blue)
                        if s.wt_error == 1:
                            w_sta.setStyleSheet(self.red)
                            w_val.setStyleSheet(self.red)
                            if mut == 0:
                                self.sndplay()
                        elif s.wt_error == 3:
                            w_sta.setStyleSheet(self.red)
                            w_val.setStyleSheet(self.red)
                        else:
                            w_sta.setStyleSheet(self.green)
                            w_val.setStyleSheet(self.green)
                            pass
                        self.s_list.append(s.wt_status + ' ' + s.wt_val)
                        if s.LOGs == "0":
                            pass
                        else:
                            self.info.setText(s.LOGs)
                QTimer().singleShot(int(self.s['REFRESH']), self.statTemp)
            else:
                self.info2.setText("Остановлено")
                self.info2.setStyleSheet(self.red)
                pass
        except Exception as e:
            log = 'StatWT ' + sensor + str(e)
            Sens.logWrite(self, log)
            pass

    def statTemp(self):
        try:
            if self.pause == False:
                for i in self.mute:
                    if i[:2] == 'TE' or i[:2] == 'PR':
                        sensor = self.sens_s[i]
                        w_val = self.sens_win_v[i]
                        mut = 1
                        s = Sens(self.s['PATH'], sensor, self.s['DUR'], self.s['REP'], self.s['LOG'], mut)
                        s.tempInit()
                        w_val.display(s.tm_val)
                        self.info2.setText("Идет процесс... TEMP")
                        self.s_list.append(sensor + ' ' + str(s.tm_val))
                self.sensWrite(self.s_list)
                QTimer().singleShot(int(self.s['REFRESH']), self.statLT)
            else:
                self.info2.setText("Остановлено")
                self.info2.setStyleSheet(self.red)
                pass
        except Exception as e:
            log = 'StatTemp ' + sensor + str(e)
            Sens.logWrite(self, log)
            pass

    def sndplay(self):
        mixer.init()
        mixer.music.load(self.s['SOUND'])
        mixer.music.play()

    def muteSens(self, but, sen):
        self.mute[sen] = 1
        but.clicked.disconnect()
        but.clicked.connect(lambda: self.unmuteSens(but, sen))
        but.setStyleSheet(self.red)

    def unmuteSens(self, but, sen):
        self.mute[sen] = 0
        try:
            but.clicked.disconnect()
        except Exception as e:
            pass
        but.clicked.connect(lambda: self.muteSens(but, sen))
        but.setStyleSheet(self.green)

    def muteALL(self):
        for sen, but in self.mute_but.items():
            self.muteSens(but, sen)
        self.btn.disconnect()
        self.btn.clicked.connect(self.unmuteALL)
        self.btn.setStyleSheet(self.red)


    def unmuteALL(self):
        for sen, but in self.mute_but.items():
            self.unmuteSens(but, sen)
        self.btn.disconnect()
        self.btn.clicked.connect(self.muteALL)
        self.btn.setStyleSheet(self.green)

    def dtimeTick(self):
        if self.pause == False:
            t = datetime.strftime(datetime.now(), "%d-%m-%y  %H:%M:%S")
            av_time = datetime.strftime(datetime.now(), "%M%S")
            if av_time == (self.s['AV_T1'] + '00') or av_time == (self.s['AV_T2'] + '00'):
                if self.s['AV_W'] != "0":
                    path = self.s['AV_P']
                    av = Av6(path)
                    self.info.setText(av.av6_rep)
            if self.s['SENS_W'] == '2' or self.s['SENS_W'] == '1':
                sensW = "Вкл"
            else:
                sensW = "Откл"
            if self.s['REP'] == '2' or self.s['REP'] == '1':
                repW = "Вкл"
            else:
                repW = "Откл"
            # if self.s['LOG'] == '2' or self.s['LOG'] == '1':
            #     logW = "Вкл"
            # else:
            #     logW ="Откл"
            if self.s['AV_W'] == '2' or self.s['AV_W'] == '1':
                av6W = "Вкл"
                av_info = ("  ( " + self.s['AV_P'] + "      " + self.s['AV_T1'][:2]
                         + " , "  + self.s['AV_T2'][:2] + " мин )")
            else:
                av6W ="Откл"
                av_info = "              "
            self.bar.showMessage("Рабочий каталог: " + self.s['PATH']
            + "                                Время ожидания файла:  "
            + str(self.s['DUR']) + " мин." + "      Время обновления:    "
            + self.s['REFRESH'][:-3] + " сек." + "       Отчет: " + repW
            + "      Sens: " + sensW  + "               AB6:  " + av6W + av_info)
            self.dtime.setText(t)
            QTimer().singleShot(1000, self.dtimeTick)
        else:
            self.dtime.clear()
            pass

    def puttySett(self, but, sen):
        but.clicked.connect(lambda: self.putty(sen))

    def putty(self, n):
        subprocess.Popen(['putty.exe', '-load', n])

    def openRep(self):
        subprocess.Popen(['notepad.exe', r'LOGs\maintReport.txt'])

    def openLog(self):
        subprocess.Popen(['notepad.exe', r'LOGs\maintLog.txt'])

    def sensWrite(self, sens):
        if self.s['SENS_W'] != '0':
            try:
                if not os.path.exists('Sens'):
                    os.mkdir('Sens')
                with open(r'Sens\Sens.dat', 'w', encoding='utf-8') as f_sens:
                    f_sens.write(self.t + '\n')
                    for s in sens:
                        f_sens.write("%s\n" % s)
            except Exception as e:
                Sens.logWrite(self, e)
                pass

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def goSett(self):
        self.statPause()
        self.close()
        SettingsInit().show()


class Sens():

    def __init__(self, iram, sens, dur, repW, logW, mut):
        self.s = {
        'PATH': iram, 'DUR': int(dur), 'REP': repW, 'LOG': logW
        }
        self.sens = sens
        self.mut = mut
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
                self.f = (self.s['PATH'] + self.sens + ".DAT")
                #Check time of file
                self.checkTime(self.f)
                if self.dift > timedelta(minutes=self.s['DUR']):
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
                    if self.mut == 0:
                        self.repWrite(self.lt_status)
            except FileNotFoundError as e:
                self.lt_status = str(self.sens + " Не найден файл с данными!!!")
                self.lt_error = 3
                self.lt_val = "ERROR"
                # self.logWrite(self.sens + " FileNotFoundError " + str(e))
            except PermissionError as e:
                self.lt_status = str(self.sens + " Обработка....")
                self.lt_error = 0
                self.lt_val = "-----"
                # self.logWrite(self.sens + " PermissionError " + str(e))
            except Exception as e:
                self.lt_status = str(self.sens + " Ошибка !!!")
                self.lt_error = 0
                self.lt_val = "-----"
                # self.logWrite(self.sens + " Exception " + str(e))
                pass
        else:
            self.lt_status = self.lt_error = self.lt_val = ' OFF'

    def clInit(self):
        if self.sens != 'OFF':
            try:
                #File in DAT_SENS define
                self.f = (self.s['PATH'] + self.sens + ".DAT")
                #Check time of file
                self.checkTime(self.f)
                if self.dift > timedelta(minutes=self.s['DUR']):
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
                    if self.mut == 0:
                        self.repWrite(self.cl_status)
            except FileNotFoundError as e:
                self.cl_status = str(self.sens + " Не найден файл с данными !!!")
                self.cl_error = 3
                self.cl_val = "ERROR"
                # self.logWrite(self.sens + " FileNotFoundError " + str(e))
            except PermissionError as e:
                self.cl_status = str(self.sens + " Обработка....")
                self.cl_error = 0
                self.cl_val = "-----"
                # self.logWrite(self.sens + " PermissionError " + str(e))
            except Exception as e:
                self.cl_status = str(self.sens + " Ошибка !!!")
                self.cl_error = 0
                self.cl_val = "-----"
                # self.logWrite(self.sens + " Exception " + str(e))
                pass
        else:
            self.cl_status = self.cl_error = self.cl_val = 'OFF'

    def wtInit(self):
        if self.sens != "OFF":
            try:
                #File in DAT_SENS define
                self.f = (self.s['PATH'] + self.sens + ".DAT")
                #Check time of file
                self.checkTime(self.f)
                if self.dift > timedelta(minutes=self.s['DUR']):
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
                    if self.mut == 0:
                        self.repWrite(self.wt_status)
            except FileNotFoundError as e:
                self.wt_status = str(self.sens + " Не найден файл с данными !!!")
                self.wt_error = 3
                self.wt_val = "ERROR"
                # self.logWrite(self.sens + " FileNotFoundError " + str(e))
            except PermissionError as e:
                self.wt_status = str(self.sens + " Обработка.... ")
                self.wt_error = 0
                self.wt_val = "-----"
                # self.logWrite(self.sens + " PermissionError " + str(e))
            except Exception as e:
                self.wt_status = str(self.sens + " Ошибка !!!")
                self.wt_error = 0
                self.wt_val = "-----"
                # self.logWrite(self.sens + " Exception " + str(e))
                pass
        else:
            self.wt_status = self.wt_error = self.wt_val = 'OFF'

    def tempInit(self):
        if self.sens != 'OFF':
            try:
                #File in DAT_SENS define
                self.f = (self.s['PATH'] + self.sens + ".DAT")
                #Check time of file
                self.checkTime(self.f)
                if self.dift > timedelta(minutes=self.s['DUR']):
                    self.tm_val = "ERROR"
                else:
                    with open(self.f, 'r', encoding='utf-8') as f:
                        self.tm_val = f.read().split()[3]
            except Exception as e:
                self.tm_val = "ERROR"
                # self.logWrite(self.sens + " Exception" + str(e))
                pass
        else:
            self.tm_val = "OFF"

    def repWrite(self, r):
        if self.s['REP'] != "0":
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

    def __init__(self, path):
        self.arh = path
        self.arhDirDef()

    def arhDirDef(self):
        try:
            self.t = datetime.strftime(datetime.now(), "%d %m %Y %H%M")
            t = self.t.split(' ')
            self.day = ('D' + t[0])
            self.month = ('M' + t[1])
            self.year = ('G' + t[2])
            self.hour = t[3]
            self.arh_src_dir = self.arh + '\\ARX__AB6' + '\\' + self.year + '\\' + self.month + '\\' + self.day
            self.arh_dst_dir = 'AV6_ARH' + '\\' + self.year + '\\' + self.month + '\\' + self.day
            self.arhCopy()
        except Exception as e:
            Sens.logWrite(self, e)
            self.LOGs = str(e)
            pass

    def arhCopy(self):
        try:
            if os.path.exists(self.arh_src_dir):
                if not os.path.exists(self.arh_dst_dir):
                    os.makedirs(self.arh_dst_dir)
                self.arh_src = self.arh_src_dir + '\\' + 'AB6.DAT'
                self.arh_dst = self.arh_dst_dir + '\\' + 'AB6_' + self.hour + '.DAT'
                try:
                    cp(self.arh_src, self.arh_dst)
                    self.av6Rep(self.hour[:2] + ':' + self.hour[2:] + ' Файл АВ-6 успешно записан!')
                except Exception as e:
                    self.av6Rep(self.hour[:2] + ':' + self.hour[2:] + ' Файл АВ-6 не записан!')
                    Sens.logWrite(self, e)
                    pass
            else:
                self.av6Rep(self.hour[:2] + ':' + self.hour[2:] + ' Исходник АВ-6 не найден!')
        except Exception as e:
            Sens.logWrite(self, e)
            self.LOGs = str(e)
            pass

    def av6Rep(self, r):
        self.av6_rep = r
        try:
            if not os.path.exists('LOGs'):
                os.mkdir('LOGs')
            with open(r'LOGs\av6Report.txt', 'a', encoding='utf-8') as f_rep:
                f_rep.write(r + "\n")
        except Exception as e:
            Sens.logWrite(self, e)
            self.LOGs = str(e)
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Window()
    sys.exit(app.exec_())
