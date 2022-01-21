// CLASE CREADA POR DAVID MATEO GARCÍA

/* En esta clase se realiza la funcionalidad de cuidar de los animales. Para esta clase, un cuidador deberá revisar el estado
 * de ánimo del animal elegido por el usuario. En caso que el animal se encuentre con mal estado de ánimo el cuidador lo
 * alimentara. Si al alimentar al animal su estado de ánimo no mejora, se le informará al usuario para que tome por si mismo
 * la decisión de qué otra funcionalidad evaluar.
 * 
 * Son necesarias las clases Animal, Cuidador y Administración.
 */

package uiMain;

import java.util.*;
import gestorAplicacion.gestionZoologico.Administracion;
import gestorAplicacion.gestionZoologico.Cuidador;
import gestorAplicacion.animalesZoologico.Animal;

public class FuncionalidadCuidar {
	static Animal animalSeleccionado;
	static Cuidador cuidadorSeleccionado;
	
	// El método cuidarAnimal() es el método a llamar desde la clase Main. Desde este método es donde se controla la ejecución de esta funcionalidad.
	static void cuidarAnimal() {
		/* Por medio de la variable "animalesDisponibles" se verifica si hay por lo menos un animal para revisar.
		 * En caso que no haya tan siquiera uno se cancela la revisión del animal. */
		boolean animalesDisponibles = seleccionarAnimal();
		if(animalesDisponibles) {
			/* Por medio de la variable "cuidadoresDisponibles" se verifica si hay por lo menos un cuidar que pueda revisar al animal, pues depende
			 * de la especie del animal y la especialidad de los cuidadores. En caso que no haya tan siquiera uno se cancela la revisión del animal. */
			boolean cuidadoresDisponibles = seleccionarCuidador();
			if(cuidadoresDisponibles) animoAnimal();
		}
		System.out.println();
		/* El método continuar() de la clase Main es usado para que el usuario tenga tiempo de leer las salidas proporcionadas por la funcionalidad
		 * Este método evita que se repita inmediatamente el ciclo de elegir la funcionalidad a realizar, esto por medio de esperar la acción del usuario */
		Main.continuar();
		return;
	}
	
	// A través del método seleccionarAnimal() se obtiene el animal que será revisado.
	static boolean seleccionarAnimal() {
		int id;
		// Con la variable "animales" se contará, como ya se dijo, si hay por lo menos un animal para revisar.
		int animales = 0;
		/* En la variable "identificaciones" se almacenarán las identificaciones de los animales listados, esto para verificar que el usuario
		 * eligió una identificación válida. */
		List<Integer> identificaciones = new ArrayList<Integer>();
		System.out.println("Elija primero el animal que desee revisar, ingresando su identificación.\n");
		System.out.println("Identificación; Especie; Hábitat; Género; Edad; Peso");
		
		// Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administración.
		for(Animal animal : Administracion.getAnimales()) {
			// Esto se hace para imprimir los datos de cada uno de los animales por pantalla para que el usuario seleccione uno para revisar.
			System.out.println(String.valueOf(animal.getIdentificacion()) + "; " + animal.getEspecie().getNombre() + "; " + 
							   animal.getHabitat().getNombre() + "; " + animal.getGenero() + "; " + 
							   String.valueOf(animal.getEdad()) + "; " + String.valueOf(animal.getPeso()));
			// Como se dijo, se van contando los animales que son listados, además de almacenar sus identificaciones.
			animales++;
			identificaciones.add(animal.getIdentificacion());
		}
		
		// En caso que no haya ni un solo animal para revisar, se le informa al usuario y la revisión queda cancelada.
		if(animales == 0) {
			System.out.println("\nNo se ha encontrado ningún animal para revisar.");
			System.out.println("REVISIÓN CANCELADA\n");
			// Se retorna false para la verificación en la clase cuidarAnimal(), como se dijo anteriormente.
			return false;
		/* En caso que haya por lo menos un animal para revisar, se le solicitará al usuario que elija el animal de
		 * acuerdo a la identificación de este. Recordar que los animales ya fueron listados con el for anterior. */
		} else {
			System.out.print("\n¿Cuál animal elije? (Identificación): ");
			id = Main.leerOpcion();
			
			boolean estado = true;
			// A través del siguiente while se le solicita al usuario la identificación tantas veces como sea necesario hasta que esta sea correcta.
			while(estado) {
				if(identificaciones.contains(id)==false) {
					System.out.println("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida.");
					System.out.print("\n¿Cuál animal elije? (Identificación): ");
					id = Main.leerOpcion();
				} else {
					// Con el siguiente for se vuelve a recorrer el listado de todos los animales.
					for(Animal animal : Administracion.getAnimales()) {
						/* En caso que la identificación de un animal corresponda a la identificación que seleccionó el usuario, se imprimen los datos 
						 * del animal seleccionado y se asigna dicho animal al atributo estático "animalSeleccionado", necesario para la revisión. */
						if(animal.getIdentificacion() == id) { 
							System.out.println("\nAnimal seleccionado:\n");
							System.out.println(animal.info());
							animalSeleccionado = animal;
							estado = false;
							break;
						}
					}
				}
			}
			// Se retorna true para la verificación en la clase cuidarAnimal(), como se dijo anteriormente.
			return true;
		}
	}
	
