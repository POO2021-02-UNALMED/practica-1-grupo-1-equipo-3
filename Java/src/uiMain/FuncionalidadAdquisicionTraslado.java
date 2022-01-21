// CLASE CREADA POR DAVID MATEO GARCÍA

/* En esta clase se realiza la funcionalidad de la adquisición y el traslado de animales. Adquirir un animal corresponde a
 * crear un objeto tipo Animal de acuerdo a los atributos que especifique el usuario, esto en base primero a la especie que
 * el usuario haya seleccionado, además de depender que haya un hábitat disponible para crear a dicho animal. Por otro lado, 
 * trasladar un animal corresponde a eliminar del sistema el objeto tipo Animal que especifique el usuario.
 * 
 * Son necesarias las clases Especie, Habitat, Animal y Administración.
 */

package uiMain;

import gestorAplicacion.gestionZoologico.Administracion;

import java.util.ArrayList;
import java.util.List;
import java.util.InputMismatchException;

import gestorAplicacion.animalesZoologico.*;

public class FuncionalidadAdquisicionTraslado {
	static Especie especieSeleccionada;
	static Habitat habitatSeleccionado;
	static Animal animalSeleccionado;
	
	// El método adquisicionTraslado() es el método a llamar desde la clase Main. Desde este método es donde se controla la ejecución de esta funcionalidad.
	static void adquisicionTraslado() {
		int opcion;
		System.out.println("Primero elija qué desea hacer:\n");
		System.out.println("1. Adquirir animales");
		System.out.println("2. Trasladar animales");
		System.out.print("\n¿Cuál opción quiere realizar? ");
		opcion = Main.leerOpcion();
		System.out.println();
		// De acuerdo a la opción que el usuario elija se ejecutará la secuencia para adquirir o trasladar un animal.
		switch(opcion) {
			case 1: {
				seleccionarEspecie("adquirir");
				/* Por medio de la variable "habitatsDisponibles" se verifica si hay por lo menos un hábitat para depositar al animal de acuerdo a la
				 * especie que seleccionó el usuario. En caso que no haya tan siquiera uno se cancela la adquisición del animal. */
				boolean habitatsDisponibles = seleccionarHabitat();
				if(habitatsDisponibles) ingresarAnimal();
				break;
			}
			case 2: {
				seleccionarEspecie("trasladar");
				/* Por medio de la variable "animalesDisponibles" se verifica si hay por lo menos un animal (de la especie seleccionada por el usuario)
				 * para trasladar. En caso que no haya tan siquiera uno se cancela el traslado del animal. */
				boolean animalesDisponibles = seleccionarAnimal();
				if(animalesDisponibles) {
					Administracion.trasladarAnimal(animalSeleccionado);
					System.out.println("\nANIMAL TRASLADADO EXITOSAMENTE\n");
				}
				break;
			}
			// En caso que el usuario haya seleccionado una opción que no corresponda, se le informa.
			default: System.out.println("OPCIÓN INCORRECTA: Solo opciones 1 y 2."); break;
		}
		/* El método continuar() de la clase Main es usado para que el usuario tenga tiempo de leer las salidas proporcionadas por la funcionalidad
		 * Este método evita que se repita inmediatamente el ciclo de elegir la funcionalidad a realizar, esto por medio de esperar la acción del usuario */
		Main.continuar();
		return;
	}
	
	/* A través del método seleccionarEspecie(...) se obtiene la especie del animal que el usuario desea tratar (Adquirir o trasladar).
	 * El parámetro "accion" es requerido para incluirlo en el mensaje mostrado al usuario, pues de acuerdo a la opción elegida por el 
	 * usuario en el método adquisionTraslado(), se puede tratar de adquirir o trasladar a un animal. */
	static void seleccionarEspecie(String accion) {
		int opcion;
		System.out.println("Elija primero la especie del animal que desea " + accion + ", eligiendo la opción correspondiente:\n");
		
		int num = 1;
		// El siguiente for imprime y enumera el nombre de cada objeto de Especie almacenado en la lista de especies de Administración
		for(Especie especie : Administracion.getEspecies()) {
			System.out.println(String.valueOf(num) + ". " + especie.getNombre());
			num++;
		}
		
		System.out.print("\n¿Cuál opción de especie elije? ");
		opcion = Main.leerOpcion();
		
		// A través del siguiente while se le solicita al usuario la opción tantas veces como sea necesario hasta que esta sea correcta.
		while(true) {
			if(opcion < 1 || opcion > 5) {
				System.out.println("\nOPCIÓN INCORRECTA: Opciones solo del 1 al 5");
				System.out.print("\n¿Cuál opción de especie elije? ");
				opcion = Main.leerOpcion();
			} else {
				System.out.println("\nEspecie seleccionada:\n");
				/* Ya que las especies fueron enumeradas en el orden de la lista de especies (empezando desde el 1), entonces la posición de la
				 * especie seleccionada en esa lista corresponderá a la opción del usuario menos 1. */
				especieSeleccionada = Administracion.getEspecies().get(opcion-1);
				System.out.println(especieSeleccionada.info());
				break;
			}
		}
	}
	
