from Juego import Juego
from Mensajes import Mensajes

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


juego = Juego()
juego.leer_ficheros()
Mensaje = Mensajes
OPC = 9999
while OPC !="0":
        OPC= mostrar_menu(menu)
        if OPC == '0':
            Mensaje.ok_msg("¡Hasta luego!")
        elif OPC == "1":
           juego.jugar()
            
        else:
            Mensaje.warning_msj("Opción inválida. Intenta de nuevo.")
            
            


       