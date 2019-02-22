'''
    SEARCH CONTROLLER
'''
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport, uic

class SearchWidget(QtWidgets.QWidget):
    ''' Component Class '''
    def __init__(self, header, parent=None):
        ''' Component builder method '''
        print('Controller: Search', end='\t\t')
        super(SearchWidget, self).__init__(parent)
        self.header = header
        uic.loadUi("views/search.ui", self)
        print('OK')

    ''' Methods to connect with the signals '''
    def searchResultSet(self, struc, filter=''):
        ''' Updates the table with the data structure received '''
        self.tableWidget.clear()
        self.tableWidget.clearSpans()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setColumnCount(len(self.header))
        rowPosition = self.tableWidget.rowCount()
        #Set header
        i = 0
        for key in self.header.keys():
            item = QtWidgets.QTableWidgetItem(self.header[key])
            self.tableWidget.setHorizontalHeaderItem(i, item)
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
            i += 1
        self.tableWidget.horizontalHeader().setSectionResizeMode(i - 1, QtWidgets.QHeaderView.ResizeToContents)
        #Set items
        if filter.lower() == '':
            for key in struc.keys():
                self.tableWidget.insertRow(rowPosition)
                i = 0
                for attr in self.header.keys():
                    cell = QtWidgets.QTableWidgetItem(struc[key][attr])
                    self.tableWidget.setItem(rowPosition , i, cell)
                    i += 1
        else:
            for key in struc.keys():
                found = False
                for attr in struc[key]:
                    if filter.lower() in attr.lower(): 
                        found = True
                if found:
                    self.tableWidget.insertRow(rowPosition)
                    i = 0
                    for attr in self.header.keys():
                        cell = QtWidgets.QTableWidgetItem(struc[key][attr])
                        self.tableWidget.setItem(rowPosition , i, cell)
                        i += 1
        self.tableWidget.setSortingEnabled(True)

    def getSelectedRow(self, index):
        ''' Returns the value of the given index as parameter of the selected line '''
        try:
            index = self.tableWidget.selectedIndexes()[index]
            key = self.tableWidget.model().data(index)
        except:
            key = False
        return key
    
    def makeTableDocument(self):
        ''' Returns a text document '''
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        rows = self.tableWidget.rowCount()
        columns = self.tableWidget.columnCount()
        table = cursor.insertTable(rows + 1, columns)
        format = table.format()
        format.setHeaderRowCount(1)
        table.setFormat(format)
        format = cursor.blockCharFormat()
        format.setFontWeight(QtGui.QFont.Bold)
        for column in range(columns):
            cursor.setCharFormat(format)
            cursor.insertText(
                self.tableWidget.horizontalHeaderItem(column).text())
            cursor.movePosition(QtGui.QTextCursor.NextCell)
        for row in range(rows):
            for column in range(columns):
                cursor.insertText(
                    self.tableWidget.item(row, column).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        return document

    def printPDF(self):
        ''' Print pdf log '''
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Exportar PDF', None, 'PDF (.pdf);;Todos arquivos ()')
        if fn != '':
            if QtCore.QFileInfo(fn).suffix() == '':
                fn += '.pdf'
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.makeTableDocument().print_(printer)