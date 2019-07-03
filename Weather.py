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
        self.wline = self.ui.wt1
        self.wSett()

    def wSett(self):
        with open('wconf.ini', 'r', encoding='utf-8') as f:
            self.iram = f.readline().strip()[8:]
            self.cl = f.readline().strip()[8:]
            self.wt = f.readline().strip()[8:]
            self.wRun()

    def wRun(self):
        s = Sens(self.iram, "", self.cl, self.wt, '1', '0', '0')
        s.clInit()
        s.wtInit()
        self.cline.setText(s.cl_val)
        self.wline.setText(s.wt_val)
        QTimer.singleShot(1000, self.wRun)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Weather_main()
    application.show()
    sys.exit(app.exec_())
