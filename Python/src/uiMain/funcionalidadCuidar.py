# CLASE CREADA POR DAVID MATEO GARCÍA

# En esta clase se realiza la funcionalidad de cuidar de los animales. Para esta clase, un cuidador deberá revisar el estado
# de ánimo del animal elegido por el usuario. En caso que el animal se encuentre con mal estado de ánimo el cuidador lo
# alimentara. Si al alimentar al animal su estado de ánimo no mejora, se le informará al usuario para que tome por si mismo
# la decisión de qué otra funcionalidad evaluar.
# 
# Son necesarias las clases Animal, Cuidador y Administración.

from main import Main
from ..gestorAplicacion.gestionZoologico.administracion import Adminstracion
from ..gestorAplicacion.gestionZoologico.cuidador import Cuidador
from ..gestorAplicacion.animalesZoologico.animal import Animal

class Cuidar:
    animalSeleccionado=None
    cuidadorSeleccionado=None
	
	# El método cuidarAnimal() es el método a llamar desde la clase Main. Desde este método es donde se controla la ejecución de esta funcionalidad.
    @classmethod
    def cuidarAnimal():
		# Por medio de la variable "animalesDisponibles" se verifica si hay por lo menos un animal para revisar.
		# En caso que no haya tan siquiera uno se cancela la revisión del animal.
        animalesDisponibles = Cuidar.seleccionarAnimal()
        if(animalesDisponibles):
			# Por medio de la variable "cuidadoresDisponibles" se verifica si hay por lo menos un cuidar que pueda revisar al animal, pues depende
			# de la especie del animal y la especialidad de los cuidadores. En caso que no haya tan siquiera uno se cancela la revisión del animal.
            cuidadoresDisponibles = Cuidar.seleccionarCuidador()
            if(cuidadoresDisponibles):
                Cuidar.animoAnimal()
                
        print()
		# El método continuar() de la clase Main es usado para que el usuario tenga tiempo de leer las salidas proporcionadas por la funcionalidad
		# Este método evita que se repita inmediatamente el ciclo de elegir la funcionalidad a realizar, esto por medio de esperar la acción del usuario.
        Main.continuar()
	
	# A través del método seleccionarAnimal() se obtiene el animal que será revisado.
    @classmethod
    def seleccionarAnimal():
        id = 0
		# Con la variable "animales" se contará, como ya se dijo, si hay por lo menos un animal para revisar.
        animales = 0
		# En la variable "identificaciones" se almacenarán las identificaciones de los animales listados, esto para verificar que el usuario
		# eligió una identificación válida. */
        identificaciones = []
        print("Elija primero el animal que desee revisar, ingresando su identificación.\n")
        print("Identificación; Especie; Hábitat; Género; Edad; Peso")
		
		# Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administración.
        for animal in Administracion.getAnimales():
			# Esto se hace para imprimir los datos de cada uno de los animales por pantalla para que el usuario seleccione uno para revisar.
            print(str(animal.getIdentificacion()) + "; " + animal.getEspecie().getNombre() + "; " + animal.getHabitat().getNombre() + "; " + animal.getGenero() + "; " + str(animal.getEdad()) + "; " + str(animal.getPeso()));
			# Como se dijo, se van contando los animales que son listados, además de almacenar sus identificaciones.
            animales += 1
            identificaciones.append(animal.getIdentificacion())
		
		# En caso que no haya ni un solo animal para revisar, se le informa al usuario y la revisión queda cancelada.
        if(animales == 0):
            print("\nNo se ha encontrado ningún animal para revisar.")
            print("REVISIÓN CANCELADA\n")
			# Se retorna false para la verificación en la clase cuidarAnimal(), como se dijo anteriormente.
            return False
		# En caso que haya por lo menos un animal para revisar, se le solicitará al usuario que elija el animal de
		# acuerdo a la identificación de este. Recordar que los animales ya fueron listados con el for anterior.
        else:
            id = int(input("\n¿Cuál animal elije? (Identificación): "))
			
            estado = True
			# A través del siguiente while se le solicita al usuario la identificación tantas veces como sea necesario hasta que esta sea correcta.
            while(estado):
                if(id in identificaciones == False):
                    print("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida.")
                    id = int(input("\n¿Cuál animal elije? (Identificación): "))
                else:
					# Con el siguiente for se vuelve a recorrer el listado de todos los animales.
                    for animal in Administracion.getAnimales():
						# En caso que la identificación de un animal corresponda a la identificación que seleccionó el usuario, se imprimen los datos 
						# del animal seleccionado y se asigna dicho animal al atributo estático "animalSeleccionado", necesario para la revisión.
                        if(animal.getIdentificacion() == id):
                            print("\nAnimal seleccionado:\n")
                            print(animal.info())
                            Cuidar.animalSeleccionado = animal
                            estado = False
                            break
			# Se retorna true para la verificación en la clase cuidarAnimal(), como se dijo anteriormente.
            return True
	
	# A través del método seleccionarCuidador() se obtiene el cuidador que revisará al animal.
    @classmethod
    def seleccionarCuidador():
        id = 0
		# Con la variable "cuidadores" se contará, como ya se dijo, si hay por lo menos un cuidador especializado en la especie del animal
		# seleccionado por el usuario para revisar a animal.
        cuidadores = 0
		# En la variable "identificaciones" se almacenarán las identificaciones de los animales listados, esto para verificar que el usuario
		# eligió una identificación válida.
        identificaciones = []
        print("\nAhora elija el cuidador que desee que revise al animal, ingresando su identificación.\n")
        print("Identificación; Nombre; Especie asignada")
		
		# Con el siguiente for se obtienen cada uno de los cuidadores almacenandos en la lista de cuidadores de la clase Administracion.
        for cuidador in Administracion.getCuidadores():
			# Con el if se buscan los cuidadores que puedan revisar al animal de acuerdo a su especie, esto para imprimir los datos de cada 
			# uno de estos cuidadores por pantalla para que el usuario seleccione el que va a revisar al animal.
            if(cuidador.getEspecieAsignada() == Cuidar.animalSeleccionado.getEspecie()):
                print(str(cuidador.getIdentificacion()) + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre())
				# Como se dijo, se van contando los cuidadores que son listados, además de almacenar sus identificaciones.
                cuidadores += 1
                identificaciones.append(cuidador.getIdentificacion())
		
		# En caso que no haya ni un solo cuidadores que pueda revisar al animal, se le informa al usuario y la revisión queda cancelada.
        if(cuidadores == 0):
            print("\nNo se ha encontrado ningún cuidador para revisar al animal.")
            print("REVISIÓN CANCELADA\n")
			# Se retorna false para la verificación en la clase cuidarAnimal(), como se dijo anteriormente.
            return False
		# En caso que haya por lo menos un cuidador para revisar al animal, se le solicitará al usuario que elija el cuidador de
		# acuerdo a la identificación de este. Recordar que los cuidadores ya fueron listados con el for anterior.
        else:
            id = int(input("\n¿Cuál cuidador elije? (Identificación) "))
			
            estado = True
			# A través del siguiente while se le solicita al usuario la identificación tantas veces como sea necesario hasta que esta sea correcta.
            while(estado):
                if(id in identificaciones == False):
                    print("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida.")
                    id = int(input("\n¿Cuál cuidador elije? (Identificación) "))
                else:
					# Con el siguiente for se vuelve a recorrer el listado de todos los cuidadores en la lista de cuidadores de la clase Administracion.
                    for cuidador in Administracion.getCuidadores():
						# En caso que la identificación de un cuidador corresponda a la identificación que seleccionó el usuario, se imprimen los datos 
						# del cuidador seleccionado y se asigna dicho cuidador al atributo estático "cuidadorSeleccionado", necesario para la revisión.
                        if(cuidador.getIdentificacion() == id):
                            print("\nCuidador seleccionado:\n")
                            print(cuidador.info())
                            Cuidar.cuidadorSeleccionado = cuidador
                            estado = False
                            break
			# Se retorna true para la verificación en la clase cuidarAnimal(), como se dijo anteriormente.
            return True
	
	# A través del método animoAnimal() se hace el proceso de revisar el estado de ánimo del animal seleccionado desde el cuidador seleccionado.
    @classmethod
    def animoAnimal():
        print("\nCuidador " + Cuidar.cuidadorSeleccionado.getNombre() + " procede a revisar al animal con identificación " + str(Cuidar.animalSeleccionado.getIdentificacion()) + ".");
		
		# En caso que el animal esté con buen estado de ánimo (revisar(...) retorna true), se le informará al usuario y se termina la funcionalidad. 
        if(Cuidar.cuidadorSeleccionado.revisar(Cuidar.animalSeleccionado)):
            print("RESULTADO: El animal se encuentra con buen estado de ánimo.\n")
		# En caso que el animal esté con mal estado de ánimo, se le informará al usuario y el cuidador seleccionado procederá a alimentar al animal
		# a través del método animentarAnimal(...).
        else:
            print("RESULTADO: El animal se encuentra con mal estado de ánimo.\n")
            print("El cuidador " + Cuidar.cuidadorSeleccionado.getNombre() + " decide alimentar al animal para mejorar su estado de ánimo.")
            Cuidar.cuidadorSeleccionado.alimentarAnimal(Cuidar.animalSeleccionado)
			
            # El estado de ánimo depende de su alimentación, su estado de salud y de la limpieza de su hábitat. El siguiente if cambia el estado
			# de ánimo del animal a bueno (true) en caso que estos tres factores también sean buenos (true). */
            if(Cuidar.animalSeleccionado.isAlimentado() and Cuidar.animalSeleccionado.isEstadoSalud() and Cuidar.animalSeleccionado.getHabitat().isLimpio()):
                Cuidar.animalSeleccionado.setEstadoAnimo(True)
                
			# Si luego de haber sido alimentado, el estado de ánimo del animal mejoró, se le informa al usuario y se termina la funcionalidad.
            if(Cuidar.cuidadorSeleccionado.revisar(Cuidar.animalSeleccionado)):
                print("Alimentar al animal ha dado buen resultado y este ahora se encuentra con buen estado de ánimo.")
			# En caso que el animal continúe con mal estado de ánimo, se le informará al usuario que alimentarlo no ha sido de ayuda. Además, se le
			# indicará al usuario que puede probar con la funcionalidad de mantenimiento y la de curar para así mejorar el estado de ánimo del animal. */
            else:
                print("Alimentar al animal no ha mejorado su estado de ánimo.")
                print("Puede solicitar que se haga mantenimiento a su hábitat o hacerlo revisar con un veterinario para mejorar su estado.")