// CLASE CREADA POR DAVID MATEO GARC�A

/* En esta clase se realiza la funcionalidad de cuidar de los animales. Para esta clase, un cuidador deber� revisar el estado
 * de �nimo del animal elegido por el usuario. En caso que el animal se encuentre con mal estado de �nimo el cuidador lo
 * alimentara. Si al alimentar al animal su estado de �nimo no mejora, se le informar� al usuario para que tome por si mismo
 * la decisi�n de qu� otra funcionalidad evaluar.
 * 
 * Son necesarias las clases Animal, Cuidador y Administraci�n.
 */

package uiMain;

import java.util.*;
import gestorAplicacion.gestionZoologico.Administracion;
import gestorAplicacion.gestionZoologico.Cuidador;
import gestorAplicacion.animalesZoologico.Animal;

public class FuncionalidadCuidar {
	static Animal animalSeleccionado;
	static Cuidador cuidadorSeleccionado;
	
	// El m�todo cuidarAnimal() es el m�todo a llamar desde la clase Main. Desde este m�todo es donde se controla la ejecuci�n de esta funcionalidad.
	static void cuidarAnimal() {
		/* Por medio de la variable "animalesDisponibles" se verifica si hay por lo menos un animal para revisar.
		 * En caso que no haya tan siquiera uno se cancela la revisi�n del animal. */
		boolean animalesDisponibles = seleccionarAnimal();
		if(animalesDisponibles) {
			/* Por medio de la variable "cuidadoresDisponibles" se verifica si hay por lo menos un cuidar que pueda revisar al animal, pues depende
			 * de la especie del animal y la especialidad de los cuidadores. En caso que no haya tan siquiera uno se cancela la revisi�n del animal. */
			boolean cuidadoresDisponibles = seleccionarCuidador();
			if(cuidadoresDisponibles) animoAnimal();
		}
		System.out.println();
		/* El m�todo continuar() de la clase Main es usado para que el usuario tenga tiempo de leer las salidas proporcionadas por la funcionalidad
		 * Este m�todo evita que se repita inmediatamente el ciclo de elegir la funcionalidad a realizar, esto por medio de esperar la acci�n del usuario */
		Main.continuar();
		return;
	}
	
