'''
    MENU CONTROLLER
'''
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from controllers import SearchCustomers, SearchWorkers, SearchLog, MessageBox
from libraries import Status
from models import Customer, Worker, Log

class MenuWidget(QtWidgets.QWidget):
    ''' Component Class '''
    def __init__(self, session, parent=None):
        ''' Component builder method '''
        print('Controller: Menu\t\t{')
        super(MenuWidget, self).__init__(parent)
        uic.loadUi('views/menu.ui', self)
        self.txtSearch.textChanged.connect(self.searchElement)
        #Load UIs
        self.dashboardWidget = uic.loadUi('views/dashboard.ui')
        self.customersWidget = SearchCustomers.SearchCustomersWidget(session)
        self.workersWidget = SearchWorkers.SearchWorkersWidget(session)
        self.reportsWidget = SearchLog.SearchLogWidget()
        self.aboutWidget = uic.loadUi('views/about.ui')
        #Connect Signals
        self.btnDashboard.clicked.connect(self.showWidgetDashboard)
        self.btnCustomers.clicked.connect(self.showWidgetCustomers)
        self.btnWorkers.clicked.connect(self.showWidgetWorkers)
        self.btnReports.clicked.connect(self.showWidgetReports)
        self.btnAbout.clicked.connect(self.showWidgetAbout)
        #MessageBox
        self.msgBox = MessageBox.MessageBoxWidget(self, 'Confirmar saída', "Deseja realmente encerrar sua sessão?")
        #Add/Set Widget in Layout
        self.content.addWidget(self.dashboardWidget)
        self.content.addWidget(self.customersWidget)
        self.content.addWidget(self.workersWidget)
        self.content.addWidget(self.reportsWidget)
        self.content.addWidget(self.aboutWidget)
        self.content.setCurrentWidget(self.dashboardWidget)
        print('Controller: Menu\t\t}')

    ''' Methods to connect with the signals '''
    def showWidgetDashboard(self):
        ''' Displays the dashboard component '''
        self.content.setCurrentWidget(self.dashboardWidget) 

    def showWidgetCustomers(self):
        ''' Displays the customers component '''
        self.btnCustomers.setChecked(True)
        self.customersWidget.showSearch()
        Status.statusVoid(self.customersWidget.searchWidget.lblStatus)
        self.content.setCurrentWidget(self.customersWidget) 

    def showWidgetWorkers(self):
        ''' Displays the workers component '''
        self.workersWidget.showSearch()
        Status.statusVoid(self.workersWidget.searchWidget.lblStatus)
        self.content.setCurrentWidget(self.workersWidget) 

    def showWidgetReports(self):
        ''' Displays the reports component '''
        self.reportsWidget.showSearch()
        self.content.setCurrentWidget(self.reportsWidget)

    def showWidgetAbout(self):
        ''' Displays the about component '''
        self.content.setCurrentWidget(self.aboutWidget)
    
    def searchElement(self):
        ''' Dynamic search of elements '''
        key = self.txtSearch.text()
        if self.btnWorkers.isChecked():
            table = self.workersWidget.searchWidget
            model = Worker.get()
        elif self.btnReports.isChecked():
            table = self.reportsWidget.searchWidget
            model = Log.get()
        else:
            table = self.customersWidget.searchWidget
            model = Customer.get()
            if key != '':
                self.showWidgetCustomers()
        table.searchResultSet(model,key)
