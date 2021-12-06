package gestorAplicacion.animalesZoologico;

import java.util.ArrayList;
import gestorAplicacion.gestionZoologico.Cuidador;
//import gestorAplicacion.animalesZoologico.Animal;

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