	// A través del método seleccionarHabitat() se obtiene el hábitat donde el animal a adquirir será depositado.
	static boolean seleccionarHabitat() {
		int id;
		/* Con la variable "habitats" se contará, como ya se dijo, si hay por lo menos un hábitat de la especie seleccionada por el usuario
		 * para depositar en dicho hábitat al animal a adquirir. */
		int habitats = 0;
		/* En la variable "identificaciones" se almacenarán las identificaciones de los animales listados, esto para verificar que el usuario
		 * eligió una identificación válida. */
		List<Integer> identificaciones = new ArrayList<Integer>();
		System.out.println("\nAhora elija el hábitat donde el animal que desea adquirir será depositado, ingresando su identificación:");
		System.out.println("(Los hábitats listados corresponden únicamente a hábitats donde la especie de dicho animal puede ser depositada)\n");
		System.out.println("Identificación; Nombre; Ambientación; Capacidad Animales / Capacidad máxima");

		
		// Con el siguiente for se obtienen cada uno de los hábitats almacenandos en la lista de habitats de la clase Administración.
		for(Habitat habitat : Administracion.getHabitats()) {
			if (habitat.getAnimalesAsociados().isEmpty()) {
				if (habitat.getNombre().equals("Veterinaria")){
					continue;
				}
				if (habitat.getNombre().equals("Jaulas")){
					continue;
				}
				System.out.println(String.valueOf(habitat.getIdentificacion()) + "; " + habitat.getNombre() + "; " + 
						   habitat.getAmbientacion() + "; " + String.valueOf(habitat.cantidadAnimales()) + " / " +
						   String.valueOf(habitat.getCapacidadMaxima()));
				// Como se dijo, se van contando los hábitats que son listados, además de almacenar sus identificaciones.
				habitats++;
				identificaciones.add(habitat.getIdentificacion());
			 
			}
			
			/* Además, con el siguiente for, se obtiene cada uno de los animales asociados a cada uno de los hábitats obtenidos con el anterior for que
			 * hayan contenido al menos un animal. */
			for(Animal animal : habitat.getAnimalesAsociados()) {
				/* Todo esto se hace para buscar de manera efectiva los hábitats que puedan contener la especie del animal que se va a adquirir,
				 * para luego imprimir los datos de cada uno de estos hábitats por pantalla para que el usuario seleccione uno. */
				if(animal.getEspecie() == especieSeleccionada && habitat.cantidadAnimales() < habitat.getCapacidadMaxima()) {
					System.out.println(String.valueOf(habitat.getIdentificacion()) + "; " + habitat.getNombre() + "; " + 
							   habitat.getAmbientacion() + "; " + String.valueOf(habitat.cantidadAnimales()) + " / " +
							   String.valueOf(habitat.getCapacidadMaxima()));
					// Como se dijo, se van contando los hábitats que son listados, además de almacenar sus identificaciones.
					habitats++;
					identificaciones.add(habitat.getIdentificacion());
					break;
				}
			}
		}
		
		// En caso que no haya ni un hábitat para depositar al animal, se le informa al usuario y la adquisición queda cancelada.
		if(habitats == 0) {
			System.out.println("\nNo se ha encontrado ningún hábitat disponible para depositar al animal.");
			System.out.println("ADQUISICIÓN CANCELADA\n");
			// Se retorna false para la verificación en la clase adquisicionTraslado(), como se dijo anteriormente.
			return false;
		/* En caso que haya por lo menos un hábitat para depositar al animal, se le solicitará al usuario que elija el hábitat de
		 * acuerdo a la identificación de este. Recordar que los hábitats ya fueron listados con los for anteriores. */
		} else {
			System.out.print("\n¿Cuál hábitat elije? (Identificación): ");
			id = Main.leerOpcion();
			
			boolean estado = true;
			// A través del siguiente while se le solicita al usuario la identificación tantas veces como sea necesario hasta que esta sea correcta.
			while(estado) {
				if(identificaciones.contains(id)==false) {
					System.out.println("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida.");
					System.out.print("\n¿Cuál hábitat elije? (Identificación): ");
					id = Main.leerOpcion();
				} else {
					// Con el siguiente for se vuelve a recorrer el listado de todos los hábitats.
					for(Habitat habitat : Administracion.getHabitats()) {
						/* En caso que la identificación de un hábitat corresponda a la identificación que seleccionó el usuario, se imprimen los datos 
						 * del hábitat seleccionado y se asigna dicho hábitat al atributo estático "habitatSeleccionado", necesario para la adquisición. */
						if(habitat.getIdentificacion() == id) { 
							System.out.println("\nHábitat seleccionado:\n");
							System.out.println(habitat.info());
							habitatSeleccionado = habitat;
							estado = false;
							break;
						}
					}
				}
			}
			// Se retorna true para la verificación en la clase adquisicionTraslado(), como se dijo anteriormente.
			return true;
		}
	}
	
