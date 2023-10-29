import numpy as np
import random 
class diabi:
    __arreglo=[]
    __tamanio=0
    def __init__(self,tamanio):
        self.__tamanio=int(tamanio)
        self.__arreglo=np.empty(self.__tamanio,dtype=int)
        
    def cereo(self):
        for i in range(self.__tamanio):
            self.__arreglo[i]=0
        
    def insertar(self,objeto):
        i=0
        #while i < self.__tamanio:
            #objeto=random.randint(0,self.__tamanio)
        direccion=self.hasheo(objeto)
        if self.__arreglo[direccion]==0:
            self.__arreglo[self.hasheo(objeto)]=objeto
            print(f"insertado en la posicion: {direccion}")
            return
        else:
            j=0
            while j<self.__tamanio:
                direccion=(direccion+1)%self.__tamanio
                if self.__arreglo[direccion]==0:
                    self.__arreglo[direccion]=objeto
                    print(f"insertado en la posicion: {direccion}")
                    return
                j+=1
    
    def insertar_primo(self):
        i=0
        while i < self.__tamanio:
            objeto=random.randint(0,self.__tamanio)
            if self.es_primo(objeto)==True:
                direccion=self.hasheo(objeto)
                if self.__arreglo[direccion]==0:
                    self.__arreglo[self.hasheo(objeto)]=objeto
                    print(f"insertado en la posicion: {direccion}")
                else:
                    j=0
                    while j<self.__tamanio:
                        direccion=(direccion+1)%self.__tamanio
                        if self.__arreglo[direccion]==0:
                            self.__arreglo[direccion]=objeto
                            print(f"insertado en la posicion: {direccion}")
                        j+=1
            i+=1
        print("Insercion completa")
        
    def hasheo(self,objeto):
        fin=objeto%self.__tamanio
        return fin
    
    def mostrar(self):
        j=0
        direccion=self.hasheo(0)
        while j<self.__tamanio:
            if self.__arreglo[j]!=0:
                print(f"Numero: {self.__arreglo[j]}")
            j+=1
            direccion=(direccion+1)%self.__tamanio
    
    def buscar(self,buscar):
        direccion=self.hasheo(buscar)
        if self.__arreglo[direccion]==buscar:
            print("Si se encuentra el numero en la tabla")
            return
        else:
            print("No se encuentra")
            return
        
    def es_primo(self,n):
        for i in range(2,int(n/2)):
            if (n%i) == 0:
                return False
        return True
if __name__=="__main__":
    tabla=diabi(10)
    tabla.cereo()
    tabla.insertar(15)
    tabla.insertar(15)
    tabla.insertar(15)
    tabla.insertar(15)
    tabla.insertar(15)
    tabla.insertar(15)
    tabla.mostrar()
    # tabla.cereo
    # tabla.insertar_primo()
    # tabla.mostrar()