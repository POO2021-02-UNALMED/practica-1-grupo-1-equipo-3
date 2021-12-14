package uiMain;
import java.util.ArrayList;

import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.Cuidador;
import gestorAplicacion.gestionZoologico.Administracion;

public class FuncionalidadMantenimiento {
	
	static Habitat habitatSeleccionado;
	static Cuidador cuidadorSeleccionado;
	static Habitat jaula = new Habitat(0, "Jaula", "Ninguna", 75);
	
	
	
	static void mantenimientoHabitat() {
		seleccionarHabitat();
		seleccionarCuidador();
		limpiezaHabitat();
		Main.continuar();
	}
	
	static void seleccionarHabitat() {
		int id;
		System.out.println("Elija primero el habitat que desee revisar, ingresando su identificación.\n");
		System.out.println("Identificacion; Nombre; Ambientacion; Especie del Habitat; Capacidad");
		
		for(Habitat habitat: Administracion.getHabitats()) {
			System.out.println(habitat.getIdentificacion() + "; " + habitat.getNombre() + "; " + 
		    habitat.getAmbientacion() + "; " + habitat.getAnimalesAsociados().get(0).getEspecie().getNombre() + "; " 
		    + habitat.getCapacidadMaxima());
		}
		
		System.out.println("Cuál habitat elije(Identificacion)");
		id = Main.leerOpcion();
		
		for(Habitat habitat: Administracion.getHabitats()) {
			if(id == habitat.getIdentificacion()) {
				System.out.println("\nHabitat seleccionado:\n");
				System.out.println(habitat.toString());
				habitatSeleccionado = habitat;
				return;
			}
		}
	}
	
	static void seleccionarCuidador() {
		int id;
		System.out.println("Ahora elija el cuidador que desee que revise el habitat, ingresando su identificación.\n");
		System.out.println("Identificación; Nombre; Especie Asginada");
		
		for(Cuidador cuidador: habitatSeleccionado.getAnimalesAsociados().get(0).getEspecie().getCuidadorAsignado() ) {
			System.out.println(cuidador.getIdentificacion() + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre());
		}
		
		System.out.println("¿Cuál cuidador elige? (Identficación) ");
		id = Main.leerOpcion();
		
		for(Cuidador cuidador : habitatSeleccionado.getAnimalesAsociados().get(0).getEspecie().getCuidadorAsignado()) {
			if(cuidador.getIdentificacion() == id) {
				System.out.println("Cuidador seleccionado: \n");
				System.out.println(cuidador.toString());
				cuidadorSeleccionado = cuidador;
				return;
				
			}
		}
		
	}
	
	static void limpiezaHabitat() {
		ArrayList<Integer> idAnimalesTristes = new ArrayList<Integer>();
		
		System.out.println("Cuidador " + cuidadorSeleccionado.getNombre() + "procede a revisar el habitat con identficacion: " + habitatSeleccionado.getIdentificacion() 
		+ ".");
		
		if(cuidadorSeleccionado.revisar(habitatSeleccionado)) {
			System.out.println("RESULTADO: El habitat se encuentra en buen estado.");
		}
		
		else {
			System.out.println("El cuidador " + cuidadorSeleccionado.getNombre() + "decide sacar a todos los animales para hacerle mantenimiento al habitat");
			cuidadorSeleccionado.limpiarHabitat(habitatSeleccionado, jaula);
		
		for(Animal animal : habitatSeleccionado.getAnimalesAsociados()) {
			if(animal.isEstadoAnimo() == false) {
				idAnimalesTristes.add(animal.getIdentificacion());
			}
		}
		
		if(idAnimalesTristes.size() == 0) {
			System.out.println("Hacerle mantenimiento al habitat ha dado buenos resultados, no hay animales tristes en este.");
		}else {
			System.out.println("Los animales con los siguientes números de identificacion no han mejorado sus estados de ánimo: ");
			for(int id : idAnimalesTristes) {
				System.out.println(id);
			}
			System.out.println("Puede solicitar alimentarlos o que los revise el veterinario");
		}
			
		}
		return;
	}
	
	

}
