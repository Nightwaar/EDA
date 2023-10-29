import numpy as np
class bucket():
    __arreglo:[]
    __M=0
    __T=0
    __b=0
    __totalar=0
    def __init__(self,t,b,m):
        self.__T=int(t)
        self.__b=int(b)
        self.__M=int(m)
        self.__totalar=self.__T+self.__M
        self.__arreglo=np.empty((self.__totalar,self.__b),dtype=int)
        print
    def cereo(self):
        val = 0
        self.__arreglo.fill(val)
        print(self.__arreglo)
        return
    
    def mostrar(self):
        print("Tabla:")
        for i in range(self.__M):
            print(self.__arreglo[i])
        print("Overflow)")
        for i in range(self.__M,self.__totalar):
            print(self.__arreglo[i]) 
    
    def hasheo(self,objeto):
        hasing=objeto%self.__M
        return hasing
    
    def insertar(self,objeto):
        direccion=self.hasheo(objeto)
        print(direccion,objeto)
        if self.__arreglo[direccion][0]==0:
            self.__arreglo[direccion][0]=objeto
            return
        else:
            print("Entre")
            i=1
            while i<self.__b:
                if self.__arreglo[direccion][i]==0:
                    self.__arreglo[direccion][i]=objeto
                    return
                i+=1
        x=self.__M
        # if self.__arreglo[x][0]==0:
        #     self.__arreglo[x][0]=objeto
        #     return
        while x<self.__totalar:
            j=0
            while j<self.__b:
                if self.__arreglo[x][j]==0:
                    self.__arreglo[x][j]=objeto
                    return
                j+=1
            x+=1
        print("Arreglo lleno")
        
    def buscar(self,objeto):
        direccion=self.hasheo(objeto)
        i=0
        while i<self.__b:
            if self.__arreglo[direccion][i]==objeto:
                print(f"Objeto encontrado: {objeto}")
                return
            i+=1
        x=self.__M
        while x<self.__totalar:
            j=0
            while j<self.__b:
                if self.__arreglo[x][j]==objeto:
                    print(f"El objeto {objeto} se encuentra en overflow")
                    return
                j+=1
            x+=1
        print("No se encontro")
        
    def eliminar(self,objeto):
        direccion=self.hasheo(objeto)
        j=0
        while j<self.__b:
            if self.__arreglo[direccion][j]==objeto:
                self.__arreglo[direccion][j]=0
                print(f"Objeto eliminado: {objeto}")
                self.reubicar(direccion,j)
                return
            j+=1
        print(f"Objeto no encontrado y eliminado:{objeto}")
        
    def reubicar(self,direccion,j):
        print("llegue")
        x=self.__M
        direccion=direccion
        while x<self.__totalar:
            print("entre uno")
            i=0
            while i<self.__b:
                print("entre dos")
                if self.hasheo(self.__arreglo[x][i])==direccion:
                    self.__arreglo[direccion][j]=self.__arreglo[x][i]
                    print(f"Objeto reubicado: {self.__arreglo[x][i]}")
                    self.__arreglo[x][i]=0
                    return
                i+=1
            x+=1
        
if __name__=="__main__":
    b=4
    M=4
    T=2
    print("Voy a crear")
    buck=bucket(T,b,M)
    buck.cereo()
    buck.insertar(1)
    buck.insertar(2)
    buck.insertar(5)
    buck.insertar(6)
    buck.insertar(7)
    buck.insertar(8)
    buck.insertar(9)
    buck.insertar(11)
    buck.insertar(12)
    buck.insertar(13)
    buck.insertar(14)
    buck.insertar(15)
    buck.insertar(16)
    buck.insertar(17)
    buck.insertar(4)
    buck.insertar(3)
    buck.insertar(10)
    buck.mostrar()
    buck.buscar(7)
    buck.buscar(17)
    buck.eliminar(13)
    buck.mostrar()