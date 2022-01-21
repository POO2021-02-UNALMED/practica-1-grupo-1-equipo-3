// CLASE CREADA POR Juan Jose Monsalve Marin

/*
 En esta clase realiza la funcionalidad de curar de los animales 
 Primero se debe de identificar el cuidador que moverï¿½ a los animales, el animal que serï¿½ trasladado a la 
 veterinaria y el veterinario tratante que atenderï¿½ al animal. Todo esto se hace despuï¿½s de que un cuidador 
 allï¿½ revisando el animal y se percatara de que el estado de animo del animal no cambio despuï¿½s de alimentarlo. 
 esto ultimo se realiza en la clase "FuncionalidadCuidar"

 Son necesarias las clases animal, veterinario y cuidador.  
*/

package uiMain;

import java.util.*;
import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;

public class FuncionalidadCurar {

    static Animal animalSeleccionado;
	static Cuidador cuidadorSeleccionado;
	static Veterinario veterinarioSeleccionado;
	static Habitat habitatSeleccionado;
	static Habitat veterinaria = new Habitat("Veterinaria");

    static String leerString() {
		return Main.sc.nextLine();
	}
    
	// El mï¿½todo curarAnimal() es el mï¿½todo a llamar desde la clase Main. Desde este mï¿½todo es donde se controla la ejecuciï¿½n de esta funcionalidad.
    static void curarAnimal() {
		/* Por medio de la variable "animalesDisponibles" se verifica si hay por lo menos un animal para revisar.
		 * En caso que no haya tan siquiera uno se cancela la revisiï¿½n del animal. */
		boolean animalesDisponibles = seleccionarAnimal();
		if(animalesDisponibles) {
			/* Por medio de la variable "cuidadoresDisponibles" se verifica si hay por lo menos un cuidar que pueda revisar al animal, pues depende
			 * de la especie del animal y la especialidad de los cuidadores. En caso que no haya tan siquiera uno se cancela la revisiï¿½n del animal. */
			boolean cuidadoresDisponible = seleccionarCuidador();
			if(cuidadoresDisponible) {
				/* Por medio de la variable "veterinariosDisponibles" se verifica si hay por lo menos un veterinario que pueda revisar al animal, pues depende
			     * de la especie del animal y la especialidad de los cuidadores. En caso que no haya tan siquiera uno se cancela la revisiï¿½n del animal. */
				boolean veterinariosDisponibles = seleccionarVeterinario();
				if(veterinariosDisponibles) {
					saludAnimal();
				}
			}
		}
		/* El mï¿½todo continuar() de la clase Main es usado para que el usuario tenga tiempo de leer las salidas proporcionadas por la funcionalidad
		 * Este mï¿½todo evita que se repita inmediatamente el ciclo de elegir la funcionalidad a realizar, esto por medio de esperar la acciï¿½n del usuario */
		Main.continuar();
	}

