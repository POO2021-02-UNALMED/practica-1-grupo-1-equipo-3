// CLASE CREADA POR Juan Jose Monsalve Marin

/*
 En esta clase realiza la funcionalidad de curar de los animales 
 Primero se debe de identificar el cuidador que moverá a los animales, el animal que será trasladado a la 
 veterinaria y el veterinario tratante que atenderá al animal. Todo esto se hace después de que un cuidador 
 allá revisando el animal y se percatara de que el estado de animo del animal no cambio después de alimentarlo. 
 esto ultimo se realiza en la clase "FuncionalidadCuidar"

 Son necesarias las clases animal, veterinario y cuidador.  
*/

package uiMain;

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
    
 // A traves del metodo seleccionarAnimal() se obtiene el animal que sera revisado.
    static void curarAnimal() {
		boolean animalesDisponibles = seleccionarAnimal();
		if(animalesDisponibles) {
			boolean cuidadoresDisponible = seleccionarCuidador();
			if(cuidadoresDisponible) {
				boolean veterinariosDisponibles = seleccionarVeterinario();
				if(veterinariosDisponibles) {
					saludAnimal();
				}
			}
		}
		Main.continuar();
	}

    static boolean seleccionarAnimal() {
		int id;
		int animales = 0;
		System.out.println("Elija primero el animal que desee revisar, ingresando su identificación.\n");
		System.out.println("Identificación; Especie; Hábitat; Género; Edad; Peso");
		
		for(Animal animal : Administracion.getAnimales()) {
			System.out.println(String.valueOf(animal.getIdentificacion()) + "; " + animal.getEspecie().getNombre() + "; " + 
							   animal.getHabitat().getNombre() + "; " + animal.getGenero() + "; " + 
							   String.valueOf(animal.getEdad()) + "; " + String.valueOf(animal.getPeso()));
			animales++;
		}
		
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
			
			for(Animal animal : Administracion.getAnimales()) {
				if(animal.getIdentificacion() == id) { 
					System.out.println("\nAnimal seleccionado:\n");
					System.out.println(animal.info());
					animalSeleccionado = animal;
					habitatSeleccionado = animal.getHabitat();
					break;
				}
			}
			return true;
		}
	}

    static boolean seleccionarVeterinario() {
		int id;
		int veterinarios = 0;
		System.out.println("\nAhora elija el veterinario que desee que revise al animal, ingresando su identificación.\n");
		System.out.println("Identificación; Nombre; Especie asignada");
		
		for(Veterinario veterinario : Administracion.getVeterinarios()) {
			if(veterinario.getEspecialidad() == animalSeleccionado.getEspecie()) {
				System.out.println(String.valueOf(veterinario.getIdentificacion()) + "; " + veterinario.getNombre() + "; " + veterinario.getEspecialidad().getNombre());
				veterinarios++;
			}
		}
		
		if(veterinarios == 0) {
			System.out.println("\nNo se ha encontrado ningún veterinario para revisar al animal.");
			System.out.println("REVISIÓN CANCELADA\n");
			return false;
		} else {
			System.out.print("\n¿Cuál veterinario elije? (Identificación) ");
			id = Main.leerOpcion();
			
			for(Veterinario veterinario : Administracion.getVeterinarios()) {
				if(veterinario.getIdentificacion() == id) { 
					System.out.println("\nVeterinario seleccionado:\n");
					System.out.println(veterinario.info());
					veterinarioSeleccionado = veterinario;
					break;
				}
			}
			return true;
		}
	}

	static boolean seleccionarCuidador() {
		int id;
		int cuidadores = 0;
		System.out.println("\nElija el cuidador que desee que traslade al animal, ingresando su identificación.\n");
		System.out.println("Identificación; Nombre; Especie asignada");
		
		for(Cuidador cuidador : Administracion.getCuidadores()) {
			if(cuidador.getEspecieAsignada() == animalSeleccionado.getEspecie()) {
				System.out.println(String.valueOf(cuidador.getIdentificacion()) + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre());
				cuidadores++;
			}
		}
		
		if(cuidadores == 0) {
			System.out.println("\nNo se ha encontrado ningún cuidador para trasladar al animal.");
			System.out.println("REVISIÓN CANCELADA\n");
			return false;
		} else {
			System.out.print("\n¿Cuál cuidador elije? (Identificación) ");
			id = Main.leerOpcion();
			
			for(Cuidador cuidador : Administracion.getCuidadores()) {
				if(cuidador.getIdentificacion() == id) { 
					System.out.println("\nCuidador seleccionado:\n");
					System.out.println(cuidador.info());
					cuidadorSeleccionado = cuidador;
					break;
				}
			}
			return true;
		}
	}

    static void saludAnimal() {
		System.out.println("\nCuidador " + cuidadorSeleccionado.getNombre() + " procede a mover al animal con identificación " + String.valueOf(animalSeleccionado.getIdentificacion()) + " a la veterinaria.");
		cuidadorSeleccionado.moverAnimal(animalSeleccionado, veterinaria);
		System.out.println("Veterinario " + veterinarioSeleccionado.getNombre() + " procede a revisar al animal con identificación " + String.valueOf(animalSeleccionado.getIdentificacion()) + ".");
		
		if(veterinarioSeleccionado.revisar(animalSeleccionado)) {
			System.out.println("RESULTADO: El animal se encuentra con buen estado de salud.\n");
			System.out.println("Cuidador " + cuidadorSeleccionado.getNombre() + " procede a mover al animal con identificación " + 
								String.valueOf(animalSeleccionado.getIdentificacion()) + " de regreso a su hábitat.");
			cuidadorSeleccionado.moverAnimal(animalSeleccionado, habitatSeleccionado);
		} else {
			System.out.println("RESULTADO: El animal se encuentra con mal estado de salud.\n");
			System.out.println("El veterinario " + veterinarioSeleccionado.getNombre() + "decide hacer curación al animal para mejorar su estado de salud.");
			veterinarioSeleccionado.curarAnimal(animalSeleccionado);
			if(animalSeleccionado.isAlimentado() && animalSeleccionado.isEstadoSalud() && animalSeleccionado.getHabitat().isLimpio()) {
				animalSeleccionado.setEstadoAnimo(true);
			}
			if(veterinarioSeleccionado.revisar(animalSeleccionado)) {
				System.out.println("Curar al animal ha dado buen resultado y este ahora se encuentra con buen estado de salud.");
				System.out.println("\nCuidador " + cuidadorSeleccionado.getNombre() + " procede a mover al animal con identificación " + 
						String.valueOf(animalSeleccionado.getIdentificacion()) + " de regreso a su hábitat.");
				cuidadorSeleccionado.moverAnimal(animalSeleccionado, habitatSeleccionado);
			} else {
				System.out.println("Curar al animal no ha mejorado su estado de ánimo.");
				System.out.println("Puede solicitar que se haga mantenimineto a su hábitat o que los alimenten.");
				System.out.println("El animal estará en revisión preventiva.");
			}
		}
		System.out.println("REVISIÓN FINALIZADA\n");
		return;
	}
    
}
