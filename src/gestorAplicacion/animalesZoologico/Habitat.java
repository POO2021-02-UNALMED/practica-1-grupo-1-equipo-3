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
	
	public Habitat(String nombre, String ambientacion, int capacidadMaxima) {
		if(Administracion.getHabitats().isEmpty()) {
			this.identificacion = 1;
		} else {
			this.identificacion = Administracion.getHabitats().get(Administracion.getHabitats().size() - 1).getIdentificacion() + 1;
		}
		this.nombre = nombre;
		this.ambientacion = ambientacion;
		this.limpio = true;
		this.CAPACIDADMAXIMA= capacidadMaxima;
		Habitat.totalHabitats++;
		Administracion.addHabitats(this);
	}
	
	public Habitat(String nombre) {
		this(nombre, "Ninguna", 999);
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
				"\nCapacidad máxima : " + String.valueOf(this.getCapacidadMaxima()));
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
}
