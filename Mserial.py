import time, sys, os, serial, threading, multiprocessing
from winreg import *
from datetime import datetime as tm
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
        self.s_tText = self.u.typesText
        self.cText = self.u.comText
        self.bText = self.u.baudText
        self.btText = self.u.byteText
        self.parText = self.u.parityText
        self.stText = self.u.sbitText
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
        self.sens_types = ['LT', 'CL', 'WT', 'MAWS', 'MILOS', 'PTB']
        self.b_list = ['300', '600', '1200', '1800', '2400', '4800', '7200', '9600']
        self.bt_list = ['5', '6', '7', '8']
        self.par_list = ['NO', 'ODD', 'EVEN', 'MARK', 'SPACE']
        self.st_list = ['1', '1.5', '2']
        self.s_dic = {}
        self.typ_dic = {}
        self.b_dic = {}
        self.bt_dic = {}
        self.par_dic = {}
        self.st_dic = {}
        self.u.comBox.addItems(['None'] + self.c_list)
        self.u.typesBox.addItems([''] + self.sens_types)
        self.u.baudBox.addItems([''] + self.b_list)
        self.u.bytesizeBox.addItems([''] + self.bt_list)
        self.u.parityBox.addItems([''] + self.par_list)
        self.u.stopbitsBox.addItems([''] + self.st_list)
        self.settRead()

    def settRead(self):
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        # Читаем настройки программы
        try:
            rKey = OpenKey(aReg, r"Software\IRAM\MAINT\PROGSETT")
            self.station = QueryValueEx(rKey, 'STATION')[0]
            # Читаем настройки СОМ портов
            rKey = OpenKey(aReg, r"Software\IRAM\MAINT\SERIAL")
            for i in self.c_list:
                self.c = i
                self.s_types = i + '_types'
                self.b = i + '_baud'
                self.bt = i + '_byte'
                self.par = i + '_par'
                self.st = i + '_sbit'
                try:
                    s = QueryValueEx(rKey, self.c)[0]
                    if s == 'None':
                        pass
                    else:
                        s_t = QueryValueEx(rKey, self.s_types)[0]
                        b = QueryValueEx(rKey, self.b)[0]
                        bt = QueryValueEx(rKey, self.bt)[0]
                        par = QueryValueEx(rKey, self.par)[0]
                        st = QueryValueEx(rKey, self.st)[0]
                        self.s_dic[i] = s
                        self.typ_dic[i] = s_t
                        self.b_dic[i] = b
                        self.bt_dic[i] = bt
                        self.par_dic[i] = par
                        self.st_dic[i] = st
                except Exception as e:
                    nKey = CreateKeyEx(aReg, r'Software\IRAM\MAINT\SERIAL', 0, KEY_ALL_ACCESS)
                    SetValueEx(nKey, self.c, 0, REG_SZ, 'None')
                    print(str(e))
                    pass
            self.textShow()
        except Exception as e:
            print(str(e))
            pass

    def settShow(self, value):
        # При выборе сом порта выставляем настройки
        if value == 'None':
            pass
        else:
            try:
                b = self.b_dic[value]
                bt = self.bt_dic[value]
                par = self.par_dic[value]
                st = self.st_dic[value]
                s = self.s_dic[value]
                s_t = self.typ_dic[value]
                self.u.sensEdit.setText(s)
                self.u.typesBox.setCurrentText(s_t)
                self.u.baudBox.setCurrentText(b)
                self.u.bytesizeBox.setCurrentText(bt)
                self.u.parityBox.setCurrentText(par)
                self.u.stopbitsBox.setCurrentText(st)
            except Exception:
                pass

    def textShow(self):
        # Выводим данные в таблицу
        self.cText.clear()
        self.bText.clear()
        self.btText.clear()
        self.parText.clear()
        self.stText.clear()
        self.s_tText.clear()
        self.sText.clear()
        for com, sens in self.s_dic.items():
            if not sens:
                pass
            else:
                self.cText.append(com)
                self.sText.append(sens)
                s_types = self.typ_dic[com]
                self.s_tText.append(s_types)
                baud = self.b_dic[com]
                self.bText.append(baud)
                byte = self.bt_dic[com]
                self.btText.append(byte)
                parity = self.par_dic[com]
                self.parText.append(parity)
                sbit = self.st_dic[com]
                self.stText.append(sbit)

    def settWrite(self):
        sens = self.u.sensEdit.text()
        s_types = self.u.typesBox.currentText()
        com = self.u.comBox.currentText()
        baud = self.u.baudBox.currentText()
        byte = self.u.bytesizeBox.currentText()
        parity = self.u.parityBox.currentText()
        sbit = self.u.stopbitsBox.currentText()

        s_t = com + '_types'
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
            SetValueEx(nKey, com, 0, REG_SZ, sens)
            SetValueEx(nKey, s_t, 0, REG_SZ, s_types)
            SetValueEx(nKey, b, 0, REG_SZ, baud)
            SetValueEx(nKey, bt, 0, REG_SZ, byte)
            SetValueEx(nKey, par, 0, REG_SZ, parity)
            SetValueEx(nKey, st, 0, REG_SZ, sbit)
            self.settRead()

    def applySett(self):
        self.close()
        window.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


