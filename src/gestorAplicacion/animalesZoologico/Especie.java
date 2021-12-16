// CLASE CREADA POR JUAN JOS� MONSALVE MAR�N

/*
La clase Especie de tipo Enum se crea con el fin de definir los 5 �nicos posibles objetos que se podr�n crear de esta clase, 
los cuales son MAMIFERO, AVE, REPTIL, PEZ y ANFIBIO, donde cada uno de estos objetos cuenta con tres atributos. 
Nombre de tipo String que corresponde al nombre de la especie, dieta de tipo String que corresponde a la dieta 
de la especie que se encuentra en el zool�gico y promedioVida que corresponde al promedio de los animales de esa especie 
que se encuentran en el zool�gico.   
*/

package gestorAplicacion.animalesZoologico;

import gestorAplicacion.gestionZoologico.*;
import gestorAplicacion.gestionZoologico.Entidad;

public enum Especie implements Entidad {

    // Se generan los 5 diferentes objetos de esta clase con sus respectivos atributos.
    MAMIFERO("Mamifero", "omnivoro", 40), 
    AVE("Ave", "granivoro", 25), 
    REPTIL("Reptil", "carnivoro", 35),
    PEZ("Pez", "omnivoro", 30),
    ANFIBIO("Anfibio", "insectivoro", 15);
	
    private static final int TOTALESPECIE = 5;
    private String nombre;
    private String dieta;
    private int promedioVida;

    /* 
    Enum es una clase especial que limita la creaci�n de objetos a los especificados en su clase 
    (por eso su constructor es privado), pero estos objetos pueden tener atributos como cualquier otra clase.
    */
    private Especie(String nombre, String dieta, int promedioVida) {
        this.nombre = nombre;
        this.dieta = dieta;
        this.promedioVida = promedioVida;
        Administracion.addEspecies(this);
    }
    
    /* El m�todo info() es implementado de la interfaz Entidad y definido aqu�. Sirve para generar el String que ser� 
	 * usado para imprimir por consola los datos de la especie en caso de ser requeridos en alguna de las funcionalidades 
	 * de la aplicaci�n.
	 */
    public String info() {
		return ("Nombre: " + this.getNombre() +
				"\nDieta: " + this.getDieta() +
				"\nPromedio de vida: " + String.valueOf(this.getPromedioVida()));
	}

    // De aqu� en adelante se definen los m�todos set y get de la clase especie. 
    public String getNombre() {
        return nombre;
    }

    public String getDieta() {
        return dieta;
    }

    public int getPromedioVida() {
        return promedioVida;
    }

    public static int getTotalEspecies() {
        return TOTALESPECIE;
    }
}