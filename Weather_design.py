# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Weather_design.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setWindowModality(QtCore.Qt.WindowModal)
        Frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QtCore.QSize(1092, 598))
        Frame.setMaximumSize(QtCore.QSize(1092, 598))
        Frame.setSizeIncrement(QtCore.QSize(0, 0))
        Frame.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Frame.setFont(font)
        Frame.setMouseTracking(True)
        Frame.setFocusPolicy(QtCore.Qt.StrongFocus)
        Frame.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        Frame.setAutoFillBackground(False)
        Frame.setStyleSheet("border-color: rgb(41, 255, 76);\n"
"background-color: rgb(17, 77, 218);")
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        Frame.setLineWidth(2)
        Frame.setMidLineWidth(1)
        self.gridLayoutWidget = QtWidgets.QWidget(Frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 120, 1071, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.cl1 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cl1.sizePolicy().hasHeightForWidth())
        self.cl1.setSizePolicy(sizePolicy)
        self.cl1.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.cl1.setFont(font)
        self.cl1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cl1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cl1.setText("")
        self.cl1.setAlignment(QtCore.Qt.AlignCenter)
        self.cl1.setObjectName("cl1")
        self.gridLayout.addWidget(self.cl1, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.wt2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wt2.sizePolicy().hasHeightForWidth())
        self.wt2.setSizePolicy(sizePolicy)
        self.wt2.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.wt2.setFont(font)
        self.wt2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wt2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wt2.setText("")
        self.wt2.setAlignment(QtCore.Qt.AlignCenter)
        self.wt2.setObjectName("wt2")
        self.gridLayout.addWidget(self.wt2, 3, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.wt1 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wt1.sizePolicy().hasHeightForWidth())
        self.wt1.setSizePolicy(sizePolicy)
        self.wt1.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.wt1.setFont(font)
        self.wt1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wt1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wt1.setText("")
        self.wt1.setAlignment(QtCore.Qt.AlignCenter)
        self.wt1.setObjectName("wt1")
        self.gridLayout.addWidget(self.wt1, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(300, 15))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.wt1.raise_()
        self.wt2.raise_()
        self.cl1.raise_()
        self.label_1.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.l_time = QtWidgets.QLabel(Frame)
        self.l_time.setGeometry(QtCore.QRect(781, 20, 300, 50))
        self.l_time.setMinimumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.l_time.setFont(font)
        self.l_time.setFrameShape(QtWidgets.QFrame.Box)
        self.l_time.setLineWidth(3)
        self.l_time.setText("")
        self.l_time.setAlignment(QtCore.Qt.AlignCenter)
        self.l_time.setObjectName("l_time")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Weather"))
        self.label_2.setText(_translate("Frame", "Ветер"))
        self.label_1.setText(_translate("Frame", "Облачность"))
        self.label_3.setText(_translate("Frame", "DDD             FF"))


