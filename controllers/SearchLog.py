'''
    SEARCH LOG CONTROLLER
'''
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport, uic
from controllers import Search, Customer, MessageBox
from models import Log as Model
from libraries import Status

class SearchLogWidget(QtWidgets.QWidget):
    ''' Component Class '''
    def __init__(self, parent=None):
        ''' Component builder method '''
        print('Controller: Modulo Log\t\t{')
        super(SearchLogWidget, self).__init__(parent)
        #Search UI
        self.searchWidget = Search.SearchWidget({ 0: 'Horário', 1: 'Usuário', 2: 'Ação'})
        self.searchWidget.lblTitle.setText('Relatório de Ações')
        self.searchWidget.btnNew.setText('EXPORTAR PDF')
        self.searchWidget.btnNew.clicked.connect(self.searchWidget.printPDF)
        self.searchWidget.btnEdit.hide()
        self.searchWidget.btnRem.hide()
        #Add/Set Widget in Layout
        self.layout = QtWidgets.QStackedLayout()
        self.layout.addWidget(self.searchWidget)
        self.setLayout(self.layout)
        print('Controller: Modulo Log\t\t}')

    ''' Methods to connect with the signals '''  
    def showSearch(self):
        ''' Displays the search form component '''
        Status.statusVoid(self.searchWidget.lblStatus)
        self.searchWidget.searchResultSet(Model.get())
        self.layout.setCurrentWidget(self.searchWidget)