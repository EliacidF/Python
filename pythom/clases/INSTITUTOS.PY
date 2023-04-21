def DNI():
        dni = int(input("Inserte los 8 digitos de tu DNI: "))
        letra = "TRWAGMYFPDXBNJZSQVHLCKE"[int(dni) % 23]
        L = f"{dni}-{letra}"
        return L

class institutos:
    tipo= int
    metros= int
    ubicacion= str
    profesor= list
    alumnos= list
        
    def __init__(self):
        self.tipo = None
        self.metros = None
        self.ubicacion = None
        self.profesor = []
        self.alumnos = []
        
    def contenido(tipo,metros,ubicacion,profesor:list,alumnos:list):
        al = institutos()
        al.tipo: tipo = input("Que tipo de instituto es: ")
        al.metros: metros = int(input("Metros: "))
        al.ubicacion: ubicacion = input("Ubicación: ")
        for e in profesor:
            al.profesor.append(e)
        for i in alumnos:
            al.alumnos.append(i)
        return al 
    
    
    
    def profesor(self):
        Nombre = input("Cual es su nombre: ")
        dni = DNI()
        materia = input("que materia Imparte")
        datos_maestro = f"{Nombre}\n   Su DNI es: {dni}\n   Materia: {materia}"
        self.profesor.append(datos_maestro)
        

    def alumnos(self):
        Nombre = input("Cual es su nombre: ")
        dni = DNI()
        CICLO = input("Que ciclo cursa: ")
        datos_alumno = f"{Nombre}\n   Su DNI es: {dni}\n   Ciclo: {CICLO}"
        self.alumnos.append(datos_alumno)
        
    def string(self):
        string1= f"Tipo {self.tipo}\nMetros: {self.metros}\nUbicacon: {self.ubicacion}\n Profesor: {self.profesor}\n Alumnos: {self.alumnos}"
        return string1
    