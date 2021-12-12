package gestorAplicacion.animalesZoologico;

<<<<<<< Updated upstream
import java.util.ArrayList;

import gestorAplicacion.gestionZoologico.Administracion;
=======
import java.util.*;
>>>>>>> Stashed changes
import gestorAplicacion.gestionZoologico.Cuidador;
//import gestorAplicacion.animalesZoologico.Animal;

public enum Especie {

    MAMIFERO("Mamifero", "omnivoro", 40), 
    AVE("Ave", "granivoro", 25), 
    REPTIL("Reptil", "carnivoro", 35),
    PEZ("Pez", "omnivoro", 30),
    ANFIBIO("Anfibio", "insectivoro", 15);

    private static final int TOTALESPECIE = 5;
    private String nombre;
    private String dieta;
    private int promedioVida;

    private Map<String, Integer> dicEspecie = new HashMap<String, Integer>();
    
    private ArrayList<Cuidador> cuidadorAsignado = new ArrayList<Cuidador>();
    private ArrayList<Animal> animales = new ArrayList<Animal>();

    private Especie(String nombre, String dieta, int promedioVida) {
        this.nombre = nombre;
        this.dieta = dieta;
        this.promedioVida = promedioVida;
<<<<<<< Updated upstream
        Administracion.addEspecies(this);
=======
        System.out.println(nombre);

        dicEspecie.put("Mamifero", 0);
        dicEspecie.put("Ave", 0);
        dicEspecie.put("Reptil", 0);
        dicEspecie.put("Pez", 0);
        dicEspecie.put("Anfibio", 0);
>>>>>>> Stashed changes
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
        else if (animal.getEspecie().nombre == "Anfibio") {
            this.dicEspecie.put("Anfibio", dicEspecie.get("Anfibio")+1);
        }
        

        

    }

}










/*
public class Especie {
    private static int totalEspecies;
    private String nombre;
    private String dieta;
    private int promedioVida;
    private ArrayList<Cuidador> cuidadorAsignado = new ArrayList<Cuidador>();
    private ArrayList<Animal> animales = new ArrayList<Animal>();

    public Especie(String nombre, String dieta, int promedioVida) {
        this.nombre = nombre;
        this.dieta = dieta;
        this.promedioVida = promedioVida;
        Especie.totalEspecies++;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDieta() {
        return dieta;
    }

    public void setDieta(String dieta) {
        this.dieta = dieta;
    }

    public int getPromedioVida() {
        return promedioVida;
    }

    public void setPromedioVida(int promedioVida) {
        this.promedioVida = promedioVida;
    }

    public void setAnimales(ArrayList<Animal> animales) {
        this.animales = animales;
    }

    public ArrayList<Animal> getAnimales() {
        return animales;
    }

    public ArrayList<Cuidador> getCuidadorAsignado() {
        return cuidadorAsignado;
    }

    public void setCuidadorAsignado(ArrayList<Cuidador> cuidadorAsignado) {
        this.cuidadorAsignado = cuidadorAsignado;
    }

    public static int getTotalEspecies() {
        return totalEspecies;
    }

    public static void setTotalEspecies(int totalEspecies) {
        Especie.totalEspecies = totalEspecies;
    }

}
*/
