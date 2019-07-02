import subprocess
from datetime import datetime
from Maintenance_main import Sens
from pygame import mixer
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer, Qt
from Maintenance_design_manas import Ui_MainWindow
from Settings import Ui_Settings
from About import Ui_AboutFrame
import sys, os

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
        self.WT5 = self.ui.lineWT5
        self.WT6 = self.ui.lineWT6
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
        self.WT5_v = self.ui.labelWT5
        self.WT6_v = self.ui.labelWT6
        self.Temp1 = self.ui.lcdTemp1
        self.Temp2 = self.ui.lcdTemp2
        self.Pres1 = self.ui.lcdPres1
        self.Pres2 = self.ui.lcdPres2
        self.pBar = self.ui.progressBar
        #Привязка виджетов Window
        self.menuSett = self.ui.menu
        self.menuIram = self.ui.iram
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
        self.btnWT5 = self.ui.btnWind5
        self.btnWT6 = self.ui.btnWind6
        #Привязка виджетов Settings
        self.iram_Sett = self.ui_s.lineIRAM
        self.snd_Sett = self.ui_s.lineSND
        self.FileTSett = self.ui_s.lineFileT
        self.TimerSett = self.ui_s.lineTimer
        self.btnIramSett = self.ui_s.buttonOK
        self.logWrite = self.ui_s.logWrite
        self.repWrite = self.ui_s.repWrite
        self.menuSett.menuAction().setStatusTip("Настройки")
        #Привязка виджетов About
        self.about = self.ui_a.about
        self.ver = self.ui_a.ver
        #Привязка кнопок
        self.start.clicked.connect(self.goStart)
        self.exit.clicked.connect(self.close)
        self.term.clicked.connect(lambda: self.putty(""))
        self.menuIram.triggered.connect(self.sett)
        self.menuAbout.triggered.connect(self.About.show)
        #Определение цвета
        self.red = "background-color: qconicalgradient(cx:1, cy:0.329773, \
                    angle:0, stop:0.3125 rgba(239, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"
        self.green = "background-color: qconicalgradient(cx:1, cy:0.529, angle:0,\
                    stop:0.215909 rgba(38, 174, 23, 255), stop:1 rgba(255, 255, 255, 255));"
        self.yellow = "background-color: qconicalgradient(cx:1, cy:0.329773, \
                    angle:0, stop:0.363636 rgba(219, 219, 0, 255), stop:1 rgba(255, 255, 255, 255));"
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
        self.WT5.clicked.connect(lambda: self.putty("WT5"))
        self.WT6.clicked.connect(lambda: self.putty("WT6"))
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
        self.btnWT5.clicked.connect(lambda: self.muteWT(4))
        self.btnWT5.setStyleSheet(self.green)
        self.btnWT6.clicked.connect(lambda: self.muteWT(5))
        self.btnWT6.setStyleSheet(self.green)
        #Привязка датчиков
        try:
            with open('sensconf.ini', 'r', encoding = 'utf-8') as f_sens:
                f_sens.readline().strip()
                if (not f_sens):
                    self.info.setText('Ошибка привязки датчиков')
                else:
                    self.c1 = f_sens.readline().strip()[4:]
                    self.c2 = f_sens.readline().strip()[4:]
                    self.c3 = f_sens.readline().strip()[4:]
                    self.c4 = f_sens.readline().strip()[4:]
                    self.l1 = f_sens.readline().strip()[4:]
                    self.l2 = f_sens.readline().strip()[4:]
                    self.l3 = f_sens.readline().strip()[4:]
                    self.l4 = f_sens.readline().strip()[4:]
                    self.l5 = f_sens.readline().strip()[4:]
                    self.l6 = f_sens.readline().strip()[4:]
                    self.w1 = f_sens.readline().strip()[4:]
                    self.w2 = f_sens.readline().strip()[4:]
                    self.w3 = f_sens.readline().strip()[4:]
                    self.w4 = f_sens.readline().strip()[4:]
                    self.w5 = f_sens.readline().strip()[4:]
                    self.w6 = f_sens.readline().strip()[4:]
        except FileNotFoundError:
            self.info.setText('Не найден файл привязки датчиков')
            QTimer().singleShot(3000, self.close)
        #инициализируем переменные выключения звука, прогресс бара, паузы
        self.ml = [0, 0, 0, 0, 0, 0]
        self.mc = [0, 0, 0, 0]
        self.mw = [0, 0, 0, 0, 0, 0]
        self.progress = 0
        self.pause = False
        #Версия программы
        self.ver.setText('Version 1.0')
    def sett(self):
        if self.pause == False:
            self.statPause()
        self.settRead()
        self.iram_Sett.setText(self.iram)
        self.snd_Sett.setText(self.snd)
        self.FileTSett.setText(self.dur)
        self.TimerSett.setText(str(self.tTimer))
        self.repWrite.setCheckState(int(self.repW))
        self.logWrite.setCheckState(int(self.logW))
        self.Settings.show()
        self.btnIramSett.accepted.connect(self.settWrite)
        self.btnIramSett.rejected.connect(lambda: self.Settings.hide())
    def settRead(self):
        try:
            with open('config.ini', 'r', encoding = 'utf-8') as f_conf:
                self.iram = f_conf.readline().strip()
                self.snd = f_conf.readline().strip()
                self.dur = f_conf.readline().strip()
                self.tTimer = int(f_conf.readline().strip())
                self.repW = int(f_conf.readline().strip())
                self.logW = int(f_conf.readline().strip())
        except (ValueError, FileNotFoundError):
            self.iram = "d:\\IRAM"
            self.snd = "sound.wav"
            self.dur = "0"
            self.tTimer = 3000
            self.repW = "0"
            self.logW = "0"
            pass
    def settWrite(self):
        self.iram = self.iram_Sett.text()
        self.snd = self.snd_Sett.text()
        self.dur = self.FileTSett.text()
        self.tTimer = int(self.TimerSett.text())
        self.repW = self.repWrite.checkState()
        self.logW = self.logWrite.checkState()
        with open('config.ini', 'w', encoding = 'utf-8') as f_conf:
            f_conf.write(self.iram + '\n'
                        + self.snd + '\n'
                        + self.dur + '\n'
                        + str(self.tTimer) + '\n'
                        + str(self.repW) + '\n'
                        + str(self.logW) + '\n')
        self.Settings.hide()
        if self.pause == True:
            self.goStart()
    def goStart(self):
        self.settRead()
        self.pause = False
        self.start.setText("Пауза")
        self.start.setStyleSheet("background-color: ")
        self.info.setStyleSheet("background-color: ")
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.statPause)
        #заводим часы
        self.dtimeTick()
        #заводим температуру и давление
        self.statTemp()
        #Запуск основного процесса
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
                self.info.setText("Идет процесс... LT" )
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
                self.info.setText("Идет процесс... CL ")
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
            l1 = [self.WT1, self.WT2, self.WT3, self.WT4, self.WT5, self.WT6]
            l2 = [self.w1, self.w2, self.w3, self.w4, self.w5, self.w6]
            l3 = [self.WT1_v, self.WT2_v, self.WT3_v, self.WT4_v, self.WT5_v, self.WT6_v]
            for i in range(0, 6):
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
            QTimer().singleShot(self.tTimer, self.statTemp)
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
        b = [self.btnWT1, self.btnWT2, self.btnWT3, self.btnWT4, self.btnWT5, self.btnWT6]
        b = b[m]
        b.setStyleSheet(self.red)
        b.clicked.disconnect()
        b.clicked.connect(lambda: self.unmuteWT(m))
        self.mw[m] = 1
    def unmuteWT(self, m):
        b = [self.btnWT1, self.btnWT2, self.btnWT3, self.btnWT4, self.btnWT5, self.btnWT6]
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
        for m in range(0, 6):
            self.muteWT(m)
        self.btn.clicked.disconnect()
        self.btn.clicked.connect(self.unmuteALL)
    def unmuteALL(self):
        for m in range(0, 6):
            self.unmuteLT(m)
        for m in range(0, 4):
            self.unmuteCL(m)
        for m in range(0, 6):
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
            if self.repW == 2 or self.repW == 1:
                repW = "Вкл"
            else:
                repW = "Откл"
            if self.logW == 2 or self.logW == 1:
                logW = "Вкл"
            else:
                logW ="Откл"
            self.bar.showMessage("Рабочий каталог: " + self.iram +
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
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Window()
    application.show()
    sys.exit(app.exec_())
