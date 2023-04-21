class mensajes:
    num_mensajes = 0

    def contador(self):
        self.num_mensajes = 0

    def get_num_msj(self):
        """Obtiene el número total de mensajes registrados."""
        return self.num_mensajes 

    def ok_msg(self, msj: str):
        """
        Muestra que el mensaje esta correcto o bien.

        msj: El mensaje a validar.
        """
        self.num_mensajes += 1
        print(f'\n✔ Bien: {msj} ✔\n')

    def error_msj(self,msj):
        """Muestra un mensaje de error.
        
         msj: mensaje de error que mostrara por pantalla.
        """
        self.num_mensajes += 1
        print(f'\n❌ Error:{msj} ❌ \n')

    def warning_msj(self, warning: str):
        """
        Muestra un mensaje de advertencia.

        warning: La advertencia a mostrar.
        """
        self.num_mensajes += 1
        print(f'\n Advertencia ⚠ : {warning} \n')

    def pedir_datos(self):
        """
        Pide que el los datos que el ususario necesita.

        return: retorna el input que el usuario necesita.
        """
        try:
            self.num_mensajes += 1
            num = input("Ingrese un número: ")
            return num
        except ValueError:
            print("Debe ingresar un número enter")