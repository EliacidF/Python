
import random
class tablero():
    def __init__(self,filas,columnas):
        self.filas = filas
        self.columnas = columnas 
        self.celda = []
        for i in range(5):
            fila = ['A'] * columnas
            self.celda.append(fila)
            
    def mostrar_tablero(self):
        """
        muestra el tablero por pantalla con el numero de posicion de  la filas y columnas.
        """
        print(" ", end=" ")
        for i in range(self.columnas):
            print(i, end=" ")
        print()
        for i in range(self.filas):
            print(i, end=" ")
            for j in range(self.columnas):
                print(self.celda[i][j], end=" ")
            print()

    def posicion(self,fila,columna):
        """
        verifica si estas se encuentran dentro de los límites del tablero.

        param (fila):compara que la fila sea mayor o igual que cero y menor que el número de filas del tablero.
        param (columna):compara que la columna sea mayor o igual que cero y menor que el número de columnas del tablero.
        """
        v =  0 <= fila < self.filas and 0 <= columna < self.columnas
        return v
    
    def colocar_barcos(self, fila, columna, orientacion, longitud):
        """
        añade los cambio de A a ve en la columnas y filas.

        param (fila): determina la fila de la tabla a la que cambiara.
        param (columna): determina la culumna de la tabla a la que cambiara.
        param (orientacion): es la oritenatcion de el tablero .
        param (longitud): es la longitud de la tabla.
        
        
        """
        for i in range(longitud):
            if orientacion == "horizontal":
                if not self.posicion(fila,columna+i) or self.celda[fila][columna+i] !="A":
                    return False
            else:
                if not self.posicion(fila+i,columna)  or self.celda[fila+i][columna] != "A":
                    return False
                
        for i in range(longitud):
            if orientacion == "horizontal":
                self.celda[fila][columna+i] = "B"
            else:
                self.celda[fila+i][columna] ="B"
        
        return True
   
  
        