'''
    WORKER CONTROLLER
'''
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from datetime import datetime

class WorkerWidget(QtWidgets.QWidget):
    ''' Component Class '''
    def __init__(self, parent=None):
        ''' Component builder method '''
        print('Controller: Worker', end='\t\t')
        super(WorkerWidget, self).__init__(parent)
        uic.loadUi("views/workers.ui", self)
        print('OK')

    ''' Methods to connect with the signals '''
    def getFields(self):
        ''' Returns form fields '''
        if self.lblIdentifier.text() == '':
            identifier = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            identifier = self.lblIdentifier.text()
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        email = self.txtEmail.text()
        privillege = self.cbPrivillege.currentText()
        current = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return (identifier, username, password, email, privillege, current)
        
    def setFields(self, worker):
        ''' Assigns form fields '''
        self.lblTitle.setText('Alteração de Funcionário')
        self.txtUsername.setText(worker[1])
        self.txtPassword.setText(worker[2])
        self.txtEmail.setText(worker[3])
        self.cbPrivillege.setCurrentText(worker[4]) 
        self.lblIdentifier.setText(worker[0])    

    def clearFields(self):
        ''' Clears form fields '''
        self.txtUsername.setText('')
        self.txtPassword.setText('')
        self.txtEmail.setText('')
        self.cbPrivillege.setCurrentIndex(0)
        self.lblIdentifier.setText('')  
