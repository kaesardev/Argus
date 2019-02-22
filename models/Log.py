'''
    LOG MODEL
'''
from datetime import datetime
from libraries import FilesFlow

def add(user, operation):
    ''' Adds event in log '''
    database = get()
    current = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    event = (current, user, operation)
    database[current] = event
    save(database)

def get():
    ''' Import database '''
    data = FilesFlow.importData('databases/log.dat')
    return FilesFlow.mountData(data)

def save(database):
    ''' Export database '''
    data = FilesFlow.unmountData(database)
    FilesFlow.exportData('databases/log.dat', data)
