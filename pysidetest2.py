#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Tony.Shao'

import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setWindowTitle("Test")
        self.setToolTip("Test2")
        btn = QtGui.QPushButton("Button",self)
        btn.setToolTip("This is a <b>QPushButton</b> widge")

        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        btn.resize(btn.sizeHint())

        btn.move(150, 50)



        self.setGeometry(300, 300, 300, 300)
        self.setWindowIcon(QtGui.QIcon("image/Test.png"))
        self.show()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox(self,"提示","关闭了啊？",  QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
        app = QtGui.QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()