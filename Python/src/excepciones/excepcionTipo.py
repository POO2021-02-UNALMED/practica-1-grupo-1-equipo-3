from excepciones.errorAplicacion import ErrorAplicacion

class ExcepcionTipo(ErrorAplicacion): #Excepcion que maneja los si los tipos de datos que entran a la aplicacion, si son los deseados.
    
    def __init__(self, mensaje):
        super().__init__("¡El tipo de dato no corresponde al solicitado!\n" + mensaje)
        self._mensaje = mensaje
        