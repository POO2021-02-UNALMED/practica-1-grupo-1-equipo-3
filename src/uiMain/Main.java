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
			System.out.println("�Bienvenido al sistema gestor de tu Zool�gico!");
			System.out.println("\n");
			System.out.println("A continuaci�n te presentamos funcionalidades disponibles:");
			System.out.println("\n");
			System.out.println("1. Mantenimiento de los habitats");
			System.out.println("2. Curar a los animales");
			System.out.println("3. Cuidar a los animales");
			System.out.println("4. Gesti�n administrativa del Zool�gico");
			System.out.println("5. Adquisici�n y traslado de animales");
			System.out.println("6. Salir del programa");
			System.out.println("\n");
			System.out.println("�Cu�l quieres realizar?");
			System.out.println("\n");
			opcion=leerOpcion();
			System.out.println("\n");
			
			switch(opcion) {
				case 1: System.out.println("En proceso 1");break;
				case 2: System.out.println("En proceso 2");break;
				case 3: System.out.println("En proceso 3");break;
				case 4: System.out.println("En proceso 4");break;
				case 5: System.out.println("En proceso 5");break;
				case 6: System.out.println("�Gracias por haber usado nuestra aplicaci�n!");break;}
		} while(opcion!=6);
	}
}