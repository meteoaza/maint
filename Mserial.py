import time, sys, os, serial
from winreg import *

class Serial():
    def __init__(self):
        self.stop = 1

    def settRead(self):
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        #Читаем настройки программы
        try:
            rKey = OpenKey(aReg, r"Software\IRAM\MAINT\SETT")
            self.station = QueryValueEx(rKey, 'STATION')[0]
        except Exception as e:
            print(e)
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
            print(e)
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
            print(e)
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
            self.port_t1_b = self.port_t2_b = self.port_p1_b = self.port_p2_b = '300'
            pass
        aReg.Close()
        #Присваиваем значения переменных из реестра
        if self.station == 'UCFM':
            self.s = [
                self.l1, self.l2, self.l3, self.l4, self.l5, self.l6,
                self.c1, self.c2, self.c3, self.c4, self.w1, self.w2,
                self.w3, self.w4, self.w5, self.w6, self.t1, self.t2,
                self.p1, self.p2
                ]
            self.p = [
                self.port_l1, self.port_l2, self.port_l3, self.port_l4,
                self.port_l5, self.port_l6, self.port_c1, self.port_c2,
                self.port_c3, self.port_c4, self.port_w1, self.port_w2,
                self.port_w3, self.port_w4, self.port_w5, self.port_w6,
                self.port_t1, self.port_t2, self.port_p1, self.port_p2
                ]
            self.b = [
                self.port_l1_b, self.port_l2_b, self.port_l3_b, self.port_l4_b,
                self.port_l5_b, self.port_l6_b, self.port_c1_b, self.port_c2_b,
                self.port_c3_b, self.port_c4_b, self.port_w1_b, self.port_w2_b,
                self.port_w3_b, self.port_w4_b, self.port_w5_b, self.port_w6_b,
                self.port_t1_b, self.port_t2_b, self.port_p1_b, self.port_p2_b
            ]
        else:
            self.s = [
                self.l1, self.l2, self.l3, self.l4, self.l5, self.l6,
                self.c1, self.c2, self.c3, self.c4, self.w1, self.w2,
                self.w3, self.w4, self.t1, self.t2, self.p1, self.p2
                ]
            self.p = [
                self.port_l1, self.port_l2, self.port_l3, self.port_l4,
                self.port_l5, self.port_l6, self.port_c1, self.port_c2,
                self.port_c3, self.port_c4, self.port_w1, self.port_w2,
                self.port_w3, self.port_w4, self.port_t1, self.port_t2,
                self.port_p1, self.port_p2
                ]
            self.b = [
                self.port_l1_b, self.port_l2_b, self.port_l3_b, self.port_l4_b,
                self.port_l5_b, self.port_l6_b, self.port_c1_b, self.port_c2_b,
                self.port_c3_b, self.port_c4_b, self.port_w1_b, self.port_w2_b,
                self.port_w3_b, self.port_w4_b, self.port_t1_b, self.port_t2_b,
                self.port_p1_b, self.port_p2_b
            ]
        self.portRead()

    def portRead(self):
        try:
            while True:
                for i in range(len(self.p)):
                    self.port=self.p[i]
                    self.baud=self.b[i]
                    self.sens = self.s[i]
                    if self.port != 'None' and self.baud != 'None':
                        #Настройки СОМ порта и считавание
                        ser = serial.Serial(
                            port=self.port,
                            baudrate=self.baud,
                            parity=serial.PARITY_EVEN,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.SEVENBITS,
                        )
                        self.ser = ser.readline()
                        print(self.sens + ' ' + str(self.ser))
                        ser.close()
                        self.sensWrite()
        except Exception as e:
            print(e)
            pass

    def sensWrite(self):
        try:
            if not os.path.exists('Serial'):
                os.mkdir('Serial')
            with open('Serial\\' + self.sens + '.dat', 'w', encoding='utf-8') as f_sens:
                f_sens.write(str(self.ser))
        except Exception as e:
            print(e)
            pass


if __name__ == "__main__":
    app = Serial()
    app.settRead()
