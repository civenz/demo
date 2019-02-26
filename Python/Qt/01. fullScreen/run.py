# -*- coding: utf-8 -*-

import sys
from PySide2 import QtWidgets

from init import MyMainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)

    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
