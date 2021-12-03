package gestorAplicacion.gestionZoologico;

import gestorAplicacion.animalesZoologico.*;
import java.util.*;

public class Cuidador extends Empleado {
	private Especie especieAsignada;
	
	public Cuidador(int identificacion, String nombre, int sueldo, Especie especieAsignada) {
		super(identificacion, nombre, sueldo);
		this.especieAsignada = especieAsignada;
	}
	
	public Especie getEspecieAsignada() {
		return this.especieAsignada;
	}
	
	public void setEspecieAsignada(Especie especieAsignada) {
		this.especieAsignada = especieAsignada;
	}
	
	public String toString() {
		return ("Tipo de empleado: CUIDADOR" + 
				"\nIdentificación: " + this.getIdentificacion() + 
				"\nNombre: " + this.getNombre() + 
				"\nSueldo: " + this.getSueldo() + 
				"\nEspecie asignada: " + this.getEspecieAsignada());
	}
/*	
	public void alimentarAnimal(Animal animal) {
		animal.setAlimentado(true);
	}
	
	public void moverAnimal(Animal animal, Habitat lugar) {
		animal.getHabitat().removeAnimalesAsociados(animal);
		animal.setHabitat(lugar);
	}
	
	public String revisar(Animal animal) {
		return animal.getEstadoAnimo;
	}
	
	public boolean revisar(Habitat habitat) {
		return habitat.getLimpio();
	}

//	En el siguiente método me parece un poco inutil, en términos de programación, mover a todos los animales para limpiar. ¿Acaso esto tiene alguna utilidad REAL para nuestra aplicación?
	public void limpiarHabitat(Habitat habitat) {
		List<Animal> animales = habitat.getAnimalesAsociados();
		
		for(Animal animal : animales) {
			this.moverAnimal(animal, jaulas);
		}
		
		habitat.setLimpio(true);
		
		for(Animal animal : animales) {
			this.moverAnimal(animal, habitat);
		}
	}
*/
}
