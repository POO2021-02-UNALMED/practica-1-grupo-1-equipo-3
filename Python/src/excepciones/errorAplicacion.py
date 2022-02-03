class ErrorAplicacion(Exception):
    
    def __init__(self, mensaje):
        self._mensaje = mensaje
        super().__init__("Manejo de errores de la Aplicación:\n" + self._mensaje)
        
    def mensaje(self):
        print("Manejo de errores de la Aplicación:\n" + self._mensaje)