//CLASE CREADA POR MATEO CARVAJAL

package uiMain;

import java.util.ArrayList;

import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.Cuidador;
import gestorAplicacion.gestionZoologico.Administracion;

public class FuncionalidadMantenimiento {

	static Habitat habitatSeleccionado;
	static Cuidador cuidadorSeleccionado;
	static Habitat jaula = new Habitat("Jaulas");
    
	//El metodo mantenimientoHabitat() es el metodo a llamar desde la clase Main. Desde este metodo es donde se controla la ejecucion de esta funcionalidad.
	static void mantenimientoHabitat() {
		// Por medio de la variable "habitatsDisponibles" se verificara que por lo menos haya un habitat dsiponible para revisar.
		boolean habitatsDisponibles = seleccionarHabitat(); 
		//En caso de que no haya se cancelara el mantenimiento.
		if(habitatsDisponibles) { 
			//Por medio de la variable "cuidadoresDisponibles" se verificara que haya por lo menos un cuidador pueda revisar el habitat
			boolean cuidadoresDisponibles = seleccionarCuidador(); //Por medio de la variable "cuidadoresDisponibles" se verificara que haya por lo menos un cuidador pueda revisar el habitat.
			//En caso de que no haya cuidadores se cancela el mantenimiento.
			if(cuidadoresDisponibles) limpiezaHabitat(); 	
		}
		System.out.println();
		/* El método continuar() de la clase Main es usado para que el usuario tenga tiempo de leer las salidas proporcionadas por la funcionalidad
		 * Este método evita que se repita inmediatamente el ciclo de elegir la funcionalidad a realizar, esto por medio de esperar la acción del usuario */
		Main.continuar();
	}

	//Con el metodo seleccionarHabitat() se selecciona el habita que se quiera revisar.
	static boolean seleccionarHabitat() {
		int id;
		int habitats = 0; //Con la variable habitats se contara si hay por lo menos un habitat que se pueda revisar 
		ArrayList<Integer> idHabitats = new ArrayList<Integer>(); // En la variable "HabitatsId" se almacenan los id de los habitat que puedan ser elegidos por el usuario.
		
		System.out.println("Elija primero el habitat que desee revisar, ingresando su identificación.\n");
		System.out.println("Identificacion; Nombre; Ambientacion; Especie del Habitat; Cantidad Animales; Capacidad Maxima");
		
		//Con el siguiente for se imprime la informacion de los Habitats que se puedan elegir y que son almacenados en el listado de habitats de administracion.
		for(Habitat habitat: Administracion.getHabitats()) {
			if(habitat.getAnimalesAsociados().size() != 0) { // En caso de que el habitat no tenga animales asociados este no se va a mostrar por pantalla.
				System.out.println(habitat.getIdentificacion() + "; " + habitat.getNombre() + "; " + 
					    habitat.getAmbientacion() + "; " + habitat.getAnimalesAsociados().get(0).getEspecie().getNombre() + "; " 
					    + habitat.cantidadAnimales() + "; " + habitat.getCapacidadMaxima());
				habitats++; //Se suma al numero de habitats que se puedan elegir.
				idHabitats.add(habitat.getIdentificacion()); //Se añade la identificacion del habitat elegible.
			}
			
		}
		
		if(habitats == 0) { // En caso de que no haya Habitats se cancela el mantenimiento.
			System.out.println("\nNo se ha encontrado ningún hábitat para revisar.");
			System.out.println("MANTENIMIENTO CANCELADO\n");
			return false; // Se retorna false para la verificacion del metodo mantenimientoHabitat()
		} else {
			
			System.out.print("\n¿Cuál hábitat elije? (Identificacion) "); // Si hay por lo menos un habitat que se pueda elegir se le socilitara al usuario elegir uno a partir de la identificacion de este.
			id = Main.leerOpcion();
			
			
			while(idHabitats.contains(id) == false) { // Ciclo while que le pedira al usuario que elige una identificacion correcta en caso que de que este escoja una erronea.
				System.out.println("IDENTIFICACION INCORRECTA: Ingrese una valida");
				System.out.print("\nPor favor seleccione un hábitat: ");
				id = Main.leerOpcion(); // Se le pide al usuario que elija otra identificacion.
			}
			//En el siguiento for se recorre de nuevo la lista de todos los habitats.
			for(Habitat habitat: Administracion.getHabitats()) {
				if(id == habitat.getIdentificacion()) { // En este if se encuentra el habitat con el mismo # de identificacion al que escogio el usuario.
					System.out.println("\nHábitat seleccionado:\n");
					System.out.println(habitat.info());	//Se imprime la informacion del habitat.
					habitatSeleccionado = habitat; // Se asigna el habitat escogido al atributo estatico habitatSeleccionado para usos futuros. 
					break;
				}
			}
			return true; //Se retorna true para la verificacion de mantenimientoHabitat()
		}
	}
	
