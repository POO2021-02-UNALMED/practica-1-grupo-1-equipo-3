package uiMain;

import gestorAplicacion.gestionZoologico.*;
import gestorAplicacion.animalesZoologico.*;

public class FuncionalidadesOtras {
	static void funcionalidades() {
		int opcion;
		System.out.println("Primero elija qué desea hacer:\n");
		System.out.println("1. Contratar empleado");
		System.out.println("2. Despedir empleado");
		System.out.println("3. Crear hábitat");
		System.out.println("4. Borrar hábitat");
		System.out.println("5. Consultar datos");
		System.out.print("\n¿Cuál opción quiere realizar? ");
		opcion = Main.leerOpcion();
		System.out.println();
		switch(opcion) {
			case 1: {
				System.out.println("Puede elegir entre:\n");
				System.out.println("1. Contratar cuidador");
				System.out.println("2. Contratar veterinario");
				System.out.print("\n¿Cuál quieres realizar? ");
				opcion = Main.leerOpcion();
				System.out.println();
				switch(opcion) {
					case 1: {
						contratarCuidador();break;
					}
					case 2: {
						
					}
					default: System.out.println("OPCIÓN INCORRECTA: Solo opciones 1 y 2."); break;
				}
			}
			case 2: {
				System.out.println("Puede elegir entre:\n");
				System.out.println("1. Despedir cuidador");
				System.out.println("2. Despedir veterinario");
				System.out.print("\n¿Cuál quieres realizar? ");
				opcion = Main.leerOpcion();
				System.out.println();
				switch(opcion) {
					case 1: {
						
					}
					case 2: {
						
					}
					default: System.out.println("OPCIÓN INCORRECTA: Solo opciones 1 y 2."); break;
				}
				
			}
			case 3: {
				
			}
			case 4: {
				
			}
			case 5: {
				System.out.println("Ahora elija qué desea hacer:\n");
				System.out.println("1. Consultar datos animales");
				System.out.println("2. Consultar datos hábitats");
				System.out.println("3. Consultar datos cuidadores");
				System.out.println("4. Consultar datos veterinarios");
				System.out.println("5. Consultar datos visitantes");
				System.out.print("\n¿Cuál opción quiere realizar? ");
				opcion = Main.leerOpcion();
				System.out.println();
				switch(opcion) {
					case 1: {
					
					}
					case 2: {
						
					}
					case 3: {
						
					}
					case 4: {
						
					}
					case 5: {
						
					}
					default: System.out.println("OPCIÓN INCORRECTA: Solo opciones del 1 al 5."); break;
				}
			}
			default: System.out.println("OPCIÓN INCORRECTA: Solo opciones del 1 al 6."); break;
		}
		Main.continuar();
	}
	
	static void contratarCuidador() {
		String nombre="";
		int sueldo=0;
		String nombreEspecialidad="";
		Especie especialidad = null;
		Cuidador nuevo=null;
		System.out.println("Ingrese el nombre del cuidador al que quiere contratar:");
		nombre=Main.sc.nextLine();
		System.out.println("Ahora ingrese el sueldo del cuidador:");
		sueldo=Main.sc.nextInt();
		System.out.println("Ahora ingrese el nombre de la especie de la que se va a encargar el cuidador:");
		nombreEspecialidad=Main.sc.nextLine();
		for (Especie especie:Administracion.getEspecies()) {
			if (especie.getNombre().equals(nombreEspecialidad)){
				especialidad=especie;
				break;}
		}
		nuevo=Administracion.contratarCuidador(nombre, sueldo, especialidad);
		System.out.println("¡"+nuevo.getNombre()+" ya hace parte de la nomina de cuidadores del zoológico!");
		System.out.println("Estas son las características del nuevo empleado:");
		System.out.println(nuevo.info());
	}
}
