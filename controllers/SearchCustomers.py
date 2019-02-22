'''
    SEARCH CUSTOMERS CONTROLLER
'''
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from controllers import Search, Customer, MessageBox
from models import Log, Customer as Model
from libraries import Status

class SearchCustomersWidget(QtWidgets.QWidget):
    ''' Component Class '''
    def __init__(self, session, parent=None):
        ''' Component builder method '''
        print('Controller: Modulo Customers\t{')
        super(SearchCustomersWidget, self).__init__(parent)
        self.session = session
        #Search UI
        self.searchWidget = Search.SearchWidget({ 1: 'CPF', 2: 'Nome', 3: 'Telefone', 12: 'Modificado em', 0: 'Criado em' })
        self.searchWidget.lblTitle.setText('Consulta de Clientes')
        self.searchWidget.btnNew.clicked.connect(self.showFormReg)
        self.searchWidget.btnEdit.clicked.connect(self.showFormEdit)
        self.searchWidget.btnRem.clicked.connect(self.showFormRem)
        #MessageBox
        self.msgBox = MessageBox.MessageBoxWidget(self.searchWidget, 'Confirmar remoção', "Deseja remover permanentemente \no item selecionado?")
        #Form Reg UI
        self.formRegWidget = Customer.CustomerWidget()
        self.formRegWidget.btnSave.clicked.connect(self.saveReg)
        self.formRegWidget.btnCancel.clicked.connect(self.showSearch)
        #Form Edit UI
        self.formEditWidget = Customer.CustomerWidget()
        self.formEditWidget.btnSave.clicked.connect(self.saveEdit)
        self.formEditWidget.btnCancel.clicked.connect(self.showSearch)
        #Add/Set Widget in Layout
        self.layout = QtWidgets.QStackedLayout()
        self.layout.addWidget(self.searchWidget)
        self.layout.addWidget(self.formRegWidget)
        self.layout.addWidget(self.formEditWidget)
        self.setLayout(self.layout)
        print('Controller: Modulo Customers\t}')

    ''' Methods to connect with the signals '''  
    def showSearch(self):
        ''' Displays the search form component '''
        Status.statusVoid(self.searchWidget.lblStatus)
        self.searchWidget.searchResultSet(Model.get())
        self.layout.setCurrentWidget(self.searchWidget)

    def showFormReg(self):
        ''' Displays the reg form component '''
        self.formRegWidget.clearFields()
        self.layout.setCurrentWidget(self.formRegWidget)

    def showFormEdit(self):
        ''' Displays the edit form component '''
        key = self.searchWidget.getSelectedRow(4)
        objects = Model.get()
        if key in objects.keys():
            obj = objects[key]
            self.formEditWidget.setFields(obj)
            self.layout.setCurrentWidget(self.formEditWidget)
        else:
            Status.statusWarning(self.searchWidget.lblStatus,'Selecione o item primeiro!')

    def showFormRem(self):
        ''' Displays the rem form component '''
        key = self.searchWidget.getSelectedRow(4)
        if key != False:
            response = self.msgBox.getResponse()
            if response == QtWidgets.QMessageBox.Yes:
                if Model.rem(key):
                    Log.add(self.session.getSession()[1], 'Removeu um cliente')
                    self.showSearch()
                    Status.statusSuccess(self.searchWidget.lblStatus, 'Remoção bem sucedida!')
                else:
                    Status.statusWarning(self.searchWidget.lblStatus,'Remoção mal sucedida!') 
        else:
            Status.statusWarning(self.searchWidget.lblStatus,'Selecione o item primeiro!')
    
    def saveReg(self):
        ''' Verifies the data, if the data is valid, then store it as a new record, otherwise warn the user '''
        obj = self.formRegWidget.getFields()
        models = Model.get().copy()
        cpf_unique = True
        for key in models.keys():
            if models[key][1] == obj[1]:
                cpf_unique = False
                break
        del models
        if obj[2] == '':
            Status.statusWarning(self.formRegWidget.lblStatus,'O campo "Nome" é obrigatório!') 
        elif obj[1] == '':
            Status.statusWarning(self.formRegWidget.lblStatus,'O campo "CPF" é obrigatório!')
        elif not cpf_unique:
            Status.statusWarning(self.formRegWidget.lblStatus,'O valor do campo "CPF" já está sendo utilizado!')
        elif obj[3] == '':
            Status.statusWarning(self.formRegWidget.lblStatus,'O campo "Telefone" é obrigatório!')
        else:
            Status.statusVoid(self.formRegWidget.lblStatus)
            Model.add(obj)
            Log.add(self.session.getSession()[1], 'Cadastrou um cliente')
            self.showSearch()
            Status.statusSuccess(self.searchWidget.lblStatus, 'Cadastro realizado com sucesso!')

    def saveEdit(self):
        ''' Verifies the data, if the data is valid, then it updates the registry, otherwise, warn the user '''
        obj = self.formEditWidget.getFields()
        models = Model.get().copy()
        models.pop(obj[0])
        cpf_unique = True
        for key in models.keys():
            if models[key][1] == obj[1]:
                cpf_unique = False
                break
        del models
        if obj[2] == '':
            Status.statusWarning(self.formEditWidget.lblStatus,'O campo "Nome" é obrigatório!') 
        elif obj[1] == '':
            Status.statusWarning(self.formEditWidget.lblStatus,'O campo "CPF" é obrigatório!')
        elif not cpf_unique:
            Status.statusWarning(self.formEditWidget.lblStatus,'O valor do campo "CPF" já está sendo utilizado!')
        elif obj[3] == '':
            Status.statusWarning(self.formEditWidget.lblStatus,'O campo "Telefone" é obrigatório!')
        else:
            Status.statusVoid(self.formEditWidget.lblStatus)
            Model.edit(obj)
            Log.add(self.session.getSession()[1], 'Alterou um cliente')
            self.showSearch()
            Status.statusSuccess(self.searchWidget.lblStatus, 'Alteração realizada com sucesso!')
