import numpy as np
from nodo import Nodo

class Hash2:
    __arreglo=None
    __dimension=0

    def __init__(self, dim):
        dimension=self.calculaPrimo(dim)
        self.__arreglo=np.empty(dimension, dtype=Nodo)
        self.__dimension=int(dimension)

        for i in range(self.__dimension):
            self.__arreglo[i]=Nodo(None)

    def calculaPrimo(self, dim):
        num=2
        while num < dim:
            mod=dim%num
            if mod == 0:
                num=2
                dim+=1
            else:
                num+=1
        return dim
    
    def hashing(self, elemento):
        return elemento%self.__dimension
    
    def insertar(self, elemento):
        mod=self.hashing(elemento)
        if self.__arreglo[mod].getDato() is None:
            self.__arreglo[mod].setDato(elemento)
            print("Elemento insertado")
        else:
            aux = self.__arreglo[mod]

            while aux.getDato() != elemento and aux.getSiguiente():
                aux=aux.getSiguiente()

            if aux.getDato() == elemento:
                print("Elemento ya existente")
            elif aux.getSiguiente() is None:
                aux.setSiguiente(Nodo(elemento))
                print("Elemento insertado")



    def mostrar(self):
        for i in range(self.__dimension):
            print(f"{self.__arreglo[i]}")

    def test(self):
        print(self.__dimension)
        print("43078713  " + str(43078713%self.__dimension))
        print("44665750  " + str(44665750%self.__dimension))
        print("44316666  " + str(44316666%self.__dimension))
        print("42432234  " + str(42432234%self.__dimension))
        print("46789234  " + str(46789234%self.__dimension))
        print("41121212  " + str(41121212%self.__dimension))
        print("41121212  " + str(41121212%self.__dimension))
        print("43078013  " + str(43078013%self.__dimension))
        print("43078413  " + str(43078413%self.__dimension))
        print("44665250  " + str(44665250%self.__dimension))
        print("44322266  " + str(44322266%self.__dimension))
        print("42432234  " + str(42432234%self.__dimension))
        print("46111134  " + str(46111134%self.__dimension))
        print("40000012  " + str(40000012%self.__dimension))
        print("49999912  " + str(49999912%self.__dimension))
        print("43024890  " + str(43024890%self.__dimension))

        print("")
        self.insertar(43078713)
        self.insertar(44665750)
        self.insertar(44316666)
        self.insertar(42432234)
        self.insertar(46789234)
        self.insertar(41121212)
        self.insertar(41121212)
        self.insertar(43078013)
        self.insertar(43078413)
        self.insertar(44665250)
        self.insertar(44322266)
        self.insertar(42432234)
        self.insertar(46111134)
        self.insertar(40000012)
        self.insertar(49999912)
        self.insertar(43024890)
        print("")
        self.mostrar()

if __name__=='__main__':
    dim=14
    h=Hash2(dim)
    h.test()
