# CLASE CREADA POR JUAN JOSE MONSALVE MARIN

"""
La clase Especie de tipo Enum se crea con el fin de definir los 5 unicos posibles objetos que se podran crear de esta clase, 
los cuales son MAMIFERO, AVE, REPTIL, PEZ y ANFIBIO, donde cada uno de estos objetos cuenta con tres atributos. 
Nombre de tipo String que corresponde al nombre de la especie, dieta de tipo String que corresponde a la dieta 
de la especie que se encuentra en el zoologico y promedioVida que corresponde al promedio de vida de los animales de esa especie 
que se encuentran en el zoologico.   
"""

from enum import Enum

class Especie(Enum):

    #_TOTALESPECIE = 5

    # Se generan los 5 diferentes objetos de esta clase con sus respectivos atributos.
    MAMIFERO = ("Mamifero", "omnivoro", 40)
    AVE = ("Ave", "granivoro", 25)
    REPTIL = ("Reptil", "carnivoro", 35)
    PEZ = ("Pez", "omnivoro", 30)
    ANFIBIO = ("Anfibio", "insectivoro", 15)

    """
    Enum es una clase especial que limita la creacion de objetos a los especificados en su clase 
    (por eso su constructor es privado), pero estos objetos pueden tener atributos como cualquier otra clase.
    """
    def __init__(self, nombre, dieta, promedioVida):
        self.nombre = nombre
        self.dieta = dieta
        self.promedioVida = promedioVida

    
    """
    El metodo info() es implementado de la interfaz Entidad y definido aqui. Sirve para generar el String que sera 
	 * usado para imprimir por consola los datos de la especie en caso de ser requeridos en alguna de las funcionalidades 
	 * de la aplicacion.
    """
    def info(self):
        cadena = ("Nombre: " + self.getNombre() + 
        "\nDieta: " + self.getDieta() + 
        "\nPromedio de vida: " + str(self.getPromedioVida()) + " años")
        
        return cadena

    # De aqui en adelante se definen los metodos get de la clase especie.
    def getNombre(self):
        return self.nombre

    def getDieta(self):
        return self.dieta

    def getPromedioVida(self):
        return self.promedioVida

    def getTotalEspecies(self):
        return self.TOTALESPECIE
    

    
