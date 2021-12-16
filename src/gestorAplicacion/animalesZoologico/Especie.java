package gestorAplicacion.animalesZoologico;

import java.util.ArrayList;

import gestorAplicacion.gestionZoologico.Administracion;
import gestorAplicacion.gestionZoologico.Entidad;
import gestorAplicacion.gestionZoologico.Cuidador;
import gestorAplicacion.gestionZoologico.Veterinario;
import java.io.Serializable;

public enum Especie implements Serializable, Entidad {

    MAMIFERO("Mamifero", "omnivoro", 40), 
    AVE("Ave", "granivoro", 25), 
    REPTIL("Reptil", "carnivoro", 35),
    PEZ("Pez", "omnivoro", 30),
    ANFIBIO("Anfibio", "insectivoro", 15);
	
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static final long serialVersionUID=1L;
    private static final int TOTALESPECIE = 5;
    private String nombre;
    private String dieta;
    private int promedioVida;

    //private Map<String, Integer> dicEspecie = new HashMap<String, Integer>();
    
    private ArrayList<Veterinario> veterinarioAsignado = new ArrayList<Veterinario>();
    private ArrayList<Cuidador> cuidadorAsignado = new ArrayList<Cuidador>();
    private ArrayList<Animal> animales = new ArrayList<Animal>();
    
    private Especie(String nombre, String dieta, int promedioVida) {
        this.nombre = nombre;
        this.dieta = dieta;
        this.promedioVida = promedioVida;
        Administracion.addEspecies(this);

        /*
        dicEspecie.put("Mamifero", 0);
        dicEspecie.put("Ave", 0);
        dicEspecie.put("Reptil", 0);
        dicEspecie.put("Pez", 0);
        dicEspecie.put("Anfibio", 0);
        */

    }
    
    /* El método info() es implementado de la interfaz Entidad y definido aquí. Sirve para generar el String que será 
	 * usado para imprimir por consola los datos de la especie en caso de ser requeridos en alguna de las funcionalidades 
	 * de la aplicación.
	 */
    public String info() {
		return ("Nombre: " + this.getNombre() +
				"\nDieta: " + this.getDieta() +
				"\nPromedio de vida: " + String.valueOf(this.getPromedioVida()));
	}

    public ArrayList<Animal> getAnimales() {
        return animales;
    }

    public void setAnimales(ArrayList<Animal> animales) {
        this.animales = animales;
    }

    public ArrayList<Cuidador> getCuidadorAsignado() {
        return cuidadorAsignado;
    }

    public void setCuidadorAsignado(ArrayList<Cuidador> cuidadorAsignado) {
        this.cuidadorAsignado = cuidadorAsignado;
    }
    
    public void removeAnimales(Animal eliminar) {
    	animales.remove(animales.indexOf(eliminar));
    }

    public void addAnimales(Animal nuevo) {
    	animales.add(nuevo);
    }

    public void removeCuidadorAsignado(Cuidador eliminar) {
        cuidadorAsignado.remove(cuidadorAsignado.indexOf(eliminar));
    }

    public void addCuidadorAsignado(Cuidador nuevo) {
        cuidadorAsignado.add(nuevo);
    }

    public String getNombre() {
        return nombre;
    }

    public String getDieta() {
        return dieta;
    }

    public int getPromedioVida() {
        return promedioVida;
    }

    public static int getTotalespecie() {
        return TOTALESPECIE;
    }

    public ArrayList<Veterinario> getVeterinarioAsignado() {
        return veterinarioAsignado;
    }

    public void setVeterinarioAsignado(ArrayList<Veterinario> veterinarioAsignado) {
        this.veterinarioAsignado = veterinarioAsignado;
    }

    public void removeVeterinarioAsignado(Veterinario eliminar) {
        veterinarioAsignado.remove(veterinarioAsignado.indexOf(eliminar));
    }

    public void addVeterinarioAsignado(Veterinario nuevo) {
        veterinarioAsignado.add(nuevo);
    }

    /*
    public Map<String, Integer> getDicEspecie() {
        return dicEspecie;
    }

    public void setDicEspecie(Map<String, Integer> dicEspecie) {
        this.dicEspecie = dicEspecie;
    }

    public void addEspecie(Animal animal) {

        if (animal.getEspecie().nombre == "Mamifero") {
            this.dicEspecie.put("Mamifero", dicEspecie.get("Mamifero")+1);
        }
        else if (animal.getEspecie().nombre == "Ave") {
            this.dicEspecie.put("Ave", dicEspecie.get("Ave")+1);
        }
        else if (animal.getEspecie().nombre == "Reptil") {
            this.dicEspecie.put("Reptil", dicEspecie.get("Reptil")+1);
        }
        else if (animal.getEspecie().nombre == "Pez") {
            this.dicEspecie.put("Pez", dicEspecie.get("Pez")+1);
        }
        else if (animal.getEspecie().nombre == "Anfibio") {
            this.dicEspecie.put("Anfibio", dicEspecie.get("Anfibio")+1);
        }
        
    }

    public void removeEspecie(Animal animal) {

        if (animal.getEspecie().nombre == "Mamifero") {
            this.dicEspecie.put("Mamifero", dicEspecie.get("Mamifero")-1);
        }
        else if (animal.getEspecie().nombre == "Ave") {
            this.dicEspecie.put("Ave", dicEspecie.get("Ave")-1);
        }
        else if (animal.getEspecie().nombre == "Reptil") {
            this.dicEspecie.put("Reptil", dicEspecie.get("Reptil")-1);
        }
        else if (animal.getEspecie().nombre == "Pez") {
            this.dicEspecie.put("Pez", dicEspecie.get("Pez")-1);
        }
        else if (animal.getEspecie().nombre == "Anfibio") {
            this.dicEspecie.put("Anfibio", dicEspecie.get("Anfibio")-1);
        }
    }
    */
}