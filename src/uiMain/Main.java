package uiMain;
import baseDatos.Serializador;
import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;

import java.util.Scanner;

public class Main {
	static Scanner sc= new Scanner(System.in);
	
	static int leerOpcion() {
		return sc.nextInt();}
	
	/* El método salirDelSistema() permite guardar en los archivos las listas de animales, visitantes, habitat, especies, veterinarios y cuidadores
	 * del objeto admin del tipo Administracion. */
	private static void salirDelSistema() {
		System.out.println("¡Gracias por haber usado nuestra aplicación! Vuelva pronto.\n");
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
		Administracion admin = new Administracion(0);
		Habitat a = new Habitat(1, "A1", "Sabana", 10);
		Habitat b = new Habitat(2, "A2", "Jungla", 25);
		Animal x = new Animal(1, Especie.MAMIFERO, a, "M", 5, 70);
		Animal y = new Animal(2, Especie.MAMIFERO, a, "F", 3, 55);
		Animal z = new Animal(3, Especie.AVE, b, "M", 2, 5);
		Cuidador xx = new Cuidador(1, "Jorge", 7500, Especie.MAMIFERO);
		Cuidador yy = new Cuidador(2, "Johanna", 7500, Especie.MAMIFERO);
		Cuidador zz = new Cuidador(3, "Camila", 200200, Especie.AVE);
		Visitante v1= new Visitante(1,"Jose",3,15);
		Visitante v2= new Visitante(2,"Diego",5,30);
		Veterinario vv= new Veterinario(11,"Elva",500,Especie.AVE);
		int opcion;
		do {
			System.out.println("\n¡Bienvenido al sistema gestor de tu Zoológico!\n");
			System.out.println("A continuación te presentamos funcionalidades disponibles:\n");
			System.out.println("1. Mantenimiento de los habitats");
			System.out.println("2. Curar a los animales");
			System.out.println("3. Cuidar a los animales");
			System.out.println("4. Gestión administrativa del Zoológico");
			System.out.println("5. Adquisición y traslado de animales");
			System.out.println("6. Salir del programa");
			System.out.print("\n¿Cuál quieres realizar? ");
			opcion=leerOpcion();
			System.out.println();
			switch(opcion) {
				case 1: FuncionalidadMantenimiento.mantenimientoHabitat(); break;
				case 2: FuncionalidadCurar.curarAnimal(); break;
				case 3: FuncionalidadCuidar.cuidarAnimal(); break;
				case 4: FuncionalidadGestion.gestionAdministrativa(); break;
				case 5: FuncionalidadAdquisicionTraslado.adquisicionTraslado(); break;
				case 6: salirDelSistema(); break;
				default: System.out.println("Opción incorrecta. Solo opciones del 1 al 6."); break;}
		} while(opcion!=6);
	}
}