package uiMain;

import gestorAplicacion.animalesZoologico.Animal;
import gestorAplicacion.animalesZoologico.Especie;
import gestorAplicacion.animalesZoologico.Habitat;

// Esta clase se hizo temporalmente para las pruebas que tengamos que hacer del c�digo que vamos desarrollando. Obviamente se elimina al final.
public class Pruebas {

	public static void main(String[] args) {

		// -------------------pruebas juan j---------------------
		Habitat obj1 = new Habitat("nombre", "ambientacion", 100);

		Animal obj2 = new Animal(Especie.ANFIBIO, obj1, "genero", 10, 2);
		Animal obj3 = new Animal(Especie.AVE, obj1, "genero", 10, 2);
		Animal obj4 = new Animal(Especie.MAMIFERO, obj1, "genero", 10, 2);
		Animal obj5 = new Animal(Especie.REPTIL, obj1, "genero", 10, 2);
		Animal obj6 = new Animal(Especie.PEZ, obj1, "genero", 10, 2);

		System.out.println(obj2.getEspecie());
		System.out.println(Especie.getTotalEspecies());

		/*
		Especie.ANFIBIO.addEspecie(obj2);
		Especie.ANFIBIO.addEspecie(obj2);
		Especie.ANFIBIO.addEspecie(obj2);

		Especie.ANFIBIO.addEspecie(obj3);
		Especie.ANFIBIO.addEspecie(obj3);
		Especie.ANFIBIO.addEspecie(obj3);

		Especie.ANFIBIO.addEspecie(obj4);
		Especie.ANFIBIO.addEspecie(obj4);
		Especie.ANFIBIO.addEspecie(obj5);
		Especie.ANFIBIO.addEspecie(obj5);
		Especie.ANFIBIO.addEspecie(obj6);

		Especie.AVE.addEspecie(obj6);

		Especie.AVE.removeEspecie(obj6);
		*/

		/*
		System.out.println(obj2.getEspecie().getDicEspecie().get("Anfibio"));
		System.out.println(obj2.getEspecie().getDicEspecie().get("Ave"));
		System.out.println(obj2.getEspecie().getDicEspecie().get("Pez"));
		System.out.println(obj2.getEspecie().getDicEspecie().get("Mamifero"));
		System.out.println(obj2.getEspecie().getDicEspecie().get("Reptil"));
		*/

		/*
		System.out.println(obj2.getEspecie().getDicEspecie());

		Especie.AVE.removeEspecie(obj5);
		System.out.println(obj2.getEspecie().getDicEspecie());
		*/

		// -------------------pruebas juan j---------------------

		
	}

}
