import subprocess, sys, os
from datetime import datetime
from Maintenance_main import Sens
from pygame import mixer
from winreg import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer, Qt#, QDateTime
from Maintenance_design_osh import Ui_MainWindow
from Settings import Ui_Settings
from About import Ui_AboutFrame


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Settings = QtWidgets.QFrame()
        self.ui_s = Ui_Settings()
        self.ui_s.setupUi(self.Settings)
        self.About = QtWidgets.QFrame()
        self.ui_a = Ui_AboutFrame()
        self.ui_a.setupUi(self.About)
        #Привязка датчиков к окнам
        self.CL1 = self.ui.lineCL1
        self.CL2 = self.ui.lineCL2
        self.CL3 = self.ui.lineCL3
        self.CL4 = self.ui.lineCL4
        self.LT1 = self.ui.lineLT1
        self.LT2 = self.ui.lineLT2
        self.LT3 = self.ui.lineLT3
        self.LT4 = self.ui.lineLT4
        self.LT5 = self.ui.lineLT5
        self.LT6 = self.ui.lineLT6
        self.WT1 = self.ui.lineWT1
        self.WT2 = self.ui.lineWT2
        self.WT3 = self.ui.lineWT3
        self.WT4 = self.ui.lineWT4
        self.CL1_v = self.ui.labelCL1
        self.CL2_v = self.ui.labelCL2
        self.CL3_v = self.ui.labelCL3
        self.CL4_v = self.ui.labelCL4
        self.LT1_v = self.ui.labelLT1
        self.LT2_v = self.ui.labelLT2
        self.LT3_v = self.ui.labelLT3
        self.LT4_v = self.ui.labelLT4
        self.LT5_v = self.ui.labelLT5
        self.LT6_v = self.ui.labelLT6
        self.WT1_v = self.ui.labelWT1
        self.WT2_v = self.ui.labelWT2
        self.WT3_v = self.ui.labelWT3
        self.WT4_v = self.ui.labelWT4
        self.Temp1 = self.ui.lcdTemp1
        self.Temp2 = self.ui.lcdTemp2
        self.Pres1 = self.ui.lcdPres1
        self.Pres2 = self.ui.lcdPres2
        self.pBar = self.ui.progressBar
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
        self.dtime = self.ui.timedate
        self.bar = self.ui.statusBar
        self.term = self.ui.terminal
        self.btnCL1 = self.ui.btnCL1
        self.btnCL2 = self.ui.btnCL2
        self.btnCL3 = self.ui.btnCL3
        self.btnCL4 = self.ui.btnCL4
        self.btnLT1 = self.ui.btnLT1
        self.btnLT2 = self.ui.btnLT2
        self.btnLT3 = self.ui.btnLT3
        self.btnLT4 = self.ui.btnLT4
        self.btnLT5 = self.ui.btnLT5
        self.btnLT6 = self.ui.btnLT6
        self.btnWT1 = self.ui.btnWind1
        self.btnWT2 = self.ui.btnWind2
        self.btnWT3 = self.ui.btnWind3
        self.btnWT4 = self.ui.btnWind4
        #Привязка виджетов Settings
        self.iram_Sett = self.ui_s.lineIRAM
        self.snd_Sett = self.ui_s.lineSND
        self.FileTSett = self.ui_s.lineFileT
        self.TimerSett = self.ui_s.lineTimer
        self.sensList = self.ui_s.boxSensors
        self.sensSett = self.ui_s.lineSensors
        self.sensAdd = self.ui_s.buttSensors
        self.sensView = self.ui_s.viewSensors
        self.checkLogW = self.ui_s.checkLogW
        self.checkRepW = self.ui_s.checkRepW
        self.btnIramSett = self.ui_s.buttOK
        self.menuSett.menuAction().setStatusTip("Настройки")
        #Привязка виджетов About
        self.about = self.ui_a.about
        #Версия программы
        self.ui_a.ver.setText('Version 1.3')
        #Привязка элементов МЕНЮ
        self.menuIram.triggered.connect(self.sett)
        self.menuReport.triggered.connect(self.openRep)
        self.menuLog.triggered.connect(self.openLog)
        self.menuAbout.triggered.connect(self.About.show)
        #Привязка кнопок
        self.start.clicked.connect(self.goStart)
        self.exit.clicked.connect(self.close)
        self.term.clicked.connect(lambda: self.putty(""))
        #Активируем Shortcuts
        self.settShct = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self)
        self.settShct.activated.connect(self.sett)
        self.repShct = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+R"), self)
        self.repShct.activated.connect(self.openRep)
        self.logShct = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+L"), self)
        self.logShct.activated.connect(self.openLog)
        #Определение цвета
        self.red = "background-color: qconicalgradient(cx:1, cy:0.329773, angle:0, \
                stop:0.3125 rgba(239, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"
        self.green = "background-color: qconicalgradient(cx:1, cy:0.529, angle:0, \
                stop:0.215909 rgba(38, 174, 23, 255), stop:1 rgba(255, 255, 255, 255));"
        self.yellow = "background-color: qconicalgradient(cx:1, cy:0.329773, angle:0, \
                stop:0.363636 rgba(219, 219, 0, 255), stop:1 rgba(255, 255, 255, 255));"
        #Привязка кнопок к putty
        self.CL1.clicked.connect(lambda: self.putty("CL1"))
        self.CL2.clicked.connect(lambda: self.putty("CL2"))
        self.CL3.clicked.connect(lambda: self.putty("CL3"))
        self.CL4.clicked.connect(lambda: self.putty("CL4"))
        self.LT1.clicked.connect(lambda: self.putty("LT1"))
        self.LT2.clicked.connect(lambda: self.putty("LT2"))
        self.LT3.clicked.connect(lambda: self.putty("LT3"))
        self.LT4.clicked.connect(lambda: self.putty("LT4"))
        self.LT5.clicked.connect(lambda: self.putty("LT5"))
        self.LT6.clicked.connect(lambda: self.putty("LT6"))
        self.WT1.clicked.connect(lambda: self.putty("WT1"))
        self.WT2.clicked.connect(lambda: self.putty("WT2"))
        self.WT3.clicked.connect(lambda: self.putty("WT3"))
        self.WT4.clicked.connect(lambda: self.putty("WT4"))
        #Привязка кнопок к mute
        self.btn.clicked.connect(self.muteALL)
        self.btnCL1.clicked.connect(lambda: self.muteCL(0))
        self.btnCL1.setStyleSheet(self.green)
        self.btnCL2.clicked.connect(lambda: self.muteCL(1))
        self.btnCL2.setStyleSheet(self.green)
        self.btnCL3.clicked.connect(lambda: self.muteCL(2))
        self.btnCL3.setStyleSheet(self.green)
        self.btnCL4.clicked.connect(lambda: self.muteCL(3))
        self.btnCL4.setStyleSheet(self.green)
        self.btnLT1.clicked.connect(lambda: self.muteLT(0))
        self.btnLT1.setStyleSheet(self.green)
        self.btnLT2.clicked.connect(lambda: self.muteLT(1))
        self.btnLT2.setStyleSheet(self.green)
        self.btnLT3.clicked.connect(lambda: self.muteLT(2))
        self.btnLT3.setStyleSheet(self.green)
        self.btnLT4.clicked.connect(lambda: self.muteLT(3))
        self.btnLT4.setStyleSheet(self.green)
        self.btnLT5.clicked.connect(lambda: self.muteLT(4))
        self.btnLT5.setStyleSheet(self.green)
        self.btnLT6.clicked.connect(lambda: self.muteLT(5))
        self.btnLT6.setStyleSheet(self.green)
        self.btnWT1.clicked.connect(lambda: self.muteWT(0))
        self.btnWT1.setStyleSheet(self.green)
        self.btnWT2.clicked.connect(lambda: self.muteWT(1))
        self.btnWT2.setStyleSheet(self.green)
        self.btnWT3.clicked.connect(lambda: self.muteWT(2))
        self.btnWT3.setStyleSheet(self.green)
        self.btnWT4.clicked.connect(lambda: self.muteWT(3))
        self.btnWT4.setStyleSheet(self.green)
        #Список датчиков в настройках
        self.sensList.addItems(['None', 'CL1', 'CL2', 'CL3', 'CL4', 'LT1', 'LT2',
                                'LT3', 'LT4', 'LT5', 'LT6', 'WT1', 'WT2',
                                'WT3', 'WT4', 'WT5', 'WT6'])
        #инициализируем переменные выключения звука, прогресс бара, паузы
        self.ml = [0, 0, 0, 0, 0, 0]
        self.mc = [0, 0, 0, 0]
        self.mw = [0, 0, 0, 0]
        self.progress = 0
        self.pause = False

    def sett(self):
        self.settRead()
        self.settSensRead()
        if self.pause == False:
            self.statPause()
        self.iram_Sett.setText(self.iram)
        self.snd_Sett.setText(self.snd)
        self.FileTSett.setText(self.dur)
        self.TimerSett.setText(self.tTimer)
        self.checkRepW.setCheckState(int(self.repW))
        self.checkLogW.setCheckState(int(self.logW))
        self.Settings.show()
        self.viewSens()
        self.btnIramSett.accepted.connect(self.settWrite)
        self.btnIramSett.rejected.connect(lambda: self.Settings.hide())
        self.sensAdd.clicked.connect(self.settSens)

        #Привязка датчиков
    def settSens(self):
        text = self.sensList.currentText()
        if text == 'CL1': self.c1 = self.sensSett.text()
        elif text == 'CL2': self.c2 = self.sensSett.text()
        elif text == 'CL3': self.c3 = self.sensSett.text()
        elif text == 'CL4': self.c4 = self.sensSett.text()
        elif text == 'LT1': self.l1 = self.sensSett.text()
        elif text == 'LT2': self.l2 = self.sensSett.text()
        elif text == 'LT3': self.l3 = self.sensSett.text()
        elif text == 'LT4': self.l4 = self.sensSett.text()
        elif text == 'LT5': self.l5 = self.sensSett.text()
        elif text == 'LT6': self.l6 = self.sensSett.text()
        elif text == 'WT1': self.w1 = self.sensSett.text()
        elif text == 'WT2': self.w2 = self.sensSett.text()
        elif text == 'WT3': self.w3 = self.sensSett.text()
        elif text == 'WT4': self.w4 = self.sensSett.text()
        self.viewSens()

    def viewSens(self):
        self.sensView.setText('CL1 -  ' + self.c1 + '\n' +
                              'CL2 -  ' + self.c2 + '\n' +
                              'CL3 -  ' + self.c3 + '\n' +
                              'CL4 -  ' + self.c4 + '\n' +
                              'LT1 -  ' + self.l1 + '\n' +
                              'LT2 -  ' + self.l2 + '\n' +
                              'LT3 -  ' + self.l3 + '\n' +
                              'LT4 -  ' + self.l4 + '\n' +
                              'LT5 -  ' + self.l5 + '\n' +
                              'LT6 -  ' + self.l6 + '\n' +
                              'WT1 -  ' + self.w1 + '\n' +
                              'WT2 -  ' + self.w2 + '\n' +
                              'WT3 -  ' + self.w3 + '\n' +
                              'WT4 -  ' + self.w4 + '\n' )

    def settSensWrite(self):
        try:
            aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
            nKey = CreateKeyEx(aReg, r'Software\IRAM\MAINT\SENS', 0, KEY_ALL_ACCESS)
            keyval = SetValueEx(nKey, 'CL1', 0, REG_SZ, self.c1)
            keyval = SetValueEx(nKey, 'CL2', 0, REG_SZ, self.c2)
            keyval = SetValueEx(nKey, 'CL3', 0, REG_SZ, self.c3)
            keyval = SetValueEx(nKey, 'CL4', 0, REG_SZ, self.c4)
            keyval = SetValueEx(nKey, 'LT1', 0, REG_SZ, self.l1)
            keyval = SetValueEx(nKey, 'LT2', 0, REG_SZ, self.l2)
            keyval = SetValueEx(nKey, 'LT3', 0, REG_SZ, self.l3)
            keyval = SetValueEx(nKey, 'LT4', 0, REG_SZ, self.l4)
            keyval = SetValueEx(nKey, 'LT5', 0, REG_SZ, self.l5)
            keyval = SetValueEx(nKey, 'LT6', 0, REG_SZ, self.l6)
            keyval = SetValueEx(nKey, 'WT1', 0, REG_SZ, self.w1)
            keyval = SetValueEx(nKey, 'WT2', 0, REG_SZ, self.w2)
            keyval = SetValueEx(nKey, 'WT3', 0, REG_SZ, self.w3)
            keyval = SetValueEx(nKey, 'WT4', 0, REG_SZ, self.w4)
            aReg.Close()
        except:
            pass

    def settWrite(self):
        self.iram = self.iram_Sett.text()
        self.snd = self.snd_Sett.text()
        self.dur = self.FileTSett.text()
        self.tTimer = self.TimerSett.text()
        self.repW = str(self.checkRepW.checkState())
        self.logW = str(self.checkLogW.checkState())
        self.Settings.hide()
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        nKey = CreateKeyEx(aReg, r'Software\IRAM\MAINT\SETT', 0, KEY_ALL_ACCESS)
        keyval = SetValueEx(nKey, 'PATH', 0, REG_SZ, self.iram)
        keyval = SetValueEx(nKey, 'SOUND', 0, REG_SZ, self.snd)
        keyval = SetValueEx(nKey, 'DUR', 0, REG_SZ, self.dur)
        keyval = SetValueEx(nKey, 'REFRESH', 0, REG_SZ, self.tTimer)
        keyval = SetValueEx(nKey, 'REP', 0, REG_SZ, self.repW)
        keyval = SetValueEx(nKey, 'LOG', 0, REG_SZ, self.logW)
        aReg.Close()
        self.settSensWrite()
        self.btnIramSett.accepted.disconnect()
        self.sensAdd.clicked.disconnect()
        if self.pause == True:
            self.goSettStart()

    def settSensRead(self):
        try:
            aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
            rKey = OpenKey(aReg, r"Software\IRAM\MAINT\SENS")
            self.c1 = QueryValueEx(rKey, 'CL1')[0]
            self.c2 = QueryValueEx(rKey, 'CL2')[0]
            self.c3 = QueryValueEx(rKey, 'CL3')[0]
            self.c4 = QueryValueEx(rKey, 'CL4')[0]
            self.l1 = QueryValueEx(rKey, 'LT1')[0]
            self.l2 = QueryValueEx(rKey, 'LT2')[0]
            self.l3 = QueryValueEx(rKey, 'LT3')[0]
            self.l4 = QueryValueEx(rKey, 'LT4')[0]
            self.l5 = QueryValueEx(rKey, 'LT5')[0]
            self.l6 = QueryValueEx(rKey, 'LT6')[0]
            self.w1 = QueryValueEx(rKey, 'WT1')[0]
            self.w2 = QueryValueEx(rKey, 'WT2')[0]
            self.w3 = QueryValueEx(rKey, 'WT3')[0]
            self.w4 = QueryValueEx(rKey, 'WT4')[0]
            aReg.Close()
        except:
            self.c1 = self.c2 = self.c3 = self.c4 = 'None'
            self.l1 = self.l2 = self.l3 = self.l4 = self.l5 = self.l6 = 'None'
            self.w1 = self.w2 = self.w3 = self.w4 = 'None'
            pass

    def settRead(self):
        try:
            aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
            rKey = OpenKey(aReg, r"Software\IRAM\MAINT\SETT")
            self.iram = QueryValueEx(rKey, 'PATH')[0]
            self.snd = QueryValueEx(rKey, 'SOUND')[0]
            self.dur = QueryValueEx(rKey, 'DUR')[0]
            self.tTimer = QueryValueEx(rKey, 'REFRESH')[0]
            self.repW = QueryValueEx(rKey, 'REP')[0]
            self.logW = QueryValueEx(rKey, 'LOG')[0]
            aReg.Close()
        except (ValueError, FileNotFoundError):
            self.iram = r"d:\IRAM"
            self.snd = "sound.wav"
            self.dur = "0"
            self.tTimer = "3000"
            self.repW = "0"
            self.logW = "0"
            pass

    def goStart(self):
        self.settRead()
        self.settSensRead()
        self.goSettStart()

    def goSettStart(self):
        self.pause = False
        self.tTimer = int(self.tTimer)
        self.start.setText("Пауза")
        self.start.setStyleSheet("background-color: ")
        self.info.setStyleSheet("background-color: ")
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.statPause)
        #заводим часы
        self.dtimeTick()
        #запуск температуры и даления
        self.statTemp()
        #Запуск процесса
        self.statLT()
    def statPause(self):
        self.pause = True
        self.start.setText("Пуск")
        self.start.setStyleSheet(self.red)
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.goStart)
    def statLT(self):
        if self.pause == False:
            l1 = [self.LT1, self.LT2, self.LT3, self.LT4, self.LT5, self.LT6]
            l2 = [self.l1, self.l2, self.l3, self.l4, self.l5, self.l6]
            l3 = [self.LT1_v, self.LT2_v, self.LT3_v, self.LT4_v, self.LT5_v, self.LT6_v]
            for i in range(0, 6):
                self.LT_l = l1[i]
                self.lt = l2[i]
                self.LT_v = l3[i]
                s = Sens(self.iram, self.lt, "", "", self.dur, self.repW, self.logW)
                s.ltInit()
                self.LT_l.setText(s.lt_status)
                self.LT_v.setText(s.lt_val)
                self.info.setText("Идет процесс... LT")
                if s.lt_error == 1:
                    self.LT_l.setStyleSheet(self.red)
                    self.LT_v.setStyleSheet(self.red)
                    if self.ml[i] == 0:
                        self.sndplay()
                elif s.lt_error == 2:
                    self.LT_l.setStyleSheet(self.yellow)
                    self.LT_v.setStyleSheet(self.yellow)
                    if self.ml[i] == 0:
                        self.sndplay()
                elif s.lt_error == 3:
                    self.LT_l.setStyleSheet(self.red)
                    self.LT_v.setStyleSheet(self.red)
                else:
                    self.LT_l.setStyleSheet(self.green)
                    self.LT_v.setStyleSheet(self.green)
                    pass
                if s.LOGs == "0":
                    pass
                else:
                    self.info.setText(s.LOGs)
            QTimer().singleShot(self.tTimer, self.statCL)
        else:
            self.info.setText("Остановлено")
            self.info.setStyleSheet(self.red)
            pass
    def statCL(self):
        if self.pause == False:
            l1 = [self.CL1, self.CL2, self.CL3, self.CL4]
            l2 = [self.c1, self.c2, self.c3, self.c4]
            l3 = [self.CL1_v, self.CL2_v, self.CL3_v, self.CL4_v]
            for i  in range(0, 4):
                self.CL_l = l1[i]
                self.cl = l2[i]
                self.CL_v = l3[i]
                s = Sens(self.iram, "", self.cl, "", self.dur, self.repW, self.logW)
                s.clInit()
                self.CL_l.setText(s.cl_status)
                self.CL_v.setText(s.cl_val)
                self.info.setText("Идет процесс... CL")
                if s.cl_error == 1:
                    self.CL_l.setStyleSheet(self.red)
                    self.CL_v.setStyleSheet(self.red)
                    if self.mc[i] == 0:
                        self.sndplay()
                elif s.cl_error == 2:
                    self.CL_l.setStyleSheet(self.yellow)
                    self.CL_v.setStyleSheet(self.yellow)
                    if self.mc[i] == 0:
                        self.sndplay()
                elif s.cl_error == 3:
                    self.CL_l.setStyleSheet(self.red)
                    self.CL_v.setStyleSheet(self.red)
                else:
                    self.CL_l.setStyleSheet(self.green)
                    self.CL_v.setStyleSheet(self.green)
                    pass
                if s.LOGs == "0":
                    pass
                else:
                    self.info.setText(s.LOGs)
            QTimer().singleShot(self.tTimer, self.statWT)
        else:
            self.info.setText("Остановлено")
            self.info.setStyleSheet(self.red)
            pass
    def statWT(self):
        if self.pause == False:
            l1 = [self.WT1, self.WT2, self.WT3, self.WT4]
            l2 = [self.w1, self.w2, self.w3, self.w4]
            l3 = [self.WT1_v, self.WT2_v, self.WT3_v, self.WT4_v]
            for i in range(0, 4):
                self.WT_l = l1[i]
                self.wt = l2[i]
                self.WT_v = l3[i]
                s = Sens(self.iram, "", "", self.wt, self.dur, self.repW, self.logW)
                s.wtInit()
                self.WT_l.setText(s.wt_status)
                self.WT_v.setText(s.wt_val)
                self.info.setText("Идет процесс... WIND")
                if s.wt_error == 1:
                    self.WT_l.setStyleSheet(self.red)
                    self.WT_v.setStyleSheet(self.red)
                    if self.mw[i] == 0:
                        self.sndplay()
                elif s.wt_error == 3:
                    self.WT_l.setStyleSheet(self.red)
                    self.WT_v.setStyleSheet(self.red)
                else:
                    self.WT_l.setStyleSheet(self.green)
                    self.WT_v.setStyleSheet(self.green)
                    pass
                if s.LOGs == "0":
                    pass
                else:
                    self.info.setText(s.LOGs)
            QTimer().singleShot(self.tTimer, self.statLT)
        else:
            self.info.setText("Остановлено")
            self.info.setStyleSheet(self.red)
            pass
    def statTemp(self):
        if self.pause == False:
            s = Sens(self.iram, "", "", "", self.dur, self.repW, self.logW)
            s.tempInit()
            self.Temp1.display(s.temp1)
            self.Temp2.display(s.temp2)
            self.Pres1.display(s.pres1)
            self.Pres2.display(s.pres2)
            QTimer().singleShot(self.tTimer+5000, self.statTemp)
        else:
            self.info.setText("Остановлено")
            self.info.setStyleSheet(self.red)
    def sndplay(self):
        mixer.init()
        mixer.music.load(self.snd)
        mixer.music.play()
    def muteLT(self, m):
        b = [self.btnLT1, self.btnLT2, self.btnLT3, self.btnLT4, self.btnLT5, self.btnLT6]
        b = b[m]
        b.setStyleSheet(self.red)
        b.clicked.disconnect()
        b.clicked.connect(lambda: self.unmuteLT(m))
        self.ml[m] = 1
    def unmuteLT(self, m):
        b = [self.btnLT1, self.btnLT2, self.btnLT3, self.btnLT4, self.btnLT5, self.btnLT6]
        b = b[m]
        b.setStyleSheet(self.green)
        b.clicked.disconnect()
        b.clicked.connect(lambda: self.muteLT(m))
        self.ml[m] = 0
    def muteCL(self, m):
        b = [self.btnCL1, self.btnCL2, self.btnCL3, self.btnCL4]
        b = b[m]
        b.setStyleSheet(self.red)
        b.clicked.disconnect()
        b.clicked.connect(lambda: self.unmuteCL(m))
        self.mc[m] = 1
    def unmuteCL(self, m):
        b = [self.btnCL1, self.btnCL2, self.btnCL3, self.btnCL4]
        b = b[m]
        b.setStyleSheet(self.green)
        b.clicked.disconnect()
        b.clicked.connect(lambda: self.muteCL(m))
        self.mc[m] = 0
    def muteWT(self, m):
        b = [self.btnWT1, self.btnWT2, self.btnWT3, self.btnWT4]
        b = b[m]
        b.setStyleSheet(self.red)
        b.clicked.disconnect()
        b.clicked.connect(lambda: self.unmuteWT(m))
        self.mw[m] = 1
    def unmuteWT(self, m):
        b = [self.btnWT1, self.btnWT2, self.btnWT3, self.btnWT4]
        b = b[m]
        b.setStyleSheet(self.green)
        b.clicked.disconnect()
        b.clicked.connect(lambda: self.muteWT(m))
        self.mw[m] = 0
    def muteALL(self):
        for m in range(0, 6):
            self.muteLT(m)
        for m in range(0, 4):
            self.muteCL(m)
        for m in range(0, 4):
            self.muteWT(m)
        self.btn.clicked.disconnect()
        self.btn.clicked.connect(self.unmuteALL)
    def unmuteALL(self):
        for m in range(0, 6):
            self.unmuteLT(m)
        for m in range(0, 4):
            self.unmuteCL(m)
        for m in range(0, 4):
            self.unmuteWT(m)
        self.btn.clicked.disconnect()
        self.btn.clicked.connect(self.muteALL)
    def dtimeTick(self):
        if self.pause == False:
            t = datetime.strftime(datetime.now(), " %d-%m-%y  %H:%M:%S")
            if self.progress != 100:
                self.progress += 5
                self.pBar.setValue(self.progress)
            else:
                self.progress = 0
            if self.repW == '2' or self.repW == '1':
                repW = "Вкл"
            else:
                repW = "Откл"
            if self.logW == '2' or self.logW == '1':
                logW = "Вкл"
            else:
                logW ="Откл"
            self.bar.showMessage("Рабочий каталог:  " + self.iram +
            "          Время ожидания файла:  " + str(self.dur) + " мин."
            + "     Время обновления:  " + str(self.tTimer)[:1] + " сек."
            + "       Отчет: " + repW +
            "     Лог: " + logW)
            self.dtime.setText(t)
            QTimer().singleShot(1000, self.dtimeTick)
        else:
            self.dtime.clear()
            pass

    def putty(self, n):
        subprocess.Popen(['putty.exe', '-load', n])

    def openRep(self):
        subprocess.Popen(['notepad.exe', r'LOGs\maintReport.txt'])

    def openLog(self):
        subprocess.Popen(['notepad.exe', r'LOGs\maintLog.txt'])

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Window()
    application.show()
    sys.exit(app.exec_())
