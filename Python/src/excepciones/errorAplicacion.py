class ErrorAplicacion(Exception): #Excepcion que maneja las excepciones inventadas, en la aplicacion
    
    def __init__(self, mensaje):
        self._mensaje = mensaje
        super().__init__("\n\nManejo de errores de la Aplicación:\n" + self._mensaje)
        
    def mensaje(self):
        print("Manejo de errores de la Aplicación:\n" + self._mensaje)