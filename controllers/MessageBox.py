'''
    SEARCH CUSTOMERS CONTROLLER
'''
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from libraries import Theme

class MessageBoxWidget(QtWidgets.QMessageBox):
    ''' Component Class '''
    def __init__(self, parent=None, title='', text=''):
        ''' Component builder method '''
        print('Controller: MessageBox', end='\t\t')
        super(MessageBoxWidget, self).__init__(parent)
        #self.setStyleSheet(Theme.getStyle('form'))
        self.setIcon(QtWidgets.QMessageBox.Question)
        self.setWindowTitle(title)
        self.setText(text)
        self.setStyleSheet('QMessageBox QLabel{ background-color: #2c3e50; color: #ecf0f1; font-family: Roboto;	font-size: 14px; }')
        self.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        btnYes = self.button(QtWidgets.QMessageBox.Yes)
        btnYes.setObjectName('btnWarning')
        btnYes.setText('SIM')
        btnNo = self.button(QtWidgets.QMessageBox.No)
        btnNo.setObjectName('btnInformative')
        btnNo.setText('NÃO')
        print('OK')
        
    ''' Methods '''
    def getResponse(self):
        ''' Returns the result of the message box '''
        return self.exec_()
