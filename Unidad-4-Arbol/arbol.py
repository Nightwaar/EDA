from nodoarbolbin import nodo
class arbol():
    __raiz=nodo
    def __init__(self):
        self.__raiz=None
    def insertar(self,numero,raiz=None):
        nuevo=nodo(numero)
        if raiz==None: raiz=self.__raiz
        if self.__raiz==None:
            self.__raiz=nuevo
            print("Agregado correctamente")
            return
        
        if raiz==None:
            raiz=nuevo
            print("Hoja agregada")
        if numero<raiz.getobjeto():
            if raiz.getmenor()==None:
                raiz.setmenor(nuevo)
                print("hoja menor agregado correctamente")
            else:   
                return self.insertar(numero,raiz.getmenor()) 
        elif numero>raiz.getobjeto():
            if raiz.getmayor()==None:
                raiz.setmayor(nuevo)
                print("hoja mayor agregado correctamente")
                
            else:
                return self.insertar(numero,raiz.getmayor())
    def mostrarraiz(self):
        print(f"La raiz es: {self.__raiz.getobjeto()}")
    def nivel(self,raiz=None,nivel=1,contador=1):
        if raiz==None:  raiz=self.__raiz
        if raiz.getmayor()!=None:
            print("llegue mayor")
            if nivel>=contador:
                print("Sumo mayor")
                contador+=1
                return self.nivel(raiz.getmayor(),nivel+1,contador)
            else:
                return self.nivel(raiz)
        elif raiz.getmenor()!=None:
            print("llegue menor")
            if nivel>=contador:
                print("Sumo menor")
                contador+=1
                return self.nivel(raiz.getmenor(),nivel+1,contador)
            else:
                return self.nivel(raiz)
        elif raiz.getmayor()==None and raiz.getmenor()==None:
            print(f"El nivel de la raiz es: {nivel}")
            

if __name__=="__main__":
    prueba=arbol()
    prueba.insertar(10)
    prueba.mostrarraiz()
    prueba.nivel()
    prueba.insertar(5)
    prueba.insertar(11)
    prueba.insertar(15)
    prueba.insertar(18)
    prueba.nivel()