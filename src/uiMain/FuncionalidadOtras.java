package uiMain;

import gestorAplicacion.gestionZoologico.*;

import java.util.ArrayList;
import java.util.List;

import gestorAplicacion.animalesZoologico.*;

public class FuncionalidadOtras {
	static void funcionalidades() {
		int opcion;
		System.out.println("Primero elija qu� desea hacer:\n");
		System.out.println("1. Contratar a un empleado");
		System.out.println("2. Despedir a un empleado");
		System.out.println("3. Construcci�n de un nuevo h�bitat");
		System.out.println("4. Consultar datos del zool�gico");
		System.out.print("\n�Cu�l opci�n quiere realizar? ");
		opcion = Main.leerOpcion();
		System.out.println();
		switch(opcion) {
			case 1: {
				System.out.println("Puede elegir entre:\n");
				System.out.println("1. Contratar cuidador");
				System.out.println("2. Contratar veterinario");
				System.out.print("\n�Cu�l quiere realizar? ");
				opcion = Main.leerOpcion();
				System.out.println();
				switch(opcion) {
					case 1: {
						contratarCuidador();break;
					}
					case 2: {
						contratarVeterinario();break;
					}
					default: System.out.println("OPCI�N INCORRECTA: Solo opciones 1 y 2."); break;
				}break;
			}
			case 2: {
				System.out.println("Puede elegir entre:\n");
				System.out.println("1. Despedir cuidador");
				System.out.println("2. Despedir veterinario");
				System.out.print("\n�Cu�l quiere realizar? ");
				opcion = Main.leerOpcion();
				System.out.println();
				switch(opcion) {
					case 1: {
						despedirCuidador();break;
					}
					case 2: {
						despedirVeterinario();break;
					}
					default: System.out.println("OPCI�N INCORRECTA: Solo opciones 1 y 2."); break;
				}break;
				
			}
			case 3: {
				crearHabitat();break;
			}
			case 4: {
				System.out.println("Puede elegir entre:\n");
				System.out.println("1. Consultar datos animales");
				System.out.println("2. Consultar datos h�bitats");
				System.out.println("3. Consultar datos cuidadores");
				System.out.println("4. Consultar datos veterinarios");
				System.out.println("5. Consultar datos visitantes");
				System.out.print("\n�Cu�l opci�n quiere realizar? ");
				opcion = Main.leerOpcion();
				System.out.println();
				switch(opcion) {
					case 1: {
						animales();break;
					}
					case 2: {
						habitats();break;
					}
					case 3: {
						cuidadores();break;
					}
					case 4: {
						veterinarios();break;
					}
					case 5: {
						visitantes();break;
					}
					default: System.out.println("OPCI�N INCORRECTA: Solo opciones del 1 al 5."); break;
				}break;
			}
			default: System.out.println("OPCI�N INCORRECTA: Solo opciones del 1 al 6."); break;
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
		System.out.println("Ahora ingrese el sueldo del cuidador (N�MERO ENTERO):");
		sueldo=Main.leerOpcion();
		System.out.println();
		System.out.println("A continu�cion se muestran las especies para que posteriormente sea ingresado el nombre de la especie.");
		for (Especie especie:Administracion.getEspecies()) {
			System.out.println("\n"+especie.info());
		}
		System.out.println();
		System.out.println("Por �ltimo ingrese el nombre de la especie de la que se va a encargar el cuidador:");
		nombreEspecialidad=Main.sc.next();
		System.out.println();
		for (Especie especie:Administracion.getEspecies()) {
			if (especie.getNombre().equals(nombreEspecialidad)){
				especialidad=especie;
				break;}
		}
		nuevo=Administracion.contratarCuidador(nombre, sueldo, especialidad);
		System.out.println("�"+nuevo.getNombre()+" ya hace parte de la nomina de cuidadores del zool�gico!\n");
		System.out.println("Estas son las caracter�sticas del nuevo cuidador:\n");
		System.out.println(nuevo.info());
		System.out.println();
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
		System.out.println("Ahora ingrese el sueldo del veterinario (N�MERO ENTERO):");
		sueldo=Main.leerOpcion();
		System.out.println();
		System.out.println("A continu�cion se muestran las especies para que posteriormente sea ingresado el nombre de la especie.");
		for (Especie especie:Administracion.getEspecies()) {
			System.out.println("\n"+especie.info());
		}
		System.out.println();
		System.out.println("Por �ltimo ingrese el nombre de la especie de la cual el veterinario est� especializado:");
		nombreEspecialidad=Main.sc.next();
		System.out.println();
		for (Especie especie:Administracion.getEspecies()) {
			if (especie.getNombre().equals(nombreEspecialidad)){
				especialidad=especie;
				break;}
		}
		nuevo=Administracion.contratarVeterinario(nombre, sueldo, especialidad);
		System.out.println("�"+nuevo.getNombre()+" ya hace parte de la nomina de veterinarios del zool�gico!\n");
		System.out.println("Estas son las caracter�sticas del nuevo veterinario:\n");
		System.out.println(nuevo.info());
		System.out.println();
	}
	
	static void despedirCuidador() {
		int id;
		boolean estado=false;
		List<Integer> identificaciones= new ArrayList<Integer>();
		System.out.println("A continuaci�n le mostraremos la n�mina de cuidadores del zool�gico:");
		for (Cuidador cuidador:Administracion.getCuidadores()) {
			System.out.println("\n"+cuidador.info());
		}
		System.out.println("�Ya se decidio por el cuidador que quiere despedir? A continuaci�n ingrese el n�mero de identificaci�n del cuidador:" );
		while (estado==false){
			id=Main.sc.nextInt();
			for (Cuidador cuidador:Administracion.getCuidadores()) {
				identificaciones.add(cuidador.getIdentificacion());
				if (cuidador.getIdentificacion()==id) {
					Administracion.despedirCuidador(id);
					System.out.println(cuidador.getNombre()+" hacia parte de la n�mina de cuidadores del zool�gico. Ha sido despedid@.");
					System.out.println();
					estado=true;
					break;
				}
			}
			//En caso de que se ingrese una identificacion que no corresponde a algun empelado de la nomina,volver� a pedir la identificaci�n hasta que se ingrese una correcta
			if (identificaciones.contains(id)==false) {
				System.out.println("\nNinguno de nuestros cuidadores tiene esa identificaci�n. Por favor vuelva a ingresar una identificaci�n v�lida.");
			}
		}
	}
	
	static void despedirVeterinario() {
		int id;
		boolean estado=false;
		List<Integer> identificaciones= new ArrayList<Integer>();
		System.out.println("A continuaci�n le mostraremos la n�mina de veterinarios del zool�gico:");
		for (Veterinario veterinario:Administracion.getVeterinarios()) {
			System.out.println("\n"+veterinario.info());
		}
		System.out.println("�Ya se decidio por el veterinario que quiere despedir? A continuaci�n ingrese el n�mero de identificaci�n del veterinario:" );
		while (estado==false){
			id=Main.sc.nextInt();
			for (Veterinario veterinario:Administracion.getVeterinarios()) {
				identificaciones.add(veterinario.getIdentificacion());
				if (veterinario.getIdentificacion()==id) {
					Administracion.despedirVeterinario(id);
					System.out.println(veterinario.getNombre()+" hacia parte de la n�mina de veterinarios del zool�gico. Ha sido despedid@.");
					System.out.println();
					estado=true;
					break;
				}
			}
			//En caso de que se ingrese una identificacion que no corresponde a algun empelado de la nomina,volver� a pedir la identificaci�n hasta que se ingrese una correcta
			if (identificaciones.contains(id)==false) {
				System.out.println("\nNinguno de nuestros veterinarios tiene esa identificaci�n. Por favor vuelva a ingresar una identificaci�n v�lida.");
			}
		}
	}
	
	static void crearHabitat() {
		String nombre;
		String ambientacion;
		int capacidad;
		Habitat nuevoHabitat;
		System.out.println("Iniciaremos la construcci�n de un nuevo h�bitat.\n");
		System.out.println("A continuaci�n ingrese el nombre del h�bitat:");
		nombre=Main.leerString();
		System.out.println();
		System.out.println("Ahora ingresela ambientaci�n que va a tener el h�bitat:");
		ambientacion=Main.leerString();
		System.out.println();
		System.out.println("Por �ltimo ingrese la capacidad m�xima de animales que puede albergar:");
		capacidad=Main.leerOpcion();
		System.out.println("\n...");
		nuevoHabitat=Administracion.construirHabitat(nombre, ambientacion, capacidad);
		System.out.println("\n�Se ha construido el nuevo h�bitat!\n");
		System.out.println("Este posee las siguientes caracter�sticas:");
		System.out.println("\n"+nuevoHabitat.info());
		System.out.println();
	}
	
	static void animales() {
		System.out.println("Este es el listado de animales con los que cuenta el zool�gico:");
		for (Animal animal:Administracion.getAnimales()) {
			System.out.println();
			System.out.println(animal.info());
		}
		System.out.println();
	}
		
	static void habitats() {
		System.out.println("Este es el listado de h�bitats con los que cuenta el zool�gico:");
		for (Habitat habitat:Administracion.getHabitats()) {
			System.out.println();
			System.out.println(habitat.info());
		}
		System.out.println();
	}
	
	static void cuidadores() {
		System.out.println("Este es la n�mina de cuidadores del zool�gico:");
		for (Cuidador cuidador:Administracion.getCuidadores()) {
			System.out.println();
			System.out.println(cuidador.info());
		}
		System.out.println();
	}
	
	static void veterinarios() {
		System.out.println("Este es la n�mina de veterinarios del zool�gico:");
		for (Veterinario veterinario:Administracion.getVeterinarios()) {
			System.out.println();
			System.out.println(veterinario.info());
		}
		System.out.println();
	}
	
	static void visitantes() {
		System.out.println("Este es el listado de personas que han visitado el zool�gico en el d�a de hoy:");
		for (Visitante visitante:Administracion.getVisitantes()) {
			System.out.println();
			System.out.println(visitante.info());
		}
		System.out.println();
	}
	
	
	
}
