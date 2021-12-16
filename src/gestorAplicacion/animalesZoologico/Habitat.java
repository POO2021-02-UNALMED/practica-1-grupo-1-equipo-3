package gestorAplicacion.animalesZoologico;

import java.util.ArrayList;
import gestorAplicacion.gestionZoologico.Administracion;
import gestorAplicacion.gestionZoologico.Entidad;
import java.io.Serializable;

public class Habitat implements Serializable, Entidad {
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static final long serialVersionUID=1L;
	private final int CAPACIDADMAXIMA;
	private static int totalHabitats;
	private int identificacion;
	private String nombre;
	private String ambientacion;
	private boolean limpio;
	private ArrayList<Animal> animalesAsociados = new ArrayList<Animal>();
	
	public Habitat(int identificacion, String nombre, String ambientacion, int capacidadMaxima) {
		this.identificacion = identificacion;
		this.nombre = nombre;
		this.ambientacion = ambientacion;
		this.limpio = true;
		this.CAPACIDADMAXIMA= capacidadMaxima;
		Habitat.totalHabitats++;
		Administracion.addHabitats(this);
	}
	
	/* El método info() es implementado de la interfaz Entidad y definido aquí. Sirve para generar el String que será 
	 * usado para imprimir por consola los datos del hábitat en caso de ser requeridos en alguna de las funcionalidades 
	 * de la aplicación.
	 */
	public String info() {
		return ("Identificación: " + String.valueOf(this.getIdentificacion()) +
				"\nNombre: " + this.getNombre() +
				"\nAmbientación: " + this.getAmbientacion() +
				"\nCantidad de Animales actual: " + String.valueOf(this.cantidadAnimales()) +
				"\nCapcidad Maxima : " + String.valueOf(this.getCapacidadMaxima()));
	}
	
	public int getCapacidadMaxima() {
		return CAPACIDADMAXIMA;
	}
	
	public void setIdentificacion(int identificacion) {
		this.identificacion = identificacion;
	}
	
	public int getIdentificacion() {
		return identificacion;
	}
	
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	public String getNombre() {
		return nombre;
	}
	
	public void setAmbientacion(String ambientacion) {
		this.ambientacion = ambientacion;
	}
	
	public String getAmbientacion() {
		return ambientacion;
	}
	
	public void setLimpio(boolean limpio) {
		this.limpio = limpio;
	}
	
	public boolean isLimpio() {
		return limpio;
	}
	
	public void setAnimalesAsociados(ArrayList<Animal> animalesAsociados) {
		this.animalesAsociados = animalesAsociados;
	}
	
	public ArrayList<Animal> getAnimalesAsociados(){
		return animalesAsociados;
	}
	
	public static void setTotalHabitats(int totalHabitats) {
		 Habitat.totalHabitats = totalHabitats;
	 }
	 
	 public static int getTotalAnimales() {
		 return totalHabitats;
	 }
	 
	 public int cantidadAnimales() {
		 return animalesAsociados.size();
	 }
	 
	 public void addAnimalesAsociados(Animal animal) {
		 animalesAsociados.add(animal);
	 }
	 
	 public void removeAnimalesAsociados(Animal animal){
		 animalesAsociados.remove(animalesAsociados.indexOf(animal));
	 }
	 
	/* public String toString() {
	*	String r = "Identificacion: " + identificacion  + "\nNombre: " + nombre + "\nAmbientacion: " + ambientacion + 
	*	"\nEspecie del Habitat: " + animalesAsociados.get(0).getEspecie().getNombre() + "\nCapacidad: " + CAPACIDADMAXIMA;
	*	return r;
	 *}
	 */

}
