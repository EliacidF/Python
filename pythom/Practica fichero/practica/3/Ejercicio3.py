"""Mediante el uso de ficheros (alumnos.txt), vamos a gestionar los datos de alumnos y sus notas.
IMPORTANTE: para cada alumno, el sistema debe permitir almacenar un número indeterminado de notas.
Cada línea del fichero contendrá el nombre del alumno y sus notas.
El programa va a permitir:
• Añadir alumno: si el alumno no existe, se añadirá el nombre y la primera nota (0..10 con decimales). Si
ya existe, mostrar mensaje de error y volver a preguntar el nombre de nuevo alumno.
• Buscar alumno: mostrará las notas del alumno introducido por teclado. Si no existe, mostrar mensaje
de error y volver a preguntar.
• Añadir nota: para un alumno introducido por teclado, añadirá una nueva nota.
• Mostrar media de notas: para un alumno introducido por teclado, mostrará la media de sus notas.
• Borrar estudiante: borrará al alumno indicado de nuestra base de datos. Si no existe, mostrar mensaje
de error y volver a preguntar el nombre del alumno a borrar.
NOTA: si nos hemos confundido de opción, introduciremos una "X" cuando nos pida el nombre del alumno.
El sistema volverá al menú principal. El menú se generará con lista o diccionario, no un print por opción.
 Menú de opciones:
 1 - Añadir alumno
 2 - Buscar alumno
 3 - Añadir nota a alumno
 4 - Mostrar la media de notas de alumno
 5 - Borrar un alumno
 0 - Salir
 Introduce opción:"""

menu = ["Salir","Añadir alumno","Buscar alumno","Añadir nota a alumno","Mostrar la media de notas de alumno","Borrar un alumno"]

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

def añadir(nombre):
    """Añade un nuevo alumno al fichero con su primera nota
        param nombre: pregunta cual es el nombre del alumno
    """
    try:
        with open("alumnos.txt", "a+") as archivo:
            archivo.seek(0)
            archivos = archivo.read().split()
            for i in archivos:
                if nombre == i:
                    print("El alumno ya existe.")
                    return
                elif nombre == "X":
                    programa()
            nota = float(input("Ingrese la nota (0..10): "))
            archivo.write(f"{nombre} = {nota}\n")
    except ValueError:
        print("valor incorrecto")
        añadir(nombre)
        
def buscar(nombre):
    """busca el alumno  en el fichero y te muestra su nota
        parametro nombre: pregunta cual es el nombre del alumno
    """
    with open("alumnos.txt", "r") as archivo:
        for linia in archivo:
            campos = linia.strip().splitlines()
            alumno = linia.strip().split()[0]
            if nombre == alumno:
                print(campos)
                break
            elif nombre == "X":
                programa()
            else:
                print("El alumno no existe")
                break

def nota(nombre):
    """Añade una nueva nota al alumno que le indique 
        param nombre: pregunta cual es el nombre del alumno
    """
    with open("alumnos.txt", "r") as archivo:
        lineas = archivo.readlines()
    with open("alumnos.txt", "w+") as archivo:
        for linea in lineas:
            campos = linea.strip().split()
            if campos[0] == nombre:
                nota = float(input("Ingrese la siguiente nota (0..10): "))
                notas = campos[1:]
                notas.append(str(nota))
                nueva_linea = campos[0] + " " + " ".join(notas) + "\n"
                archivo.write(nueva_linea)
            else:
                archivo.write(linea)
        if nombre == "X":
            programa()
        
def mostrar(nombre):
    """Muestra la media de la nota de el alumno que le indiquemos.
        param nombre: pregunta cual es el nombre del alumno
    """
    with open("alumnos.txt", "r") as archivo:
        for linea in archivo:
            lineas = linea.strip().split()
            if nombre == lineas[0]:
                notas = []
                for nota in lineas[2:]:
                    try:
                        notas.append(float(nota))
                    except ValueError:
                        print(f"La nota '{nota}' no es un número válido.")
                media = sum(notas) / len(notas)
                print(f"La media de {nombre} es: {media:}")
                break
            elif nombre == "X":
                programa()
        else:
            print("el alumno  no existe")
def borrar():
    """borra el alumno que indiquemos juntos con su nota
    """
    nombre_borrar = input("Ingrese el nombre del alumno a borrar: ")
    lineas = []
    with open("alumnos.txt", "r") as archivo:
        for linea in archivo:
            if nombre_borrar not in linea.strip():
                lineas.append(linea)

    with open("alumnos.txt", "w") as archivo:
        for linea in lineas:
            archivo.write(linea)
    if nombre_borrar == "X":
        programa()


def programa():  
    """nos permite eligir la opcion que queremos del menu
        Opc(int):cantidad de veces que ponemos elegir las opciones
    """       
    OPC = 9999
    while OPC !="0":
        OPC= mostrar_menu(menu)
        if OPC == '0':
            print("El Programa a cerrado")
        elif OPC == "1":
            alumnos=input("Introdusca el nombre del alumnos: ") 
            añadir(alumnos)
        elif OPC == "2":
            alumnos=input("Introdusca el nombre del alumnos: ")
            buscar(alumnos)
            
        elif OPC == "3":
            alumnos=input("Introdusca el nombre del alumnos: ")
            nota(alumnos)
            print("AÑADIDO LA NUEVA NOTA")
        elif OPC == "4":
            alumnos=input("Introdusca el nombre del alumnos: ")
            mostrar(alumnos)
            
        elif OPC == "5":
            borrar()
            print("BORRADO EL ALUMNO")
          
        else:
            print("opcion Incorrecta")
            programa()
        
    
programa()