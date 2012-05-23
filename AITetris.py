##!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Tony.Shao'

import sys
from PySide import QtCore, QtGui

class Tetris(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
    def initUI(self):
        self.setGeometry(100, 100, 400, 600)
        self.setWindowTitle("AI Tetris")
        self.centralWidget = QtGui.QWidget()
        self.centralWidget.setObjectName("centralWidget")
        self.startButton = QtGui.QPushButton(self.centralWidget)
        self.startButton.setGeometry(QtCore.QRect(300, 10, 75, 23))
        self.startButton.setObjectName("startButton")
        self.pauseButton = QtGui.QPushButton(self.centralWidget)
        self.pauseButton.setGeometry(QtCore.QRect(300, 50, 75, 23))
        self.pauseButton.setObjectName("pauseButton")
        self.main_frame = QtGui.QFrame(self.centralWidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 251, 571))
        self.main_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.score_frame = QtGui.QFrame(self.centralWidget)
        self.score_frame.setGeometry(QtCore.QRect(260, 90, 151, 301))
        self.score_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.score_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.score_frame.setObjectName("score_frame")

        self.setCentralWidget(self.centralWidget)
        self.retranslateUI()
        self.show()

    def retranslateUI(self):
        self.setWindowTitle(QtGui.QApplication.translate("AI Tetris", "AI Tetris", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("startButton", "开始", None, QtGui.QApplication.UnicodeUTF8))
        self.pauseButton.setText(QtGui.QApplication.translate("pauseButton", "暂定", None, QtGui.QApplication.UnicodeUTF8))

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Tetris()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

