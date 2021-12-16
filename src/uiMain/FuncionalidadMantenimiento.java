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
		boolean habitatsDisponibles = seleccionarHabitat();
		if(habitatsDisponibles) {
			boolean cuidadoresDisponibles = seleccionarCuidador();
			if(cuidadoresDisponibles) limpiezaHabitat();
		}
		Main.continuar();
	}

	static boolean seleccionarHabitat() {
		int id;
		int habitats = 0;
		System.out.println("Elija primero el habitat que desee revisar, ingresando su identificación.\n");
		System.out.println("Identificacion; Nombre; Ambientacion; Especie del Habitat; Cantidad Animales; Capacidad Maxima");
		
		for(Habitat habitat: Administracion.getHabitats()) {
			if(habitat.getAnimalesAsociados().size() != 0) {
				System.out.println(habitat.getIdentificacion() + "; " + habitat.getNombre() + "; " + 
					    habitat.getAmbientacion() + "; " + habitat.getAnimalesAsociados().get(0).getEspecie().getNombre() + "; " 
					    + habitat.cantidadAnimales() + "; " + habitat.getCapacidadMaxima());
				habitats++;
			}
			
		}
		
		if(habitats == 0) {
			System.out.println("\nNo se ha encontrado ningún hábitat para revisar.");
			System.out.println("MANTENIMIENTO CANCELADO\n");
			return false;
		} else {
			System.out.print("\n¿Cuál hábitat elije? (Identificacion) ");
			id = Main.leerOpcion();
			
			while(id == 0) {
				System.out.print("Por favor SELECCIONE otro hábitat ");
				id = Main.leerOpcion();
			}
			
			for(Habitat habitat: Administracion.getHabitats()) {
				if(id == habitat.getIdentificacion()) {
					System.out.println("\nHábitat seleccionado:\n");
					System.out.println(habitat.info());
					habitatSeleccionado = habitat;
					
				}
			}
			return true;
		}
	}

	static boolean seleccionarCuidador() {
		int id;
		int cuidadores = 0;
		System.out.println("\nAhora elija el cuidador que desee que revise el hábitat, ingresando su identificación.\n");
		System.out.println("Identificación; Nombre; Especie Asignada");

		for (Cuidador cuidador : Administracion.getCuidadores()) {
			System.out.println(cuidador.getIdentificacion() + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre());
			cuidadores++;
		}
		
		if(cuidadores == 0) {
			System.out.println("\nNo se ha encontrado ningún cuidador para que revise el hábitat.");
			System.out.println("MANTENIMIENTO CANCELADO\n");
			return false;
		} else {
			System.out.print("\n¿Cuál cuidador elige? (Identificación) ");
			id = Main.leerOpcion();
	
			for (Cuidador cuidador : Administracion.getCuidadores()) {
				if (cuidador.getIdentificacion() == id) {
					System.out.println("Cuidador seleccionado: \n");
					System.out.println(cuidador.info());
					cuidadorSeleccionado = cuidador;
					break;
				}
			}
			return true;
		}
	}

	static void limpiezaHabitat() {
		ArrayList<Integer> idAnimalesTristes = new ArrayList<Integer>();

		System.out.println("\nCuidador " + cuidadorSeleccionado.getNombre()
				+ " procede a revisar el habitat con identficacion " + habitatSeleccionado.getIdentificacion() + ".");

		if (cuidadorSeleccionado.revisar(habitatSeleccionado)) {
			System.out.println("RESULTADO: El habitat se encuentra en buen estado.\n");
		}

		else {
			System.out.println("El cuidador " + cuidadorSeleccionado.getNombre()
					+ " decide sacar a todos los animales para hacer mantenimiento al habitat");
			cuidadorSeleccionado.limpiarHabitat(habitatSeleccionado, jaula);

			for (Animal animal : habitatSeleccionado.getAnimalesAsociados()) {
				if (animal.isEstadoAnimo() == false) {
					idAnimalesTristes.add(animal.getIdentificacion());
				}
			}

			if (idAnimalesTristes.size() == 0) {
				System.out.println("Hacerle mantenimiento al habitat ha dado buenos resultados, no hay animales tristes en este.");
			} else {
				System.out.println("Los animales con los siguientes números de identificacion no han mejorado sus estados de ánimo: ");
				for (int id : idAnimalesTristes) {
					System.out.println(id);
				}
				System.out.println("Puede solicitar alimentarlos o que los revise un veterinario");
			}
		}
		return;
	}
}
