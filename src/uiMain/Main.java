package uiMain;
import baseDatos.*;
import gestorAplicacion.*;
import java.util.Scanner;

public class Main {
	static Scanner sc= new Scanner(System.in);
	
	static int leerOpcion() {
		return sc.nextInt();}
	
	public static void main(String args[]) {
		int opcion;
		do {
			System.out.println("¡Bienvenido al sistema gestor de tu Zoológico!");
			System.out.println("\n");
			System.out.println("A continuación te presentamos funcionalidades disponibles:");
			System.out.println("\n");
			System.out.println("1. Mantenimiento de los habitats");
			System.out.println("2. Curar a los animales");
			System.out.println("3. Cuidar a los animales");
			System.out.println("4. Gestión administrativa del Zoológico");
			System.out.println("5. Adquisición y traslado de animales");
			System.out.println("6. Salir del programa");
			System.out.println("\n");
			System.out.println("¿Cuál quieres realizar?");
			System.out.println("\n");
			opcion=leerOpcion();
			System.out.println("\n");
			
			switch(opcion) {
				case 1: System.out.println("En proceso 1");break;
				case 2: System.out.println("En proceso 2");break;
				case 3: System.out.println("En proceso 3");break;
				case 4: System.out.println("En proceso 4");break;
				case 5: System.out.println("En proceso 5");break;
				case 6: System.out.println("¡Gracias por haber usado nuestra aplicación!");break;}
		} while(opcion!=6);
	}
}