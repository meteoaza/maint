# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutFrame(object):
    def setupUi(self, AboutFrame):
        AboutFrame.setObjectName("AboutFrame")
        AboutFrame.resize(402, 185)
        self.about = QtWidgets.QTextBrowser(AboutFrame)
        self.about.setGeometry(QtCore.QRect(20, 20, 371, 141))
        self.about.setMaximumSize(QtCore.QSize(371, 141))
        self.about.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.about.setObjectName("about")

        self.retranslateUi(AboutFrame)
        QtCore.QMetaObject.connectSlotsByName(AboutFrame)

    def retranslateUi(self, AboutFrame):
        _translate = QtCore.QCoreApplication.translate
        AboutFrame.setWindowTitle(_translate("AboutFrame", "About"))
        self.about.setHtml(_translate("AboutFrame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Maintenance made specially for engeneers by Meteoaza</span></p></body></html>"))


