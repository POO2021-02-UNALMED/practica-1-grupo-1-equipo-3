# CLASE CREADA POR DAVID MATEO GARCÍA

# En esta clase se realiza la funcionalidad de la adquisición y el traslado de animales. Adquirir un animal corresponde a
# crear un objeto tipo Animal de acuerdo a los atributos que especifique el usuario, esto en base primero a la especie que
# el usuario haya seleccionado, además de depender que haya un hábitat disponible para crear a dicho animal. Por otro lado, 
# trasladar un animal corresponde a eliminar del sistema el objeto tipo Animal que especifique el usuario.
# 
# Son necesarias las clases Especie, Habitat, Animal y Administración.

from main import Main
from ..gestorAplicacion.gestionZoologico.administracion import Administracion

class AdquisicionTraslado:
    especieSeleccionada = None
    habitatSeleccionado = None
    animalSeleccionado = None
	
	# El método adquisicionTraslado() es el método a llamar desde la clase Main. Desde este método es donde se controla la ejecución de esta funcionalidad.
    @classmethod
    def adquisicionTraslado():
        opcion=0
        print("Primero elija qué desea hacer:\n")
        print("1. Adquirir animales")
        print("2. Trasladar animales")
        opcion = int(input("\n¿Cuál opción quiere realizar? "))
        print()
		# De acuerdo a la opción que el usuario elija se ejecutará la secuencia para adquirir o trasladar un animal.
        if(opcion==1):
            AdquisicionTraslado.seleccionarEspecie("adquirir");
			# Por medio de la variable "habitatsDisponibles" se verifica si hay por lo menos un hábitat para depositar al animal de acuerdo a la
			# especie que seleccionó el usuario. En caso que no haya tan siquiera uno se cancela la adquisición del animal.
            habitatsDisponibles = AdquisicionTraslado.seleccionarHabitat()
            if(habitatsDisponibles):
                AdquisicionTraslado.ingresarAnimal()
        elif(opcion==2):
            AdquisicionTraslado.seleccionarEspecie("trasladar")
				# Por medio de la variable "animalesDisponibles" se verifica si hay por lo menos un animal (de la especie seleccionada por el usuario)
				# para trasladar. En caso que no haya tan siquiera uno se cancela el traslado del animal.
            animalesDisponibles = AdquisicionTraslado.seleccionarAnimal()
            if(animalesDisponibles):
                Administracion.trasladarAnimal(AdquisicionTraslado.animalSeleccionado)
                print("\nANIMAL TRASLADADO EXITOSAMENTE\n")
        else:
			# En caso que el usuario haya seleccionado una opción que no corresponda, se le informa.
            print("OPCIÓN INCORRECTA: Solo opciones 1 y 2.")
		# El método continuar() de la clase Main es usado para que el usuario tenga tiempo de leer las salidas proporcionadas por la funcionalidad
		# Este método evita que se repita inmediatamente el ciclo de elegir la funcionalidad a realizar, esto por medio de esperar la acción del usuario
        Main.continuar()
        
	
	# A través del método seleccionarEspecie(...) se obtiene la especie del animal que el usuario desea tratar (Adquirir o trasladar).
	# El parámetro "accion" es requerido para incluirlo en el mensaje mostrado al usuario, pues de acuerdo a la opción elegida por el 
	# usuario en el método adquisionTraslado(), se puede tratar de adquirir o trasladar a un animal.
    @classmethod
    def seleccionarEspecie(accion):
        opcion=0
        print("Elija primero la especie del animal que desea " + accion + ", eligiendo la opción correspondiente:\n")
		
        num = 1;
		# El siguiente for imprime y enumera el nombre de cada objeto de Especie almacenado en la lista de especies de Administración
        for especie in Administracion.getEspecies():
            print(str(num) + ". " + especie.getNombre())
            num += 1
		
        opcion = int(input("\n¿Cuál opción de especie elije? "))
		
		# A través del siguiente while se le solicita al usuario la opción tantas veces como sea necesario hasta que esta sea correcta.
        while(True):
            if(opcion < 1 or opcion > 5):
                print("\nOPCIÓN INCORRECTA: Opciones solo del 1 al 5")
                opcion = int(input("\n¿Cuál opción de especie elije? "))
            else:
                print("\nEspecie seleccionada:\n")
				# Ya que las especies fueron enumeradas en el orden de la lista de especies (empezando desde el 1), entonces la posición de la
				# especie seleccionada en esa lista corresponderá a la opción del usuario menos 1.
                AdquisicionTraslado.especieSeleccionada = Administracion.getEspecies()[opcion-1]
                print(AdquisicionTraslado.especieSeleccionada.info())
                break
	
	# A través del método seleccionarHabitat() se obtiene el hábitat donde el animal a adquirir será depositado.
    @classmethod
    def seleccionarHabitat():
        id=0
		# Con la variable "habitats" se contará, como ya se dijo, si hay por lo menos un hábitat de la especie seleccionada por el usuario
		# para depositar en dicho hábitat al animal a adquirir.
        habitats = 0
		# En la variable "identificaciones" se almacenarán las identificaciones de los animales listados, esto para verificar que el usuario
		# eligió una identificación válida.
        identificaciones = []
        print("\nAhora elija el hábitat donde el animal que desea adquirir será depositado, ingresando su identificación:")
        print("(Los hábitats listados corresponden únicamente a hábitats donde la especie de dicho animal puede ser depositada)\n")
        print("Identificación; Nombre; Ambientación; Capacidad Animales / Capacidad máxima")
		
		# Con el siguiente for se obtienen cada uno de los hábitats almacenandos en la lista de habitats de la clase Administración.
        for habitat in Administracion.getHabitats():
            if len(habitat.getAnimalesAsociados()) == 0:
                if (habitat.getNombre() == "Veterinaria"):
                    continue
                if (habitat.getNombre() == "Jaulas"):
                    continue
                print(str(habitat.getIdentificacion()) + "; " + habitat.getNombre() + "; " + habitat.getAmbientacion() + "; " + str(habitat.cantidadAnimales()) + " / " + str(habitat.getCapacidadMaxima()))
				# Como se dijo, se van contando los hábitats que son listados, además de almacenar sus identificaciones.
                habitats += 1
                identificaciones.append(habitat.getIdentificacion())
			
			# Además, con el siguiente for, se obtiene cada uno de los animales asociados a cada uno de los hábitats obtenidos con el anterior for que
			# hayan contenido al menos un animal.
            for animal in habitat.getAnimalesAsociados():
				# Todo esto se hace para buscar de manera efectiva los hábitats que puedan contener la especie del animal que se va a adquirir,
				# para luego imprimir los datos de cada uno de estos hábitats por pantalla para que el usuario seleccione uno.
                if(animal.getEspecie() == AdquisicionTraslado.especieSeleccionada and habitat.cantidadAnimales() < habitat.getCapacidadMaxima()):
                    print(str(habitat.getIdentificacion()) + "; " + habitat.getNombre() + "; " + habitat.getAmbientacion() + "; " + str(habitat.cantidadAnimales()) + " / " + str(habitat.getCapacidadMaxima()))
					# Como se dijo, se van contando los hábitats que son listados, además de almacenar sus identificaciones.
                    habitats += 1
                    identificaciones.append(habitat.getIdentificacion())
                    break
		
		# En caso que no haya ni un hábitat para depositar al animal, se le informa al usuario y la adquisición queda cancelada.
        if(habitats == 0):
            print("\nNo se ha encontrado ningún hábitat disponible para depositar al animal.")
            print("ADQUISICIÓN CANCELADA\n")
			# Se retorna false para la verificación en la clase adquisicionTraslado(), como se dijo anteriormente.
            return False
		# En caso que haya por lo menos un hábitat para depositar al animal, se le solicitará al usuario que elija el hábitat de
		# acuerdo a la identificación de este. Recordar que los hábitats ya fueron listados con los for anteriores.
        else:
            id = int(input("\n¿Cuál hábitat elije? (Identificación): "))
			
            estado = True
			# A través del siguiente while se le solicita al usuario la identificación tantas veces como sea necesario hasta que esta sea correcta.
            while(estado):
                if(id in identificaciones == False):
                    print("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida.")
                    id = int(input("\n¿Cuál hábitat elije? (Identificación): "))
                else:
					# Con el siguiente for se vuelve a recorrer el listado de todos los hábitats.
                    for habitat in Administracion.getHabitats():
						# En caso que la identificación de un hábitat corresponda a la identificación que seleccionó el usuario, se imprimen los datos 
						# del hábitat seleccionado y se asigna dicho hábitat al atributo estático "habitatSeleccionado", necesario para la adquisición.
                        if(habitat.getIdentificacion() == id): 
                            print("\nHábitat seleccionado:\n")
                            print(habitat.info())
                            AdquisicionTraslado.habitatSeleccionado = habitat
                            estado = False
                            break
			# Se retorna true para la verificación en la clase adquisicionTraslado(), como se dijo anteriormente.
            return True
	
	# A través del método seleccionarAnimal() se obtiene el animal que será trasladado.
    @classmethod
    def seleccionarAnimal():
        id=0
		# Con la variable "animales" se contará, como ya se dijo, si hay por lo menos un animal de la especie seleccionada por el usuario
		# para trasladar.
        animales = 0
		# En la variable "identificaciones" se almacenarán las identificaciones de los animales listados, esto para verificar que el usuario
		# eligió una identificación válida.
        identificaciones = []
        print("\nAhora elija el animal que desee trasladar, ingresando su identificación.\n")
        print("Identificación; Especie; Hábitat; Género; Edad; Peso")
		
		# Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administración.
        for animal in Administracion.getAnimales():
			# Esto se hace para buscar los animales correspondientes a la especie del animal que se va a trasladar, para luego imprimir 
			# los datos de cada uno de estos animales por pantalla para que el usuario seleccione uno para trasladar.
            if(animal.getEspecie() == AdquisicionTraslado.especieSeleccionada):
                print(str(animal.getIdentificacion()) + "; " + animal.getEspecie().getNombre() + "; " + animal.getHabitat().getNombre() + "; " + animal.getGenero() + "; " + str(animal.getEdad()) + "; " + str(animal.getPeso()))
				# Como se dijo, se van contando los animales que son listados, además de almacenar sus identificaciones.
                animales += 1
                identificaciones.append(animal.getIdentificacion())
		
		# En caso que no haya ni un solo animal de la especie seleccionada, se le informa al usuario y el traslado queda cancelado.
        if(animales == 0):
            print("\nNo se ha encontrado ningún animal de la especie solicitada para trasladar.")
            print("TRASLADO CANCELADO\n")
			# Se retorna false para la verificación en la clase adquisicionTraslado(), como se dijo anteriormente.
            return False
		# En caso que haya por lo menos un animal de la especie seleccionada, se le solicitará al usuario que elija el animal de
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
						# del animal seleccionado y se asigna dicho animal al atributo estático "animalSeleccionado", necesario para el traslado.
                        if(animal.getIdentificacion() == id):
                            print("\nAnimal seleccionado:\n")
                            print(animal.info())
                            AdquisicionTraslado.animalSeleccionado = animal
                            estado = False
                            break
			# Se retorna true para la verificación en la clase adquisicionTraslado(), como se dijo anteriormente.
            return True
	
	# A través del método ingresarAnimal() el usuario ingresa los atributos del animal a adquirir.
    @classmethod
    def ingresarAnimal():
        print("\nPor último, ingrese los datos del animal que se va a adquirir:\n")
        genero = input("Género (M o H): ")
        while(True):
            if(genero == "M" or genero == "H"):
                break
            else:
                print("\nGÉNERO INCORRECTO: Ingrese M o H\n")
                genero= input("Género (M o H): ")
                
        edad = int(input("Edad en años (Número): "))
        while(True):
            if(edad < 0):
                print("\nEDAD INCORRECTA: Ingrese un número positivo\n")
                edad = int(input("Edad en años (Número): "))
            else:
                break
        
        peso = float(input("Peso en Kg (Número): "))
        while(True):
            if(peso < 0.0):
                print("\nPESO INCORRECTO: Ingrese un número positivo\n")
                peso = float(input("Peso en Kg (Número): "))
            else:
                break

		# Se llama al método adquirirAnimal(...) de la clase Administracion, pues este método se encarga de crear el objeto tipo Animal
		# en base a los atributos que el usuario ingresó. */
        Administracion.adquirirAnimal(AdquisicionTraslado.especieSeleccionada, AdquisicionTraslado.habitatSeleccionado, genero, edad, peso);
        print("\nANIMAL ADQUIRIDO EXITOSAMENTE\n")