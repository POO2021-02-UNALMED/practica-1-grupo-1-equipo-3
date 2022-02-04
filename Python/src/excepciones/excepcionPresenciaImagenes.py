
from PIL import Image
from tkinter import messagebox
from excepciones.excepcionPresencia import ExcepcionPresencia

class ExcepcionPresenciaImagenes(ExcepcionPresencia):
    
    def __init__(self, faltantes):
        self._faltantes = faltantes
        super().__init__("Tipo de elemento: Imagen\nImagenes faltantes: " + self._faltantes)

    @classmethod
    def presenciaImagenes(cls, direcciones):
        mensaje = ""
        advertencia= "Por favor asegurese que las siguientes imagenes existen en sus respectivos directorios :\n\n"
        faltantes= 0
        for i in range(len(direcciones)):
            try:
                Image.open(direcciones[i])
            except FileNotFoundError:
                if i == len(direcciones) - 1:
                     mensaje += direcciones[i] + "\n\n"
                else:
                    mensaje += direcciones[i] + ","
                advertencia += direcciones[i].split("/")[-1] + "\n"
                faltantes += 1
        if faltantes > 0:
            messagebox.showwarning(title= "Advertencia", message= advertencia)
            raise ExcepcionPresenciaImagenes(mensaje)
                

if __name__ == "main":
    ExcepcionPresenciaImagenes.presenciaImagenes(["Imagenes/Animales/4.jpg", "Imagenes/Animales/5.jpg", "Imagenes/Animales/6.jpg"])