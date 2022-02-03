from excepciones.excepcionPresencia import ExcepcionPresencia
from tkinter import messagebox

class ExcepcionPresenciaDatos(ExcepcionPresencia):
    
    def __init__(self, criterios, valores):
        self._criterios = criterios
        self._valores = valores
        self._mensaje = "Tipo de elemento: Dato\nDatos faltantes: "
        self._advertencia = "Por favor llene todos los campos. Los siguientes campos no tienen ningún valor:\n\n"
        self._faltantes = 0
        for i in range(len(self._valores)):
            if self._valores[i] == "":
                self._mensaje = self._mensaje + self._criterios[i] + " "
                self._advertencia = self._advertencia + self._criterios[i] + "\n"
                self._faltantes += 1
        if self._faltantes > 0:
            raise ExcepcionPresenciaDatos(self._criterios, self._valores)
        
        super().__init__(self._mensaje)
        
    def mostrarAdvertencia(self):
        messagebox.showwarning(title="Advertencia",
                               message=self._advertencia)