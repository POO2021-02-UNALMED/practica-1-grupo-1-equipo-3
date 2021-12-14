package uiMain;

import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;

public class FuncionalidadCuidar {
	static Animal animalSeleccionado;
	static Cuidador cuidadorSeleccionado;
	
	static String leerString() {
		return Main.sc.nextLine();
	}
	
	static void cuidarAnimal() {
		seleccionarAnimal();
		seleccionarCuidador();
		animoAnimal();
		System.out.print("Presione Enter para continuar...");
		Main.sc.nextLine();
	}
	
	static void seleccionarAnimal() {
		int id;
		System.out.println("Elija primero el animal que desee revisar, ingresando su identificación.\n");
		System.out.println("Identificación; Especie; Hábitat; Género; Edad; Peso");
		
		for(Animal animal : Administracion.getAnimales()) {
			System.out.println(String.valueOf(animal.getIdentificacion()) + "; " + animal.getEspecie().getNombre() + "; " + 
							   animal.getHabitat().getNombre() + "; " + animal.getGenero() + "; " + 
							   String.valueOf(animal.getEdad()) + "; " + String.valueOf(animal.getPeso()));
		}
		
		System.out.print("\n¿Cuál animal elije? (Identificación): ");
		id = Main.leerOpcion();
		
		for(Animal animal : Administracion.getAnimales()) {
			if(animal.getIdentificacion() == id) { 
				System.out.println("\nAnimal seleccionado:\n");
				System.out.println(animal.toString());
				animalSeleccionado = animal;
				break;
			}
		}
		return;
	}
	
	static void seleccionarCuidador() {
		int id;
		System.out.println("\nAhora elija el cuidador que desee que revise al animal, ingresando su identificación.\n");
		System.out.println("Identificación; Nombre; Especie asignada");
		
		for(Cuidador cuidador : animalSeleccionado.getEspecie().getCuidadorAsignado()) {
			System.out.println(String.valueOf(cuidador.getIdentificacion()) + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre());
		}
		
		System.out.print("\n¿Cuál cuidador elije? (Identificación) ");
		id = Main.leerOpcion();
		
		for(Cuidador cuidador : FuncionalidadCuidar.animalSeleccionado.getEspecie().getCuidadorAsignado()) {
			if(cuidador.getIdentificacion() == id) { 
				System.out.println("\nCuidador seleccionado:\n");
				System.out.println(cuidador.toString());
				cuidadorSeleccionado = cuidador;
				break;
			}
		}
		return;
	}
	
	static void animoAnimal() {
		System.out.println("\nCuidador " + cuidadorSeleccionado.getNombre() + " procede a revisar al animal con identificación " + 
							String.valueOf(animalSeleccionado.getIdentificacion()) + ".");
		
		if(cuidadorSeleccionado.revisar(animalSeleccionado)) {
			System.out.println("RESULTADO: El animal se encuentra con buen estado de ánimo.\n");
		} else {
			System.out.println("RESULTADO: El animal se encuentra con mal estado de ánimo.\n");
			System.out.println("El cuidador " + cuidadorSeleccionado.getNombre() + "decide alimentar al animal para mejorar su estado de ánimo.");
			cuidadorSeleccionado.alimentarAnimal(animalSeleccionado);
			if(animalSeleccionado.isAlimentado() && animalSeleccionado.isEstadoSalud() && animalSeleccionado.getHabitat().isLimpio()) {
				animalSeleccionado.setEstadoAnimo(true);
			}
			if(cuidadorSeleccionado.revisar(animalSeleccionado)) {
				System.out.println("Alimentar al animal ha dado buen resultado y este ahora se encuentra con buen estado de ánimo.");
			} else {
				System.out.println("Alimentar al animal no ha mejorado su estado de ánimo.");
				System.out.println("Puede solicitar que se haga mantenimineto a su hábitat o hacerlo revisar con un veterinario para mejorar su estado.");
			}
		}
		return;
	}
}
