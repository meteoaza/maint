# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings_design.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(731, 831)
        Settings.setMaximumSize(QtCore.QSize(731, 831))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/icons/icons8-settings-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings.setWindowIcon(icon)
        Settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gridLayout_2 = QtWidgets.QGridLayout(Settings)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Settings)
        self.label_3.setMinimumSize(QtCore.QSize(180, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.viewSensors = QtWidgets.QTextBrowser(Settings)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.viewSensors.setFont(font)
        self.viewSensors.setObjectName("viewSensors")
        self.horizontalLayout_3.addWidget(self.viewSensors)
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)
        self.label_0 = QtWidgets.QLabel(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_0.sizePolicy().hasHeightForWidth())
        self.label_0.setSizePolicy(sizePolicy)
        self.label_0.setMinimumSize(QtCore.QSize(180, 0))
        self.label_0.setMaximumSize(QtCore.QSize(500, 30))
        self.label_0.setObjectName("label_0")
        self.gridLayout.addWidget(self.label_0, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineAV6 = QtWidgets.QLineEdit(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineAV6.sizePolicy().hasHeightForWidth())
        self.lineAV6.setSizePolicy(sizePolicy)
        self.lineAV6.setMinimumSize(QtCore.QSize(0, 20))
        self.lineAV6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineAV6.setObjectName("lineAV6")
        self.horizontalLayout_5.addWidget(self.lineAV6, 0, QtCore.Qt.AlignLeft)
        self.label = QtWidgets.QLabel(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.lineAVtime1 = QtWidgets.QLineEdit(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineAVtime1.sizePolicy().hasHeightForWidth())
        self.lineAVtime1.setSizePolicy(sizePolicy)
        self.lineAVtime1.setMinimumSize(QtCore.QSize(0, 20))
        self.lineAVtime1.setObjectName("lineAVtime1")
        self.horizontalLayout_5.addWidget(self.lineAVtime1, 0, QtCore.Qt.AlignLeft)
        self.lineAVtime2 = QtWidgets.QLineEdit(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineAVtime2.sizePolicy().hasHeightForWidth())
        self.lineAVtime2.setSizePolicy(sizePolicy)
        self.lineAVtime2.setMinimumSize(QtCore.QSize(0, 20))
        self.lineAVtime2.setObjectName("lineAVtime2")
        self.horizontalLayout_5.addWidget(self.lineAVtime2, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label_8 = QtWidgets.QLabel(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(110, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.checkAv6 = QtWidgets.QCheckBox(Settings)
        self.checkAv6.setMinimumSize(QtCore.QSize(0, 15))
        self.checkAv6.setText("")
        self.checkAv6.setObjectName("checkAv6")
        self.horizontalLayout_5.addWidget(self.checkAv6, 0, QtCore.Qt.AlignRight)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Settings)
        self.label_4.setMinimumSize(QtCore.QSize(180, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_1 = QtWidgets.QLabel(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setMinimumSize(QtCore.QSize(180, 0))
        self.label_1.setMaximumSize(QtCore.QSize(500, 30))
        self.label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineTimer = QtWidgets.QLineEdit(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineTimer.sizePolicy().hasHeightForWidth())
        self.lineTimer.setSizePolicy(sizePolicy)
        self.lineTimer.setMinimumSize(QtCore.QSize(40, 15))
        self.lineTimer.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineTimer.setObjectName("lineTimer")
        self.horizontalLayout_8.addWidget(self.lineTimer, 0, QtCore.Qt.AlignLeft)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.label_6 = QtWidgets.QLabel(Settings)
        self.label_6.setMinimumSize(QtCore.QSize(110, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.checkSerial = QtWidgets.QCheckBox(Settings)
        self.checkSerial.setEnabled(True)
        self.checkSerial.setMinimumSize(QtCore.QSize(0, 15))
        self.checkSerial.setText("")
        self.checkSerial.setCheckable(True)
        self.checkSerial.setChecked(False)
        self.checkSerial.setTristate(False)
        self.checkSerial.setObjectName("checkSerial")
        self.horizontalLayout_8.addWidget(self.checkSerial, 0, QtCore.Qt.AlignRight)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineFileT = QtWidgets.QLineEdit(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineFileT.sizePolicy().hasHeightForWidth())
        self.lineFileT.setSizePolicy(sizePolicy)
        self.lineFileT.setMinimumSize(QtCore.QSize(40, 15))
        self.lineFileT.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineFileT.setObjectName("lineFileT")
        self.horizontalLayout_7.addWidget(self.lineFileT, 0, QtCore.Qt.AlignLeft)
        spacerItem8 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.label_5 = QtWidgets.QLabel(Settings)
        self.label_5.setMinimumSize(QtCore.QSize(110, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.checkRepW = QtWidgets.QCheckBox(Settings)
        self.checkRepW.setMinimumSize(QtCore.QSize(0, 15))
        self.checkRepW.setText("")
        self.checkRepW.setObjectName("checkRepW")
        self.horizontalLayout_7.addWidget(self.checkRepW, 0, QtCore.Qt.AlignRight)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineStation = QtWidgets.QLabel(Settings)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineStation.setFont(font)
        self.lineStation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lineStation.setText("")
        self.lineStation.setAlignment(QtCore.Qt.AlignCenter)
        self.lineStation.setObjectName("lineStation")
        self.horizontalLayout_4.addWidget(self.lineStation)
        self.boxStation = QtWidgets.QComboBox(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxStation.sizePolicy().hasHeightForWidth())
        self.boxStation.setSizePolicy(sizePolicy)
        self.boxStation.setObjectName("boxStation")
        self.horizontalLayout_4.addWidget(self.boxStation)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Settings)
        self.label_2.setMinimumSize(QtCore.QSize(180, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineIRAM = QtWidgets.QLineEdit(Settings)
        self.lineIRAM.setMinimumSize(QtCore.QSize(0, 15))
        self.lineIRAM.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineIRAM.setObjectName("lineIRAM")
        self.gridLayout.addWidget(self.lineIRAM, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.boxSensors = QtWidgets.QComboBox(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxSensors.sizePolicy().hasHeightForWidth())
        self.boxSensors.setSizePolicy(sizePolicy)
        self.boxSensors.setMinimumSize(QtCore.QSize(80, 0))
        self.boxSensors.setObjectName("boxSensors")
        self.horizontalLayout_2.addWidget(self.boxSensors)
        spacerItem13 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.lineSensors = QtWidgets.QLineEdit(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineSensors.sizePolicy().hasHeightForWidth())
        self.lineSensors.setSizePolicy(sizePolicy)
        self.lineSensors.setMinimumSize(QtCore.QSize(80, 15))
        self.lineSensors.setObjectName("lineSensors")
        self.horizontalLayout_2.addWidget(self.lineSensors)
        self.buttSensors = QtWidgets.QPushButton(Settings)
        self.buttSensors.setObjectName("buttSensors")
        self.horizontalLayout_2.addWidget(self.buttSensors)
        spacerItem14 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(180, 0))
        self.label_7.setMaximumSize(QtCore.QSize(500, 30))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineSND = QtWidgets.QLineEdit(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineSND.sizePolicy().hasHeightForWidth())
        self.lineSND.setSizePolicy(sizePolicy)
        self.lineSND.setMinimumSize(QtCore.QSize(270, 15))
        self.lineSND.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineSND.setObjectName("lineSND")
        self.horizontalLayout_9.addWidget(self.lineSND)
        spacerItem16 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        spacerItem17 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem17)
        self.label_9 = QtWidgets.QLabel(Settings)
        self.label_9.setMinimumSize(QtCore.QSize(110, 0))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter)
        self.checkSensW = QtWidgets.QCheckBox(Settings)
        self.checkSensW.setMinimumSize(QtCore.QSize(0, 15))
        self.checkSensW.setText("")
        self.checkSensW.setObjectName("checkSensW")
        self.horizontalLayout_9.addWidget(self.checkSensW, 0, QtCore.Qt.AlignRight)
        spacerItem18 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem18)
        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 6, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.buttHelp = QtWidgets.QPushButton(Settings)
        self.buttHelp.setObjectName("buttHelp")
        self.gridLayout_2.addWidget(self.buttHelp, 1, 0, 1, 1)
        self.buttOK = QtWidgets.QDialogButtonBox(Settings)
        self.buttOK.setMaximumSize(QtCore.QSize(630, 23))
        self.buttOK.setFocusPolicy(QtCore.Qt.TabFocus)
        self.buttOK.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttOK.setCenterButtons(False)
        self.buttOK.setObjectName("buttOK")
        self.gridLayout_2.addWidget(self.buttOK, 1, 1, 1, 1)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)
        Settings.setTabOrder(self.buttOK, self.lineIRAM)
        Settings.setTabOrder(self.lineIRAM, self.lineSensors)
        Settings.setTabOrder(self.lineSensors, self.buttSensors)
        Settings.setTabOrder(self.buttSensors, self.viewSensors)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Настройки"))
        self.label_3.setText(_translate("Settings", "Время ожидания файла (мин)"))
        self.label_0.setText(_translate("Settings", "Выбор Станции"))
        self.label.setText(_translate("Settings", "Время записи АВ-6"))
        self.label_8.setText(_translate("Settings", "Запись АВ-6"))
        self.label_4.setText(_translate("Settings", "Время обновления опроса (мсек)"))
        self.label_1.setText(_translate("Settings", "Путь к папке IRAM"))
        self.label_6.setText(_translate("Settings", "Mserial"))
        self.label_5.setText(_translate("Settings", "Запись Report файла"))
        self.label_2.setText(_translate("Settings", "Путь к WAV файлу"))
        self.buttSensors.setText(_translate("Settings", "Добавить"))
        self.label_7.setText(_translate("Settings", "Путь к архиву АВ-6"))
        self.label_9.setText(_translate("Settings", "Запись Sens файла"))
        self.buttHelp.setText(_translate("Settings", "Help"))


