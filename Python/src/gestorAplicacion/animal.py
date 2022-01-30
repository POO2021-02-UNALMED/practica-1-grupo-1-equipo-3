
class Animal():
    
    _totalAnimales = 0

    def __init__(self, especie, habitat, genero, edad, peso):
        from administracion import Administracion

        if (not Administracion.getAnimales()):
            self._identificacion = 1
        else:
            self._identificacion = Administracion.getAnimales[-1].getIdentificacion() + 1
        
        self._especie = especie
        self._habitat = habitat
        self._genero = genero
        self._edad = edad
        self._peso = peso
        self._estadoAnimo = True
        self._estadoSalud = True
        self._alimentado = True
        Animal._totalAnimales += 1
        Administracion.addAnimales(self)

    
    def info(self):
        cadena = ("Identificacion: " + str(self.getIdentificacion()) + "\nEspecie: " + self.getEspecie().getNombre() + 
        "\nHábitat: " + self.getHabitat().getNombre() + "(" + self.getHabitat().getAmbientacion() + ")" + "\nGénero: " + 
        self.getGenero() + "\nEdad: " + str(self.getEdad()) + "años" + "\nPeso: " + str(self.getPeso()))
        
        return cadena


    def setIdentificacion(self, id):
        self._identificacion = id

    def getIdentificacion(self):
        return self._identificacion
        
    def setEspecie(self, especie):
        self._especie = especie

    def getEspecie(self):
        return self._especie

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getHabitat(self):
        return self._habitat

    def setGenero(self, genero):
        if(genero in ("f", "m")):
            self._genero = genero

    def getGenero(self):
        return self._genero

    def setEdad(self, edad):
        self._edad = edad

    def getEdad(self):
        return self._edad

    def setPeso(self, peso):
        self._peso = peso

    def getPeso(self):
        return self._peso

    def setEstadoAnimo(self, animo):
        self._estadoAnimo = animo

    def isEstadoAnimo(self):
        return self._estadoAnimo

    def setEstadoSalud(self, salud):
        self._estadoSalud = salud

    def isEstadoSalud(self):
        return self._estadoSalud

    def setAlimentado(self, alimentado):
        self._alimentado = alimentado
    
    def isAlimentado(self):
        return self._alimentado

    def morir(self):
        from administracion import Administracion
        Animal._totalAnimales -= 1
        self._habitat.removeAnimalesAsociados(self)
        Administracion.removeAnimales(self)


    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales    

    

