from Mensajes import Mensajes
import random


class Juego:
    def __init__(self):
        self.adivinanzas = []
        self.pistas = []
        self.respuestas = []
        self.pistas_disponibles = 3
        self.pistas_acertadas = 0

    def leer_ficheros(self):
        with open("Acertijos.txt", "r") as archivo:
            self.adivinanzas = archivo.readlines()
        with open("Pista.txt", "r") as archivo:
            self.pistas = archivo.readlines()
        with open("Respuesta.txt", "r") as archivo:
            self.respuestas = archivo.readlines()
            
    
    def elegir_adivinanza(self):
        if not self.adivinanzas:  
            return None, None, None  
        i = random.randint(0, len(self.adivinanzas) - 1)
        adivinanza = self.adivinanzas[i]
        pista = self.pistas[i]
        respuesta = self.respuestas[i]
        return adivinanza, pista, respuesta

    def jugar(self):
        Mensaje = Mensajes()
        while True:
            adivinanza, pista, respuesta = self.elegir_adivinanza()
            if not adivinanza:  
                Mensaje.warning_msj("")
                break
            t= "-" * 150
            Mensaje.mst(f"Adivinansa:\n{t}\n{adivinanza}\n{t}")
            while True:
                respuesta_usuario = input("Indique tu respuesta: ")
                if respuesta_usuario.strip().lower().split(':') == respuesta.strip().lower().split(':'):
                    Mensaje.ok_msg("¡Correcto!")
                    self.adivinanzas.remove(adivinanza)
                    self.pistas.remove(pista)
                    self.respuestas.remove(respuesta)
                    self.pistas_disponibles += 1
                    self.pistas_acertadas += 1
                    break
                else:
                    Mensaje.error_msj("Respuesta incorrecta")
                    if self.pistas_disponibles > 0:
                        Mensaje.mst(f"Pistas disponibles: {self.pistas_disponibles}")
                        u = input("¿Quieres usar una pista? (s/n): ")
                        if u.strip().lower() == "s":
                            Mensaje.mst(pista)
                            self.pistas_disponibles -= 1
                            
                    else:
                        Mensaje.warning_msj(f"No tienes mas pistas disponibles.\nLa respuesta es: {respuesta}")
                        self.adivinanzas.remove(adivinanza)
                        self.pistas_acertadas = 0
