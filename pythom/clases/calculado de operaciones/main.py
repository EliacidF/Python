from operaciones import operaciones
from mensajes import mensajes

def mostrar_menu(opciones):
    """nos muestra un menu en base a la lista que tengamos

        opciones (lista): muestra la lista en forma de opciones

    Returns: pide que elijamos una opcion del menu 
    """
    try:
        seleccion = ""
        for i in range(len(opciones)):
            print(i,opciones[i], sep="-")
        seleccion = input("seleccione la opcion: ")
    except (ValueError,TypeError):
        pass
    return seleccion

def programa():  
    """nos permite eligir la opcion que queremos del menu
        Opc(int):cantidad de veces que ponemos elegir las opciones
    """       
    OPC = 9999
    menu = ["Salir","suma","division","cuadrado","ecuacion de segundo grado"]
   
    while OPC !="0":
        OPC= mostrar_menu(menu)
        mensaje = mensajes()
        op = operaciones()
        
        if OPC == '0':
            mensaje.ok_msg("El Programa a cerrado")
        
        elif OPC == "1":
            n1 = mensaje.pedir_datos()
            n2 = mensaje.pedir_datos()
            op.suma(n1, n2)
           
        elif OPC == "2":
            n1 = mensaje.pedir_datos()
            n2 = mensaje.pedir_datos()
            op.division(n1, n2)
   
        elif OPC == "3":
            n = mensaje.pedir_datos()
            op.cuadrado(n)
         
        elif OPC == "4":
            A = mensaje.pedir_datos()
            B = mensaje.pedir_datos()
            C = mensaje.pedir_datos()
            op.ecuacion2grado(A,B,C)
            
        else:
           
            mensaje.error_msj("Opcion Incorrecta")
             
programa()

