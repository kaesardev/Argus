'''
    STATE MODEL
'''
from libraries import FilesFlow

def get():
    ''' Import database '''
    data = FilesFlow.importData('databases/states.dat')
    database = FilesFlow.mountDataArray1D(data)
    return database
