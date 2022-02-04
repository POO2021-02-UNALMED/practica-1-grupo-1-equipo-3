from excepciones.excepcionTipo import ExcepcionTipo
from tkinter import messagebox

class ExcepcionTipoFloat(ExcepcionTipo): #Excepcion que maneja si uno o varios datos reales son mayores que 0
    
    def __init__(self, errados):
        self._errados = errados
        super().__init__("Datos que no corresponden: " + self._errados)
        
    @classmethod
    def tipoFloat(cls, criterios, valores):
        mensaje = ""
        advertencia = ""
        errados = 0 #Contador de datos menores o iguales que 0
        for i in range(len(valores)):
            try:
                num = float(valores[i])
                if num <= 0.0:
                    raise ValueError #Se identifican los casos desfavorables con un ValueError
            except ValueError:
                if i == len(valores)-1:
                    mensaje += criterios[i] + "\n\n"
                else:                                #Se construye el mensaje que va a ser pasado al constructor del padre
                    mensaje += criterios[i] + ", "
                #Se construye la cadena que se va mostrar junto al messagebox de advertencia    
                advertencia += "El valor del campo \"" + criterios[i] + "\" debe ser un número real mayor a 0.0\n\n"
                errados += 1
        if errados > 0:
            messagebox.showwarning(title="Advertencia", #Se muestra el messagebox de advertencia y se pasa el mensaje al padre mediante el constructor de la clase.
                                   message=advertencia)
            raise ExcepcionTipoFloat(mensaje)