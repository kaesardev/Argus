'''
    STATUS LIBRARY
'''
def statusVoid(lblStatus):
    ''' Updates the status label to void mode '''
    lblStatus.setText('')
    lblStatus.setStyleSheet('font-size: 12px;')

def statusWarning(lblStatus, message):
    ''' Updates the status label to warning mode '''
    lblStatus.setText(message)
    lblStatus.setStyleSheet('font-size: 12px; background-color: #c0392b; color: #ecf0f1; border-radius: 5px;')

def statusSuccess(lblStatus, message):
    ''' Updates the status label to success mode '''
    lblStatus.setText(message)
    lblStatus.setStyleSheet('font-size: 12px; background-color: #27ae60; color: #ecf0f1; border-radius: 5px;')
