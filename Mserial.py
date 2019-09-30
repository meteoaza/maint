import time, sys, os, serial, threading
from winreg import *
# from subprocess import Popen, PIPE
from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from Mserial_design import Ui_MainWindow as ComView
from PortSettings_design import Ui_Frame as Settings


class SerialSett(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.u = Settings()
        self.u.setupUi(self)
        self.sText = self.u.sensText
        self.cText = self.u.comText
        self.bText = self.u.baudText
        self.btText = self.u.byteText
        self.parText = self.u.parityText
        self.stText = self.u.sbitText

        self.s_dic = {}
        self.b_dic = {}
        self.bt_dic = {}
        self.par_dic = {}
        self.st_dic = {}

        self.u.addButton.clicked.connect(self.settWrite)
        self.u.applyButton.clicked.connect(self.applySett)
        self.u.extButton.clicked.connect(self.close)
        self.u.comBox.currentTextChanged.connect(self.settShow)

        self.c_list = [
        'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',
        'COM10', 'COM11', 'COM12', 'COM13', 'COM14', 'COM15', 'COM16', 'COM17',
        'COM18', 'COM19', 'COM20', 'COM21', 'COM22', 'COM23', 'COM24', 'COM25',
        'COM26', 'COM27', 'COM28', 'COM29', 'COM30', 'COM31', 'COM32'
        ]
        self.b_list = ['300', '600', '1200', '1800', '2400', '4800', '7200', '9600']
        self.bt_list = ['5', '6', '7', '8']
        self.par_list = ['NO', 'ODD', 'EVEN', 'MARK', 'SPACE']
        self.st_list = ['1', '1.5', '2']

        self.u.comBox.addItems(['None'] + self.c_list)
        self.u.baudBox.addItems([''] + self.b_list)
        self.u.bytesizeBox.addItems([''] + self.bt_list)
        self.u.parityBox.addItems([''] + self.par_list)
        self.u.stopbitsBox.addItems([''] + self.st_list)
        self.settRead()

    def settRead(self):
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        #Читаем настройки программы
        try:
            rKey = OpenKey(aReg, r"Software\IRAM\MAINT\SETT")
            self.station = QueryValueEx(rKey, 'STATION')[0]
            #Читаем настройки СОМ портов
            rKey = OpenKey(aReg, r"Software\IRAM\MAINT\SERIAL")
            for i in self.c_list:
                self.c = i
                self.b = i + '_baud'
                self.bt = i + '_byte'
                self.par = i + '_par'
                self.st = i + '_sbit'
                try:
                    s = QueryValueEx(rKey, self.c)[0]
                    b = QueryValueEx(rKey, self.b)[0]
                    bt = QueryValueEx(rKey, self.bt)[0]
                    par = QueryValueEx(rKey, self.par)[0]
                    st = QueryValueEx(rKey, self.st)[0]
                    self.s_dic[i] = s
                    self.b_dic[i] = b
                    self.bt_dic[i] = bt
                    self.par_dic[i] = par
                    self.st_dic[i] = st
                    rKey.close()
                except Exception:
                    pass
            self.textShow()
        except Exception as e:
            self.settWrite()
            pass

    def settShow(self, value):
        #При выборе сом порта выставляем настройки
        if value == 'None': pass
        else:
            try:
                b = self.b_dic[value]
                bt = self.bt_dic[value]
                par = self.par_dic[value]
                st = self.st_dic[value]
                s = self.s_dic[value]
                self.u.sensEdit.setText(s)
                self.u.baudBox.setCurrentText(b)
                self.u.bytesizeBox.setCurrentText(bt)
                self.u.parityBox.setCurrentText(par)
                self.u.stopbitsBox.setCurrentText(st)
            except Exception:
                pass

    def textShow(self):
        #Выводим данные в таблицу
        self.cText.clear()
        self.bText.clear()
        self.btText.clear()
        self.parText.clear()
        self.stText.clear()
        self.sText.clear()
        for com, sens in self.s_dic.items():
            if not sens:
                pass
            else:
                self.cText.append(f'{com}')
                self.sText.append(f'{sens}')
                baud = self.b_dic[com]
                self.bText.append(f'{baud}')
                byte = self.bt_dic[com]
                self.btText.append(f'{byte}')
                parity = self.par_dic[com]
                self.parText.append(f'{parity}')
                sbit = self.st_dic[com]
                self.stText.append(f'{sbit}')

    def settWrite(self):
        sens = self.u.sensEdit.text()
        com = self.u.comBox.currentText()
        baud = self.u.baudBox.currentText()
        byte = self.u.bytesizeBox.currentText()
        parity = self.u.parityBox.currentText()
        sbit = self.u.stopbitsBox.currentText()

        b = com + '_baud'
        bt = com + '_byte'
        par = com + '_par'
        st = com + '_sbit'
        if com == 'None':
            pass
        else:
            try:
                aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
                nKey = CreateKeyEx(aReg, r'Software\IRAM\MAINT\SERIAL', 0, KEY_ALL_ACCESS)
            except Exception:
                pass
            keyval = SetValueEx(nKey, com, 0, REG_SZ, sens)
            keyval = SetValueEx(nKey, b, 0, REG_SZ, baud)
            keyval = SetValueEx(nKey, bt, 0, REG_SZ, byte)
            keyval = SetValueEx(nKey, par, 0, REG_SZ, parity)
            keyval = SetValueEx(nKey, st, 0, REG_SZ, sbit)
            self.settRead()

    def applySett(self):
        serS.close()
        ser.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


class Thread1(QThread):

    data_slot = pyqtSignal(str)

    def __init__(self, data):
        super().__init__()
        self.data = data

    def run(self):
        self.data_slot.emit(self.data)

class Serial(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = ComView()
        self.ui.setupUi(self)
        self.comBx1 = self.ui.comBox1
        self.comBx2 = self.ui.comBox2
        self.comBx3 = self.ui.comBox3
        self.comBx4 = self.ui.comBox4
        self.comBr1 = self.ui.comBrowser1
        self.comBr2 = self.ui.comBrowser2
        self.comBr3 = self.ui.comBrowser3
        self.comBr4 = self.ui.comBrowser4
        self.senBt1 = self.ui.sensButton1
        self.senBt2 = self.ui.sensButton2
        self.senBt3 = self.ui.sensButton3
        self.senBt4 = self.ui.sensButton4
        self.senBt1.clicked.connect(lambda: self.comBr1.setText(' '))
        self.senBt2.clicked.connect(lambda: self.comBr2.setText(' '))
        self.senBt3.clicked.connect(lambda: self.comBr3.setText(' '))
        self.senBt4.clicked.connect(lambda: self.comBr4.setText(' '))
        self.ui.actSettings.triggered.connect(self.settInit)
        #Берем настройки из SerialSett
        self.s = SerialSett()
        self.s.settRead()
        self.port_sens = self.s.s_dic
        self.baud = self.s.b_dic
        self.byte = self.s.bt_dic
        self.parity = self.s.par_dic
        self.sbit = self.s.st_dic
        #Заполняем боксы наименованиеми портов
        self.port_list = ['None']
        for com, sens in self.port_sens.items():
            if not sens: pass
            else:
                self.port_list += [com]
        self.comBx1.addItems(self.port_list)
        self.comBx2.addItems(self.port_list)
        self.comBx3.addItems(self.port_list)
        self.comBx4.addItems(self.port_list)
        self.threadStart()

    def threadStart(self):
        #Запуск потоков подключенных портов
        try:
            for com, sens in self.port_sens.items():
                if not sens: pass
                else:
                    port=com
                    baud=self.baud[com]
                    byte = self.byte[com]
                    parity = self.parity[com]
                    sbit = self.sbit[com]
                    self.t = threading.Thread(target=self.portRead, args=(port, baud, byte, parity, sbit, sens), daemon=True)
                    self.t.start()
        except Exception as e:
            print('err_threadStart' + str(e))
            pass

    def portRead(self, port, baud , byte, par, sbit, sens):
        #Считывание данных с СОМ портов, вывод в файл и на Ui
        try:
            #Настройки СОМ порта
            if par == 'EVEN': parity=serial.PARITY_EVEN
            elif par == 'ODD': parity=serial.PARITY_ODD
            elif par == 'NO': parity=serial.PARITY_NONE
            elif par == 'MARK': parity=serial.PARITY_MARK
            elif per =='SPACE': parity=serial.PARITY_SPACE
            ser = serial.Serial(
            port=port,
            baudrate=baud,
            bytesize=int(byte),
            parity=parity,
            stopbits=int(sbit),
            )
        except Exception as e:
            print('err_portRead0' + str(e))
            pass
        try:
            #Запуск считывания сом порта
            while True:
                d = ser.readline()
                # time.sleep(10)
                try:
                    data = d.decode('utf-8')
                except Exception as e:
                    print('err_portRead1' + str(e))
                    pass
                self.com = port
                self.sens = sens
                print(str(datetime.now().strftime("%H:%M")) + ' ' + self.com + ' ' + self.sens + ' ' + str(data))
                #Запуск потока для передачи текста на Ui
                self.thread = Thread1(data)
                self.thread.data_slot.connect(self.textSend)
                self.thread.start()
                #Инициализация записи в файл
                self.dataWrite(data)
        except Exception as e:
            print('err_portRead2' + str(e))
            pass

    def textSend(self, data):
        try:
            #Отображение текста на Ui
            com1 = self.comBx1.currentText()
            com2 = self.comBx2.currentText()
            com3 = self.comBx3.currentText()
            com4 = self.comBx4.currentText()
            if com1 == self.com:
                self.comBr1.append(data)
                self.senBt1.setText(self.sens)
            elif com2 == self.com:
                self.comBr2.append(data)
                self.senBt2.setText(self.sens)
            elif com3 == self.com:
                self.comBr3.append(data)
                self.senBt3.setText(self.sens)
            elif com4 == self.com:
                self.comBr4.append(data)
                self.senBt4.setText(self.sens)
            if com1 == 'None': self.comBr1.setText(' '); self.senBt1.setText(' ')
            if com2 == 'None': self.comBr2.setText(' '); self.senBt2.setText(' ')
            if com3 == 'None': self.comBr3.setText(' '); self.senBt3.setText(' ')
            if com4 == 'None': self.comBr4.setText(' '); self.senBt4.setText(' ')
        except Exception as e:
            print('err_textSend' + str(e))
            pass

    def dataWrite(self, data):
        #Запись данных с портов в файл
        try:
            if not os.path.exists('Serial'):
                os.mkdir('Serial')
            with open('Serial\\' + self.sens + '.dat', 'w', encoding='ANSI') as f_sens:
                f_sens.write(str(data))
        except Exception as e:
            print('err_sensWrite' + str(e))
            pass

    def settInit(self):
        ser.close()
        serS.show()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ser = Serial()
    serS = SerialSett()
    ser.show()
    sys.exit(app.exec_())
