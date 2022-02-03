from excepciones.excepcionPresencia import ExcepcionPresencia
from tkinter import messagebox

class ExcepcionPresenciaDatos(ExcepcionPresencia):
    
    def __init__(self, faltantes):
        self._faltantes = faltantes
        super().__init__("Tipo de elemento: Dato\nDatos faltantes: " + self._faltantes)
        
    @classmethod
    def presenciaDatos(cls, criterios, valores):
        mensaje = ""
        advertencia = "Por favor llene todos los campos.\nLos siguientes campos faltan por llenar:\n\n"
        faltantes = 0
        for i in range(len(valores)):
            if valores[i] == "":
                if i == len(valores)-1:
                    mensaje += criterios[i] + "\n\n"
                else:
                    mensaje += criterios[i] + ", "
                advertencia += criterios[i] + "\n"
                faltantes += 1
        if faltantes > 0:
            messagebox.showwarning(title="Advertencia",
                                   message=advertencia)
            raise ExcepcionPresenciaDatos(mensaje)