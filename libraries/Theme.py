'''
    FILES FLOW LIBRARY
'''
from libraries import FilesFlow
import gc

def replaceVars(key, value, string):
    ''' Replace theme vars '''
    keySize = len(key)
    strSize = len(string)
    result = str()
    i = 0
    while i < strSize:
        flag = True
        if key[0] == string[i]:
            j = 0
            while j < keySize and i + j < strSize and flag:
                if key[j] != string[i + j]:
                    flag = False
                j += 1
            if not flag:
                result += string[i]
                i += 1
            else:
                result += value
                i += keySize
        else:
            result += string[i]
            i += 1
    gc.collect() 
    return result

def getStyle(filename):
    ''' Return stylesheet data '''
    theme = FilesFlow.mountData(FilesFlow.importData('databases/theme.dat'))
    data = FilesFlow.importData('resources/theme/' + filename + '.qss')
    for var in theme.keys():
        data = replaceVars(var, theme[var][1], data)
    FilesFlow.exportData('resources/theme/' + filename + '.css', data)
    return data
