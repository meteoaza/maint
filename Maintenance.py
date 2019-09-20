import subprocess, sys, os, time
from datetime import datetime
from Maintenance_main import Sens, Av6
from pygame import mixer
from winreg import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer, Qt
from Maintenance_design_manas import Ui_MainWindow as MainWindowManas
from Maintenance_design_osh import Ui_MainWindow as MainWindowOsh
from Settings import Ui_Settings
from About import Ui_AboutFrame


global ver
ver = '1.9'

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
        self.comList = self.ui.boxCom
        self.baudList = self.ui.boxBaud
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
        self.settRead()
    #Настройки чтение
    def settRead(self):
        self.stationSett.activated[str].connect(self.stChange)
        #Читаем настройки программы
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        try:
            rKey = OpenKey(aReg, r"Software\IRAM\MAINT\SETT")
            self.station = QueryValueEx(rKey, 'STATION')[0]
            self.iram = QueryValueEx(rKey, 'PATH')[0]
            self.snd = QueryValueEx(rKey, 'SOUND')[0]
            self.dur = QueryValueEx(rKey, 'DUR')[0]
            self.tTimer = QueryValueEx(rKey, 'REFRESH')[0]
            self.av_path = QueryValueEx(rKey, 'AV_P')[0]
            self.sensW = QueryValueEx(rKey, 'SENS_W')[0]
            self.repW = QueryValueEx(rKey, 'REP')[0]
            self.logW = QueryValueEx(rKey, 'LOG')[0]
            self.av6W = QueryValueEx(rKey, 'AV_W')[0]
            self.av_time1 = QueryValueEx(rKey, 'AV_T1')[0]
            self.av_time2 = QueryValueEx(rKey, 'AV_T2')[0]
        except (ValueError, FileNotFoundError)as e:
            Sens.logWrite(self, e)
            self.iram = r"d:\IRAM"
            self.snd = r"d:\IRAM\KRAMS_DAT\WAV\Srok1M.WAV"
            self.dur = "1"
            self.tTimer = "3"
            self.av_path = r'd:\IRAM'
            self.sensW = "0"
            self.repW = "0"
            self.logW = "0"
            self.av6W = "0"
            self.av_time1 = "00"
            self.av_time2 = "30"
            pass
        #Список датчиков и СОМ портов в настройках
        try:
            if self.station == 'UCFM':
                self.s_list = [
                    'None', 'CL1', 'CL2', 'CL3', 'CL4', 'LT1', 'LT2',
                    'LT3', 'LT4', 'LT5', 'LT6', 'WT1', 'WT2', 'WT3',
                    'WT4', 'WT5', 'WT6', 'TEMP1', 'TEMP2', 'PRES1', 'PRES2']
                self.com_list = [
                    'None', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5',
                    'COM6', 'COM7', 'COM8', 'COM9', 'COM10', 'COM11',
                    'COM12', 'COM13', 'COM14', 'COM15', 'COM16', 'COM17',
                    'COM18', 'COM19', 'COM20', 'COM21', 'COM22', 'COM23',
                    'COM24', 'COM25', 'COM26', 'COM27', 'COM28', 'COM29',
                    'COM30', 'COM31', 'COM32']
                self.baud_list = ['300', '1200', '4800', '9600']
            elif self.station == 'UCFO':
                self.s_list = ['None', 'CL1', 'CL2', 'CL3', 'CL4', 'LT1', 'LT2',
                           'LT3', 'LT4', 'LT5', 'LT6', 'WT1', 'WT2',
                           'WT3', 'WT4', 'TEMP1', 'TEMP2', 'PRES1', 'PRES2']
                self.com_list = [
                    'None', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5',
                    'COM6', 'COM7', 'COM8', 'COM9', 'COM10', 'COM11',
                    'COM12', 'COM13', 'COM14', 'COM15', 'COM16', 'COM17',
                    'COM18', 'COM19', 'COM20', 'COM21', 'COM22', 'COM23',
                    'COM24', 'COM25', 'COM26', 'COM27', 'COM28', 'COM29',
                    'COM30', 'COM31', 'COM32']
                self.baud_list = ['300', '1200', '4800', '9600']
            else:
                self.s_list = ['None']
                self.com_list = ['None']
                self.baud_list = ['None']
            self.sensList.addItems(self.s_list)
            self.comList.addItems(self.com_list)
            self.baudList.addItems(self.baud_list)
        except Exception as e:
            Sens.logWrite(self, e)
            self.station = '----'
        #Читаем настройки датчиков
        try:
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
            if self.station == 'UCFM':
                self.w5 = QueryValueEx(rKey, 'WT5')[0]
                self.w6 = QueryValueEx(rKey, 'WT6')[0]
            self.t1 = QueryValueEx(rKey, 'TEMP1')[0]
            self.t2 = QueryValueEx(rKey, 'TEMP2')[0]
            self.p1 = QueryValueEx(rKey, 'PRES1')[0]
            self.p2 = QueryValueEx(rKey, 'PRES2')[0]
        except Exception as e:
            Sens.logWrite(self, e)
            self.c1 = self.c2 = self.c3 = self.c4 = 'None'
            self.l1 = self.l2 = self.l3 = self.l4 = self.l5 = self.l6 = 'None'
            self.w1 = self.w2 = self.w3 = self.w4 = 'None'
            if self.station == 'UCFM':
                self.w5 = self.w6 = 'None'
            self.t1 = self.t2 = self.p1 = self.p2 = 'None'
            pass
        #Читаем настройки СОМ портов
        try:
            rKey = OpenKey(aReg, r"Software\IRAM\MAINT\SERIAL")
            self.port_c1 = QueryValueEx(rKey, 'CL1')[0]
            self.port_c2 = QueryValueEx(rKey, 'CL2')[0]
            self.port_c3 = QueryValueEx(rKey, 'CL3')[0]
            self.port_c4 = QueryValueEx(rKey, 'CL4')[0]
            self.port_l1 = QueryValueEx(rKey, 'LT1')[0]
            self.port_l2 = QueryValueEx(rKey, 'LT2')[0]
            self.port_l3 = QueryValueEx(rKey, 'LT3')[0]
            self.port_l4 = QueryValueEx(rKey, 'LT4')[0]
            self.port_l5 = QueryValueEx(rKey, 'LT5')[0]
            self.port_l6 = QueryValueEx(rKey, 'LT6')[0]
            self.port_w1 = QueryValueEx(rKey, 'WT1')[0]
            self.port_w2 = QueryValueEx(rKey, 'WT2')[0]
            self.port_w3 = QueryValueEx(rKey, 'WT3')[0]
            self.port_w4 = QueryValueEx(rKey, 'WT4')[0]
            if self.station == 'UCFM':
                self.port_w5 = QueryValueEx(rKey, 'WT5')[0]
                self.port_w6 = QueryValueEx(rKey, 'WT6')[0]
            self.port_t1 = QueryValueEx(rKey, 'TEMP1')[0]
            self.port_t2 = QueryValueEx(rKey, 'TEMP2')[0]
            self.port_p1 = QueryValueEx(rKey, 'PRES1')[0]
            self.port_p2 = QueryValueEx(rKey, 'PRES2')[0]
            #Читаем настройки скорости СОМ
            self.port_c1_b = QueryValueEx(rKey, 'CL1_baud')[0]
            self.port_c2_b = QueryValueEx(rKey, 'CL2_baud')[0]
            self.port_c3_b = QueryValueEx(rKey, 'CL3_baud')[0]
            self.port_c4_b = QueryValueEx(rKey, 'CL4_baud')[0]
            self.port_l1_b = QueryValueEx(rKey, 'LT1_baud')[0]
            self.port_l2_b = QueryValueEx(rKey, 'LT2_baud')[0]
            self.port_l3_b = QueryValueEx(rKey, 'LT3_baud')[0]
            self.port_l4_b = QueryValueEx(rKey, 'LT4_baud')[0]
            self.port_l5_b = QueryValueEx(rKey, 'LT5_baud')[0]
            self.port_l6_b = QueryValueEx(rKey, 'LT6_baud')[0]
            self.port_w1_b = QueryValueEx(rKey, 'WT1_baud')[0]
            self.port_w2_b = QueryValueEx(rKey, 'WT2_baud')[0]
            self.port_w3_b = QueryValueEx(rKey, 'WT3_baud')[0]
            self.port_w4_b = QueryValueEx(rKey, 'WT4_baud')[0]
            if self.station == 'UCFM':
                self.port_w5_b = QueryValueEx(rKey, 'WT5_baud')[0]
                self.port_w6_b = QueryValueEx(rKey, 'WT6_baud')[0]
            self.port_t1_b = QueryValueEx(rKey, 'TEMP1_baud')[0]
            self.port_t2_b = QueryValueEx(rKey, 'TEMP2_baud')[0]
            self.port_p1_b = QueryValueEx(rKey, 'PRES1_baud')[0]
            self.port_p2_b = QueryValueEx(rKey, 'PRES2_baud')[0]
        except Exception as e:
            Sens.logWrite(self, e)
            self.port_c1 = self.port_c2 = self.port_c3 = self.port_c4 = 'None'
            self.port_l1 = self.port_l2 = self.port_l3 = self.port_l4 = 'None'
            self.port_l5 = self.port_l6 = 'None'
            self.port_w1 = self.port_w2 = self.port_w3 = self.port_w4 = 'None'
            if self.station == 'UCFM':
                self.port_w5 = self.port_w6 = 'None'
            self.port_t1 = self.port_t2 = self.port_p1 = self.port_p2 = 'None'
            self.port_c1_b = self.port_c2_b = self.port_c3_b = self.port_c4_b = '300'
            self.port_l1_b = self.port_l2_b = self.port_l3_b = self.port_l4_b = '300'
            self.port_l5_b = self.port_l6_b = '300'
            self.port_w1_b = self.port_w2_b = self.port_w3_b = self.port_w4_b = '300'
            if self.station == 'UCFM':
                self.port_w5_b = self.port_w6_b = '300'
            self.port_t1_b = self.port_t2_b = self.port_p1_b = self.port_p2_b = '300b'
            pass
        aReg.Close()
        #Выводим текст настроек в Settings
        self.stInd.setText(self.station)
        self.iram_Sett.setText(self.iram)
        self.snd_Sett.setText(self.snd)
        self.FileTSett.setText(self.dur)
        self.TimerSett.setText(self.tTimer)
        self.av_Sett.setText(self.av_path)
        self.checkSensW.setCheckState(int(self.sensW))
        self.checkRepW.setCheckState(int(self.repW))
        self.checkLogW.setCheckState(int(self.logW))
        self.checkAv6.setCheckState(int(self.av6W))
        self.av_Time1.setText(self.av_time1)
        self.av_Time2.setText(self.av_time2)
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
        text_port = self.comList.currentText()
        text_port_b = self.baudList.currentText()
        if text == 'CL1': self.c1 = self.sensSett.text(); self.port_c1 = text_port; self.port_c1_b = text_port_b
        elif text == 'CL2': self.c2 = self.sensSett.text(); self.port_c2 = text_port; self.port_c2_b = text_port_b
        elif text == 'CL3': self.c3 = self.sensSett.text(); self.port_c3 = text_port; self.port_c3_b = text_port_b
        elif text == 'CL4': self.c4 = self.sensSett.text(); self.port_c4 = text_port; self.port_c4_b = text_port_b
        elif text == 'LT1': self.l1 = self.sensSett.text(); self.port_l1 = text_port; self.port_l1_b = text_port_b
        elif text == 'LT2': self.l2 = self.sensSett.text(); self.port_l2 = text_port; self.port_l2_b = text_port_b
        elif text == 'LT3': self.l3 = self.sensSett.text(); self.port_l3 = text_port; self.port_l3_b = text_port_b
        elif text == 'LT4': self.l4 = self.sensSett.text(); self.port_l4 = text_port; self.port_l4_b = text_port_b
        elif text == 'LT5': self.l5 = self.sensSett.text(); self.port_l5 = text_port; self.port_l5_b = text_port_b
        elif text == 'LT6': self.l6 = self.sensSett.text(); self.port_l6 = text_port; self.port_l6_b = text_port_b
        elif text == 'WT1': self.w1 = self.sensSett.text(); self.port_w1 = text_port; self.port_w1_b = text_port_b
        elif text == 'WT2': self.w2 = self.sensSett.text(); self.port_w2 = text_port; self.port_w2_b = text_port_b
        elif text == 'WT3': self.w3 = self.sensSett.text(); self.port_w3 = text_port; self.port_w3_b = text_port_b
        elif text == 'WT4': self.w4 = self.sensSett.text(); self.port_w4 = text_port; self.port_w4_b = text_port_b
        elif text == 'WT5': self.w5 = self.sensSett.text(); self.port_w5 = text_port; self.port_w5_b = text_port_b
        elif text == 'WT6': self.w6 = self.sensSett.text(); self.port_w6 = text_port; self.port_w6_b = text_port_b
        elif text == 'TEMP1': self.t1 = self.sensSett.text(); self.port_t1 = text_port; self.port_t1_b = text_port_b
        elif text == 'TEMP2': self.t2 = self.sensSett.text(); self.port_t2 = text_port; self.port_t2_b = text_port_b
        elif text == 'PRES1': self.p1 = self.sensSett.text(); self.port_p1 = text_port; self.port_p1_b = text_port_b
        elif text == 'PRES2': self.p2 = self.sensSett.text(); self.port_p2 = text_port; self.port_p2_b = text_port_b
        elif text == 'None': self.sensSett.setText('')
        self.viewSens()
    #Просмотр привязки датчиков
    def viewSens(self):
        if self.station == 'UCFM':
            self.sensView.setText(
                'CL1 -  ' + self.port_c1 + ' - ' + self.port_c1_b + ' - ' + self.c1 + '\n' +
                'CL2 -  ' + self.port_c2 + ' - ' + self.port_c2_b + ' - ' + self.c2 + '\n' +
                'CL3 -  ' + self.port_c3 + ' - ' + self.port_c3_b + ' - ' + self.c3 + '\n' +
                'CL4 -  ' + self.port_c4 + ' - ' + self.port_c4_b + ' - ' + self.c4 + '\n' +
                'LT1 -  ' + self.port_l1 + ' - ' + self.port_l1_b + ' - ' + self.l1 + '\n' +
                'LT2 -  ' + self.port_l2 + ' - ' + self.port_l2_b + ' - ' + self.l2 + '\n' +
                'LT3 -  ' + self.port_l3 + ' - ' + self.port_l3_b + ' - ' + self.l3 + '\n' +
                'LT4 -  ' + self.port_l4 + ' - ' + self.port_l4_b + ' - ' + self.l4 + '\n' +
                'LT5 -  ' + self.port_l5 + ' - ' + self.port_l5_b + ' - ' + self.l5 + '\n' +
                'LT6 -  ' + self.port_l6 + ' - ' + self.port_l6_b + ' - ' + self.l6 + '\n' +
                'WT1 -  ' + self.port_w1 + ' - ' + self.port_w1_b + ' - ' + self.w1 + '\n' +
                'WT2 -  ' + self.port_w2 + ' - ' + self.port_w2_b + ' - ' + self.w2 + '\n' +
                'WT3 -  ' + self.port_w3 + ' - ' + self.port_w3_b + ' - ' + self.w3 + '\n' +
                'WT4 -  ' + self.port_w4 + ' - ' + self.port_w4_b + ' - ' + self.w4 + '\n' +
                'WT5 -  ' + self.port_w5 + ' - ' + self.port_w5_b + ' - ' + self.w5 + '\n' +
                'WT6 -  ' + self.port_w6 + ' - ' + self.port_w6_b + ' - ' + self.w6 + '\n' +
                'TEMP1 - ' + self.port_t1 + ' - ' + self.port_t1_b + ' - ' + self.t1 + '\n' +
                'TEMP2 - ' + self.port_t2 + ' - ' + self.port_t2_b + ' - ' + self.t2 + '\n' +
                'PRES1 - ' + self.port_p1 + ' - ' + self.port_p1_b + ' - ' + self.p1 + '\n' +
                'PRES2 - ' + self.port_p2 + ' - ' + self.port_p2_b + ' - ' + self.p2 + '\n'
                )
        else:
            self.sensView.setText(
                'CL1 -  ' + self.port_c1 + ' - ' + self.port_c1_b + ' - ' + self.c1 + '\n' +
                'CL2 -  ' + self.port_c2 + ' - ' + self.port_c2_b + ' - ' + self.c2 + '\n' +
                'CL3 -  ' + self.port_c3 + ' - ' + self.port_c3_b + ' - ' + self.c3 + '\n' +
                'CL4 -  ' + self.port_c4 + ' - ' + self.port_c4_b + ' - ' + self.c4 + '\n' +
                'LT1 -  ' + self.port_l1 + ' - ' + self.port_l1_b + ' - ' + self.l1 + '\n' +
                'LT2 -  ' + self.port_l2 + ' - ' + self.port_l2_b + ' - ' + self.l2 + '\n' +
                'LT3 -  ' + self.port_l3 + ' - ' + self.port_l3_b + ' - ' + self.l3 + '\n' +
                'LT4 -  ' + self.port_l4 + ' - ' + self.port_l4_b + ' - ' + self.l4 + '\n' +
                'LT5 -  ' + self.port_l5 + ' - ' + self.port_l5_b + ' - ' + self.l5 + '\n' +
                'LT6 -  ' + self.port_l6 + ' - ' + self.port_l6_b + ' - ' + self.l6 + '\n' +
                'WT1 -  ' + self.port_w1 + ' - ' + self.port_w1_b + ' - ' + self.w1 + '\n' +
                'WT2 -  ' + self.port_w2 + ' - ' + self.port_w2_b + ' - ' + self.w2 + '\n' +
                'WT3 -  ' + self.port_w3 + ' - ' + self.port_w3_b + ' - ' + self.w3 + '\n' +
                'WT4 -  ' + self.port_w4 + ' - ' + self.port_w4_b + ' - ' + self.w4 + '\n' +
                'TEMP1 - ' + self.port_t1 + ' - ' + self.port_t1_b + ' - ' + self.t1 + '\n' +
                'TEMP2 - ' + self.port_t2 + ' - ' + self.port_t2_b + ' - ' + self.t2 + '\n' +
                'PRES1 - ' + self.port_p1 + ' - ' + self.port_p1_b + ' - ' + self.p1 + '\n' +
                'PRES2 - ' + self.port_p2 + ' - ' + self.port_p2_b + ' - ' + self.p2 + '\n'
                                  )
    #Настройки запись
    def settWrite(self):
        #Читаем настройки программы из полей для записи в реестр
        self.station = self.stInd.text()
        self.iram = self.iram_Sett.text()
        self.snd = self.snd_Sett.text()
        self.dur = self.FileTSett.text()
        self.tTimer = self.TimerSett.text()
        self.av_path = self.av_Sett.text()
        self.sensW =str(self.checkSensW.checkState())
        self.repW = str(self.checkRepW.checkState())
        self.logW = str(self.checkLogW.checkState())
        self.av6W = str(self.checkAv6.checkState())
        self.av_time1 = self.av_Time1.text()
        self.av_time2 = self.av_Time2.text()
        #Пишем настройки программы в реестр
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        try:
            nKey = CreateKeyEx(aReg, r'Software\IRAM\MAINT\SETT', 0, KEY_ALL_ACCESS)
            keyval = SetValueEx(nKey, 'STATION', 0, REG_SZ, self.station)
            keyval = SetValueEx(nKey, 'PATH', 0, REG_SZ, self.iram)
            keyval = SetValueEx(nKey, 'SOUND', 0, REG_SZ, self.snd)
            keyval = SetValueEx(nKey, 'DUR', 0, REG_SZ, self.dur)
            keyval = SetValueEx(nKey, 'REFRESH', 0, REG_SZ, self.tTimer)
            keyval = SetValueEx(nKey, 'AV_P', 0, REG_SZ, self.av_path)
            keyval = SetValueEx(nKey, 'SENS_W', 0, REG_SZ, self.sensW)
            keyval = SetValueEx(nKey, 'REP', 0, REG_SZ, self.repW)
            keyval = SetValueEx(nKey, 'LOG', 0, REG_SZ, self.logW)
            keyval = SetValueEx(nKey, 'AV_W', 0, REG_SZ, self.av6W)
            keyval = SetValueEx(nKey, 'AV_T1', 0, REG_SZ, self.av_time1)
            keyval = SetValueEx(nKey, 'AV_T2', 0, REG_SZ, self.av_time2)
        except Exception as e:
            Sens.logWrite(self, e)
            pass
        #Пишем настройки датчиков в реестр
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
            if self.station == 'UCFM':
                keyval = SetValueEx(nKey, 'WT5', 0, REG_SZ, self.w5)
                keyval = SetValueEx(nKey, 'WT6', 0, REG_SZ, self.w6)
            keyval = SetValueEx(nKey, 'TEMP1', 0, REG_SZ, self.t1)
            keyval = SetValueEx(nKey, 'TEMP2', 0, REG_SZ, self.t2)
            keyval = SetValueEx(nKey, 'PRES1', 0, REG_SZ, self.p1)
            keyval = SetValueEx(nKey, 'PRES2', 0, REG_SZ, self.p2)
        except Exception as e:
            Sens.logWrite(self, e)
            pass
        #Пишем настройки COM в реестр
        try:
            aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
            nKey = CreateKeyEx(aReg, r'Software\IRAM\MAINT\SERIAL', 0, KEY_ALL_ACCESS)
            keyval = SetValueEx(nKey, 'CL1', 0, REG_SZ, self.port_c1)
            keyval = SetValueEx(nKey, 'CL2', 0, REG_SZ, self.port_c2)
            keyval = SetValueEx(nKey, 'CL3', 0, REG_SZ, self.port_c3)
            keyval = SetValueEx(nKey, 'CL4', 0, REG_SZ, self.port_c4)
            keyval = SetValueEx(nKey, 'LT1', 0, REG_SZ, self.port_l1)
            keyval = SetValueEx(nKey, 'LT2', 0, REG_SZ, self.port_l2)
            keyval = SetValueEx(nKey, 'LT3', 0, REG_SZ, self.port_l3)
            keyval = SetValueEx(nKey, 'LT4', 0, REG_SZ, self.port_l4)
            keyval = SetValueEx(nKey, 'LT5', 0, REG_SZ, self.port_l5)
            keyval = SetValueEx(nKey, 'LT6', 0, REG_SZ, self.port_l6)
            keyval = SetValueEx(nKey, 'WT1', 0, REG_SZ, self.port_w1)
            keyval = SetValueEx(nKey, 'WT2', 0, REG_SZ, self.port_w2)
            keyval = SetValueEx(nKey, 'WT3', 0, REG_SZ, self.port_w3)
            keyval = SetValueEx(nKey, 'WT4', 0, REG_SZ, self.port_w4)
            if self.station == 'UCFM':
                keyval = SetValueEx(nKey, 'WT5', 0, REG_SZ, self.port_w5)
                keyval = SetValueEx(nKey, 'WT6', 0, REG_SZ, self.port_w6)
            keyval = SetValueEx(nKey, 'TEMP1', 0, REG_SZ, self.port_t1)
            keyval = SetValueEx(nKey, 'TEMP2', 0, REG_SZ, self.port_t2)
            keyval = SetValueEx(nKey, 'PRES1', 0, REG_SZ, self.port_p1)
            keyval = SetValueEx(nKey, 'PRES2', 0, REG_SZ, self.port_p2)
            #Настройки скорости
            keyval = SetValueEx(nKey, 'CL1_baud', 0, REG_SZ, self.port_c1_b)
            keyval = SetValueEx(nKey, 'CL2_baud', 0, REG_SZ, self.port_c2_b)
            keyval = SetValueEx(nKey, 'CL3_baud', 0, REG_SZ, self.port_c3_b)
            keyval = SetValueEx(nKey, 'CL4_baud', 0, REG_SZ, self.port_c4_b)
            keyval = SetValueEx(nKey, 'LT1_baud', 0, REG_SZ, self.port_l1_b)
            keyval = SetValueEx(nKey, 'LT2_baud', 0, REG_SZ, self.port_l2_b)
            keyval = SetValueEx(nKey, 'LT3_baud', 0, REG_SZ, self.port_l3_b)
            keyval = SetValueEx(nKey, 'LT4_baud', 0, REG_SZ, self.port_l4_b)
            keyval = SetValueEx(nKey, 'LT5_baud', 0, REG_SZ, self.port_l5_b)
            keyval = SetValueEx(nKey, 'LT6_baud', 0, REG_SZ, self.port_l6_b)
            keyval = SetValueEx(nKey, 'WT1_baud', 0, REG_SZ, self.port_w1_b)
            keyval = SetValueEx(nKey, 'WT2_baud', 0, REG_SZ, self.port_w2_b)
            keyval = SetValueEx(nKey, 'WT3_baud', 0, REG_SZ, self.port_w3_b)
            keyval = SetValueEx(nKey, 'WT4_baud', 0, REG_SZ, self.port_w4_b)
            if self.station == 'UCFM':
                keyval = SetValueEx(nKey, 'WT5_baud', 0, REG_SZ, self.port_w5_b)
                keyval = SetValueEx(nKey, 'WT6_baud', 0, REG_SZ, self.port_w6_b)
            keyval = SetValueEx(nKey, 'TEMP1_baud', 0, REG_SZ, self.port_t1_b)
            keyval = SetValueEx(nKey, 'TEMP2_baud', 0, REG_SZ, self.port_t2_b)
            keyval = SetValueEx(nKey, 'PRES1_baud', 0, REG_SZ, self.port_p1_b)
            keyval = SetValueEx(nKey, 'PRES2_baud', 0, REG_SZ, self.port_p2_b)
        except Exception as e:
            Sens.logWrite(self, e)
            pass
        aReg.Close()
        self.goWindow()
        self.stationSett.activated[str].disconnect()
        self.btnIramSett.accepted.disconnect()
        self.btnHelp.clicked.disconnect()
        self.sensAdd.clicked.disconnect()
        self.serRun.clicked.disconnect()

    def stChange(self):
        self.station = self.stationSett.currentText()
        self.stationSett.activated[str].disconnect()
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        nKey = CreateKeyEx(aReg, r'Software\IRAM\MAINT\SETT', 0, KEY_ALL_ACCESS)
        keyval = SetValueEx(nKey, 'STATION', 0, REG_SZ, self.station)
        aReg.Close()
        self.settRead()

    def help(self):
        self.w = QtWidgets.QMainWindow()
        if self.station == 'UCFM':
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
        if self.set.station == 'UCFM':
            self.ui = MainWindowManas()
        elif self.set.station == 'UCFO':
            self.ui =MainWindowOsh()
        else:
            SettingsInit().show()
        try:
            self.ui.setupUi(self)
            self.show()
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
            if self.set.station == 'UCFM':
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
            if self.set.station == 'UCFM':
                self.WT5_v = self.ui.labelWT5
                self.WT6_v = self.ui.labelWT6
            self.Temp1_v = self.ui.lcdTemp1
            self.Temp2_v = self.ui.lcdTemp2
            self.Pres1_v = self.ui.lcdPres1
            self.Pres2_v = self.ui.lcdPres2
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
            if self.set.station == 'UCFM':
                self.btnWT5 = self.ui.btnWind5
                self.btnWT6 = self.ui.btnWind6
            self.menuSett.menuAction().setStatusTip("Настройки")
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
            #Определение цвета
            self.red = "background-color: qconicalgradient(cx:1, cy:0.329773, \
                        angle:0, stop:0.3125 rgba(239, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"
            self.green = "background-color: qconicalgradient(cx:1, cy:0.529, angle:0,\
                        stop:0.215909 rgba(38, 174, 23, 255), stop:1 rgba(255, 255, 255, 255));"
            self.yellow = "background-color: qconicalgradient(cx:1, cy:0.329773, \
                        angle:0, stop:0.363636 rgba(219, 219, 0, 255), stop:1 rgba(255, 255, 255, 255));"
            self.blue = "background-color: qconicalgradient(cx:1, cy:0.529, angle:0,\
                        stop:0.215909 rgba(100, 200, 250, 200), stop:1 rgba(255, 255, 255, 255));"
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
            if self.set.station == 'UCFM':
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
            if self.set.station == 'UCFM':
                self.btnWT5.clicked.connect(lambda: self.muteWT(4))
                self.btnWT5.setStyleSheet(self.green)
                self.btnWT6.clicked.connect(lambda: self.muteWT(5))
                self.btnWT6.setStyleSheet(self.green)
            #инициализируем переменные выключения звука, прогресс бара, паузы
            self.ml = [0, 0, 0, 0, 0, 0]
            self.mc = [0, 0, 0, 0]
            self.mw = [0, 0, 0, 0, 0, 0]
            self.progress = 0
            self.pause = True
            #Привязка переменных из класса SettingsInit
            self.station = self.set.station
            self.iram = self.set.iram
            self.snd = self.set.snd
            self.dur = self.set.dur
            self.tTimer = self.set.tTimer
            self.tTimer = int(self.tTimer)*1000
            self.av_path = self.set.av_path
            self.sensW = self.set.sensW
            self.repW = self.set.repW
            self.logW = self.set.logW
            self.av6W = self.set.av6W
            self.av_time1 = self.set.av_time1 + '00'
            self.av_time2 = self.set.av_time2 + '00'
            self.c1 = self.set.c1
            self.c2 = self.set.c2
            self.c3 = self.set.c3
            self.c4 = self.set.c4
            self.l1 = self.set.l1
            self.l2 = self.set.l2
            self.l3 = self.set.l3
            self.l4 = self.set.l4
            self.l5 = self.set.l5
            self.l6 = self.set.l6
            self.w1 = self.set.w1
            self.w2 = self.set.w2
            self.w3 = self.set.w3
            self.w4 = self.set.w4
            if self.set.station == 'UCFM':
                self.w5 = self.set.w5
                self.w6 = self.set.w6
            self.t1 = self.set.t1
            self.t2 = self.set.t2
            self.p1 = self.set.p1
            self.p2 = self.set.p2
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
        self.s_list = list()
        if self.pause == False:
            l1 = [self.LT1, self.LT2, self.LT3,
                  self.LT4, self.LT5, self.LT6]
            l2 = [self.l1, self.l2, self.l3,
                  self.l4, self.l5, self.l6]
            l3 = [self.LT1_v, self.LT2_v, self.LT3_v,
                  self.LT4_v, self.LT5_v, self.LT6_v]
            for i in range(6):
                self.LT_l = l1[i]
                self.lt = l2[i]
                self.LT_v = l3[i]
                s = Sens(self.iram, self.lt, self.dur, self.repW, self.logW)
                s.ltInit()
                self.LT_l.setText(s.lt_status)
                self.LT_v.setText(s.lt_val)
                self.info2.setText("Идет процесс... LT" )
                self.info2.setStyleSheet(self.blue)
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
                self.s_list.append(s.lt_status + ' ' + s.lt_val)
                if s.LOGs == "0":
                    pass
                else:
                    self.info.setText(s.LOGs)
            QTimer().singleShot(self.tTimer, self.statCL)
        else:
            self.info2.setText("Остановлено")
            self.info2.setStyleSheet(self.red)
            pass
    def statCL(self):
        if self.pause == False:
            l1 = [self.CL1, self.CL2, self.CL3, self.CL4]
            l2 = [self.c1, self.c2, self.c3, self.c4]
            l3 = [self.CL1_v, self.CL2_v, self.CL3_v, self.CL4_v]
            for i  in range(4):
                self.CL_l = l1[i]
                self.cl = l2[i]
                self.CL_v = l3[i]
                s = Sens(self.iram, self.cl, self.dur, self.repW, self.logW)
                s.clInit()
                self.CL_l.setText(s.cl_status)
                self.CL_v.setText(s.cl_val)
                self.info2.setText("Идет процесс... CL ")
                self.info2.setStyleSheet(self.blue)
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
                self.s_list.append(s.cl_status + ' ' + s.cl_val)
                if s.LOGs == "0":
                    pass
                else:
                    self.info.setText(s.LOGs)
            QTimer().singleShot(self.tTimer, self.statWT)
        else:
            self.info2.setText("Остановлено")
            self.info2.setStyleSheet(self.red)
            pass
    def statWT(self):
        if self.pause == False:
            if self.set.station == 'UCFM':
                l1 = [self.WT1, self.WT2, self.WT3,
                      self.WT4, self.WT5, self.WT6]
                l2 = [self.w1, self.w2, self.w3,
                      self.w4, self.w5, self.w6]
                l3 = [self.WT1_v, self.WT2_v, self.WT3_v,
                      self.WT4_v, self.WT5_v, self.WT6_v]
            else:
                l1 = [self.WT1, self.WT2, self.WT3, self.WT4]
                l2 = [self.w1, self.w2, self.w3, self.w4]
                l3 = [self.WT1_v, self.WT2_v, self.WT3_v, self.WT4_v]
            for i in range(len(l2)):
                self.WT_l = l1[i]
                self.wt = l2[i]
                self.WT_v = l3[i]
                s = Sens(self.iram, self.wt, self.dur, self.repW, self.logW)
                s.wtInit()
                self.WT_l.setText(s.wt_status)
                self.WT_v.setText(s.wt_val)
                self.info2.setText("Идет процесс... WIND")
                self.info2.setStyleSheet(self.blue)
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
                self.s_list.append(s.wt_status + ' ' + s.wt_val)
                if s.LOGs == "0":
                    pass
                else:
                    self.info.setText(s.LOGs)
            QTimer().singleShot(self.tTimer, self.statTemp)
        else:
            self.info2.setText("Остановлено")
            self.info2.setStyleSheet(self.red)
            pass
    def statTemp(self):
        if self.pause == False:
            l1 = [self.t1, self.t2, self.p1, self.p2]
            l2 = [self.Temp1_v, self.Temp2_v, self.Pres1_v, self.Pres2_v]
            for i in range(4):
                self.tm = l1[i]
                self.tm_v = l2[i]
                s = Sens(self.iram, self.tm, self.dur, self.repW, self.logW)
                s.tempInit()
                self.tm_v.display(s.tm_val)
                self.info2.setText("Идет процесс... TEMP")
                self.s_list.append(str(self.tm) + ' ' + str(s.tm_val))
            self.sensWrite(self.s_list)
            QTimer().singleShot(self.tTimer, self.statLT)
        else:
            self.info2.setText("Остановлено")
            self.info2.setStyleSheet(self.red)
            pass
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
        if self.set.station == 'UCFM':
            b = [self.btnWT1, self.btnWT2, self.btnWT3, self.btnWT4, self.btnWT5, self.btnWT6]
        else: b = [self.btnWT1, self.btnWT2, self.btnWT3, self.btnWT4]
        b = b[m]
        b.setStyleSheet(self.red)
        b.clicked.disconnect()
        b.clicked.connect(lambda: self.unmuteWT(m))
        self.mw[m] = 1
    def unmuteWT(self, m):
        if self.set.station == 'UCFM':
            b = [self.btnWT1, self.btnWT2, self.btnWT3, self.btnWT4, self.btnWT5, self.btnWT6]
        else: b = [self.btnWT1, self.btnWT2, self.btnWT3, self.btnWT4]
        b = b[m]
        b.setStyleSheet(self.green)
        b.clicked.disconnect()
        b.clicked.connect(lambda: self.muteWT(m))
        self.mw[m] = 0
    def muteALL(self):
        for m in range(6):
            self.muteLT(m)
        for m in range(4):
            self.muteCL(m)
        if self.set.station == 'UCFM':
            r = 6
        else: r = 4
        for m in range(r):
            self.muteWT(m)
        self.btn.clicked.disconnect()
        self.btn.clicked.connect(self.unmuteALL)
    def unmuteALL(self):
        for m in range(6):
            self.unmuteLT(m)
        for m in range(4):
            self.unmuteCL(m)
        if self.set.station == 'UCFM':
            r = 6
        else: r = 4
        for m in range(r):
            self.unmuteWT(m)
        self.btn.clicked.disconnect()
        self.btn.clicked.connect(self.muteALL)
    def dtimeTick(self):
        if self.pause == False:
            self.t = datetime.strftime(datetime.now(), "%d-%m-%y  %H:%M:%S")
            self.av_time = self.t.split()[1].split(':')[1] + self.t.split()[1].split(':')[2]
            if self.av_time == self.av_time1 or self.av_time == self.av_time2:
                self.copyAB6()
            if self.sensW == '2' or self.sensW == '1':
                sensW = "Вкл"
            else:
                sensW = "Откл"
            if self.repW == '2' or self.repW == '1':
                repW = "Вкл"
            else:
                repW = "Откл"
            # if self.logW == '2' or self.logW == '1':
            #     logW = "Вкл"
            # else:
            #     logW ="Откл"
            if self.av6W == '2' or self.av6W == '1':
                av6W = "Вкл"
                av_info = ("  ( " + self.av_path + "      " + self.av_time1[:2]
                         + " , "  + self.av_time2[:2] + " мин )")
            else:
                av6W ="Откл"
                av_info = "              "
            self.bar.showMessage("Рабочий каталог: " + self.iram
            + "                                Время ожидания файла:  "
            + str(self.dur) + " мин." + "      Время обновления:    "
            + str(self.tTimer)[:-3] + " сек." + "       Отчет: " + repW
            + "      Sens: " + sensW  + "               AB6:  " + av6W + av_info)
            self.dtime.setText(self.t)
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

    def copyAB6(self):
        av = Av6(self.av_path, self.av6W)
        self.info.setText(av.av6_rep)

    def sensWrite(self, sens):
        if self.sensW != '0':
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Window()
    sys.exit(app.exec_())
