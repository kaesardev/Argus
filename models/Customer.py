'''
    CUSTOMER MODEL
'''
from libraries import FilesFlow, Cryptography

def add(obj):
    ''' Adds object in database '''
    database = get()
    result = False
    if obj[0] not in database.keys():
        database[obj[0]] = obj
        save(database)
        result = True
    return result

def edit(obj):
    ''' Update object in database '''
    database = get()
    result = False
    if obj[0] in database.keys():
        database[obj[0]] = obj
        save(database)
        result = True
    return result

def rem(key):
    ''' Remove object in database '''
    database = get()
    result = False
    if key in database.keys():
        del database[key]
        save(database)
        result = True
    return result

def get():
    ''' Import database '''
    dataEncrypt = FilesFlow.importData('databases/customers.dat')
    data = Cryptography.decrypt(dataEncrypt)
    return FilesFlow.mountData(data)

def save(database):
    ''' Export database '''
    data = FilesFlow.unmountData(database)
    dataEncrypt = Cryptography.encrypt(data)
    FilesFlow.exportData('databases/customers.dat', dataEncrypt)
