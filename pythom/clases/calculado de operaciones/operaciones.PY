from mensajes import mensajes
class operaciones:
    operaciones_totales = int
    mensaje = mensajes()
    def __init__(self):
        self.operaciones_totales = 0
   
    def suma(self,N1:int, N2: int): 
        """ Suma los datos que pide el ususario.

            N1:  es el primer dato del usuario.
            N2: es el segundo dato de usuario.
            
        """
        r = N1 + N2
        self.operaciones_totales += 1
        mensaje = mensajes()
        mensaje.ok_msg(f"La suma de {N1} y {N2} es: {r}")
       
    def division(self, N1:int,N2: int):
        """ divide los datos que pide el ususario.

            N1: es el primer dato del usuario.
            N2: es el segundo dato de usuario.
            
        """
        try:
            r = round(N1 / N2, 3)
            self.operaciones_totales += 1
            mensaje = mensajes()
            mensaje.ok_msg(f"La división de {N1} y {N2} es: {r}")
        except (ZeroDivisionError, TypeError):
            mensaje.error_msj("No se puede dividir por cero")
                                        
    def cuadrado(self,N1:int): 
        """ eleva el cuadrado que pide el ususario.

            N1: es el dato que vamos a elevar al cuadrado
            
        """
        mensaje = mensajes()
        if N1 > 0:
            r = N1 ** 2
            self.operaciones_totales += 1
            mensaje.ok_msg(f"El cuadrado de {N1} es: {r}")

        elif N1 < 0:
            mensaje.warning_msj("El número debe ser positivo para poder calcular su cuadrado")
        
        else:
            mensaje.error_msj("Es Imposible calcular el cuadrado")
      
    def ecuacion2grado(self, a:int,b:int,c:int): 
        """
        calcula los 2 resultado de la ecuacion.

        a: es el primer datos de la ecuacion.
        b: es el segundo datos de la ecuacion.
        c: es el tercero datos de la ecuacion.
        """
        e = b**2 - 4*a*c
        if e >= 0:
            raiz = (e)**0.5
            x1 = (-b + raiz) / (2*a)
            x2 = (-b - raiz) / (2*a)
            mensaje = mensajes()
            mensaje.ok_msg(f"Las soluciones son:\nDe X1= {x1} y X2= {x2}")
        else:
            mensaje.error_msj("La ecuación no tiene soluciones reales.")