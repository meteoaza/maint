from Maintenance_main import Sens
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer, Qt
from Weather_design import Ui_MainWindow
import sys


class Weather_main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cline = self.ui.cl1
        self.w1line = self.ui.wt1
        self.w2line = self.ui.wt2
        self.wSett()

    def wSett(self):
        with open('wconf.ini', 'r', encoding='utf-8') as f:
            self.iram = f.readline().strip()[8:]
            self.cl = f.readline().strip()[8:]
            self.wt1 = f.readline().strip()[8:]
            self.wt2 = f.readline().strip()[8:]
            self.wRun()

    def wRun(self):
        wt = [self.wt1, self.wt2]
        wline = [self.w1line, self.w2line]
        for i in range(0, 2):
            self.wt = wt[i]
            self.wline = wline[i]
            s = Sens(self.iram, "", self.cl, self.wt, '1', '0', '0')
            s.wtInit()
            s.clInit()
            self.wline.setText(s.wt_val)
            self.cline.setText(s.cl_val)
        QTimer.singleShot(3000, self.wRun)


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Weather_main()
    application.show()
    sys.exit(app.exec_())