	// A travï¿½s del mï¿½todo seleccionarAnimal() se obtiene el animal que serï¿½ revisado.
    static boolean seleccionarAnimal() {
		int id;
		// Con la variable "animales" se contarï¿½, como ya se dijo, si hay por lo menos un animal para revisar.
		int animales = 0;
		/* En la variable "identificaciones" se almacenarï¿½n las identificaciones de los animales listados, esto para verificar que el usuario
		 * eligiï¿½ una identificaciï¿½n vï¿½lida. */
		List<Integer> identificaciones = new ArrayList<Integer>();
		System.out.println("Elija primero el animal que desee revisar, ingresando su identificación.\n");
		System.out.println("Identificación; Especie; Hábitat; Género; Edad; Peso");
		
		// Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administraciï¿½n.
		for(Animal animal : Administracion.getAnimales()) {
			System.out.println(String.valueOf(animal.getIdentificacion()) + "; " + animal.getEspecie().getNombre() + "; " + 
							   animal.getHabitat().getNombre() + "; " + animal.getGenero() + "; " + 
							   String.valueOf(animal.getEdad()) + "; " + String.valueOf(animal.getPeso()));
			// Como se dijo, se van contando los animales que son listados, ademï¿½s de almacenar sus identificaciones.
			animales++;
			identificaciones.add(animal.getIdentificacion());
		}
		
		// En caso que no haya ni un solo animal para revisar, se le informa al usuario y la revisiï¿½n queda cancelada
		if(animales == 0) {
			System.out.println("\nNo se ha encontrado ningún animal para revisar.");
			System.out.println("REVISIÓN CANCELADA\n");
			// Se retorna false para la verificaciï¿½n en la clase cuidarAnimal(), como se dijo anteriormente.
			return false;
		/* En caso que haya por lo menos un animal para revisar, se le solicitarï¿½ al usuario que elija el animal de
		 * acuerdo a la identificaciï¿½n de este. Recordar que los animales ya fueron listados con el for anterior. */
		} else {
			System.out.print("\n¿Cuál animal elije? (Identificación): ");
			id = Main.leerOpcion();

			boolean estado = true;
			// A travï¿½s del siguiente while se le solicita al usuario la identificaciï¿½n tantas veces como sea necesario hasta que esta sea correcta.
			while(estado) {
				if(identificaciones.contains(id)==false) {
					System.out.println("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida.");
					System.out.print("\n¿Cuál animal elije? (Identificación): ");
					id = Main.leerOpcion();
				} else {
					// Con el siguiente for se vuelve a recorrer el listado de todos los animales.
					for(Animal animal : Administracion.getAnimales()) {
						/* En caso que la identificaciï¿½n de un animal corresponda a la identificaciï¿½n que seleccionï¿½ el usuario, se imprimen los datos 
						 * del animal seleccionado y se asigna dicho animal al atributo estï¿½tico "animalSeleccionado", necesario para la revisiï¿½n. */
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
			// Se retorna true para la verificaciï¿½n en la clase cuidarAnimal(), como se dijo anteriormente.
			return true;
		}
	}

	// A travï¿½s del mï¿½todo seleccionarVeterinario() se obtiene el veterinario que revisarï¿½ y curara al animal.
    static boolean seleccionarVeterinario() {
		int id;
		/* Con la variable "veterinarios" se contarï¿½, como ya se dijo, si hay por lo menos un veterinario especializado en la especie del animal
		 * seleccionado por el usuario para revisar a animal. */
		int veterinarios = 0;
		/* En la variable "identificaciones" se almacenarï¿½n las identificaciones de los veterinarios listados, esto para verificar que el usuario
		 * eligiï¿½ una identificaciï¿½n vï¿½lida. */
		List<Integer> identificaciones = new ArrayList<Integer>();
		System.out.println("\nAhora elija el veterinario que desee que revise al animal, ingresando su identificación.\n");
		System.out.println("Identificación; Nombre; Especie asignada");
		
		// Con el siguiente for se obtienen cada uno de los veterinarios almacenandos en la lista de veterinarios de la clase Administracion.
		for(Veterinario veterinario : Administracion.getVeterinarios()) {
			/* Con el if se buscan los veterinarios que puedan revisar al animal de acuerdo a su especie, esto para imprimir los datos de cada 
			 * uno de estos veterinarios por pantalla para que el usuario seleccione el que va a revisar al animal. */
			if(veterinario.getEspecialidad() == animalSeleccionado.getEspecie()) {
				System.out.println(String.valueOf(veterinario.getIdentificacion()) + "; " + veterinario.getNombre() + "; " + veterinario.getEspecialidad().getNombre());
				// Como se dijo, se van contando los veterinarios que son listados, ademï¿½s de almacenar sus identificaciones.
				veterinarios++;
				identificaciones.add(veterinario.getIdentificacion());
			}
		}
		
		// En caso que no haya ni un solo veterinario que pueda revisar al animal, se le informa al usuario y la revisiï¿½n queda cancelada.
		if(veterinarios == 0) {
			System.out.println("\nNo se ha encontrado ningún veterinario para revisar al animal.");
			System.out.println("REVISIÓN CANCELADA\n");
			// Se retorna false para la verificaciï¿½n en la clase curarAnimal(), como se dijo anteriormente.
			return false;
			/* En caso que haya por lo menos un veterinario para revisar al animal, se le solicitarï¿½ al usuario que elija el veterinario de
		     * acuerdo a la identificaciï¿½n de este. Recordar que los veterinarios ya fueron listados con el for anterior. */
		} else {
			System.out.print("\n¿Cuál veterinario elije? (Identificación) ");
			id = Main.leerOpcion();

			boolean estado = true;
			// A travï¿½s del siguiente while se le solicita al usuario la identificaciï¿½n tantas veces como sea necesario hasta que esta sea correcta.
			while(estado) {
				if(identificaciones.contains(id)==false) {
					System.out.println("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida.");
					System.out.print("\n¿Cuál veterinario elije? (Identificación) ");
					id = Main.leerOpcion();
				} else {
					// Con el siguiente for se vuelve a recorrer el listado de todos los veterinarios en la lista de veterinarios de la clase Administracion.
					for(Veterinario veterinario : Administracion.getVeterinarios()) {
						/* En caso que la identificaciï¿½n de un veterinario corresponda a la identificaciï¿½n que seleccionï¿½ el usuario, se imprimen los datos 
						 * del veterinario seleccionado y se asigna dicho veterinario al atributo estï¿½tico "veterinarioSeleccionado", necesario para la revisiï¿½n. */
						if(veterinario.getIdentificacion() == id) { 
							System.out.println("\nCuidador seleccionado:\n");
							System.out.println(veterinario.info());
							veterinarioSeleccionado = veterinario;
							estado = false;
							break;
						}
					}
				}
			}
			// Se retorna true para la verificaciï¿½n en la clase cuidarAnimal(), como se dijo anteriormente.
			return true;
		}
	}

	// A travï¿½s del mï¿½todo seleccionarCuidador() se obtiene el cuidador que revisarï¿½ al animal.
	static boolean seleccionarCuidador() {

		int id;
		/* Con la variable "cuidadores" se contarï¿½, como ya se dijo, si hay por lo menos un cuidador especializado en la especie del animal
		 * seleccionado por el usuario para revisar a animal. */
		int cuidadores = 0;
		/* En la variable "identificaciones" se almacenarï¿½n las identificaciones de los animales listados, esto para verificar que el usuario
		 * eligiï¿½ una identificaciï¿½n vï¿½lida. */
		List<Integer> identificaciones = new ArrayList<Integer>();
		System.out.println("\nElija el cuidador que desee que traslade al animal, ingresando su identificación.\n");
		System.out.println("Identificación; Nombre; Especie asignada");
		
		// Con el siguiente for se obtienen cada uno de los cuidadores almacenandos en la lista de cuidadores de la clase Administracion.
		for(Cuidador cuidador : Administracion.getCuidadores()) {
			/* Con el if se buscan los cuidadores que puedan revisar al animal de acuerdo a su especie, esto para imprimir los datos de cada 
			 * uno de estos cuidadores por pantalla para que el usuario seleccione el que va a revisar al animal. */
			if(cuidador.getEspecieAsignada() == animalSeleccionado.getEspecie()) {
				System.out.println(String.valueOf(cuidador.getIdentificacion()) + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre());
				// Como se dijo, se van contando los cuidadores que son listados, ademï¿½s de almacenar sus identificaciones.
				cuidadores++;
				identificaciones.add(cuidador.getIdentificacion());
			}
		}
		
		// En caso que no haya ni un solo cuidadores que pueda revisar al animal, se le informa al usuario y la revisiï¿½n queda cancelada.
		if(cuidadores == 0) {
			System.out.println("\nNo se ha encontrado ningún cuidador para trasladar al animal.");
			System.out.println("REVISIÓN CANCELADA\n");
			// Se retorna false para la verificaciï¿½n en la clase cuidarAnimal(), como se dijo anteriormente.
			return false;
		/* En caso que haya por lo menos un cuidador para revisar al animal, se le solicitarï¿½ al usuario que elija el cuidador de
		 * acuerdo a la identificaciï¿½n de este. Recordar que los cuidadores ya fueron listados con el for anterior. */
		} else {
			System.out.print("\n¿Cuál cuidador elije? (Identificación) ");
			id = Main.leerOpcion();

			boolean estado = true;
			// A travï¿½s del siguiente while se le solicita al usuario la identificaciï¿½n tantas veces como sea necesario hasta que esta sea correcta.
			while(estado) {
				if(identificaciones.contains(id)==false) {
					System.out.println("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida.");
					System.out.print("\n¿Cuál cuidador elije? (Identificación) ");
					id = Main.leerOpcion();
				} else {
					// Con el siguiente for se vuelve a recorrer el listado de todos los cuidadores en la lista de cuidadores de la clase Administracion.
					for(Cuidador cuidador : Administracion.getCuidadores()) {
						/* En caso que la identificaciï¿½n de un cuidador corresponda a la identificaciï¿½n que seleccionï¿½ el usuario, se imprimen los datos 
						 * del cuidador seleccionado y se asigna dicho cuidador al atributo estï¿½tico "cuidadorSeleccionado", necesario para la revisiï¿½n. */
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
			// Se retorna true para la verificaciï¿½n en la clase cuidarAnimal(), como se dijo anteriormente.
			return true;
		}
	}

	// A travï¿½s del mï¿½todo saludAnimal() se hace el proceso de revisar el estado de salud del animal seleccionado desde el cuidador seleccionado y veterinario seleccionado.
    static void saludAnimal() {
		// SE guarda el habitad de procedencia del animal, para que luego pueda ser devuelto.
		habitatSeleccionado = animalSeleccionado.getHabitat();
		System.out.println("\nCuidador " + cuidadorSeleccionado.getNombre() + " procede a mover al animal con identificación " + String.valueOf(animalSeleccionado.getIdentificacion()) + " a la veterinaria.");
		cuidadorSeleccionado.moverAnimal(animalSeleccionado, veterinaria);
		System.out.println("Veterinario " + veterinarioSeleccionado.getNombre() + " procede a revisar al animal con identificación " + String.valueOf(animalSeleccionado.getIdentificacion()) + ".");
		
		// En caso que el animal estï¿½ con buen estado de salud (revisar(...) retorna true), se le informarï¿½ al usuario y se termina la funcionalidad.
		if(veterinarioSeleccionado.revisar(animalSeleccionado)) {
			System.out.println("RESULTADO: El animal se encuentra con buen estado de salud.\n");
			System.out.println("Cuidador " + cuidadorSeleccionado.getNombre() + " procede a mover al animal con identificación " + 
								String.valueOf(animalSeleccionado.getIdentificacion()) + " de regreso a su hábitat.");
			// Se regresa al animal a su habitad
			cuidadorSeleccionado.moverAnimal(animalSeleccionado, habitatSeleccionado);
			
			if(animalSeleccionado.isAlimentado() && animalSeleccionado.getHabitat().isLimpio()) {
				animalSeleccionado.setEstadoAnimo(true);}
			
			if (animalSeleccionado.isEstadoAnimo()==false) {
				System.out.println("El estado de animo para est animal sigue siendo malo. Puede solicitar mantenimiento de habitat o alimentación del animal.");
			} else {
				System.out.println("El animal se encuentra con un buen estado de ánimo.");
			}
			
		/* En caso que el animal estï¿½ con mal estado de salud, se le informarï¿½ al usuario y el veterinario seleccionado procederï¿½ a curar al animal
		 * a travï¿½s del mï¿½todo curarAnimal(...). */
		} else {
			System.out.println("RESULTADO: El animal se encuentra con mal estado de salud.\n");
			System.out.println("El veterinario " + veterinarioSeleccionado.getNombre() + "decide hacer curación al animal para mejorar su estado de salud.");
			veterinarioSeleccionado.curarAnimal(animalSeleccionado);
			// Si luego de haber sido curado, el estado de ánimo del animal mejora, se le informa al usuario y se termina la funcionalidad.
			if(veterinarioSeleccionado.revisar(animalSeleccionado)) {
				System.out.println("Curar al animal ha dado buen resultado y este ahora se encuentra con buen estado de salud.");
				System.out.println("\nCuidador " + cuidadorSeleccionado.getNombre() + " procede a mover al animal con identificación " + 
						String.valueOf(animalSeleccionado.getIdentificacion()) + " de regreso a su hábitat.");
				cuidadorSeleccionado.moverAnimal(animalSeleccionado, habitatSeleccionado);}
			/* El estado de ï¿½nimo depende de su alimentaciï¿½n, su estado de salud y de la limpieza de su hï¿½bitat. El siguiente if cambia el estado
			 * de ï¿½nimo del animal a bueno (true) en caso que estos tres factores tambiï¿½n sean buenos (true). */
			if(animalSeleccionado.isAlimentado() && animalSeleccionado.isEstadoSalud() && animalSeleccionado.getHabitat().isLimpio()) {
				animalSeleccionado.setEstadoAnimo(true);
			}
			if (animalSeleccionado.isEstadoAnimo()) {
				System.out.println("Curar la salud del animal ha dado buenos resultados. El animal ya no se encuentra triste.");
			} else {
				System.out.println("El estado de animo para este animal sigue siendo malo. Puede solicitar mantenimiento de habitat o alimentación del animal.");
			}}
		System.out.println("REVISIÓN FINALIZADA\n");
		return;
	}
    
}
