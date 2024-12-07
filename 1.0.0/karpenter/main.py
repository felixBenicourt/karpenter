# -*- encoding: utf-8 -*-
"""
Module with launch functions
"""



import karpenterWindow
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import CONSTANTS
import ctypes



if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    app_icon = QIcon(f'{CONSTANTS.rootProject}/icons/karpenter_icone.png')
    app.setWindowIcon(app_icon)
    
    if hasattr(ctypes, 'windll'):
        myappid = 'karpenter'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    window = karpenterWindow.MainUI()
    window.show()
    sys.exit(app.exec_())