	// A través del método seleccionarCuidador() se obtiene el cuidador que revisará al animal.
	static boolean seleccionarCuidador() {
		int id;
		/* Con la variable "cuidadores" se contará, como ya se dijo, si hay por lo menos un cuidador especializado en la especie del animal
		 * seleccionado por el usuario para revisar a animal. */
		int cuidadores = 0;
		/* En la variable "identificaciones" se almacenarán las identificaciones de los animales listados, esto para verificar que el usuario
		 * eligió una identificación válida. */
		List<Integer> identificaciones = new ArrayList<Integer>();
		System.out.println("\nAhora elija el cuidador que desee que revise al animal, ingresando su identificación.\n");
		System.out.println("Identificación; Nombre; Especie asignada");
		
		// Con el siguiente for se obtienen cada uno de los cuidadores almacenandos en la lista de cuidadores de la clase Administracion.
		for(Cuidador cuidador : Administracion.getCuidadores()) {
			/* Con el if se buscan los cuidadores que puedan revisar al animal de acuerdo a su especie, esto para imprimir los datos de cada 
			 * uno de estos cuidadores por pantalla para que el usuario seleccione el que va a revisar al animal. */
			if(cuidador.getEspecieAsignada() == animalSeleccionado.getEspecie()) {
				System.out.println(String.valueOf(cuidador.getIdentificacion()) + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre());
				// Como se dijo, se van contando los cuidadores que son listados, además de almacenar sus identificaciones.
				cuidadores++;
				identificaciones.add(cuidador.getIdentificacion());
			}
		}
		
		// En caso que no haya ni un solo cuidadores que pueda revisar al animal, se le informa al usuario y la revisión queda cancelada.
		if(cuidadores == 0) {
			System.out.println("\nNo se ha encontrado ningún cuidador para revisar al animal.");
			System.out.println("REVISIÓN CANCELADA\n");
			// Se retorna false para la verificación en la clase cuidarAnimal(), como se dijo anteriormente.
			return false;
		/* En caso que haya por lo menos un cuidador para revisar al animal, se le solicitará al usuario que elija el cuidador de
		 * acuerdo a la identificación de este. Recordar que los cuidadores ya fueron listados con el for anterior. */
		} else {
			System.out.print("\n¿Cuál cuidador elije? (Identificación) ");
			id = Main.leerOpcion();
			
			boolean estado = true;
			// A través del siguiente while se le solicita al usuario la identificación tantas veces como sea necesario hasta que esta sea correcta.
			while(estado) {
				if(identificaciones.contains(id)==false) {
					System.out.println("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida.");
					System.out.print("\n¿Cuál cuidador elije? (Identificación) ");
					id = Main.leerOpcion();
				} else {
					// Con el siguiente for se vuelve a recorrer el listado de todos los cuidadores en la lista de cuidadores de la clase Administracion.
					for(Cuidador cuidador : Administracion.getCuidadores()) {
						/* En caso que la identificación de un cuidador corresponda a la identificación que seleccionó el usuario, se imprimen los datos 
						 * del cuidador seleccionado y se asigna dicho cuidador al atributo estático "cuidadorSeleccionado", necesario para la revisión. */
						if(cuidador.getIdentificacion() == id) { 
							System.out.println("\nCuidador seleccionado:\n");
							System.out.println(cuidador.info());
							cuidadorSeleccionado = cuidador;
							estado = false;
							break;
						}
					}
				}
			}
			// Se retorna true para la verificación en la clase cuidarAnimal(), como se dijo anteriormente.
			return true;
		}
	}
	
	// A través del método animoAnimal() se hace el proceso de revisar el estado de ánimo del animal seleccionado desde el cuidador seleccionado.
	static void animoAnimal() {
		System.out.println("\nCuidador " + cuidadorSeleccionado.getNombre() + " procede a revisar al animal con identificación " + 
							String.valueOf(animalSeleccionado.getIdentificacion()) + ".");
		
		// En caso que el animal esté con buen estado de ánimo (revisar(...) retorna true), se le informará al usuario y se termina la funcionalidad. 
		if(cuidadorSeleccionado.revisar(animalSeleccionado)) {
			System.out.println("RESULTADO: El animal se encuentra con buen estado de ánimo.\n");
		/* En caso que el animal esté con mal estado de ánimo, se le informará al usuario y el cuidador seleccionado procederá a alimentar al animal
		 * a través del método animentarAnimal(...). */
		} else {
			System.out.println("RESULTADO: El animal se encuentra con mal estado de ánimo.\n");
			System.out.println("El cuidador " + cuidadorSeleccionado.getNombre() + " decide alimentar al animal para mejorar su estado de ánimo.");
			cuidadorSeleccionado.alimentarAnimal(animalSeleccionado);
			/* El estado de ánimo depende de su alimentación, su estado de salud y de la limpieza de su hábitat. El siguiente if cambia el estado
			 * de ánimo del animal a bueno (true) en caso que estos tres factores también sean buenos (true). */
			if(animalSeleccionado.isAlimentado() && animalSeleccionado.isEstadoSalud() && animalSeleccionado.getHabitat().isLimpio()) {
				animalSeleccionado.setEstadoAnimo(true);
			}
			// Si luego de haber sido alimentado, el estado de ánimo del animal mejoró, se le informa al usuario y se termina la funcionalidad.
			if(cuidadorSeleccionado.revisar(animalSeleccionado)) {
				System.out.println("Alimentar al animal ha dado buen resultado y este ahora se encuentra con buen estado de ánimo.");
			/* En caso que el animal continúe con mal estado de ánimo, se le informará al usuario que alimentarlo no ha sido de ayuda. Además, se le
			 * indicará al usuario que puede probar con la funcionalidad de mantenimiento y la de curar para así mejorar el estado de ánimo del animal. */
			} else {
				System.out.println("Alimentar al animal no ha mejorado su estado de ánimo.");
				System.out.println("Puede solicitar que se haga mantenimiento a su hábitat o hacerlo revisar con un veterinario para mejorar su estado.");
			}
		}
		return;
	}
}
