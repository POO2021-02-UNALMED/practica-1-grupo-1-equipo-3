from excepciones.excepcionTipo import ExcepcionTipo
from tkinter import messagebox

class ExcepcionTipoInt(ExcepcionTipo):
    
    def __init__(self, errados):
        self._errados = errados
        super().__init__("Datos que no corresponden: " + self._errados)
        
    @classmethod
    def tipoInt(cls, criterios, valores):
        mensaje = ""
        advertencia = ""
        errados = 0
        for i in range(len(valores)):
            try:
                num = int(valores[i])
                if num <= 0:
                    raise ValueError
            except ValueError:
                if i == len(valores)-1:
                    mensaje += criterios[i] + "\n\n"
                else:
                    mensaje += criterios[i] + ", "
                advertencia += "El valor del campo \"" + criterios[i] + "\" debe ser un número entero mayor a 0\n\n"
                errados += 1
        if errados > 0:
            messagebox.showwarning(title="Advertencia",
                                   message=advertencia)
            raise ExcepcionTipoInt(mensaje)