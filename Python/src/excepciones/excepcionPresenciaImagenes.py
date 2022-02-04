
from PIL import Image
from tkinter import messagebox
from excepciones.excepcionPresencia import ExcepcionPresencia

class ExcepcionPresenciaImagenes(ExcepcionPresencia): #Excepcion que maneja la presencia o no de imagenes usadas en la aplicacion.
    
    def __init__(self, faltantes):
        self._faltantes = faltantes
        super().__init__("Tipo de elemento: Imagen\nImagenes faltantes: " + self._faltantes)

    @classmethod
    def presenciaImagenes(cls, direcciones):
        mensaje = ""
        advertencia= "Por favor asegurese que las siguientes imagenes existen en sus respectivos directorios :\n\n"
        faltantes= 0  #Contador de que si hace falta imagenes
        for i in range(len(direcciones)):
            try:
                Image.open(direcciones[i]) #Se detecta que no se encuentra la imagen con un FileNotFoundError
            except FileNotFoundError:
                if i == len(direcciones) - 1:
                     mensaje += direcciones[i] + "\n\n"
                else:                                   #Se construye el mensaje que se va a enviar al constructo del padre.
                    mensaje += direcciones[i] + ","
                advertencia += direcciones[i].split("/")[-1] + "\n" #Se construye imagen que se va a mostrar en un messagebox
                faltantes += 1
        if faltantes > 0: 
            messagebox.showwarning(title= "Advertencia", message= advertencia) #Se muestra el messagebox de advertencia
            raise ExcepcionPresenciaImagenes(mensaje) #Se pasa el mensaje al constructor del padre mediante el constructor de la clase
                

