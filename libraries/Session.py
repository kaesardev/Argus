'''
    SESSION LIBRARY
'''
class Session():
    ''' Session Class '''
    def __init__(self):
        ''' Builder method '''
        self.__LOGGED = False
        self.__USERNAME = str()
        self.__PRIVILLEGE = str()

    def setSession(self,username, privillege):
        ''' Assigns the current session '''
        self.__LOGGED = True
        self.__USERNAME = username
        self.__PRIVILLEGE = privillege

    def getSession(self):
        ''' Returns the current session '''
        return self.__LOGGED, self.__USERNAME, self.__PRIVILLEGE

    def delSession(self):
        ''' Destroy the current session '''
        self.__LOGGED = False
        self.__USERNAME = str()
        self.__PRIVILLEGE = str()
