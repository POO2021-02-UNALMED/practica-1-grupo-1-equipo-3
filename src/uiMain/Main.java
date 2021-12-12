package uiMain;
import baseDatos.*;
import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;

import java.util.Scanner;

public class Main {
	static Scanner sc= new Scanner(System.in);
	
	static int leerOpcion() {
		return sc.nextInt();}
	
	public static void main(String args[]) {
		Habitat a = new Habitat(1, "A1", "Sabana", 10);
		Habitat b = new Habitat(2, "A2", "Jungla", 25);
		Animal x = new Animal(1, Especie.MAMIFERO, a, "M", 5, 70);
		Animal y = new Animal(2, Especie.MAMIFERO, a, "F", 3, 55);
		Animal z = new Animal(3, Especie.AVE, b, "M", 2, 5);
		Cuidador xx = new Cuidador(1, "Jorge", 750, Especie.MAMIFERO);
		Cuidador yy = new Cuidador(2, "Johanna", 750, Especie.MAMIFERO);
		Cuidador zz = new Cuidador(3, "Camila", 650, Especie.AVE);
		
		int opcion;
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
				case 1: System.out.println("En proceso 1\n"); break;
				case 2: System.out.println("En proceso 2\n"); break;
				case 3: FuncionalidadCuidar.cuidarAnimal(); break;
				case 4: System.out.println("En proceso 4\n"); break;
				case 5: System.out.println("En proceso 5\n"); break;
				case 6: System.out.println("�Gracias por haber usado nuestra aplicaci�n!\n");break;}
		} while(opcion!=6);
	}
}