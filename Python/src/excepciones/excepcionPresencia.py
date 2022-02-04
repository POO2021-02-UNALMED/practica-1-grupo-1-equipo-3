from excepciones.errorAplicacion import ErrorAplicacion 

class ExcepcionPresencia(ErrorAplicacion): #Excepcion que maneja la presencia o no de datos, imagene, etc. Dentro de la aplicación
    
    def __init__(self, mensaje):
        self._mensaje = mensaje
        super().__init__("¡No se ha encontrado el elemento al que se hace referencia!\n" + self._mensaje)
        