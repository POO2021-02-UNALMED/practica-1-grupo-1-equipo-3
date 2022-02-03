from excepciones.errorAplicacion import ErrorAplicacion

class ExcepcionTipo(ErrorAplicacion):
    
    def __init__(self, mensaje):
        self._mensaje = mensaje
        super().__init__("¡El tipo de dato no corresponde al solicitado!\n" + self._mensaje)