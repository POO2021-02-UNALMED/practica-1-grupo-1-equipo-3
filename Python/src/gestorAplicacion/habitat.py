#CLASE CREAD POR MATEO CARVAJAL SÁNCHEZ

from gestorAplicacion.entidad import Entidad


#Clase HabItat diseñada con el fin de definir los atributos y los metodos de los objetos tipo habitat,
#que corresponden a los habitats donde habitan los animales del zoologico.

#Se heredad de la interfaz Entidad para sobreescribir el metodo info() de esta.
class Habitat(Entidad):
    
    _totalHabitats = 0

    # El constructor de la clase Hábitat: Recibe como parámetro los atributos nombre, ambientación 
	# y capacidad máxima, los cuales corresponden respectivamente al nombre, ambientación 
	# y capacidad máxima del hábitat a crear. A los atributo limpio e identificación se les asigna
	# un valor automáticamente. El objeto creado va a ser añadido a la lista de hábitats de la 
	# administración mediante el método  estático addHabitats de la clase 	Administración y se le suma 1 al 
	# atributo cantidadHabitats para llevar la cuenta del número de hábitats del zoológico. Aunque no es asignado
	# a nada el atributo animalesAsociados corresponde a los animales que viven dentro del habitat.

    def __init__(self, nombre, ambientacion = "Ninguna", capacidadMaxima = 999):
        from gestorAplicacion.administracion import Administracion
        if(not Administracion.getHabitats()):
            self._identificacion = 1 
        else:
            self._identificacion = Administracion.getHabitats()[-1].getIdentificacion() + 1 
        
        self._nombre = nombre
        self._ambientacion = ambientacion
        self._CAPACIDADMAXIMA = capacidadMaxima
        self._limpio= True
        self._animalesAsociados = []
        Habitat._totalHabitats += 1
        Administracion.addHabitats(self)
        

    #Metodo info() heredado de la interfaz Entidad.
    def info(self):
        if(not self._animalesAsociados):
            cadena = ("\nIdentificación: " + str(self.getIdentificacion()) + "\nNombre: " + self.getNombre() + "\nAmbientación: " + self.getAmbientacion() + 
            "\nCantidad de Animales actual: " + str(self.cantidadAnimales()) + "\nCapacidad máxima: " + str(self.getCapacidadMaxima()) + " animales")
        else:
            cadena = ("\nIdentificación: " + str(self.getIdentificacion()) + "\nNombre: " + self.getNombre()  +"\nAmbientación: " + self.getAmbientacion() + 
            "\nCantidad de Animales actual: " + str(self.cantidadAnimales()) + "\nCapacidad máxima: " + str(self.getCapacidadMaxima()) + " animales" + 
            "\nEspecie que lo habita: " + self.getAnimalesAsociados()[0].getEspecie().getNombre())
        
        return cadena
    
    #MÉTODOS GET Y SET
    def getCapacidadMaxima(self):
        return self._CAPACIDADMAXIMA
    
    def setIdentificacion(self, id):
        self._identificacion = id
    
    def getIdentificacion(self):
        return self._identificacion
    
    def setNombre(self, nombre):
        self._nombre = nombre 
    
    def getNombre(self):
        return self._nombre
    
    def setAmbientacion(self, ambientacion):
        self._ambientacion = ambientacion

    def getAmbientacion(self):
        return self._ambientacion
    
    def setLimpio(self, limpio):
        self._limpio = limpio
    
    def isLimpio(self):
        return self._limpio
    
    def setAnimalesAsociados(self, animales):
        self._animalesAsociados = animales
    
    def getAnimalesAsociados(self):
        return self._animalesAsociados
    
    def getEspecie(self):
        if self.getAnimalesAsociados() == []:
            return None
        else:
            return self.getAnimalesAsociados()[0].getEspecie()
    
    def cantidadAnimales(self):
        return len(self._animalesAsociados)
    #Metodo para añadir animales a la lista del atributo animalesAsociados
    def addAnimalesAsociados(self, animal):
        self._animalesAsociados.append(animal)
    
    #Metodo para quitar animales de la lista del atributo animalesAsociados
    def removeAnimalesAsociados(self,animal):
        self._animalesAsociados.remove(animal)

    @classmethod
    def getTotalHabitats(cls):
        return cls._totalHabitats
    
    def setTotalHabitats(cls,nuevo):
        cls._totalHabitats=nuevo