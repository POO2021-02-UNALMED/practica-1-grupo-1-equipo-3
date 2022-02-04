from excepciones.excepcionPresencia import ExcepcionPresencia
from tkinter import messagebox

class ExcepcionPresenciaArchivos(ExcepcionPresencia): #Excepcion que maneja la presencia o no de archivos para que se pueda hacer el proceso de
    def __init__(self, faltantes):                    #serializacion y deserializacion.
        self._faltantes = faltantes
        super().__init__("Tipo de elemento: Archivo\n Archivos faltantes: " + self._faltantes)

    
    @classmethod
    def presenciaArchivos(cls, direcciones):
        mensaje = ""
        advertencia= "Por favor asegurese que los siguientes archivos existen en sus respectivos directorios :\n\n"
        faltantes= 0 #Contador de archivos que faltan
        for i in range(len(direcciones)):
            try:
                f= open(direcciones[i], "r") #Se detecta que un archivo falta con un FileNotFoundError.
            except FileNotFoundError:
                if i == len(direcciones) - 1:
                    mensaje += direcciones[i] +"\n\n" 
                else:                                 #Se construye el mensaje que se va a mandar al consturctor del padre en caso de que no haya archivo.
                    mensaje += direcciones[i] + ","
                
                advertencia +=  direcciones[i].split("/")[-1] + "\n" #Se construye la cadena que se va a mostrar junto al messagebox de advertencia.
                faltantes += 1
                   
        if faltantes > 0 :
            messagebox.showwarning(title= "Advertencia", message= advertencia) #Se muestra el messagebox de emergencia y se manda el mensaje al constructor del padre medainte el constructor de la clase.
            raise ExcepcionPresenciaArchivos(mensaje)


