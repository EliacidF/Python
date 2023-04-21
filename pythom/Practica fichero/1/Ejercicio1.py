"""A partir de un fichero de nombres y apellidos (personas.txt), cada uno de ellos en una línea diferente, crearemos
un menú que nos permita crear un fichero nuevo según sea esa opción:
• Opción 1: nuevo fichero con nombres (nombres.txt)
• Opción 2: nuevo fichero con apellidos (apellidos.txt)
• Opción 3: nuevo fichero con nombres y apellidos, siempre que el nombre tenga, como máximo, el
número de letras solicitadas al usuario (nom_de_X_letras.txt), donde la X del número máximo de letras
del nombre.
• Opción 4: nuevo fichero con nombres y apellidos, siempre que el nombre empiece por una letra
solicitada al usuario (nom_de_letra_X.txt), donde la X del nombre del documento es la letra indicada.
"""
menu = ["Salir","Nombres","Apellidos","Cantidad de letras","Letra de inicio"]
def mostar_menu(opciones):
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

def nombres():
    """Crea un fichero con la posicion 0 de la lista y lo Muestra por pantalla
        nombres (lista): lista de nombres que nos piden
        personas(lista): lista con nombres posicion 0 y apellido posicion 1
        return: retorna pa lista con la posicion 0
    """
    nombres= []
    with open("nombres.txt","w+") as nombre:
        for j in personas:
            nombres.append(j[0])
        for x in nombres:
            nombre.write(x+"\n")
    print(nombres)
    return nombres
        

def apellidos():
    """Crea un fichero con la posicion 1 de la lista y lo Muestra por pantalla
        
        return: retorna pa lista con la posicion 1
    """
    Apellidos= []
    with open("Apellidos.txt","w+") as Apellido:
        for j in personas:
            Apellidos.append(j[1])
        for x in Apellidos:
            Apellido.write(x+"\n")
    print(Apellidos)      
    return Apellidos
        
def nombres_y_apellidos():
    """Crea un fichero con la maxima cantidad de letra que solicitamos y los muestra por pantalla
        
        return: el contedido de nom
    """
    try:
        cantidad = int(input("Maximo de letras permitido para los nombres: "))
        nom=[]
        with open("personas.txt", "r") as personas:
            with open(f"nombres_de_{cantidad}_letras.txt", "w") as nombres_l:
                for linea in personas:
                    nombre = linea.strip().split()[0] 
                    apellido = linea.strip().split()[1]
                    if len(nombre) <= cantidad:
                            nombres_l.write(nombre +" "+ apellido+"\n")
                            nom.append(nombre.strip('\n')+" "+apellido)
            print(nom)
            return nom
    except ValueError:
        print("no es un numero lo que indicaste")
        nombres_y_apellidos()
        
def letras():
    """Crea un fichero con la letra principal y los muestra por 
    pantalla todos los nombre que comiensa con esa letra.
        
        return: el contedido de nom
    """
    letra= input("Letra Iniciar de los nombres en Mayuscula: ")
    nom=[]
    with open("personas.txt", "r") as personas:
        with open(f"nombres_de_letras_{letra}.txt", "w") as nombres_l:
            for linea in personas:
                nombre = linea.strip().split()[0] 
                apellido = linea.strip().split()[1]
                if nombre[0] == letra:
                    nombres_l.write(nombre +" "+ apellido+"\n")
                    nom.append(nombre.strip('\n')+" "+apellido)
                
    print(nom)         
    return nom


def programa():  
    """nos permite eligir la opcion que queremos del menu
        Opc(int):cantidad de veces que ponemos elegir las opciones
    """       
    OPC = 9999
    while OPC !="0":
        OPC= mostar_menu(menu)
        if OPC == '0':
            print("El Programa a cerrado")
        elif OPC == "1":
                nombres()
        elif OPC == "2":
                apellidos()
        elif OPC == "3":
                nombres_y_apellidos()
        elif OPC == "4":
                letras()
        else:
            print("opcion Incorrecta")
            programa()
        

personas=[]
with open("personas.txt","r") as persona:
    f= persona.read().splitlines()
    for i in range(len(f)):
        completo = f[i].split()
        personas.append(completo)
print(personas) 
programa()