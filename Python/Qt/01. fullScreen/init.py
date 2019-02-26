# -*- coding: utf-8 -*-

## All Qt Modules - http://doc.qt.io/qt-5/qtmodules.html
## QtWidgets    - http://doc.qt.io/qt-5/qtwidgets-module.html
## QtCore       - http://doc.qt.io/qt-5/qtcore-module.html
## QtGui        - http://doc.qt.io/qt-5/qtgui-module.html

## 语言国际化设计参考 https://www.cnblogs.com/ibingshan/p/9965139.html

import sys
from PySide2 import QtWidgets, QtCore

## 引用设计好的 UI [fullScreen.py] ##
import fullScreen as ui

class MyMainWindow(QtWidgets.QMainWindow, ui.Ui_Form):

    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.initUI()

        self.setStyleSheet("background-color: #ffffff; border-image:url(./test.jpg) no-repeat;")
        self.pushButton.setStyleSheet("background-color: #ffffff; border: 1px solid red; border-image: none;")

        ## 窗口水平居中显示 ##
        self.desktop_width = QtWidgets.QApplication.desktop().width()
        self.desktop_height = QtWidgets.QApplication.desktop().height()
        self.move((self.desktop_width-self.width())/2,(self.desktop_height-self.height())/3)
        ## 全屏
        self.showFullScreen()

    def resizeEvent(self, *args):
        ## 按键 水平居中 | 垂直固定底部 
        self.pushButton.move((self.width()-self.pushButton.width())/2, (self.height()-self.pushButton.height())/2 )


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            print('hello')
            ##QDialogButtonBox
            ##self.close()

    def initUI(self):
        self.pushButton.clicked.connect(QtCore.QCoreApplication.quit)
