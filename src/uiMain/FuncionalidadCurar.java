package uiMain;

import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;

public class FuncionalidadCurar {

    static Animal animalSeleccionado;
	static Cuidador cuidadorSeleccionado;
	static Veterinario veterinarioSeleccionado;
	static Habitat habitatSeleccionado;
	static Habitat veterinaria = new Habitat(100, "veterinaria", "Ninguna", 10);

    static String leerString() {
		return Main.sc.nextLine();
	}

    static void curarAnimal() {
		seleccionarAnimal();
		seleccionarCuidador();
        seleccionarVeterinario();
        saludAnimal();
		seleccionarHabitat();
		Main.continuar();
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
				System.out.println(animal.info());
				animalSeleccionado = animal;
				return;
			}
		}
	}

    static void seleccionarVeterinario() {
		int id;
		System.out.println("\nAhora elija el veterinario que desee que revise al animal, ingresando su identificaci�n.\n");
		System.out.println("Identificaci�n; Nombre; Especie asignada");
		
		for(Veterinario veterinario : animalSeleccionado.getEspecie().getVeterinariosAsignados()) {
			System.out.println(String.valueOf(veterinario.getIdentificacion()) + "; " + veterinario.getNombre() + "; " + veterinario.getEspecialidad().getNombre());
		}
		
		System.out.print("\n�Cu�l veterinario elije? (Identificaci�n) ");
		id = Main.leerOpcion();
		
		for(Veterinario veterinario : FuncionalidadCurar.animalSeleccionado.getEspecie().getVeterinariosAsignados()) {
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
		System.out.println("\nElija el cuidador que desee que traslade al animal, ingresando su identificaci�n.\n");
		System.out.println("Identificaci�n; Nombre; Especie asignada");
		
		for(Cuidador cuidador : animalSeleccionado.getEspecie().getCuidadoresAsignados()) {
			System.out.println(String.valueOf(cuidador.getIdentificacion()) + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre());
		}
		
		System.out.print("\n�Cu�l cuidador elije? (Identificaci�n) ");
		id = Main.leerOpcion();
		
		for(Cuidador cuidador : FuncionalidadCurar.animalSeleccionado.getEspecie().getCuidadoresAsignados()) {
			if(cuidador.getIdentificacion() == id) { 
				System.out.println("\nCuidador seleccionado:\n");
				System.out.println(cuidador.info());
				cuidadorSeleccionado = cuidador;
				return;
			}
		}
	}

	static void seleccionarHabitat() {
		int id;
		System.out.println("Elija el habitat que desee regresar al animal, ingresando su identificaci�n.\n");
		System.out.println("Identificacion; Nombre; Ambientacion; Especie del Habitat; Capacidad");
		
		for(Habitat habitat: Administracion.getHabitats()) {
			System.out.println(habitat.getIdentificacion() + "; " + habitat.getNombre() + "; " + 
		    habitat.getAmbientacion() + "; " + habitat.getAnimalesAsociados().get(0).getEspecie().getNombre() + "; " 
		    + habitat.getCapacidadMaxima());
		}
		
		System.out.println("�Cu�l habitat elije? (Identificaci�n)");
		id = Main.leerOpcion();
		
		for(Habitat habitat: Administracion.getHabitats()) {
			if(id == habitat.getIdentificacion()) {
				System.out.println("\nH�bitat seleccionado:\n");
				System.out.println(habitat.info());
				habitatSeleccionado = habitat;
				return;
			}
		}
	}

    static void saludAnimal() {

		System.out.println("\nCuidador " + cuidadorSeleccionado.getNombre() + " procede a mover al animal con identificaci�n " + String.valueOf(animalSeleccionado.getIdentificacion()) + "a la veterinaria.");
		cuidadorSeleccionado.moverAnimal(animalSeleccionado, veterinaria);

		System.out.println("\nVeterinario " + veterinarioSeleccionado.getNombre() + " procede a revisar al animal con identificaci�n " + String.valueOf(animalSeleccionado.getIdentificacion()) + ".");
		
		if(veterinarioSeleccionado.revisar(animalSeleccionado)) {
			System.out.println("RESULTADO: El animal se encuentra con buen estado de salud.\n");
		} else {
			System.out.println("RESULTADO: El animal se encuentra con mal estado de salud.\n");
			System.out.println("El veterinario " + veterinarioSeleccionado.getNombre() + "decide hacer curaci�n al animal para mejorar su estado de salud.");
			veterinarioSeleccionado.curarAnimal(animalSeleccionado);
			if(animalSeleccionado.isAlimentado() && animalSeleccionado.isEstadoSalud() && animalSeleccionado.getHabitat().isLimpio()) {
				animalSeleccionado.setEstadoAnimo(true);
			}
			if(veterinarioSeleccionado.revisar(animalSeleccionado)) {
				System.out.println("Curar al animal ha dado buen resultado y este ahora se encuentra con buen estado de salud.");
			} else {
				System.out.println("Curar al animal no ha mejorado su estado de �nimo.");
				System.out.println("Puede solicitar que se haga mantenimineto a su h�bitat o que los alimenten.");
				System.out.println("El animal estar� en revisi�n preventiva.");
			}
		}
		return;
	}
    
}
