class nodo():
    __objeto=int
    __siguiente=None
    def __init__(self):
        self.__objeto=0
        self.__siguiente=None
    
    def setSiguiente(self,sig):
        self.__siguiente=sig
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getObjeto(self):
        return self.__objeto
    
    def setObjeto(self,objeto):
        self.__objeto=objeto