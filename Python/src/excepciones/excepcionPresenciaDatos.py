from excepciones.excepcionPresencia import ExcepcionPresencia

class ExcepcionPresenciaDatos(ExcepcionPresencia):
    advertencia = ""
    
    def __init__(self, faltantes):
        self._faltantes = faltantes
        super().__init__("Tipo de elemento: Dato\nDatos faltantes: " + self._faltantes)
        
    @classmethod
    def presenciaDatos(cls, criterios, valores):
        mensaje = ""
        cls.advertencia = "Por favor llene todos los campos.\nLos siguientes campos faltan por llenar:\n\n"
        faltantes = 0
        for i in range(len(valores)):
            if valores[i] == "":
                if i == len(valores)-1:
                    mensaje += criterios[i]
                else:
                    mensaje += criterios[i] + ", "
                cls.advertencia += criterios[i] + "\n"
                faltantes += 1
        if faltantes > 0:
            raise ExcepcionPresenciaDatos(mensaje)