package uiMain;

import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;

public class FuncionalidadAdquisicionTraslado {
	static Especie especieSeleccionada;
	static Habitat habitatSeleccionado;
	static Animal animalSeleccionado;
	
	static String leerString() {
		return Main.sc.nextLine();
	}
	
	static void adquisicionTraslado() {
		int opcion;
		System.out.println("Primero elija qué desea hacer:\n");
		System.out.println("1. Adquirir animales");
		System.out.println("2. Trasladar animales");
		System.out.print("\n¿Cuál opción quiere realizar? ");
		opcion = Main.leerOpcion();
		System.out.println();
		switch(opcion) {
			case 1: {
				seleccionarEspecie("adquirir");
				boolean habitatsDisponibles = seleccionarHabitat();
				if(habitatsDisponibles) ingresarAnimal();
				break;
			}
			case 2: {
				seleccionarEspecie("trasladar");
				boolean animalesDisponibles = seleccionarAnimal();
				if(animalesDisponibles) {
					Administracion.trasladarAnimal(animalSeleccionado);
					System.out.println("\nANIMAL TRASLADADO EXITOSAMENTE\n");
				}
				break;
			}
			default: System.out.println("Opción incorrecta. Solo opciones 1 y 2."); break;
		}
		Main.continuar();
		return;
	}
	
	static void seleccionarEspecie(String accion) {
		int num = 1;
		int opcion;
		System.out.println("Elija primero la especie del animal que desea " + accion + ", eligiendo la opción correspondiente:\n");
		
		for(Especie especie : Administracion.getEspecies()) {
			System.out.println(String.valueOf(num) + ". " + especie.getNombre());
			num++;
		}
		
		System.out.print("\n¿Cuál opción de especie elije? ");
		opcion = Main.leerOpcion();
		
		System.out.println("\nEspecie seleccionada:\n");
		especieSeleccionada = Administracion.getEspecies().get(opcion-1);
		System.out.println("Nombre: " + especieSeleccionada.getNombre() +
							"\nDieta: " + especieSeleccionada.getDieta() +
							"\nPromedio de vida: " + String.valueOf(especieSeleccionada.getPromedioVida()));
		return;
	}
	
	static boolean seleccionarHabitat() {
		int id;
		int habitats = 0;
		System.out.println("\nAhora elija el hábitat donde el animal que desea adquirir será depositado, ingresando su identificación:");
		System.out.println("(Los hábitats listados corresponden únicamente a hábitats donde la especie de dicho animal puede ser depositada)\n");
		System.out.println("Identificación; Nombre; Ambientación; Capacidad actual; Capacidad máxima");
		
		for(Habitat habitat : Administracion.getHabitats()) {
			for(Animal animal : habitat.getAnimalesAsociados()) {
				if(animal.getEspecie() == especieSeleccionada && habitat.cantidadAnimales() < habitat.getCapacidadMaxima()) {
					System.out.println(String.valueOf(habitat.getIdentificacion()) + "; " + habitat.getNombre() + "; " + 
							   habitat.getAmbientacion() + "; " + String.valueOf(habitat.cantidadAnimales()) + "; " +
							   String.valueOf(habitat.getCapacidadMaxima()));
					habitats++;
					break;
				}
			}
		}
		
		if(habitats == 0) {
			System.out.println("\nNo se ha encontrado ningún hábitat disponible para depositar al animal.");
			System.out.println("ADQUISICIÓN CANCELADA\n");
			return false;
		} else {
			System.out.print("\n¿Cuál hábitat elije? (Identificación): ");
			id = Main.leerOpcion();
			
			for(Habitat habitat : Administracion.getHabitats()) {
				if(habitat.getIdentificacion() == id) { 
					System.out.println("\nHábitat seleccionado:\n");
					System.out.println("Identificación: " + String.valueOf(habitat.getIdentificacion()) +
										"\nNombre: " + habitat.getNombre() +
										"\nAmbientación: " + habitat.getAmbientacion() +
										"\nCapacidad actual / Capacidad máxima: " + String.valueOf(habitat.cantidadAnimales()) +
										" / " + String.valueOf(habitat.getCapacidadMaxima()));
					habitatSeleccionado = habitat;
					break;
				}
			}
			return true;
		}
	}
	
	static boolean seleccionarAnimal() {
		int id;
		int animales = 0;
		System.out.println("\nAhora elija el animal que desee trasladar, ingresando su identificación.\n");
		System.out.println("Identificación; Especie; Hábitat; Género; Edad; Peso");
		
		for(Animal animal : Administracion.getAnimales()) {
			if(animal.getEspecie() == especieSeleccionada) {
				System.out.println(String.valueOf(animal.getIdentificacion()) + "; " + animal.getEspecie().getNombre() + "; " + 
						   animal.getHabitat().getNombre() + "; " + animal.getGenero() + "; " + 
						   String.valueOf(animal.getEdad()) + "; " + String.valueOf(animal.getPeso()));
				animales++;
			}
		}
		
		if(animales == 0) {
			System.out.println("\nNo se ha encontrado ningún animal de la especie solicitada para trasladar.");
			System.out.println("TRASLADO CANCELADO\n");
			return false;
		} else {
		
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
			return true;
		}
	}
	
	static void ingresarAnimal() {
		System.out.println("\nPor último, ingrese los datos del animal que se va a adquirir:\n");
		System.out.print("Identificación (Número): ");
		int identificacion=Main.sc.nextInt();
		System.out.print("Género (M o H): ");
		String genero=Main.sc.next();
		System.out.print("Edad (Número): ");
		int edad=Main.sc.nextInt();
		System.out.print("Peso (Número): ");
		float peso=Main.sc.nextFloat();
		Administracion.adquirirAnimal(identificacion, especieSeleccionada, habitatSeleccionado, genero, edad, peso);
		System.out.println("\nANIMAL ADQUIRIDO EXITOSAMENTE\n");
	}
}
