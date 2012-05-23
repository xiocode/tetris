# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tetris.ui'
#
# Created: Mon May 21 22:48:37 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 586)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(300, 10, 75, 23))
        self.startButton.setObjectName("startButton")
        self.pauseButton = QtGui.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(300, 50, 75, 23))
        self.pauseButton.setObjectName("pauseButton")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 251, 571))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.score_panel = QtGui.QFrame(self.centralwidget)
        self.score_panel.setGeometry(QtCore.QRect(260, 90, 151, 301))
        self.score_panel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.score_panel.setFrameShadow(QtGui.QFrame.Raised)
        self.score_panel.setObjectName("score_panel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("MainWindow", "开始", None, QtGui.QApplication.UnicodeUTF8))
        self.pauseButton.setText(QtGui.QApplication.translate("MainWindow", "暂定", None, QtGui.QApplication.UnicodeUTF8))