	//Con el metodo seleccionarCuidador() se selecciona el cuidador que revisara el habitat. Similarmente al metodo seleccionarHabitat()
	static boolean seleccionarCuidador() {
		int id;
		int cuidadores = 0; // Variable "cuidadores" que nos indicara si hay por lo menos un cuidador que el usuario pueda elegir
		ArrayList<Integer> idCuidadores = new ArrayList<Integer>(); // Varible "idCuidadores" que almacena las identificaciones de los cuidadores que el usuario puede elegir.
		
		System.out.println("\nAhora elija el cuidador que desee que revise el hábitat, ingresando su identificación.\n");
		System.out.println("Identificación; Nombre; Especie Asignada");

		//Con el siguiente for se imprime la informacion de los cuidadores que pueden escoger el usario.
		for (Cuidador cuidador : Administracion.getCuidadores()) {
			if (cuidador.getEspecieAsignada().getNombre().equals(habitatSeleccionado.getAnimalesAsociados().get(0).getEspecie().getNombre())) {
			System.out.println(cuidador.getIdentificacion() + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre());
			cuidadores++; // Se cuentan los cuidadores que se esten listando.
			idCuidadores.add(cuidador.getIdentificacion()); // Se agreagan las identificaciones de los cuidadores que se esten listando.
		}}
		
		if(cuidadores == 0) { // En caso de que no haya cuidadores se le informara al usuario que se cancela el mantenimiento.
			System.out.println("\nNo se ha encontrado ningún cuidador para que revise el hábitat.");
			System.out.println("MANTENIMIENTO CANCELADO\n");
			return false; // Se retorna false para la verificacion del metodo mantenimientoHabitat().
		} else {
			System.out.print("\n¿Cuál cuidador elige? (Identificación) "); // Si hay por lo menos un cuidador que se pueda elegir se le socilitara al usuario elegir uno a partir de la identificacion de este.
			id = Main.leerOpcion();
			
			while(idCuidadores.contains(id) == false) { // Ciclo while que le pedira al usuario que elige una identificacion correcta en caso que de que este escoja una erronea. 
				System.out.println("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida."); 
				System.out.print("\n¿Cuál cuidador elije? (Identificación) ");
				id = Main.leerOpcion(); // Se le pide al usuario que elija otra identificacion.
				} 
	
			// En el siguient for se recorre de nuevo el listado de todos los cuidadores.
			for (Cuidador cuidador : Administracion.getCuidadores()) {
				if (cuidador.getIdentificacion() == id) { // Con este if se encuentra al cuidador que tenga el mismo # de identificacion al que escogio el usuario. 
					System.out.println("Cuidador seleccionado: \n");
					System.out.println(cuidador.info()); // Se imprime la informacion de los cuidadores.
					cuidadorSeleccionado = cuidador; //Se asigna al atributo
					break;
				}
			}
			return true; //Se retorna true para la verificacion de mantenimientoHabitat().
		}
	}
    
	//Con el metodo limpiezaHabitat() se hace el proceso de revisar el habitat y en caso de que sea necesario hacer le mantenimiento
	static void limpiezaHabitat() {
		ArrayList<Integer> idAnimalesTristes = new ArrayList<Integer>(); //Variable "idAnimalesTristes" que almacena las identificaciones de animales cuyos estados de animo no hayan mejorado despues de hacer el mantenimento al habitat.

		System.out.println("\nCuidador " + cuidadorSeleccionado.getNombre()
				+ " procede a revisar el habitat con identficacion " + habitatSeleccionado.getIdentificacion() + ".");

		if (cuidadorSeleccionado.revisar(habitatSeleccionado)) { // En caso de que el habitat este en buen estado (metodo revisarEstado() retorna true), se le informara al usuario y se termina la funcionalidad.
			System.out.println("RESULTADO: El habitat se encuentra en buen estado.\n");
		}

		else {
			System.out.println("El cuidador " + cuidadorSeleccionado.getNombre()
					+ " decide sacar a todos los animales para hacer mantenimiento al habitat");
			cuidadorSeleccionado.limpiarHabitat(habitatSeleccionado, jaula); /* Metodo limpiarHabitat(habitatSeleccionado, jaula) que saca a todos los animales del habitat para meterlos en otro vacio(jaula), 
			                                                                    cambia el atributo limpio del habitatSeleccionado mediante el metodo setLimpio(bool) a true y luego devuelve a todos los animales
			                                                                    al habitat original. Al devolver a cada animal se le revisa si el estado de animo y de salud de este son true y si este es el caso, 
			                                                                    se le pone el estado de animo a true mediante el metodo setEstadoAnimo(true)   (Para mas especificaciones ver la clase Cuidador)*/ 

			
			for (Animal animal : habitatSeleccionado.getAnimalesAsociados()) { /* Se recorre la animales dentro del habitat buscando a aquellos cuyo estado de animo no haya mejorado despues del mantenimiento.
			                                                                       Esto con el fin de notificarle al usuario que todavia hay animales con el estado de animo malo*/
				                                                               
				if (animal.isEstadoAnimo() == false) {
					if (idAnimalesTristes.contains(animal.getIdentificacion())==false){
					idAnimalesTristes.add(animal.getIdentificacion()); //Se añaden las identificaciones de los animales con estado de animo malo a la lista idAnimalesTristes.
				}}
			}

			if (idAnimalesTristes.size() == 0) { //En caso que no haya ningun animal con estado de animo malo, se le notifica al usuario que el mantenimiento ha sido todo un exito y se termina la funcionalidad.
				System.out.println("Hacerle mantenimiento al habitat ha dado buenos resultados, no hay animales tristes en este.");
			} else { // En caso de que haya animales con estado de animo malo se le notificara al usuario.
				System.out.println("Los animales con los siguientes números de identificacion no han mejorado sus estados de ánimo: ");
				for (int id : idAnimalesTristes) { // En este for se imprime las identificaciones de todos los animales con estado de animo malo.
					System.out.println(id);
				}
				System.out.println("Puede solicitar alimentarlos o que los revise un veterinario"); // Se le recomienda al usuario que puede usar las otras funcionalidades de cuidar o curacion para asi mejorar el estado de animo de los animales. 
			}
		}
		return;
	}
}
