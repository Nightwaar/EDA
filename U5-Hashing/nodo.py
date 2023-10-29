class Nodo():
    __objeto=int
    __siguiente=None
    def __init__(self):
        self.__dato=0
        self.__siguiente=None
    
    def setSiguiente(self,sig):
        self.__siguiente=sig
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self):
        return self.__dato
    
    def getDato(self,objeto):
        self.__dato=objeto