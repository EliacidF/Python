
"""A partir del fichero "nums_dni.txt", que contiene diversos números de DNI (en la misma línea o en líneas
diferentes, crea un nuevo fichero (el nombre deberá solicitarse al usuario) que almacene, línea por línea,
los DNIs completos en formato "12345678-X".
Finalmente, una vez tengamos el nuevo documento, deberemos mostrarlo por pantalla en el siguiente
formato:
 DNIs
 ---------
 XXXXXXXX-X
Recuerda que las letras son: TRWAGMYFPDXBNJZSQVHLCKE
y las letras se relacionan del 0 al 22:
0 = T
1 = R
2 = W
etc..."""
def leer_dnis():
    """Lee el contenido del archivo que contiene los números de DNI y devuelve una lista con los DNIs
        return: el contendo de el fichero por linia
    """
    with open("nums_dni.txt", 'r') as archivo:
        contenido = archivo.read().split()
    return contenido

def escribir(contenido,nombre):
    """Escribe en un nuevo archivo los DNIs completos y devuelve el nombre del archivo
        param contenido: recorre el contenido
        param nombre: otorga el nombre del archivo
        return: retorna el nombre del archivo
    """  
    with open(f"{nombre}.txt","w") as nuevo_archivo:
        for dni in contenido:
            letra = "TRWAGMYFPDXBNJZSQVHLCKE"[int(dni) % 23]
            nuevo_archivo.write(f"{dni}-{letra}\n")
    return nombre

def mostrar(nombre):
    """Muestra los DNIs completos 
        param nombre: nombre del archivo que tiene que leer
    """
    with open(f"{nombre}.txt", "r") as archivo:
        for linea in archivo:
            print("DNIs\n---------\n"+linea.strip())


dnis = leer_dnis()
nombre = input("Introduce el nombre del archivo: ")
nombres=escribir(dnis,nombre)
mostrar(nombres)
