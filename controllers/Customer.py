'''
    CUSTOMER CONTROLLER
'''
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from models import City, State
from libraries import BubbleSort
from datetime import datetime

class CustomerWidget(QtWidgets.QWidget):
    ''' Component Class '''
    def __init__(self, parent=None):
        ''' Component builder method '''
        print('Controller: Customer', end='\t\t')
        super(CustomerWidget, self).__init__(parent)
        #Load UI
        uic.loadUi("views/customers.ui", self)
        #Load States
        self.cbState.clear()
        states = State.get()
        states = BubbleSort.bubbleSort(states)
        for state in states:
            self.cbState.addItem(state)
        #Load Cities
        self.updateCities()
        #Connect Signals
        self.cbState.currentIndexChanged.connect(self.updateCities)
        print('OK')
        
    ''' Methods to connect with the signals '''
    def getFields(self):
        ''' Returns form fields '''
        if self.lblIdentifier.text() == '':
            identifier = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            identifier = self.lblIdentifier.text()
        fullname = self.txtFullname.text()
        cpf = self.txtCpf.text()
        phone = self.txtPhone.text()
        gender = self.cbGender.currentText()
        birthday = self.dtBirthday.date().toPyDate().strftime("%Y-%m-%d")
        street = self.txtStreet.text()
        number = self.txtNumber.text()
        complement = self.txtComplement.text()
        district = self.txtDistrict.text()
        state = self.cbState.currentText()
        city = self.cbCity.currentText()
        current = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return (identifier, cpf, fullname, phone, birthday, gender, street, number, complement, district, state, city, current)
        
    def setFields(self, customer):
        ''' Assigns form fields '''
        self.lblTitle.setText('Alteração de Cliente')
        self.txtCpf.setText(customer[1])
        self.txtFullname.setText(customer[2])
        self.txtPhone.setText(customer[3])
        self.dtBirthday.setDateTime(QtCore.QDateTime(QtCore.QDate.fromString(customer[4], 'yyyy-MM-dd')))
        self.cbGender.setCurrentText(customer[5])
        self.txtStreet.setText(customer[6])
        self.txtNumber.setText(customer[7])
        self.txtComplement.setText(customer[8])
        self.txtDistrict.setText(customer[9])
        self.cbState.setCurrentText(customer[10])
        self.cbCity.setCurrentText(customer[11]) 
        self.lblIdentifier.setText(customer[0])

    def clearFields(self):
        ''' Clears form fields '''
        self.txtCpf.setText('')
        self.txtFullname.setText('')
        self.txtPhone.setText('')
        self.dtBirthday.setDateTime(QtCore.QDateTime.currentDateTime())
        self.cbGender.setCurrentIndex(0)
        self.txtStreet.setText('')
        self.txtNumber.setText('')
        self.txtComplement.setText('')
        self.txtDistrict.setText('')
        self.cbState.setCurrentText('PE')
        self.cbCity.setCurrentText('Recife')
        self.lblIdentifier.setText('')

    def updateCities(self):
        ''' Updates cities from the combobox '''
        self.cbCity.clear()
        cities = City.get(self.cbState.currentText())
        cities = BubbleSort.bubbleSort(cities)
        for city in cities:
            self.cbCity.addItem(city)
