# CLASE CREADA POR Juan Jose Monsalve Marin

"""
 En esta clase realiza la funcionalidad de curar de los animales 
 Primero se debe de identificar el cuidador que mover� a los animales, el animal que ser� trasladado a la 
 veterinaria y el veterinario tratante que atender� al animal. Todo esto se hace despu�s de que un cuidador 
 all� revisando el animal y se percatara de que el estado de animo del animal no cambio despu�s de alimentarlo. 
 esto ultimo se realiza en la clase "FuncionalidadCuidar"

 Son necesarias las clases animal, veterinario y cuidador.  
"""

from main import Main
from ..gestorAplicacion.gestionZoologico.administracion import Adminstracion
from ..gestorAplicacion.gestionZoologico.cuidador import Cuidador
from ..gestorAplicacion.gestionZoologico.veterinario import Veterinario
from ..gestorAplicacion.animalesZoologico.animal import Animal
from Python.src.gestorAplicacion.gestionZoologico import veterinario
from ..gestorAplicacion.gestionZoologico.administracion import Administracion

class Curar:
    animalSeleccionado=None
    cuidadorSeleccionado=None
    veterinarioSeleccionado=None

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
                            Curar.animalSeleccionado = animal
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
            if(cuidador.getEspecieAsignada() == Curar.animalSeleccionado.getEspecie()):
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
                            Curar.cuidadorSeleccionado = cuidador
                            estado = False
                            break
			# Se retorna true para la verificación en la clase cuidarAnimal(), como se dijo anteriormente.
            return True

    
    # A través del método seleccionarVeterinario() se obtiene el veterinario que revisará al animal.
    @classmethod
    def seleccionarVeterinario():
        id = 0
		# Con la variable "veterinario" se contará, como ya se dijo, si hay por lo menos un veterinario especializado en la especie del animal
		# seleccionado por el usuario para revisar al animal.
        veterinarios = 0
		# En la variable "identificaciones" se almacenarán las identificaciones de los veterinarios listados, esto para verificar que el usuario
		# eligió una identificación válida.
        identificaciones = []
        print("\nAhora elija el veterinario que desee que revise al animal, ingresando su identificación.\n")
        print("Identificación; Nombre; Especie asignada")
		
		# Con el siguiente for se obtienen cada uno de los veterinarios almacenandos en la lista de veterinarios de la clase Administracion.
        for veterinario in Administracion.getVeterinarios():
			# Con el if se buscan los veterinarios que puedan revisar al animal de acuerdo a su especie, esto para imprimir los datos de cada 
			# uno de estos veterinarios por pantalla para que el usuario seleccione el que va a revisar al animal.
            if(veterinario.getEspecieAsignada() == Curar.animalSeleccionado.getEspecie()):
                print(str(veterinario.getIdentificacion()) + "; " + veterinario.getNombre() + "; " + veterinario.getEspecieAsignada().getNombre())
				# Como se dijo, se van contando los veterinarios que son listados, además de almacenar sus identificaciones.
                veterinarios += 1
                identificaciones.append(veterinario.getIdentificacion())
		
		# En caso que no haya ni un solo veterinario que pueda revisar al animal, se le informa al usuario y la revisión queda cancelada.
        if(veterinarios == 0):
            print("\nNo se ha encontrado ningún veterinario para revisar al animal.")
            print("REVISIÓN CANCELADA\n")
			# Se retorna false para la verificación en la clase cuidarAnimal(), como se dijo anteriormente.
            return False
		# En caso que haya por lo menos un veterinario para revisar al animal, se le solicitará al usuario que elija el veterinario de
		# acuerdo a la identificación de este. Recordar que los veterinarios ya fueron listados con el for anterior.
        else:
            id = int(input("\n¿Cuál veterinario elije? (Identificación) "))
			
            estado = True
			# A través del siguiente while se le solicita al usuario la identificación tantas veces como sea necesario hasta que esta sea correcta.
            while(estado):
                if(id in identificaciones == False):
                    print("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida.")
                    id = int(input("\n¿Cuál veterinario elije? (Identificación) "))
                else:
					# Con el siguiente for se vuelve a recorrer el listado de todos los veterinarios en la lista de veterinarios de la clase Administracion.
                    for veterinario in Administracion.getVeterinarios():
						# En caso que la identificación de un veterinario corresponda a la identificación que seleccionó el usuario, se imprimen los datos 
						# del veterinario seleccionado y se asigna dicho veterinario al atributo estático "veterinarioSeleccionado", necesario para la revisión.
                        if(veterinario.getIdentificacion() == id):
                            print("\nVeterinario seleccionado:\n")
                            print(veterinario.info())
                            veterinario.veterinarioSeleccionado = veterinario
                            estado = False
                            break
			# Se retorna true para la verificación en la clase cuidarAnimal(), como se dijo anteriormente.
            return True

    # A trav�s del m�todo saludAnimal() se hace el proceso de revisar el estado de salud del animal seleccionado desde el cuidador seleccionado y veterinario seleccionado.
    @classmethod
    def saludAnimal():
        # Se guarda el habitad de procedencia del animal, para que luego pueda ser devuelto.
        habitatSeleccionado = Curar.animalSeleccionado.getHabitat()
        print("\nCuidador " + Curar.cuidadorSeleccionado.getNombre() + " procede a mover al animal con identificaci�n " + str(Curar.animalSeleccionado.getIdentificacion()) + " a la veterinaria.")
        Curar.cuidadorSeleccionado.moverAnimal(Curar.animalSeleccionado, habitatSeleccionado)
        print("Veterinario " + Curar.veterinarioSeleccionado.getNombre() + " procede a revisar al animal con identificaci�n " + str(Curar.animalSeleccionado.getIdentificacion()) + ".")

        # En caso que el animal est� con buen estado de salud (revisar(...) retorna true), se le informar� al usuario y se termina la funcionalidad.
        if(Curar.veterinarioSeleccionado.revisarAnimal(Curar.animalSeleccionado)):
            print("RESULTADO: El animal se encuentra con buen estado de salud.\n")
            print("Cuidador " + Curar.cuidadorSeleccionado.getNombre() + " procede a mover al animal con identificaci�n " + 
				    str(Curar.animalSeleccionado.getIdentificacion()) + " de regreso a su h�bitat.")
            # Se regresa al animal a su habitad
            Curar.cuidadorSeleccionado.moverAnimal(Curar.animalSeleccionado, habitatSeleccionado)

            if(Curar.animalSeleccionado.isAlimentado() and Curar.animalSeleccionado.getHabitat().isLimpio()):
                Curar.animalSeleccionado.setEstadoAnimo(True)

            if (Curar.animalSeleccionado.isEstadoAnimo()==False):
                print("El estado de animo para est animal sigue siendo malo. Puede solicitar mantenimiento de habitat o alimentaci�n del animal.")
            else:
                print("El animal se encuentra con un buen estado de �nimo.")

            # En caso que el animal est� con mal estado de salud, se le informar� al usuario y el veterinario seleccionado proceder� a curar al animal a trav�s del m�todo curarAnimal(...)
        else:
            print("RESULTADO: El animal se encuentra con mal estado de salud.\n")
            print("El veterinario " + Curar.veterinarioSeleccionado.getNombre() + "decide hacer curaci�n al animal para mejorar su estado de salud.")
            Curar.veterinarioSeleccionado.curarAnimal(Curar.animalSeleccionado)
            # Si luego de haber sido curado, el estado de �nimo del animal mejora, se le informa al usuario y se termina la funcionalidad.
            if(Curar.veterinarioSeleccionado.revisar(Curar.animalSeleccionado)):
                print("Curar al animal ha dado buen resultado y este ahora se encuentra con buen estado de salud.")
                print("\nCuidador " + Curar.cuidadorSeleccionado.getNombre() + " procede a mover al animal con identificaci�n " + str(Curar.animalSeleccionado.getIdentificacion()) + " de regreso a su h�bitat.")
                Curar.cuidadorSeleccionado.moverAnimal(Curar.animalSeleccionado, habitatSeleccionado)
                # El estado de �nimo depende de su alimentaci�n, su estado de salud y de la limpieza de su h�bitat. El siguiente if cambia el estado de �nimo del animal a bueno (true) en caso que estos tres factores tambi�n sean buenos (true).
                if(Curar.animalSeleccionado.isAlimentado() and Curar.animalSeleccionado.isEstadoSalud() and Curar.animalSeleccionado.getHabitat().isLimpio()):
                    Curar.animalSeleccionado.setEstadoAnimo(True)
                if(Curar.animalSeleccionado.isEstadoAnimo()):
                    print("Curar la salud del animal ha dado buenos resultados. El animal ya no se encuentra triste.")
                else:
                    print("El estado de animo para este animal sigue siendo malo. Puede solicitar mantenimiento de habitat o alimentaci�n del animal.")
            
            print("REVISI�N FINALIZADA\n")
			    


			





        
