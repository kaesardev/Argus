'''
    AUTHENTICATE CONTROLLER
'''
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from libraries import Status, Session, Email
from controllers import Menu, MessageBox
from models import Worker, Log

class Authenticate(QtWidgets.QMainWindow):
    ''' Component Class '''
    def setupUi(self, MainWindow):
        ''' UI initialization method '''
        print('Controller: Authenticate\t{')
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Argus")
        MainWindow.setWindowIcon(QtGui.QIcon('resources/favicon.ico'))
        MainWindow.resize(950, 550)
        #Login UI
        self.loginWidget = uic.loadUi('views/login.ui')
        self.loginWidget.txtUsername.returnPressed.connect(self.authenticate)
        self.loginWidget.txtPassword.returnPressed.connect(self.authenticate)
        self.loginWidget.btnLogin.clicked.connect(self.authenticate)
        self.loginWidget.btnRecover.clicked.connect(self.showWidgetRecover)
        #Recover UI
        self.recoverWidget = uic.loadUi("views/recover.ui")
        self.recoverWidget.btnRecover.clicked.connect(self.recover)
        self.recoverWidget.btnLogin.clicked.connect(self.showWidgetLogin)
        #Session
        self.session = Session.Session()
        #Menu UI
        self.menuWidget = Menu.MenuWidget(self.session)
        self.menuWidget.btnLogout.clicked.connect(self.logout)
        #Add/Set Widget in Layout
        self.centralWidget = QtWidgets.QStackedWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.addWidget(self.loginWidget)
        self.centralWidget.addWidget(self.recoverWidget)
        self.centralWidget.addWidget(self.menuWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        print('Controller: Authenticate\t}')

    ''' Methods to connect with the signals '''
    def showWidgetRecover(self):
        ''' Displays the recovery component '''
        self.recoverWidget.txtUsername.setText(self.loginWidget.txtUsername.text())
        self.centralWidget.setCurrentWidget(self.recoverWidget)
        Status.statusVoid(self.recoverWidget.lblStatus)

    def showWidgetLogin(self):
        ''' Displays the login component '''
        self.loginWidget.txtUsername.setText(self.recoverWidget.txtUsername.text())
        self.centralWidget.setCurrentWidget(self.loginWidget)
        Status.statusVoid(self.loginWidget.lblStatus)

    def authenticate(self):
        ''' Verifies that the user's credentials are authentic '''
        username = self.loginWidget.txtUsername.text()
        password = self.loginWidget.txtPassword.text()
        workers = Worker.get()
        for key in workers.keys():
            if username == workers[key][1] and password == workers[key][2]:
                self.session.setSession(workers[key][1], workers[key][4])
        logged, username, privillege = self.session.getSession()
        if logged == True:
            self.menuWidget.btnProfile.setText(username.capitalize())
            self.menuWidget.showWidgetDashboard()
            self.menuWidget.btnDashboard.setChecked(True)
            if privillege == 'Básico':
                self.menuWidget.btnReports.hide()
                self.menuWidget.btnWorkers.hide()
            elif privillege == 'Gerente':
                self.menuWidget.btnReports.show()
                self.menuWidget.btnWorkers.hide()
            elif privillege == 'Administrador':
                self.menuWidget.btnReports.show()
                self.menuWidget.btnWorkers.show()
            self.centralWidget.setCurrentWidget(self.menuWidget)
            Log.add(username, 'Iniciou sessão no sistema')
        else:
            Status.statusWarning(self.loginWidget.lblStatus, 'Usuário e/ou senha não coincidem!')
    
    def recover(self):
        ''' Retrieve user credentials '''
        username = self.recoverWidget.txtUsername.text()
        email = self.recoverWidget.txtEmail.text()
        worker = None
        workers = Worker.get()
        for key in workers.keys():
            if username == workers[key][1] and email == workers[key][3]:
                worker = workers[key]
        if worker != None:
            from_addr = 'argus@email.com' 
            to_addr_list = [worker[3]]
            cc_addr_list = []
            subject = 'Argus - Recuperação de senha'
            message = 'Olá,' + worker[1] + '\nSua senha no sistema Argus é: ' + worker[2] + '\n\nEmail automático não responder!'
            login = 'argus'
            password = '*******'
            try:
                Email.sendemail(from_addr, to_addr_list, cc_addr_list, subject, message, login, password)
                Status.statusSuccess(self.recoverWidget.lblStatus, 'Verifique sua caixa de entrada!')
            except:
                Status.statusWarning(self.recoverWidget.lblStatus, 'Servidor de email não responde!')
        else:
            Status.statusWarning(self.recoverWidget.lblStatus, 'Usuário e/ou email não coincidem!')

    def logout(self):
        ''' Logs off the authenticated user session '''
        response = self.menuWidget.msgBox.getResponse()
        if response == QtWidgets.QMessageBox.Yes:
            Log.add(self.session.getSession()[1], 'Encerrou sessão no sistema')
            self.session.delSession()
            self.loginWidget.txtPassword.setText('')
            self.centralWidget.setCurrentWidget(self.loginWidget)
            Status.statusSuccess(self.loginWidget.lblStatus, 'Sessão encerrada com sucesso!') 
