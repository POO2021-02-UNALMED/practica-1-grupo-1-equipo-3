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
	static Habitat veterinaria;

    static String leerString() {
		return Main.sc.nextLine();
	}

    static void curarAnimal() {
		seleccionarAnimal();
		seleccionarCuidador();
        seleccionarVeterinario();
        saludAnimal();
		Main.continuar();
	}
	// A traves del metodo seleccionarAnimal() se obtiene el animal que sera revisado.
    static void seleccionarAnimal() {
		int id;
		System.out.println("Elija primero el animal que desee revisar, ingresando su identificacion.\n");
		System.out.println("Identificacion; Especie; Habitat; Genero; Edad; Peso");
		
		for(Animal animal : Administracion.getAnimales()) {
			System.out.println(String.valueOf(animal.getIdentificacion()) + "; " + animal.getEspecie().getNombre() + "; " + 
							   animal.getHabitat().getNombre() + "; " + animal.getGenero() + "; " + 
							   String.valueOf(animal.getEdad()) + "; " + String.valueOf(animal.getPeso()));
		}
		
		System.out.print("\n¿Cual animal elije? (Identificacion): ");
		id = Main.leerOpcion();
		
		for(Animal animal : Administracion.getAnimales()) {
			if(animal.getIdentificacion() == id) { 
				System.out.println("\nAnimal seleccionado:\n");
				System.out.println(animal.info());
				animalSeleccionado = animal;
				return;
			}
		}
	}

    static void seleccionarVeterinario() {
		int id;
		System.out.println("\nAhora elija el veterinario que desee que revise al animal, ingresando su identificacion.\n");
		System.out.println("Identificacion; Nombre; Especie asignada");
		
		for(Veterinario veterinario : Administracion.getVeterinarios()) {
			System.out.println(String.valueOf(veterinario.getIdentificacion()) + "; " + veterinario.getNombre() + "; " + veterinario.getEspecialidad().getNombre());
		}
		
		System.out.print("\n¿Cual veterinario elije? (Identificacion) ");
		id = Main.leerOpcion();
		
		for(Veterinario veterinario : Administracion.getVeterinarios()) {
			if(veterinario.getIdentificacion() == id) { 
				System.out.println("\nVeterinario seleccionado:\n");
				System.out.println(veterinario.info());
				veterinarioSeleccionado = veterinario;
				return;
			}
		}
	}

	static void seleccionarCuidador() {
		int id;
		System.out.println("\nElija el cuidador que desee que traslade al animal, ingresando su identificacion.\n");
		System.out.println("Identificacion; Nombre; Especie asignada");
		
		for(Cuidador cuidador : Administracion.getCuidadores()) {
			System.out.println(String.valueOf(cuidador.getIdentificacion()) + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre());
		}
		
		System.out.print("\n¿Cual cuidador elije? (Identificacion) ");
		id = Main.leerOpcion();
		
		for(Cuidador cuidador : Administracion.getCuidadores()) {
			if(cuidador.getIdentificacion() == id) { 
				System.out.println("\nCuidador seleccionado:\n");
				System.out.println(cuidador.info());
				cuidadorSeleccionado = cuidador;
				return;
			}
		}
	}


    static void saludAnimal() {

		Habitat habitad = animalSeleccionado.getHabitat();

		System.out.println("\nCuidador " + cuidadorSeleccionado.getNombre() + " procede a mover al animal con identificacion " + String.valueOf(animalSeleccionado.getIdentificacion()) + "a la veterinaria.");
		cuidadorSeleccionado.moverAnimal(animalSeleccionado, veterinaria);

		System.out.println("\nVeterinario " + veterinarioSeleccionado.getNombre() + " procede a revisar al animal con identificacion " + String.valueOf(animalSeleccionado.getIdentificacion()) + ".");
		
		if(veterinarioSeleccionado.revisar(animalSeleccionado)) {
			System.out.println("RESULTADO: El animal se encuentra con buen estado de salud.\n");
			cuidadorSeleccionado.moverAnimal(animalSeleccionado, habitad);
		} else {
			System.out.println("RESULTADO: El animal se encuentra con mal estado de salud.\n");
			System.out.println("El veterinario " + veterinarioSeleccionado.getNombre() + "decide hacer curacion al animal para mejorar su estado de salud.");
			veterinarioSeleccionado.curarAnimal(animalSeleccionado);
			if(animalSeleccionado.isAlimentado() && animalSeleccionado.isEstadoSalud() && animalSeleccionado.getHabitat().isLimpio()) {
				animalSeleccionado.setEstadoAnimo(true);
				cuidadorSeleccionado.moverAnimal(animalSeleccionado, habitad);
			}
			if(veterinarioSeleccionado.revisar(animalSeleccionado)) {
				System.out.println("Curar al animal ha dado buen resultado y este ahora se encuentra con buen estado de salud.");
				cuidadorSeleccionado.moverAnimal(animalSeleccionado, habitad);
			} else {
				System.out.println("Curar al animal no ha mejorado su estado de animo.");
				System.out.println("Puede solicitar que se haga mantenimineto a su habitat o que los alimenten.");
				System.out.println("El animal estara en revision preventiva.");
			}
		}
		return;
	}
    
}
