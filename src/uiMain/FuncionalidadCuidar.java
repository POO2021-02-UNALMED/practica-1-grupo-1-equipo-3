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
		System.out.println("Elija primero el animal que desee revisar, ingresando su identificaci�n.\n");
		System.out.println("Identificaci�n; Especie; H�bitat; G�nero; Edad; Peso");
		
		for(Animal animal : Administracion.getAnimales()) {
			System.out.println(String.valueOf(animal.getIdentificacion()) + "; " + animal.getEspecie().getNombre() + "; " + 
							   animal.getHabitat().getNombre() + "; " + animal.getGenero() + "; " + 
							   String.valueOf(animal.getEdad()) + "; " + String.valueOf(animal.getPeso()));
		}
		
		System.out.print("\n�Cu�l animal elije? (Identificaci�n): ");
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
		System.out.println("\nAhora elija el cuidador que desee que revise al animal, ingresando su identificaci�n.\n");
		System.out.println("Identificaci�n; Nombre; Especie asignada");
		
		for(Cuidador cuidador : animalSeleccionado.getEspecie().getCuidadorAsignado()) {
			System.out.println(String.valueOf(cuidador.getIdentificacion()) + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre());
		}
		
		System.out.print("\n�Cu�l cuidador elije? (Identificaci�n) ");
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
		System.out.println("\nCuidador " + cuidadorSeleccionado.getNombre() + " procede a revisar al animal con identificaci�n " + 
							String.valueOf(animalSeleccionado.getIdentificacion()) + ".");
		
		if(cuidadorSeleccionado.revisar(animalSeleccionado)) {
			System.out.println("RESULTADO: El animal se encuentra con buen estado de �nimo.\n");
		} else {
			System.out.println("RESULTADO: El animal se encuentra con mal estado de �nimo.\n");
			System.out.println("El cuidador " + cuidadorSeleccionado.getNombre() + "decide alimentar al animal para mejorar su estado de �nimo.");
			cuidadorSeleccionado.alimentarAnimal(animalSeleccionado);
			if(animalSeleccionado.isAlimentado() && animalSeleccionado.isEstadoSalud() && animalSeleccionado.getHabitat().isLimpio()) {
				animalSeleccionado.setEstadoAnimo(true);
			}
			if(cuidadorSeleccionado.revisar(animalSeleccionado)) {
				System.out.println("Alimentar al animal ha dado buen resultado y este ahora se encuentra con buen estado de �nimo.");
			} else {
				System.out.println("Alimentar al animal no ha mejorado su estado de �nimo.");
				System.out.println("Puede solicitar que se haga mantenimineto a su h�bitat o hacerlo revisar con un veterinario para mejorar su estado.");
			}
		}
		return;
	}
}