	// A trav�s del m�todo seleccionarAnimal() se obtiene el animal que ser� revisado.
	static boolean seleccionarAnimal() {
		int id;
		// Con la variable "animales" se contar�, como ya se dijo, si hay por lo menos un animal para revisar.
		int animales = 0;
		/* En la variable "identificaciones" se almacenar�n las identificaciones de los animales listados, esto para verificar que el usuario
		 * eligi� una identificaci�n v�lida. */
		List<Integer> identificaciones = new ArrayList<Integer>();
		System.out.println("Elija primero el animal que desee revisar, ingresando su identificaci�n.\n");
		System.out.println("Identificaci�n; Especie; H�bitat; G�nero; Edad; Peso");
		
		// Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administraci�n.
		for(Animal animal : Administracion.getAnimales()) {
			// Esto se hace para imprimir los datos de cada uno de los animales por pantalla para que el usuario seleccione uno para revisar.
			System.out.println(String.valueOf(animal.getIdentificacion()) + "; " + animal.getEspecie().getNombre() + "; " + 
							   animal.getHabitat().getNombre() + "; " + animal.getGenero() + "; " + 
							   String.valueOf(animal.getEdad()) + "; " + String.valueOf(animal.getPeso()));
			// Como se dijo, se van contando los animales que son listados, adem�s de almacenar sus identificaciones.
			animales++;
			identificaciones.add(animal.getIdentificacion());
		}
		
		// En caso que no haya ni un solo animal para revisar, se le informa al usuario y la revisi�n queda cancelada.
		if(animales == 0) {
			System.out.println("\nNo se ha encontrado ning�n animal para revisar.");
			System.out.println("REVISI�N CANCELADA\n");
			// Se retorna false para la verificaci�n en la clase cuidarAnimal(), como se dijo anteriormente.
			return false;
		/* En caso que haya por lo menos un animal para revisar, se le solicitar� al usuario que elija el animal de
		 * acuerdo a la identificaci�n de este. Recordar que los animales ya fueron listados con el for anterior. */
		} else {
			System.out.print("\n�Cu�l animal elije? (Identificaci�n): ");
			id = Main.leerOpcion();
			
			boolean estado = true;
			// A trav�s del siguiente while se le solicita al usuario la identificaci�n tantas veces como sea necesario hasta que esta sea correcta.
			while(estado) {
				if(identificaciones.contains(id)==false) {
					System.out.println("\nIDENTIFICACI�N INCORRECTA: Ingrese una v�lida.");
					System.out.print("\n�Cu�l animal elije? (Identificaci�n): ");
					id = Main.leerOpcion();
				} else {
					// Con el siguiente for se vuelve a recorrer el listado de todos los animales.
					for(Animal animal : Administracion.getAnimales()) {
						/* En caso que la identificaci�n de un animal corresponda a la identificaci�n que seleccion� el usuario, se imprimen los datos 
						 * del animal seleccionado y se asigna dicho animal al atributo est�tico "animalSeleccionado", necesario para la revisi�n. */
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
			// Se retorna true para la verificaci�n en la clase cuidarAnimal(), como se dijo anteriormente.
			return true;
		}
	}
	
	// A trav�s del m�todo seleccionarCuidador() se obtiene el cuidador que revisar� al animal.
	static boolean seleccionarCuidador() {
		int id;
		/* Con la variable "cuidadores" se contar�, como ya se dijo, si hay por lo menos un cuidador especializado en la especie del animal
		 * seleccionado por el usuario para revisar a animal. */
		int cuidadores = 0;
		/* En la variable "identificaciones" se almacenar�n las identificaciones de los animales listados, esto para verificar que el usuario
		 * eligi� una identificaci�n v�lida. */
		List<Integer> identificaciones = new ArrayList<Integer>();
		System.out.println("\nAhora elija el cuidador que desee que revise al animal, ingresando su identificaci�n.\n");
		System.out.println("Identificaci�n; Nombre; Especie asignada");
		
		// Con el siguiente for se obtienen cada uno de los cuidadores almacenandos en la lista de cuidadores de la clase Administracion.
		for(Cuidador cuidador : Administracion.getCuidadores()) {
			/* Con el if se buscan los cuidadores que puedan revisar al animal de acuerdo a su especie, esto para imprimir los datos de cada 
			 * uno de estos cuidadores por pantalla para que el usuario seleccione el que va a revisar al animal. */
			if(cuidador.getEspecieAsignada() == animalSeleccionado.getEspecie()) {
				System.out.println(String.valueOf(cuidador.getIdentificacion()) + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre());
				// Como se dijo, se van contando los cuidadores que son listados, adem�s de almacenar sus identificaciones.
				cuidadores++;
				identificaciones.add(cuidador.getIdentificacion());
			}
		}
		
		// En caso que no haya ni un solo cuidadores que pueda revisar al animal, se le informa al usuario y la revisi�n queda cancelada.
		if(cuidadores == 0) {
			System.out.println("\nNo se ha encontrado ning�n cuidador para revisar al animal.");
			System.out.println("REVISI�N CANCELADA\n");
			// Se retorna false para la verificaci�n en la clase cuidarAnimal(), como se dijo anteriormente.
			return false;
		/* En caso que haya por lo menos un cuidador para revisar al animal, se le solicitar� al usuario que elija el cuidador de
		 * acuerdo a la identificaci�n de este. Recordar que los cuidadores ya fueron listados con el for anterior. */
		} else {
			System.out.print("\n�Cu�l cuidador elije? (Identificaci�n) ");
			id = Main.leerOpcion();
			
			boolean estado = true;
			// A trav�s del siguiente while se le solicita al usuario la identificaci�n tantas veces como sea necesario hasta que esta sea correcta.
			while(estado) {
				if(identificaciones.contains(id)==false) {
					System.out.println("\nIDENTIFICACI�N INCORRECTA: Ingrese una v�lida.");
					System.out.print("\n�Cu�l cuidador elije? (Identificaci�n) ");
					id = Main.leerOpcion();
				} else {
					// Con el siguiente for se vuelve a recorrer el listado de todos los cuidadores en la lista de cuidadores de la clase Administracion.
					for(Cuidador cuidador : Administracion.getCuidadores()) {
						/* En caso que la identificaci�n de un cuidador corresponda a la identificaci�n que seleccion� el usuario, se imprimen los datos 
						 * del cuidador seleccionado y se asigna dicho cuidador al atributo est�tico "cuidadorSeleccionado", necesario para la revisi�n. */
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
			// Se retorna true para la verificaci�n en la clase cuidarAnimal(), como se dijo anteriormente.
			return true;
		}
	}
	
	// A trav�s del m�todo animoAnimal() se hace el proceso de revisar el estado de �nimo del animal seleccionado desde el cuidador seleccionado.
	static void animoAnimal() {
		System.out.println("\nCuidador " + cuidadorSeleccionado.getNombre() + " procede a revisar al animal con identificaci�n " + 
							String.valueOf(animalSeleccionado.getIdentificacion()) + ".");
		
		// En caso que el animal est� con buen estado de �nimo (revisar(...) retorna true), se le informar� al usuario y se termina la funcionalidad. 
		if(cuidadorSeleccionado.revisar(animalSeleccionado)) {
			System.out.println("RESULTADO: El animal se encuentra con buen estado de �nimo.\n");
		/* En caso que el animal est� con mal estado de �nimo, se le informar� al usuario y el cuidador seleccionado proceder� a alimentar al animal
		 * a trav�s del m�todo animentarAnimal(...). */
		} else {
			System.out.println("RESULTADO: El animal se encuentra con mal estado de �nimo.\n");
			System.out.println("El cuidador " + cuidadorSeleccionado.getNombre() + " decide alimentar al animal para mejorar su estado de �nimo.");
			cuidadorSeleccionado.alimentarAnimal(animalSeleccionado);
			/* El estado de �nimo depende de su alimentaci�n, su estado de salud y de la limpieza de su h�bitat. El siguiente if cambia el estado
			 * de �nimo del animal a bueno (true) en caso que estos tres factores tambi�n sean buenos (true). */
			if(animalSeleccionado.isAlimentado() && animalSeleccionado.isEstadoSalud() && animalSeleccionado.getHabitat().isLimpio()) {
				animalSeleccionado.setEstadoAnimo(true);
			}
			// Si luego de haber sido alimentado, el estado de �nimo del animal mejor�, se le informa al usuario y se termina la funcionalidad.
			if(cuidadorSeleccionado.revisar(animalSeleccionado)) {
				System.out.println("Alimentar al animal ha dado buen resultado y este ahora se encuentra con buen estado de �nimo.");
			/* En caso que el animal contin�e con mal estado de �nimo, se le informar� al usuario que alimentarlo no ha sido de ayuda. Adem�s, se le
			 * indicar� al usuario que puede probar con la funcionalidad de mantenimiento y la de curar para as� mejorar el estado de �nimo del animal. */
			} else {
				System.out.println("Alimentar al animal no ha mejorado su estado de �nimo.");
				System.out.println("Puede solicitar que se haga mantenimiento a su h�bitat o hacerlo revisar con un veterinario para mejorar su estado.");
			}
		}
		return;
	}
}