class SerialWindow(QtWidgets.QMainWindow):

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
        self.statText = self.ui.statBrowser
        self.startBt = self.ui.startButton
        self.startBt.clicked.connect(self.portStart)
        self.ui.actSettings.triggered.connect(self.settInit)
        self.senBt1.clicked.connect(lambda: self.comBr1.setText(' '))
        self.senBt2.clicked.connect(lambda: self.comBr2.setText(' '))
        self.senBt3.clicked.connect(lambda: self.comBr3.setText(' '))
        self.senBt4.clicked.connect(lambda: self.comBr4.setText(' '))
        # Активируем Shortcuts
        self.settShct = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self)
        self.settShct.activated.connect(self.settInit)
        self.runShct = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+R"), self)
        self.runShct.activated.connect(self.portStart)
        # Берем настройки из SerialSett
        self.s_dic = sett.s_dic
        self.typ_dic = sett.typ_dic
        self.b_dic = sett.b_dic
        self.bt_dic = sett.bt_dic
        self.par_dic = sett.par_dic
        self.st_dic = sett.st_dic
        # Заполняем боксы наименованиеми портов
        self.port_list = ['None']
        for com, sens in self.s_dic.items():
            if not sens:
                pass
            else:
                self.port_list += [com]
        self.comBx1.addItems(self.port_list)
        self.comBx2.addItems(self.port_list)
        self.comBx3.addItems(self.port_list)
        self.comBx4.addItems(self.port_list)
        # Start port reading
        self.portStart()

    def threadPorts(self):
        self.threads_stop = False
        # Запуск потоков подключенных портов
        try:
            for com, sens in self.s_dic.items():
                if not sens:
                    pass
                else:
                    port_args = [
                        com,
                        self.b_dic[com],  # baud
                        self.bt_dic[com],  # byte
                        self.par_dic[com],  # parity
                        self.st_dic[com],  # stop bit
                        self.s_dic[com],  # sens
                        self.typ_dic[com]  # types
                    ]
                    self.t = threading.Thread(target=self.comListen, args=(port_args),
                                              daemon=True)
                    self.t.start()
        except Exception as e:
            self.logWrite(f'threadPorts {e}')
            pass

    def comListen(self, *port_args):
        # Считывание данных с СОМ портов, вывод в файл и на Ui
        try:
            # Настройки СОМ порта
            if port_args[3] == 'EVEN':
                parity = serial.PARITY_EVEN
            elif port_args[3] == 'ODD':
                parity = serial.PARITY_ODD
            elif port_args[3] == 'NO':
                parity = serial.PARITY_NONE
            elif port_args[3] == 'MARK':
                parity = serial.PARITY_MARK
            elif port_args[3] == 'SPACE':
                parity = serial.PARITY_SPACE
            else:
                parity = 'NO'
            ser = serial.Serial(
                port=port_args[0],
                baudrate=port_args[1],
                bytesize=int(port_args[2]),
                parity=parity,
                stopbits=int(port_args[4]),
                timeout=3,
            )
            while not self.threads_stop:
                # Запуск считывания сом порта
                try:
                    if port_args[6] == 'CL':
                        buf = ser.read_until('\r').rstrip()
                    elif port_args[6] == 'LT':
                        b = ser.readline()
                        buf = b + ser.read_until('\r').rstrip()
                    elif port_args[6] == 'MILOS':
                        buf = ser.readline().strip()
                    else:
                        buf = ser.readline().rstrip()
                    data = buf.decode('utf-8')
                except Exception as e:
                    print(e)
                    continue
                if not data:
                    pass
                else:
                    text = [data, port_args[0], port_args[5], port_args[6]]
                    # Инициализация записи в файл и вывод на gui
                    self.thread.getData(text)
                    self.dataSort(text)
                time.sleep(1)
        except Exception as e:
            self.logWrite(f'comListen {e}')

    def dataSort(self, text):
        try:
            data = text[0]
            com = text[1]
            sens = text[2]
            types = text[3]
            timeNow = tm.now().strftime("%H:%M:%S %d-%m-%Y  ")
            if types == 'WT':
                if 'WIMWV' in data:
                    buf = data.split(',')
                    data = timeNow + com + ' ' + str(buf[1]) + ' ' + str(buf[3])
                    self.dataWrite(sens, data)
                elif 'TU' in data:
                    data = timeNow + '\n' + data
                    self.dataWrite(com + '_TU', data)
            if types == 'MAWS':
                if 'PAMWV' in data:
                    buf = data.split(',')
                    data = timeNow + com + ' ' + str(buf[1]) + ' ' + str(buf[3])
                    self.dataWrite(sens, data)
                elif 'TU' in data:
                    data = timeNow + '\n' + data
                    self.dataWrite(com + '_TU', data)
            if types == 'MILOS':
                if 'A' in data:
                    pos = data.index('A')
                    if pos <= 1:
                        buf = data[pos:]
                        if len(buf) == 6:
                            vd = buf[1:]
                            v = int(vd[:3]) / 10
                            d = int(vd[3:]) * 4.66
                            data = timeNow + com + ' ' + str(d) + ' ' + str(v)
                            self.dataWrite(sens, data)
                elif 'TU' in data:
                    buf = data[4:].split()
                    buf.insert(0, 'TU')
                    data = ','.join(buf).replace(',', ' ')
                    data = timeNow + '\n' + data
                    self.dataWrite(com + '_TU', data)
                elif 'P' in data:
                    data = timeNow + '\n' + data
                    self.dataWrite(com + '_P', data)
            if types == 'LT':
                if 'LT' in data and 'VIS' in data:
                    data = timeNow + '\n' + data
                    self.dataWrite(sens, data)
            if types == 'CL':
                if 'CT' in data:
                    data = timeNow + '\n' + data
                    self.dataWrite(sens, data)
            if types == 'PTB':
                if 'PTB' in data:
                    data = timeNow + '\n' + data
                    self.dataWrite(sens, data)
        except Exception as e:
            self.logWrite(f'dataSort {e}')

    def dataWrite(self, sens, data):
        # Запись данных с портов в файл
        try:
            if not os.path.exists('Serial'):
                os.mkdir('Serial')
            with open('Serial\\' + sens + '.dat', 'w', encoding='ANSI') as f_sens:
                f_sens.write(data)
        except Exception as e:
            self.logWrite(f'dataWrite {e}')
            pass

    def textSend(self, text):
        try:
            data = text[0]
            com = text[1]
            sens = text[2]
            # Отображение текста на Ui
            self.statText.setText(data)
            com1 = self.comBx1.currentText()
            com2 = self.comBx2.currentText()
            com3 = self.comBx3.currentText()
            com4 = self.comBx4.currentText()
            if com1 == com:
                self.comBr1.append(data)
                self.senBt1.setText(sens)
            elif com2 == com:
                self.comBr2.append(data)
                self.senBt2.setText(sens)
            elif com3 == com:
                self.comBr3.append(data)
                self.senBt3.setText(sens)
            elif com4 == com:
                self.comBr4.append(data)
                self.senBt4.setText(sens)
            if com1 == 'None':
                self.comBr1.setText(' ')
                self.senBt1.setText(' ')
            if com2 == 'None':
                self.comBr2.setText(' ')
                self.senBt2.setText(' ')
            if com3 == 'None':
                self.comBr3.setText(' ')
                self.senBt3.setText(' ')
            if com4 == 'None':
                self.comBr4.setText(' ')
                self.senBt4.setText(' ')
        except Exception as e:
            self.logWrite(f'textSend {e}  {text}')
            pass

    def portStart(self):
        try:
            self.startBt.disconnect()
            self.startBt.setText('STOP')
            self.startBt.clicked.connect(self.portStop)
            self.threadPorts()
            self.thread = Thread1()
            self.thread.slot.connect(self.textSend)
            self.thread.start()
        except Exception as e:
            self.logWrite(f'portStart {e}')

    def portStop(self):
        try:
            self.threads_stop = True
            self.startBt.disconnect()
            self.startBt.setText('START')
            self.startBt.clicked.connect(self.portStart)
        except Exception as e:
            self.logWrite(f'portStop {e}')

    def settInit(self):
        self.close()
        sett.show()

    def logWrite(self, log):
        if not os.path.exists('LOGs'):
            os.mkdir('LOGs')
        t = tm.now().strftime("%d-%m-%y %H:%M:%S")
        with open(r'LOGs\serLog.txt', 'a', encoding='utf-8') as f_rep:
            f_rep.write(t + " " + log + "\n")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


class Thread1(QThread):
    slot = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.text = "Thread start"

    def run(self):
        if self.text != "Thread start":
            self.slot.emit(self.text)

    def getData(self, data):
        self.text = data
        self.run()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sett = SerialSett()
    window = SerialWindow()
    window.show()
    sys.exit(app.exec_())
