# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(529, 428)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icons8-settings-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings.setWindowIcon(icon)
        Settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalLayoutWidget = QtWidgets.QWidget(Settings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 0, 511, 109))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setMaximumSize(QtCore.QSize(500, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.lineSND = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineSND.setObjectName("lineSND")
        self.gridLayout.addWidget(self.lineSND, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineIRAM = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineIRAM.setObjectName("lineIRAM")
        self.gridLayout.addWidget(self.lineIRAM, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineFileT = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineFileT.setObjectName("lineFileT")
        self.gridLayout.addWidget(self.lineFileT, 2, 1, 1, 1)
        self.buttonOK = QtWidgets.QDialogButtonBox(Settings)
        self.buttonOK.setGeometry(QtCore.QRect(360, 370, 156, 23))
        self.buttonOK.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonOK.setObjectName("buttonOK")

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Настройки"))
        self.label.setText(_translate("Settings", "Путь к папке IRAM"))
        self.label_2.setText(_translate("Settings", "Путь к WAV файлу"))
        self.label_3.setText(_translate("Settings", "Время ожидания файла"))


