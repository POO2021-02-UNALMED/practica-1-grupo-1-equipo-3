# CLASE CREADA POR JUAN JOSE MONSALVE MAR�N

""" 
La clase Veterinario se crea con la finalidad de definir los diferentes atributos y metodos de los objetos de tipo veterinario. 
En esta clase se define el atributo "especialidad" el cual corresponde a la especie que cada veterinario esta especializado 
en tratar. Se definen los metodos de revisar(), el cual se encarga de verificar el estado de salud de los animales del 
zoologico y se define el metodo curarAnimal() el cual se encarga de que se implementen los cuidados y procedimientos 
necesarios para curar al animal. Esta clase hereda de la clase Empleado
"""

from gestorAplicacion.empleado import Empleado

class Veterinario(Empleado):

    """
    Constructor de la clase Veterinario: Recibe como parámetros los atributos identificación, nombre, sueldo 
	y especieAsignada, los cuales respectivamente corresponden a la identificación única, nombre, sueldo 
	y especieAsignada del Veterinario a ser creado. Los primeros tres atributos son heredados de la clase padre 
	Empleado, y el cuarto se asigna normalmente al cuidador creado. Luego se relaciona 
	con al objeto de la especie asignada al cuidador dicho objeto cuidador, e igualmente el cuidador se asocia 
	con el objeto único de tipo Administracion, esto a través de las listas que estas clases manejan y por medio
	de los métodos addCuidadorAsignado de la clase Especie y addVeterinarios de la clase Administracion. 
    """
    def __init__(self, nombre, sueldo, especieAsignada):
        from gestorAplicacion.administracion import Administracion
        if len(Administracion.getVeterinarios())==0:
            identificacion = 1
        else:
            identificacion = Administracion.getVeterinarios()[-1].getIdentificacion() + 1
        super().__init__(identificacion, nombre, sueldo);
        self._especieAsignada = especieAsignada
        Administracion.addVeterinarios(self)

    """
    El método info() es implementado de la interfaz Entidad y definido aquí. Sirve para generar el String que será 
	usado para imprimir por consola los datos del cuidador en caso de ser requeridos en alguna de las funcionalidades 
	de la aplicación.
    """
    def info(self):
        return ("\nTipo de empleado: VETERINARIO" + 
                "\nIdentificación: " + str(self.getIdentificacion()) + 
                "\nNombre: " + self.getNombre() + 
                "\nSueldo: " + str(self.getSueldo()) + 
                "\nEspecie asignada: " + self.getEspecieAsignada().getNombre());

    """
    El metodo revisar(Animal animal) es el metodo encargado de verificar el estado de saludo de los animales del zoologico. 
    Este metodo admite como parametro un objeto de tipo Animal y con este verifica el estado de salud de los animales.  
    """
    def revisarAnimal(animal):
        return animal.isEstadoSalud()

    """
    El metodo curarAnimal(Animal animal) se encarga de cambiar el estado de salud de un animal  del zoologico cuando se encuentra enfermo (false), 
    luego de que un veterinario realice todos los procedimientos necesarios para curar al animal. Este metodo admite como parametro un objeto de tipo animal.  
    """
    def curarAnimal(animal):
        animal.setEstadoSalud(True)

    # De aqui en adelante se definen los metodos set y get del atributo "especialidad".
    def getEspecieAsignada(self):
        return self._especieAsignada
	
    def setEspecieAsignada(self, especieAsignada):
        self._especieAsignada = especieAsignada