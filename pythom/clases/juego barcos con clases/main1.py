from Jugador import Jugador

menu = ["Salir","Jugar"]

def mostrar_menu(opciones):
    """nos muestra un menu en base a la lista que tengamos
    Args:
        opciones (lista): muestra la lista en forma de opciones

    Returns:
        _Input: pide que elijamos una opcion del menu 
    """
    
    try:
    
        seleccion = ""
        for i in range(len(opciones)):
            print(i,opciones[i], sep="-")
        seleccion = input("seleccione la opcion: ")
    except ValueError:
        pass
    except TypeError:
        pass    
    return seleccion



OPC = 9999
while OPC !="0":
        OPC= mostrar_menu(menu)
        if OPC == '0':
            print("El Programa a cerrado")
        elif OPC == "1":
           
            Jugador1 = Jugador()
            Jugador2 = Jugador()

       
        while True:
         
            print("Tablero de", Jugador1.nombre, " "*10, "Tablero de", Jugador2.nombre)
            for i in range(5):
                for j in range(5):
                    print(Jugador1.tableros_propio.celda[i][j], end=" ")
                print(" "*20, end="")
                for j in range(5):
                    print(Jugador2.tableros_propio.celda[i][j], end=" ")
                print()
            print()

         
            print("Turno de", Jugador1.nombre)
            Jugador1.tirar()
            print()

            if Jugador2.ganador(Jugador1.tableros_propio):
                print("¡", Jugador2.nombre, "ha ganado!")
                break


            print("Turno de", Jugador2.nombre)
            Jugador2.tirar()
            print()

            if Jugador1.ganador(Jugador2.tableros_propio):
                print("¡", Jugador1.nombre, "ha ganado!")
                break

            elif Jugador1.num_tiradas == 0 and Jugador2.num_tiradas == 0:
                print("¡El juego ha terminado en empate!")
                break
        else:
            print("opcion Incorrecta")
            