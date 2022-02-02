#CLASE CREADA POR MATEO CARVAJAL SÁNCHEZ

#La clase animal esta diseñada con el fin de definir los atributos y metodos de 
# los objetos tipo animal que corresponderian a los animales del zoologico. 
# En particular se define el metodo morir que elimina todos las referencias 
# del objeto tipo animal de la aplicacion y el metodo getTotalAnimales que junto 
# con el atributo totalAnimales nos permite tener una cuenta de cuantos 
# animales hay en el sistema.

from gestorAplicacion.entidad import Entidad

#Se hereda de la interfaz entidad para sobreescribir el metodo info() de esta.
class Animal(Entidad):
    
    
    _totalAnimales = 0
    
    #Constructor de la clase Animal: Recibe como parametros los atributos especie, habitat, 
	#genero, edad y peso que corresponden respectivamente a la especie, habitat, genero, 
	#edad y peso del animal a crear. A los atributos estadoAnimo, estadoSalud, alimentado
	#y identificacion se les asigna un valor automaticamente. El objeto creado va a ser 
	#añadido a la lista de animales de la administracion mediante el medoto estatico 
	#de la clase Adminsitracion addAnimalesAsociados(). Ademas se le sumara 1 al atributo
	#totalAnimales para lleavr la cuenta de los animales que hay dentro del zoologico.*/
   
    def __init__(self, especie, habitat, genero, edad, peso):
        from gestorAplicacion.administracion import Administracion

        if (not Administracion.getAnimales()):
            self._identificacion = 1
        else:
            self._identificacion = Administracion.getAnimales()[-1].getIdentificacion() + 1
        
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
        habitat.addAnimalesAsociados(self)

    #Metodo heredado de Entidad el cual permite imprimir informacion del animal en caso de que sea necesario en alguna funcionaldad.
    def info(self):
        cadena = ("\nIdentificacion: " + str(self.getIdentificacion()) + "\nEspecie: " + self.getEspecie().getNombre() + 
        "\nHábitat: " + self.getHabitat().getNombre() + "(" + self.getHabitat().getAmbientacion() + ")" + "\nGénero: " + 
        self.getGenero() + "\nEdad: " + str(self.getEdad()) + "años" + "\nPeso: " + str(self.getPeso()))
        
        return cadena

    #METODOS SET Y GET 
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

    #Metodo morir que elimina todas las referencias del objeto tipo animal que lo invoque.
    def morir(self):
        from gestorAplicacion.administracion import Administracion
        Animal._totalAnimales -= 1
        self._habitat.removeAnimalesAsociados(self)
        Administracion.removeAnimales(self)


    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales    

    

