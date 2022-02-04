# CLASE CREADA POR DAVID MATEO GARCÍA

# La clase Cuidador se crea con el fin de manejar los objetos correspondientes a los cuidadores 
# del zoológico. En esta clase se define el atributo especieAsignada, correspondiente a la especie 
# que el cuidador tiene asignada. Además se definen los métodos get y set para ese atributo y los 
# métodos necesarios para implementar las funcionalidades que requieran de algún cuidador. 

from gestorAplicacion.empleado import Empleado

class Cuidador(Empleado):
	
	# Constructor de la clase Cuidador: Recibe como parámetros los atributos identificación, nombre, sueldo 
	# y especieAsignada, los cuales respectivamente corresponden a la identificación única, nombre, sueldo 
	# y especieAsignada del cuidador a ser creado. Los primeros tres atributos son pasados a la clase padre 
	# de esta clase, la clase Empleado, y el cuarto se asigna normalmente al cuidador creado. Luego se relaciona 
	# con al objeto de la especie asignada al cuidador dicho objeto cuidador, e igualmente el cuidador se asocia 
	# con el objeto único de tipo Administracion, esto a través de las listas que estas clases manejan y por medio
	# de los métodos addCuidadorAsignado de la clase Especie y addCuidadores de la clase Administracion. 
    def __init__(self, nombre, sueldo, especieAsignada):
        from gestorAplicacion.administracion import Administracion
        if len(Administracion.getCuidadores())==0:
            identificacion = 1
        else:
            identificacion = Administracion.getCuidadores()[-1].getIdentificacion() + 1
        super().__init__(identificacion, nombre, sueldo);
        self._especieAsignada = especieAsignada
        Administracion.addCuidadores(self)
	
	# El método info() es implementado de la interfaz Entidad y definido aquí. Sirve para generar el String que será 
	# usado para imprimir por consola los datos del cuidador en caso de ser requeridos en alguna de las funcionalidades 
	# de la aplicación.
    def info(self):
        return ("\nTipo de empleado: CUIDADOR" + "\nIdentificación: " + str(self.getIdentificacion()) + "\nNombre: " + self.getNombre() + "\nSueldo: " + str(self.getSueldo()) + "\nEspecie asignada: " + self.getEspecieAsignada().getNombre());
	
	# El método alimentarAnimal() simplemente cambia a true el estado del atributo "alimentado" del objeto tipo Animal 
	# que se le pasa como parámetro.
    def alimentarAnimal(self, animal):
        animal.setAlimentado(True)
	
	#El método moverAnimal() recibe como primer parámetro el objeto tipo Animal que el cuidador debe mover y como 
	# segundo parámetro el hábitat al que será movido dicho objeto animal. Con estos parámetros el método se encarga
	# de cortar la relación entre el animal y su anterior hábitat por medio del atributo de lista "animalesAsociados" 
	# de la clase Habitat, para luego asignar al animal su nuevo hábitat, correspondiente al pasado como parámetro.
    def moverAnimal(self, animal, lugar):
        animal.getHabitat().removeAnimalesAsociados(animal)
        animal.setHabitat(lugar)
        lugar.addAnimalesAsociados(animal)
	
	# Este método revisar() es heredado de la clase abstracta padre Empleado y definido aquí, además que aplica la 
	# sobrecarga de métodos. La siguiente es la primera definición del método, que recibe como parámetro un objeto 
	# tipo Animal y que en base a ese objeto retorna su atributo "estadoAnimo".
    def revisarAnimal(self, animal):
        return animal.isEstadoAnimo()
	
	# La siguiente es la segunda definición del método sobrecargado, que recibe como parámetro un objeto tipo Habitat 
	# y que en base a ese objeto retorna su atributo "limpio".
    def revisarHabitat(self, habitat):
        return habitat.isLimpio()
	
	# El siguiente método limpiarHabitat() recibo como primer parámetro el objeto tipo Habitat a limpiar y como segundo
	# parámetro el objeto tipo Habitat correspondiente al hábitat/zona a donde serán movidos los animales durante la
	# limpieza. El método consiste en que, de acuerdo a los objetos tipo Animal almacenados en el atributo de lista
	# "animalesAsociados" del objeto tipo Habitat que se pasó como primer parámetro, los animales son movidos por el
	# objeto tipo Cuidador sobre el cual se está invocando el método a un hábitat temporal pasado como segundo parámetro, 
	# esto para cambiar el estado del atributo "limpio" del hábitat que se pasó como primer parámetro a true y regresar
	# a los animales a dicho hábitat.
    def limpiarHabitat(self, habitat, jaulas):
        for animal in habitat.getAnimalesAsociados():
            self.moverAnimal(animal, jaulas)   
        habitat.setLimpio(True)
		
        for animal in jaulas.getAnimalesAsociados():
			# El siguiente if se encarga, para cada animal, de cambiar su atributo de "estadoAnimo" a true en caso que los dos 
			# atributos de esta clase necesarios para este cambio se encuentren en true, o sea, "alimentado" y "estadoSalud".
			# Otro atributo requerido para esto es el atributo "limpio" relacionado con el hábitat con que dicho animal está
			# asociado, que en este caso se asume como true pues el hábitat acabe de ser limpiado.
            if (animal.isAlimentado()==True) and (animal.isEstadoSalud()==True):
                animal.setEstadoAnimo(True)  
            self.moverAnimal(animal, habitat)
	
	# DE ACÁ PARA ABAJO ESTÁN LOS MÉTODOS GET Y SET
    def getEspecieAsignada(self):
        return self._especieAsignada
	
    def setEspecieAsignada(self, especieAsignada):
        self._especieAsignada = especieAsignada