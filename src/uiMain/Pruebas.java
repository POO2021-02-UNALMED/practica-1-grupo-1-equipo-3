package uiMain;

import gestorAplicacion.*;
import gestorAplicacion.animalesZoologico.Animal;
import gestorAplicacion.animalesZoologico.Especie;
import gestorAplicacion.animalesZoologico.Habitat;

// Esta clase se hizo temporalmente para las pruebas que tengamos que hacer del c�digo que vamos desarrollando. Obviamente se elimina al final.
public class Pruebas {

	public static void main(String[] args) {

		// -------------------pruebas juan j---------------------
		Habitat obj1 = new Habitat(123, "nombre", "ambientacion", 100);
		Animal obj2 = new Animal(12345, Especie.ANFIBIO, obj1, "genero", 10, 2);

		System.out.println(obj2.getEspecie());
		System.out.println(Especie.getTotalespecie());

		Especie.ANFIBIO.addEspecie(obj2);
		Especie.ANFIBIO.addEspecie(obj2);
		Especie.ANFIBIO.addEspecie(obj2);

		System.out.println(obj2.getEspecie().getDicEspecie().get("Anfibio"));

		


		

		// -------------------pruebas juan j---------------------

		
	}

}