	// A través del método seleccionarAnimal() se obtiene el animal que será trasladado.
	static boolean seleccionarAnimal() {
		int id;
		/* Con la variable "animales" se contará, como ya se dijo, si hay por lo menos un animal de la especie seleccionada por el usuario
		 * para trasladar. */
		int animales = 0;
		/* En la variable "identificaciones" se almacenarán las identificaciones de los animales listados, esto para verificar que el usuario
		 * eligió una identificación válida. */
		List<Integer> identificaciones = new ArrayList<Integer>();
		System.out.println("\nAhora elija el animal que desee trasladar, ingresando su identificación.\n");
		System.out.println("Identificación; Especie; Hábitat; Género; Edad; Peso");
		
		// Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administración.
		for(Animal animal : Administracion.getAnimales()) {
			/* Esto se hace para buscar los animales correspondientes a la especie del animal que se va a trasladar, para luego imprimir 
			 * los datos de cada uno de estos animales por pantalla para que el usuario seleccione uno para trasladar. */
			if(animal.getEspecie() == especieSeleccionada) {
				System.out.println(String.valueOf(animal.getIdentificacion()) + "; " + animal.getEspecie().getNombre() + "; " + 
						   animal.getHabitat().getNombre() + "; " + animal.getGenero() + "; " + 
						   String.valueOf(animal.getEdad()) + "; " + String.valueOf(animal.getPeso()));
				// Como se dijo, se van contando los animales que son listados, además de almacenar sus identificaciones.
				animales++;
				identificaciones.add(animal.getIdentificacion());
			}
		}
		
		// En caso que no haya ni un solo animal de la especie seleccionada, se le informa al usuario y el traslado queda cancelado.
		if(animales == 0) {
			System.out.println("\nNo se ha encontrado ningún animal de la especie solicitada para trasladar.");
			System.out.println("TRASLADO CANCELADO\n");
			// Se retorna false para la verificación en la clase adquisicionTraslado(), como se dijo anteriormente.
			return false;
		/* En caso que haya por lo menos un animal de la especie seleccionada, se le solicitará al usuario que elija el animal de
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
						 * del animal seleccionado y se asigna dicho animal al atributo estático "animalSeleccionado", necesario para el traslado. */
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
			// Se retorna true para la verificación en la clase adquisicionTraslado(), como se dijo anteriormente.
			return true;
		}
	}
	
	// A través del método ingresarAnimal() el usuario ingresa los atributos del animal a adquirir.
	static void ingresarAnimal() {
		System.out.println("\nPor último, ingrese los datos del animal que se va a adquirir:\n");
		System.out.print("Género (M o H): ");
		String genero=Main.sc.next();
		while(true) {
			if(genero.equals("M") || genero.equals("H")) {
				break;
			} else {
				System.out.println("\nGÉNERO INCORRECTO: Ingrese M o H\n");
				System.out.print("Género (M o H): ");
				genero=Main.sc.next();
			}
		}
		System.out.print("Edad en años (Número): ");
		int edad=Main.sc.nextInt();
		while(true) {
			if(edad < 0) {
				System.out.println("\nEDAD INCORRECTA: Ingrese un número positivo\n");
				System.out.print("Edad en años (Número): ");
				edad=Main.sc.nextInt();
			} else {
				break;
			}
		}
		System.out.print("Peso en Kg (Número): ");
		float peso=Main.sc.nextFloat();
		while(true) {
			if(peso < 0.0) {
				System.out.println("\nPESO INCORRECTO: Ingrese un número positivo\n");
				System.out.print("Peso en Kg (Número): ");
				peso=Main.sc.nextFloat();
			} else {
				break;
			}
		}
		/* Se llama al método adquirirAnimal(...) de la clase Administracion, pues este método se encarga de crear el objeto tipo Animal
		 * en base a los atributos que el usuario ingresó. */
		Administracion.adquirirAnimal(especieSeleccionada, habitatSeleccionado, genero, edad, peso);
		System.out.println("\nANIMAL ADQUIRIDO EXITOSAMENTE\n");
	}
}
