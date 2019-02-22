'''
    CRYPTOGRAPHY LIBRARY
'''
from libraries.FilesFlow import importData

def importKey(filename):
    ''' Import string from a file and return key '''
    data = importData('databases/' + filename)
    e = str()
    n = str()
    flag = True
    for char in data:
        if char == ' ' or char == '\n':
            flag = False
        if flag:
            e += char
        else:
            n += char
    return int(e), int(n)

def encrypt(string):
    ''' Encrypts the string '''
    e, n = importKey('public.key')
    result = str()
    for char in string:
        result += str(ord(char) ** e % n) + ' '
    return result

def decrypt(string):
    ''' Decrypts the string '''
    d, n = importKey('private.key')
    result = str()
    attr = str()
    for char in string:
        if char == ' ':
            result += chr(int(attr) ** d % n)
            attr = ''
        else:
            attr += char 
    return result
