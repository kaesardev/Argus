'''
    LAUNCHER
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from controllers import Authenticate

app = None

def main():
    print('------- Argus Application -------')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Authenticate.Authenticate()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()