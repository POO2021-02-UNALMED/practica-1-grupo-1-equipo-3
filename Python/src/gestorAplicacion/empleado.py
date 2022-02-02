# CLASE CREADA POR DAVID MATEO GARCÍA

# La clase Empleado se crea con el fin de ser heredada por las clases Cuidador y Veterinario,
# pues en esta clase se definen los atributos correspondientes a la identificación del empleado, 
# al nombre del empleado, al sueldo del empleado y a si este empleado se le ha pagado el sueldo
# o está a la espera de esto. Además, esta clase define los métodos get y set para dichos atributos.
# La clase es definida como abstracta pues define el método abstracto toString(), método necesario
# para visualizar los datos del empleado. 

from gestorAplicacion.entidad import Entidad

class Empleado(Entidad):
	
	
	# Constructor de la clase Empleado: Recibe como parámetros los atributos identificación, nombre 
	# y sueldo, los cuales respectivamente corresponden a la identificación única, nombre y sueldo 
	# del empleado a ser creado. 
    def __init__(self, identificacion, nombre, sueldo, pagado = False):
        self.identificacion = identificacion
        self.nombre = nombre
        self.sueldo = sueldo
	
	# Método abstracto declarado para ser definido por las clases Cuidador y Veterinario, que lo heredan.
    def revisar(self, animal):
        pass
	
    def info(self): #//Para la ligadura dinámica
        return "\nIdentificación: " + str(self.getIdentificacion()) + "\nNombre: " + self.getNombre() + "\nSueldo: " + str(self.getSueldo())
	
	# DE ACÁ PARA ABAJO ESTÁN LOS MÉTODOS GET Y SET
    def getIdentificacion(self):
        return self.identificacion
	
    def setIdentificacion(self, identificacion):
        self.identificacion = identificacion
	
    def getNombre(self):
        return self.nombre
	
    def setNombre(self, nombre):
        self.nombre = nombre
	
    def getSueldo(self):
        return self.sueldo
	
    def setSueldo(self, sueldo):
        self.sueldo = sueldo
	
    def isPagado(self):
        return self.pagado
	
    def setPagado(self, estado):
        self.pagado=estado