'''
    CITY MODEL
'''
from libraries import FilesFlow

def get(state):
    ''' returns the cities of the state '''
    database = request()
    result = []
    for item in database:
        if item[0] == state:
            result.append(item[1])
    return result

def request():
    ''' Import database '''
    data = FilesFlow.importData('databases/cities.dat')
    return FilesFlow.mountDataArray2D(data)
