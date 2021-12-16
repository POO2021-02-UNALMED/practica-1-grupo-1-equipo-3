package uiMain;

import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;
import java.io.Serializable;
import baseDatos.Deserializador;
import baseDatos.Serializador;

import java.util.Scanner;

public class Main implements Serializable {
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static final long serialVersionUID = 1L;
	static Scanner sc= new Scanner(System.in);
	
	static int leerOpcion() {
		return sc.nextInt();}
	
	/* El m�todo salirDelSistema() permite guardar en los archivos las listas de animales, visitantes, habitat, especies, veterinarios y cuidadores
	 * del objeto admin del tipo Administracion. */
	private static void salirDelSistema() {
		System.out.println("�Gracias por haber usado nuestra aplicaci�n! Vuelva pronto.\n");
		Serializador.serializar();
		continuar();
		System.exit(0);
	}
	
	static void continuar(){
		System.out.println("Presione \"ENTER\" para continuar...");
		Scanner continuar = new Scanner(System.in);
		continuar.nextLine();
	}
	
	public static void main(String args[]) {
		/* La siguiente l�nea permite cargar las listas de animales, visitantes, habitat, especies, veterinarios y cuidadores
		 * al objeto Administracion creado. */
		Deserializador.deserializar();
/*		Administracion admin = new Administracion();
		Habitat a = new Habitat("A1", "Sabana", 10);
		Habitat b = new Habitat("A2", "Jungla", 25);
		Cuidador xx = new Cuidador("Jorge", 7500, Especie.MAMIFERO);
		Cuidador yy = new Cuidador("Johanna", 7500, Especie.MAMIFERO);
		Cuidador zz = new Cuidador("Camila", 200200, Especie.AVE);
		Veterinario vv= new Veterinario("Elva",500,Especie.AVE);
		Animal x = new Animal(Especie.MAMIFERO, a, "M", 5, 70);
		Animal y = new Animal(Especie.MAMIFERO, a, "F", 3, 55);
		Animal z = new Animal(Especie.AVE, b, "M", 2, 5);
		Visitante v1= new Visitante("Jose",3,15);
		Visitante v2= new Visitante("Diego",5,30);
*/		int opcion;
		do {
			System.out.println("\n�Bienvenido al sistema gestor de tu Zool�gico!\n");
			System.out.println("A continuaci�n te presentamos funcionalidades disponibles:\n");
			System.out.println("1. Mantenimiento de los habitats");
			System.out.println("2. Curar a los animales");
			System.out.println("3. Cuidar a los animales");
			System.out.println("4. Gesti�n administrativa del Zool�gico");
			System.out.println("5. Adquisici�n y traslado de animales");
			System.out.println("6. Salir del programa");
			System.out.print("\n�Cu�l quieres realizar? ");
			opcion=leerOpcion();
			System.out.println();
			switch(opcion) {
				case 1: FuncionalidadMantenimiento.mantenimientoHabitat(); break;
				case 2: FuncionalidadCurar.curarAnimal(); break;
				case 3: FuncionalidadCuidar.cuidarAnimal(); break;
				case 4: FuncionalidadGestion.gestionAdministrativa(); break;
				case 5: FuncionalidadAdquisicionTraslado.adquisicionTraslado(); break;
				case 6: salirDelSistema(); break;
				default: System.out.println("Opci�n incorrecta. Solo opciones del 1 al 6."); break;}
		} while(opcion!=6);
	}
}