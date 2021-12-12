package gestorAplicacion.gestionZoologico;

import gestorAplicacion.animalesZoologico.*;
import java.util.*;

public class Cuidador extends Empleado {
	private Especie especieAsignada;
	
	public Cuidador(int identificacion, String nombre, int sueldo, Especie especieAsignada) {
		super(identificacion, nombre, sueldo);
		this.especieAsignada = especieAsignada;
		Administracion.addCuidadores(this);
	}
	
	public Especie getEspecieAsignada() {
		return this.especieAsignada;
	}
	
	public void setEspecieAsignada(Especie especieAsignada) {
		this.especieAsignada = especieAsignada;
	}
	
	public String toString() {
		return ("Tipo de empleado: CUIDADOR" + 
				"\nIdentificaci�n: " + String.valueOf(this.getIdentificacion()) + 
				"\nNombre: " + this.getNombre() + 
				"\nSueldo: " + String.valueOf(this.getSueldo()) + 
				"\nEspecie asignada: " + this.getEspecieAsignada().getNombre());
	}
	
	public void alimentarAnimal(Animal animal) {
		animal.setAlimentado(true);
	}
	
	public void moverAnimal(Animal animal, Habitat lugar) {
		animal.getHabitat().removeAnimalesAsociados(animal);
		animal.setHabitat(lugar);
	}
	
	public boolean revisar(Animal animal) {
		return animal.isEstadoAnimo();
	}
	
	public boolean revisar(Habitat habitat) {
		return habitat.isLimpio();
	}

//	En el siguiente m�todo me parece un poco inutil, en t�rminos de programaci�n, mover a todos los animales para limpiar. �Acaso esto tiene alguna utilidad REAL para nuestra aplicaci�n?
	public void limpiarHabitat(Habitat habitat, Habitat jaulas) {
		List<Animal> animales = habitat.getAnimalesAsociados();
		
		for(Animal animal : animales) {
			this.moverAnimal(animal, jaulas);
		}
		
		habitat.setLimpio(true);
		
		for(Animal animal : animales) {
			this.moverAnimal(animal, habitat);
		}
	}

}
