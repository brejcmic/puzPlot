# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sam.ui'
#
# Created: Fri Jan 26 16:11:12 2018
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 336)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("iconaSAM.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 210, 291, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 250, 91, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 291, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 250, 41, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 250, 41, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 250, 41, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 250, 41, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(320, 10, 301, 231))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuVolba_Postavy = QtGui.QMenu(self.menubar)
        self.menuVolba_Postavy.setObjectName(_fromUtf8("menuVolba_Postavy"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionTechnik = QtGui.QAction(MainWindow)
        self.actionTechnik.setObjectName(_fromUtf8("actionTechnik"))
        self.actionPilot = QtGui.QAction(MainWindow)
        self.actionPilot.setObjectName(_fromUtf8("actionPilot"))
        self.actionDustojnik = QtGui.QAction(MainWindow)
        self.actionDustojnik.setObjectName(_fromUtf8("actionDustojnik"))
        self.actionPoradce = QtGui.QAction(MainWindow)
        self.actionPoradce.setObjectName(_fromUtf8("actionPoradce"))
        self.actionVedec = QtGui.QAction(MainWindow)
        self.actionVedec.setObjectName(_fromUtf8("actionVedec"))
        self.menuVolba_Postavy.addAction(self.actionTechnik)
        self.menuVolba_Postavy.addAction(self.actionPilot)
        self.menuVolba_Postavy.addAction(self.actionDustojnik)
        self.menuVolba_Postavy.addAction(self.actionPoradce)
        self.menuVolba_Postavy.addAction(self.actionVedec)
        self.menubar.addAction(self.menuVolba_Postavy.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Answering Machine", None))
        self.pushButton.setText(_translate("MainWindow", "Odeslat", None))
        self.pushButton_2.setText(_translate("MainWindow", "1", None))
        self.pushButton_3.setText(_translate("MainWindow", "2", None))
        self.pushButton_4.setText(_translate("MainWindow", "3", None))
        self.pushButton_5.setText(_translate("MainWindow", "4", None))
        self.menuVolba_Postavy.setTitle(_translate("MainWindow", "Volba Postavy", None))
        self.actionTechnik.setText(_translate("MainWindow", "Technik", None))
        self.actionPilot.setText(_translate("MainWindow", "Pilot", None))
        self.actionDustojnik.setText(_translate("MainWindow", "Dustojnik", None))
        self.actionPoradce.setText(_translate("MainWindow", "Poradce", None))
        self.actionVedec.setText(_translate("MainWindow", "Vedec", None))

