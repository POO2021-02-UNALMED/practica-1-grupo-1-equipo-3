package gestorAplicacion.animalesZoologico;

import java.io.Serializable;
import gestorAplicacion.gestionZoologico.Administracion;

public class Animal implements Serializable {
	private static final long serialVersionUID=1L;
	private static int totalAnimales;
	private int identificacion;
	private Especie especie;
	private Habitat habitat;
	private String genero;
	private int edad;
	private float peso;
	private boolean estadoAnimo;
	private boolean estadoSalud;
	private boolean alimentado;
	
	
	public Animal(int identificacion, Especie especie, Habitat habitat, String genero, int edad, float peso) {
		this.identificacion = identificacion;
		this.especie = especie;
		this.habitat = habitat;
		this.genero= genero;
		this.edad = edad;
		this.peso = peso;
		this.estadoAnimo = true;
		this.estadoSalud = true;
		this.alimentado = true;
		Animal.totalAnimales++;
		habitat.addAnimalesAsociados(this);
		Administracion.addAnimales(this);
		
		
	}
	
	public void setIdentificacion(int identificacion) {
		this.identificacion = identificacion;
	}
	
	public int getIdentificacion() {
		return identificacion;
	}
	
	public void setEspecie(Especie especie) {
		this.especie = especie;
	}
	
	public Especie getEspecie() {
		return especie;
	}	
	
	public void setHabitat(Habitat habitat) {
		this.habitat = habitat;
	}
	
	public Habitat getHabitat() {
		return habitat;
	}
	
	public void setGenero(String genero) {
		if(genero == "f" || genero == "m") {
			this.genero = genero;			
		}
		else {}
	}
	
	public String getGenero() {
		return genero;
	}
	
	public void setEdad(int edad) {
		this.edad = edad;
	}
	
	public int getEdad() {
		return edad;
	}
	
	public void setPeso(float peso) {
		this.peso = peso;
	}
	
	public float getPeso() {
		return peso;
	}
	
	public void setEstadoAnimo(boolean estadoAnimo) {
		this.estadoAnimo= estadoAnimo;
	}
	
	public boolean isEstadoAnimo() {
		return estadoAnimo;
	}
	
	public void setEstadoSalud(boolean estadoSalud) {
		this.estadoSalud = estadoSalud;
	}
	
	public boolean isEstadoSalud() {
		return estadoSalud;
	}
	
	public void setAlimentado(boolean alimentado) {
		this.alimentado = alimentado;
	}
	
	public boolean isAlimentado() {
		return alimentado;
	}
	
	static public void setTotalAnimales(int totalAnimales) {
		Animal.totalAnimales = totalAnimales;
	}
	
	static public int getTotalAnimales() {
		return totalAnimales;
	}
	
	public void morir() {
		Animal este=this;
		totalAnimales--;
		habitat.removeAnimalesAsociados(this);
		Administracion.removeAnimales(this);
		este = null;
		
	}
	
	public String toString() {
		return ("Identificación: " + String.valueOf(this.getIdentificacion()) + 
				"\nEspecie: " + this.getEspecie().getNombre() + 
				"\nHábitat: " + this.getHabitat() + 
				"\nGénero: " + this.getGenero() +
				"\nEdad: " + String.valueOf(this.getEdad()) +
				"\nPeso: " + String.valueOf(this.getPeso()));
	}
	
}
