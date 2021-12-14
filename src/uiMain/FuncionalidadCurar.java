package uiMain;

import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;

public class FuncionalidadCurar {

    static Animal animalSeleccionado;
	static Veterinario veterinarioSeleccionado;

    static String leerString() {
		return Main.sc.nextLine();
	}

    static void curarAnimal() {
		seleccionarAnimal();
        seleccionarVeterinario();
        saludAnimal();
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
				return;
			}
		}
	}

    static void seleccionarVeterinario() {
		int id;
		System.out.println("\nAhora elija el veterinario que desee que revise al animal, ingresando su identificaci�n.\n");
		System.out.println("Identificaci�n; Nombre; Especie asignada");
		
		for(Veterinario veterinario : animalSeleccionado.getEspecie().getVeterinarioAsignado()) {
			System.out.println(String.valueOf(veterinario.getIdentificacion()) + "; " + veterinario.getNombre() + "; " + veterinario.getEspecialidad().getNombre());
		}
		
		System.out.print("\n�Cu�l veterinario elije? (Identificaci�n) ");
		id = Main.leerOpcion();
		
		for(Veterinario veterinario : FuncionalidadCurar.animalSeleccionado.getEspecie().getVeterinarioAsignado()) {
			if(veterinario.getIdentificacion() == id) { 
				System.out.println("\nVeterinario seleccionado:\n");
				System.out.println(veterinario.toString());
				veterinarioSeleccionado = veterinario;
				return;
			}
		}
	}

    static void saludAnimal() {
		System.out.println("\nVeterinario " + veterinarioSeleccionado.getNombre() + " procede a revisar al animal con identificaci�n " + String.valueOf(animalSeleccionado.getIdentificacion()) + ".");
		
		if(veterinarioSeleccionado.revisarAnimal(animalSeleccionado)) {
			System.out.println("RESULTADO: El animal se encuentra con buen estado de salud.\n");
		} else {
			System.out.println("RESULTADO: El animal se encuentra con mal estado de salud.\n");
			System.out.println("El veterinario " + veterinarioSeleccionado.getNombre() + "decide hacer curaci�n al animal para mejorar su estado de salud.");
			veterinarioSeleccionado.curarAnimal(animalSeleccionado);
			if(animalSeleccionado.isAlimentado() && animalSeleccionado.isEstadoSalud() && animalSeleccionado.getHabitat().isLimpio()) {
				animalSeleccionado.setEstadoAnimo(true);
			}
			if(veterinarioSeleccionado.revisarAnimal(animalSeleccionado)) {
				System.out.println("Curar al animal ha dado buen resultado y este ahora se encuentra con buen estado de salud.");
			} else {
				System.out.println("Curar al animal no ha mejorado su estado de �nimo.");
				System.out.println("Puede solicitar que se haga mantenimineto a su h�bitat o que los alimenten.");
			}
		}
		return;
	}
    
}
