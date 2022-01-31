class Habitat:
    
    _totalHabitats = 0

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

    
    def info(self):

        if(not self._animalesAsociados):
            cadena = ("Identificación: " + str(self.getIdentificacion()) + "\nNombre" + self.getNombre() + "\nAmbientación: " + self.getAmbientacion() + 
            "\nCantidad de Animales actual: " + str(self.cantidadAnimales()) + "\nCapacidad máxima: " + str(self.getCapacidadMaxima() + "animales"))
        else:
            cadena = ("Identificación: " + str(self.getIdentificacion()) + "\nNombre" + self.getNombre()  +"\nAmbientación: " + self.getAmbientacion() + 
            "\nCantidad de Animales actual: " + str(self.cantidadAnimales()) + "\nCapacidad máxima: " + str(self.getCapacidadMaxima() + "animales" + 
            "\nEspecie que lo habita: " + self.getAnimalesAsociados()[0].getEspecie().getNombre()))
        
        return cadena
    
    
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
    
    def addAnimalesAsociados(self, animal):
        self._animalesAsociados.append(animal)
    
    def removeAnimalesAsociados(self,animal):
        self._animalesAsociados.remove(animal)