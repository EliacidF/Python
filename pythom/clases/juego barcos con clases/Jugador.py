from Tablero import tablero  # Tablero es otra clase
import random


class Jugador():
    id = ""
    nombre = ""
    num_tiradas = ""
    tableros = None
    def __init__(self):
        try:
            self.id = int(input("ID: "))
            self.nombre = input("Nombre: ")
            self.num_tiradas = 6
            self.tableros_propio = tablero(5,5)
            self.barcos()
        except ValueError:
            print("VALOR INCORRECTO")

    def barcos(self):
        """
        coloca de forma ramdom cada barcos en el juego.
        """
        barcos=[(2,0),(2,1),(3,4)]
        for barco in barcos:
            while True:
                fila = random.randint(0,4)
                columna = random.randint(0,4)
                orientacion = random.choice(["horizontal","vertical"])
                if self.tableros_propio.colocar_barcos(fila,columna,orientacion,barco[0]):
                    break
   
    def ganador(self, tableros_oponente):
        """
        determina cual es el ganador del juego.
        """
        for fila in range(len(tableros_oponente.celda)):
            for columna in range(len(tableros_oponente.celda[0])):
             if tableros_oponente.celda[fila][columna] == "B":
                return False
        return True
    
    def tirar(self):
        """
        gestiona las tirada y el cambio en cada celda del tablero.
        """
        try:
            while self.num_tiradas > 0:
                print("Estado actual de trablero")  
                self.tableros_propio.mostrar_tablero()
                fila = int(input("indique la fila (0-4): "))
                columna = int(input("indique la culumna (0-4): "))
                print("\n")
                if self.tableros_propio.celda[fila][columna] == "B":
                    print("!Tocado¡")
                    self.tableros_propio.celda[fila][columna] = "T"
                else:
                    print("!Agua¡")
                    self.tableros_propio.celda[fila][columna] = "X" 
                self.num_tiradas -=1
        except (ValueError, IndexError): 
            print("VALOR INCORRECTO")
            return False
        
    def mostrar_estado_tablero(self):
        """
        muestra por pantalla el tablero.
        """
        print(f"Estado actual del tablero del jugador {self.nombre}:")
        self.tableros_propio.mostrar_tablero()

    def __str__(self):
        string = f"El jugador {self.id}, llamado {self.nombre} tiene {self.num_tiradas} disponibles."
        return string



