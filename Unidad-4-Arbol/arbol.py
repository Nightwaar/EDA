from nodoarbolbin import nodo
class arbol():
    __raiz=nodo
    def __init__(self):
        self.__raiz=None
    def insertar(self,numero,raiz=None):
        raiz=self.__raiz
        nuevo=nodo(numero)
        if self.__raiz==None:
            self.__raiz=nuevo
            print("Agregado correctamente")
            return
        
        if raiz==None:
            raiz=nuevo
            print("Hoja agregada")
        if numero<raiz.getobjeto():
            if self.__raiz.getmenor()==None:
                self.__raiz.setmenor(nuevo)
                print("hoja menor agregado correctamente")
            else:   
                return self.insertar(numero,raiz.getmenor())
            
        elif numero>raiz.getobjeto():
            if self.__raiz.getmayor()==None:
                self.__raiz.setmayor(nuevo)
                print("hoja mayor agregado correctamente")
                
            else:
                return self.insertar(numero,raiz.getmayor())
    def mostrarraiz(self):
        print(f"La raiz es: {self.__raiz.getobjeto()}")


if __name__=="__main__":
    prueba=arbol()
    prueba.insertar(10)
    prueba.mostrarraiz()
    prueba.insertar(5)
    prueba.insertar(15)