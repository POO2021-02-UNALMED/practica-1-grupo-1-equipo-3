package uiMain;

import gestorAplicacion.gestionZoologico.*;

import java.util.ArrayList;
import java.util.List;

import gestorAplicacion.animalesZoologico.*;

public class FuncionalidadesOtras {
	static void funcionalidades() {
		int opcion;
		System.out.println("Primero elija qué desea hacer:\n");
		System.out.println("1. Contratar empleado");
		System.out.println("2. Despedir empleado");
		System.out.println("3. Crear hábitat");
		System.out.println("4. Consultar datos");
		System.out.print("\n¿Cuál opción quiere realizar? ");
		opcion = Main.leerOpcion();
		System.out.println();
		switch(opcion) {
			case 1: {
				System.out.println("Puede elegir entre:\n");
				System.out.println("1. Contratar cuidador");
				System.out.println("2. Contratar veterinario");
				System.out.print("\n¿Cuál quiere realizar? ");
				opcion = Main.leerOpcion();
				System.out.println();
				switch(opcion) {
					case 1: {
						contratarCuidador();break;
					}
					case 2: {
						contratarVeterinario();break;
					}
					default: System.out.println("OPCIÓN INCORRECTA: Solo opciones 1 y 2."); break;
				}
			}
			case 2: {
				System.out.println("Puede elegir entre:\n");
				System.out.println("1. Despedir cuidador");
				System.out.println("2. Despedir veterinario");
				System.out.print("\n¿Cuál quiere realizar? ");
				opcion = Main.leerOpcion();
				System.out.println();
				switch(opcion) {
					case 1: {
						despedirCuidador();break;
					}
					case 2: {
						despedirVeterinario();break;
					}
					default: System.out.println("OPCIÓN INCORRECTA: Solo opciones 1 y 2."); break;
				}
				
			}
			case 3: {
				
			}
			case 4: {
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
		String nombre;
		int sueldo;
		String nombreEspecialidad;
		Especie especialidad=null;
		Cuidador nuevo;
		System.out.println("Ingrese el nombre del cuidador al que quiere contratar:");
		nombre=Main.leerString();
		System.out.println();
		System.out.println("Ahora ingrese el sueldo del cuidador:");
		sueldo=Main.leerOpcion();
		System.out.println();
		System.out.println("Ahora ingrese el nombre de la especie de la que se va a encargar el cuidador:");
		nombreEspecialidad=Main.sc.next();
		System.out.println();
		for (Especie especie:Administracion.getEspecies()) {
			if (especie.getNombre().equals(nombreEspecialidad)){
				especialidad=especie;
				break;}
		}
		nuevo=Administracion.contratarCuidador(nombre, sueldo, especialidad);
		System.out.println("¡"+nuevo.getNombre()+" ya hace parte de la nomina de cuidadores del zoológico!\n");
		System.out.println("Estas son las características del nuevo cuidador:\n");
		System.out.println(nuevo.info());
	}
	
	static void contratarVeterinario() {
		String nombre;
		int sueldo;
		String nombreEspecialidad="";
		Especie especialidad = null;
		Veterinario nuevo;
		System.out.println("Ingrese el nombre del veterinario al que quiere contratar:");
		nombre=Main.leerString();
		System.out.println();
		System.out.println("Ahora ingrese el sueldo del veterinario:");
		sueldo=Main.leerOpcion();
		System.out.println();
		System.out.println("Ahora ingrese el nombre de la especie de la cual el veterinario está especializado:");
		nombreEspecialidad=Main.sc.next();
		System.out.println();
		for (Especie especie:Administracion.getEspecies()) {
			if (especie.getNombre().equals(nombreEspecialidad)){
				especialidad=especie;
				break;}
		}
		nuevo=Administracion.contratarVeterinario(nombre, sueldo, especialidad);
		System.out.println("¡"+nuevo.getNombre()+" ya hace parte de la nomina de veterinarios del zoológico!\n");
		System.out.println("Estas son las características del nuevo veterinario:\n");
		System.out.println(nuevo.info());
	}
	
	static void despedirCuidador() {
		int id;
		boolean estado=false;
		List<Integer> identificaciones= new ArrayList<Integer>();
		System.out.println("A continuación le mostraremos la nómina de cuidadores del zoológico:");
		for (Cuidador cuidador:Administracion.getCuidadores()) {
			System.out.println("\n"+cuidador.info());
		}
		System.out.println("¿Ya se decidio por el cuidador que quiere despedir? A continuación ingrese el número de identificación del cuidador:" );
		while (estado==false){
			id=Main.sc.nextInt();
			for (Cuidador cuidador:Administracion.getCuidadores()) {
				identificaciones.add(cuidador.getIdentificacion());
				if (cuidador.getIdentificacion()==id) {
					Administracion.despedirCuidador(id);
					System.out.println(cuidador.getNombre()+" hacia parte de la nómina de cuidadores del zoológico. Ha sido despedid@.");
					estado=true;
					break;
				}
			}
			//En caso de que se ingrese una identificacion que no corresponde a algun empelado de la nomina,volverá a pedir la identificación hasta que se ingrese una correcta
			if (identificaciones.contains(id)==false) {
				System.out.println("\nNinguno de nuestros empleados tiene esa identificación. Por favor vuelva a ingresar una identificación válida.");
			}
		}
	}
	
	static void despedirVeterinario() {
		int id;
		boolean estado=false;
		List<Integer> identificaciones= new ArrayList<Integer>();
		System.out.println("A continuación le mostraremos la nómina de veterinarios del zoológico:");
		for (Veterinario veterinario:Administracion.getVeterinarios()) {
			System.out.println("\n"+veterinario.info());
		}
		System.out.println("¿Ya se decidio por el veterinario que quiere despedir? A continuación ingrese el número de identificación del veterinario:" );
		while (estado==false){
			id=Main.sc.nextInt();
			for (Veterinario veterinario:Administracion.getVeterinarios()) {
				identificaciones.add(veterinario.getIdentificacion());
				if (veterinario.getIdentificacion()==id) {
					Administracion.despedirVeterinario(id);
					System.out.println(veterinario.getNombre()+" hacia parte de la nómina de cuidadores del zoológico. Ha sido despedid@.");
					estado=true;
					break;
				}
			}
			//En caso de que se ingrese una identificacion que no corresponde a algun empelado de la nomina,volverá a pedir la identificación hasta que se ingrese una correcta
			if (identificaciones.contains(id)==false) {
				System.out.println("\nNinguno de nuestros empleados tiene esa identificación. Por favor vuelva a ingresar una identificación válida.");
			}
		}
	}
	
	
}
