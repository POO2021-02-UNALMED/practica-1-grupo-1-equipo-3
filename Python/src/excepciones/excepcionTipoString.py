from msilib.schema import _Validation_records
from multiprocessing.sharedctypes import Value
from excepciones.excepcionTipo import ExcepcionTipo
from tkinter import E, messagebox

class ExcepcionTipoString(ExcepcionTipo):

    def __init__(self, errados):
        super().__init__("Datos que no corresponden: " + errados)
        
        
        
    
    @classmethod
    def tipoString(cls, criterios, valores):
        mensaje = ""
        advertencia = ""
        errado= 0
        for i in range(len(valores)):
            try:
                num =  float(valores[i])
                if i == len(valores) - 1:
                    mensaje += criterios[i] + "\n\n"
                else:
                    mensaje += criterios[i] + ","
                advertencia += "El valor del campo \"" + criterios[i] + "\" no puede ser un número\n\n"
                errado += 1
            except ValueError:
                pass
        if errado > 0:
            messagebox.showwarning(title= "Advertencia", message= advertencia)
            raise  ExcepcionTipoString(mensaje) 
            

                


            
