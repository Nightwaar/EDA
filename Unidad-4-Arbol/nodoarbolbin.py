class nodo():
    __objeto=None
    __hijomenor=None
    __hijomayor=None
    def __init__(self,objeto):
        self.__objeto=objeto
    def setmenor(self,menor):
        self.__hijomenor=menor
    def setmayor(self,mayor):
        self.__hijomayor=mayor
    def getmenor(self):
        return self.__hijomenor
    def getmayor(self):
        return self.__hijomayor
    def getobjeto(self):
        return self.__objeto