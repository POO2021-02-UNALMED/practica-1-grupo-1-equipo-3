from excepciones.excepcionPresencia import ExcepcionPresencia
from tkinter import messagebox

class ExcepcionPresenciaDatos(ExcepcionPresencia): #Excepcion que maneja la falta de datos de entrada en las funcionalidades.
    
    def __init__(self, faltantes):
        self._faltantes = faltantes
        super().__init__("Tipo de elemento: Dato\nDatos faltantes: " + self._faltantes)
        
    @classmethod
    def presenciaDatos(cls, criterios, valores):
        mensaje = ""
        advertencia = "Por favor llene todos los campos.\nLos siguientes campos faltan por llenar:\n\n"
        faltantes = 0 #Contador de widgets entry sin datos
        for i in range(len(valores)):
            if valores[i] == "": 
                if i == len(valores)-1:
                    mensaje += criterios[i] + "\n\n"
                else:                                #Se construye el mensaje que va a pasar al constructor del padre por si hay entries si datos.
                    mensaje += criterios[i] + ", "
                advertencia += criterios[i] + "\n" #Se construye la cadena que se va a mostrar en un messagebox de advertencia
                faltantes += 1
        if faltantes > 0:
            messagebox.showwarning(title="Advertencia", #Se muestra el mensaje y se pasa el mensaje al constructor del padre mediante el constructor de la clase
                                   message=advertencia)
            raise ExcepcionPresenciaDatos(mensaje)