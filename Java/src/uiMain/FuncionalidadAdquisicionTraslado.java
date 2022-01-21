// CLASE CREADA POR DAVID MATEO GARC�A

/* En esta clase se realiza la funcionalidad de la adquisici�n y el traslado de animales. Adquirir un animal corresponde a
 * crear un objeto tipo Animal de acuerdo a los atributos que especifique el usuario, esto en base primero a la especie que
 * el usuario haya seleccionado, adem�s de depender que haya un h�bitat disponible para crear a dicho animal. Por otro lado, 
 * trasladar un animal corresponde a eliminar del sistema el objeto tipo Animal que especifique el usuario.
 * 
 * Son necesarias las clases Especie, Habitat, Animal y Administraci�n.
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
	
	// El m�todo adquisicionTraslado() es el m�todo a llamar desde la clase Main. Desde este m�todo es donde se controla la ejecuci�n de esta funcionalidad.
	static void adquisicionTraslado() {
		int opcion;
		System.out.println("Primero elija qu� desea hacer:\n");
		System.out.println("1. Adquirir animales");
		System.out.println("2. Trasladar animales");
		System.out.print("\n�Cu�l opci�n quiere realizar? ");
		opcion = Main.leerOpcion();
		System.out.println();
		// De acuerdo a la opci�n que el usuario elija se ejecutar� la secuencia para adquirir o trasladar un animal.
		switch(opcion) {
			case 1: {
				seleccionarEspecie("adquirir");
				/* Por medio de la variable "habitatsDisponibles" se verifica si hay por lo menos un h�bitat para depositar al animal de acuerdo a la
				 * especie que seleccion� el usuario. En caso que no haya tan siquiera uno se cancela la adquisici�n del animal. */
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
			// En caso que el usuario haya seleccionado una opci�n que no corresponda, se le informa.
			default: System.out.println("OPCI�N INCORRECTA: Solo opciones 1 y 2."); break;
		}
		/* El m�todo continuar() de la clase Main es usado para que el usuario tenga tiempo de leer las salidas proporcionadas por la funcionalidad
		 * Este m�todo evita que se repita inmediatamente el ciclo de elegir la funcionalidad a realizar, esto por medio de esperar la acci�n del usuario */
		Main.continuar();
		return;
	}
	
	/* A trav�s del m�todo seleccionarEspecie(...) se obtiene la especie del animal que el usuario desea tratar (Adquirir o trasladar).
	 * El par�metro "accion" es requerido para incluirlo en el mensaje mostrado al usuario, pues de acuerdo a la opci�n elegida por el 
	 * usuario en el m�todo adquisionTraslado(), se puede tratar de adquirir o trasladar a un animal. */
	static void seleccionarEspecie(String accion) {
		int opcion;
		System.out.println("Elija primero la especie del animal que desea " + accion + ", eligiendo la opci�n correspondiente:\n");
		
		int num = 1;
		// El siguiente for imprime y enumera el nombre de cada objeto de Especie almacenado en la lista de especies de Administraci�n
		for(Especie especie : Administracion.getEspecies()) {
			System.out.println(String.valueOf(num) + ". " + especie.getNombre());
			num++;
		}
		
		System.out.print("\n�Cu�l opci�n de especie elije? ");
		opcion = Main.leerOpcion();
		
		// A trav�s del siguiente while se le solicita al usuario la opci�n tantas veces como sea necesario hasta que esta sea correcta.
		while(true) {
			if(opcion < 1 || opcion > 5) {
				System.out.println("\nOPCI�N INCORRECTA: Opciones solo del 1 al 5");
				System.out.print("\n�Cu�l opci�n de especie elije? ");
				opcion = Main.leerOpcion();
			} else {
				System.out.println("\nEspecie seleccionada:\n");
				/* Ya que las especies fueron enumeradas en el orden de la lista de especies (empezando desde el 1), entonces la posici�n de la
				 * especie seleccionada en esa lista corresponder� a la opci�n del usuario menos 1. */
				especieSeleccionada = Administracion.getEspecies().get(opcion-1);
				System.out.println(especieSeleccionada.info());
				break;
			}
		}
	}
	
	// A trav�s del m�todo seleccionarHabitat() se obtiene el h�bitat donde el animal a adquirir ser� depositado.
	static boolean seleccionarHabitat() {
		int id;
		/* Con la variable "habitats" se contar�, como ya se dijo, si hay por lo menos un h�bitat de la especie seleccionada por el usuario
		 * para depositar en dicho h�bitat al animal a adquirir. */
		int habitats = 0;
		/* En la variable "identificaciones" se almacenar�n las identificaciones de los animales listados, esto para verificar que el usuario
		 * eligi� una identificaci�n v�lida. */
		List<Integer> identificaciones = new ArrayList<Integer>();
		System.out.println("\nAhora elija el h�bitat donde el animal que desea adquirir ser� depositado, ingresando su identificaci�n:");
		System.out.println("(Los h�bitats listados corresponden �nicamente a h�bitats donde la especie de dicho animal puede ser depositada)\n");
		System.out.println("Identificaci�n; Nombre; Ambientaci�n; Capacidad Animales / Capacidad m�xima");

		
		// Con el siguiente for se obtienen cada uno de los h�bitats almacenandos en la lista de habitats de la clase Administraci�n.
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
				// Como se dijo, se van contando los h�bitats que son listados, adem�s de almacenar sus identificaciones.
				habitats++;
				identificaciones.add(habitat.getIdentificacion());
			 
			}
			
			/* Adem�s, con el siguiente for, se obtiene cada uno de los animales asociados a cada uno de los h�bitats obtenidos con el anterior for que
			 * hayan contenido al menos un animal. */
			for(Animal animal : habitat.getAnimalesAsociados()) {
				/* Todo esto se hace para buscar de manera efectiva los h�bitats que puedan contener la especie del animal que se va a adquirir,
				 * para luego imprimir los datos de cada uno de estos h�bitats por pantalla para que el usuario seleccione uno. */
				if(animal.getEspecie() == especieSeleccionada && habitat.cantidadAnimales() < habitat.getCapacidadMaxima()) {
					System.out.println(String.valueOf(habitat.getIdentificacion()) + "; " + habitat.getNombre() + "; " + 
							   habitat.getAmbientacion() + "; " + String.valueOf(habitat.cantidadAnimales()) + " / " +
							   String.valueOf(habitat.getCapacidadMaxima()));
					// Como se dijo, se van contando los h�bitats que son listados, adem�s de almacenar sus identificaciones.
					habitats++;
					identificaciones.add(habitat.getIdentificacion());
					break;
				}
			}
		}
		
		// En caso que no haya ni un h�bitat para depositar al animal, se le informa al usuario y la adquisici�n queda cancelada.
		if(habitats == 0) {
			System.out.println("\nNo se ha encontrado ning�n h�bitat disponible para depositar al animal.");
			System.out.println("ADQUISICI�N CANCELADA\n");
			// Se retorna false para la verificaci�n en la clase adquisicionTraslado(), como se dijo anteriormente.
			return false;
		/* En caso que haya por lo menos un h�bitat para depositar al animal, se le solicitar� al usuario que elija el h�bitat de
		 * acuerdo a la identificaci�n de este. Recordar que los h�bitats ya fueron listados con los for anteriores. */
		} else {
			System.out.print("\n�Cu�l h�bitat elije? (Identificaci�n): ");
			id = Main.leerOpcion();
			
			boolean estado = true;
			// A trav�s del siguiente while se le solicita al usuario la identificaci�n tantas veces como sea necesario hasta que esta sea correcta.
			while(estado) {
				if(identificaciones.contains(id)==false) {
					System.out.println("\nIDENTIFICACI�N INCORRECTA: Ingrese una v�lida.");
					System.out.print("\n�Cu�l h�bitat elije? (Identificaci�n): ");
					id = Main.leerOpcion();
				} else {
					// Con el siguiente for se vuelve a recorrer el listado de todos los h�bitats.
					for(Habitat habitat : Administracion.getHabitats()) {
						/* En caso que la identificaci�n de un h�bitat corresponda a la identificaci�n que seleccion� el usuario, se imprimen los datos 
						 * del h�bitat seleccionado y se asigna dicho h�bitat al atributo est�tico "habitatSeleccionado", necesario para la adquisici�n. */
						if(habitat.getIdentificacion() == id) { 
							System.out.println("\nH�bitat seleccionado:\n");
							System.out.println(habitat.info());
							habitatSeleccionado = habitat;
							estado = false;
							break;
						}
					}
				}
			}
			// Se retorna true para la verificaci�n en la clase adquisicionTraslado(), como se dijo anteriormente.
			return true;
		}
	}
	
	// A trav�s del m�todo seleccionarAnimal() se obtiene el animal que ser� trasladado.
	static boolean seleccionarAnimal() {
		int id;
		/* Con la variable "animales" se contar�, como ya se dijo, si hay por lo menos un animal de la especie seleccionada por el usuario
		 * para trasladar. */
		int animales = 0;
		/* En la variable "identificaciones" se almacenar�n las identificaciones de los animales listados, esto para verificar que el usuario
		 * eligi� una identificaci�n v�lida. */
		List<Integer> identificaciones = new ArrayList<Integer>();
		System.out.println("\nAhora elija el animal que desee trasladar, ingresando su identificaci�n.\n");
		System.out.println("Identificaci�n; Especie; H�bitat; G�nero; Edad; Peso");
		
		// Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administraci�n.
		for(Animal animal : Administracion.getAnimales()) {
			/* Esto se hace para buscar los animales correspondientes a la especie del animal que se va a trasladar, para luego imprimir 
			 * los datos de cada uno de estos animales por pantalla para que el usuario seleccione uno para trasladar. */
			if(animal.getEspecie() == especieSeleccionada) {
				System.out.println(String.valueOf(animal.getIdentificacion()) + "; " + animal.getEspecie().getNombre() + "; " + 
						   animal.getHabitat().getNombre() + "; " + animal.getGenero() + "; " + 
						   String.valueOf(animal.getEdad()) + "; " + String.valueOf(animal.getPeso()));
				// Como se dijo, se van contando los animales que son listados, adem�s de almacenar sus identificaciones.
				animales++;
				identificaciones.add(animal.getIdentificacion());
			}
		}
		
		// En caso que no haya ni un solo animal de la especie seleccionada, se le informa al usuario y el traslado queda cancelado.
		if(animales == 0) {
			System.out.println("\nNo se ha encontrado ning�n animal de la especie solicitada para trasladar.");
			System.out.println("TRASLADO CANCELADO\n");
			// Se retorna false para la verificaci�n en la clase adquisicionTraslado(), como se dijo anteriormente.
			return false;
		/* En caso que haya por lo menos un animal de la especie seleccionada, se le solicitar� al usuario que elija el animal de
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
						 * del animal seleccionado y se asigna dicho animal al atributo est�tico "animalSeleccionado", necesario para el traslado. */
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
			// Se retorna true para la verificaci�n en la clase adquisicionTraslado(), como se dijo anteriormente.
			return true;
		}
	}
	
	// A trav�s del m�todo ingresarAnimal() el usuario ingresa los atributos del animal a adquirir.
	static void ingresarAnimal() {
		System.out.println("\nPor �ltimo, ingrese los datos del animal que se va a adquirir:\n");
		System.out.print("G�nero (M o H): ");
		String genero=Main.sc.next();
		while(true) {
			if(genero.equals("M") || genero.equals("H")) {
				break;
			} else {
				System.out.println("\nG�NERO INCORRECTO: Ingrese M o H\n");
				System.out.print("G�nero (M o H): ");
				genero=Main.sc.next();
			}
		}
		System.out.print("Edad en a�os (N�mero): ");
		int edad=Main.sc.nextInt();
		while(true) {
			if(edad < 0) {
				System.out.println("\nEDAD INCORRECTA: Ingrese un n�mero positivo\n");
				System.out.print("Edad en a�os (N�mero): ");
				edad=Main.sc.nextInt();
			} else {
				break;
			}
		}
		System.out.print("Peso en Kg (N�mero): ");
		float peso=Main.sc.nextFloat();
		while(true) {
			if(peso < 0.0) {
				System.out.println("\nPESO INCORRECTO: Ingrese un n�mero positivo\n");
				System.out.print("Peso en Kg (N�mero): ");
				peso=Main.sc.nextFloat();
			} else {
				break;
			}
		}
		/* Se llama al m�todo adquirirAnimal(...) de la clase Administracion, pues este m�todo se encarga de crear el objeto tipo Animal
		 * en base a los atributos que el usuario ingres�. */
		Administracion.adquirirAnimal(especieSeleccionada, habitatSeleccionado, genero, edad, peso);
		System.out.println("\nANIMAL ADQUIRIDO EXITOSAMENTE\n");
	}
}
