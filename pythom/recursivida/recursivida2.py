"""
EJERCICIO 3: HUNDIR LA FLOTA ------------------------------

El código va a crear un tablero de 4x4 y va a colocar 2 barcos en él. El código debe permitir, fácilmente, cambiar
la posición de los barcos antes de lanzar el programa.

# Antes de empezar a jugar:
- Creamos un tablero de 4x4 vacío ('A')
- Colocamos 2 barcos (posición con 'B'), uno de 2 celdas y otro de 3 celdas (horizontal o vertical pero que no solapen)

# Al iniciar el programa...
- Mostrar el menú de juego (diccionario o lista) y tablero inicial con los barcos:
        1 - Jugar
        0 - Salir
- En random, hacemos tiradas:
    - devolver posición de la tirada
    - devolver agua (cambiar la casilla vacía 'A' por 'X') o tocado (cambiar la casilla de barco 'B' por 'T')
    - devolver estado del tablero
    - Esperar 'ENTER' para siguiente tirada
- Al completar 6 tiradas, deberemos devolver un mensaje según si hemos conseguido hundir todos los barcos o no

EJEMPLO DEL 1ER TURNO ----------------------------------------------------
-  Mostramos el tablero al empezar el juego:
           0 1 2 3
         0 A B B A
         1 A A A B
         2 A A A B
         3 A A A B

- Vemos las posiciones del disparo:
    Se dispara en la posicion x: 0 y: 1
    Tocado!

- Mostramos el tablero con las modificaciones:
           0 1 2 3
         0 A T B A
         1 A A A B
         2 A A A B
         3 A A A B
- Esperamos al siguiente turno:   "Pulsa ENTER para continuar..."

INSTRUCCIONES:

	No se permitirán prints innecesarios ni dentro de condicionales ni iteraciones, salvo que sean necesarios
	No se permite el uso de métodos o funciones que no se han expuesto en clase
	Se entregarán tanto archivos como ejercicios tenga la prueba
	No se evaluará código comentado
	No se valorarán métodos/funciones de + 10 líneas.
	El programa principal podrá tener también un máximo de 10 líneas. Con excepción de encadenamientos de elif y las líneas de control de errores, que no contarán para este limite.
	Controlar los errores que se puedan producir FUERA de los métodos/funciones. El programa NO puede fallar.
	Todos los métodos deberán estar comentados como se expuso en clase:

def ejemplo(str):
'''
Esta función no hace nada
:param str: es un string que conforma una palabra para nada
:return: el 1, porque funciona
'''
print("esto no hace nada")
return 1
---------------------------------------------------------------------------------------------------
"""
import random

import random

def mostrar_menu():
    menu = ["SALIR", "Jugar"]
    for i in range(len(menu)):
         print(i,menu[i], sep="-")
    opciones = int(input("seleccione la opcion: "))
    return opciones

def decir_adios():
    print("Adios")

def tablero():
    tablero = [[" A ", " B ", " B ", " A "],
               [" A ", " A ", " A ", " B "],
               [" A ", " A ", " A ", " B "],
               [" A ", " A ", " A ", " B "]
               ]
    return tablero

def mostrar_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end="")
        print()

def disparar(tablero, fila, columna):
    if tablero[fila][columna] == " B ":
        tablero[fila][columna] = " T "
        print("Tocado!")
    else:
        tablero[fila][columna] = " X "
        print("Agua")
    return tablero

def jugar():
    mi_tablero = tablero()
    mostrar_tablero(mi_tablero)
    contador_tiros = 0
    while contador_tiros < 6:
        fila_tiro = random.randint(0, 3)
        columna_tiro = random.randint(0, 3)
        print(f"Se dispara en la posicion x: {fila_tiro} y: {columna_tiro}")
        mi_tablero = disparar(mi_tablero, fila_tiro, columna_tiro)
        mostrar_tablero(mi_tablero)
        contador_tiros += 1
        if mi_tablero == [[" X ", " X ", " X ", " X "],
                          [" X ", " X ", " X ", " X "],
                          [" X ", " X ", " X ", " X "],
                          [" X ", " X ", " X ", " X "]]:
            print("¡Has hundido todos los barcos!")
            return
    print("Fin del juego, no has conseguido hundir todos los barcos.")

opcion = mostrar_menu()
if opcion == 1:
    jugar()
elif opcion == 0:
    decir_adios()