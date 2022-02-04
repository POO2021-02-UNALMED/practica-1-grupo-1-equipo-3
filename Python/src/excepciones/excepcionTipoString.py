from msilib.schema import _Validation_records
from multiprocessing.sharedctypes import Value
from excepciones.excepcionTipo import ExcepcionTipo
from tkinter import E, messagebox

class ExcepcionTipoString(ExcepcionTipo):

    def __init__(self, errados):
        super().__init__("Datos que no corresponden: " + errados)
        
        
        
    
    @classmethod
    def tipoString(cls, criterios, valores): #Excepcion que maneja si uno o varios datos son compuestos de solo números
        mensaje = ""
        advertencia = ""
        errado= 0
        for i in range(len(valores)):
            try:
                num =  float(valores[i]) #Si el dato puede hacer esta conversion significa un caso desfavorable
                if i == len(valores) - 1:
                    mensaje += criterios[i] + "\n\n"
                else:                               #Se construye el mensaje que va a ser pasado al constructor del padre
                    mensaje += criterios[i] + ","
                #Se construye la cadena que va acompañar el messsagebox de advertencia
                advertencia += "El valor del campo \"" + criterios[i] + "\" no puede ser un número\n\n"
                errado += 1
            except ValueError: #Se identifica los casos favorables si se arroja un ValueError si se intenta hacer la conversion del dato a un float
                pass #No ocurre nada porque es el caso favorable
        if errado > 0:
            messagebox.showwarning(title= "Advertencia", message= advertencia) #Se muestra el messagebox de advertencia y se pasa el mensaje al padre mediante el constructor de la clase.
            raise  ExcepcionTipoString(mensaje) 
            

                


            
