//CLASE CREADA POR MATEO CARVAJAL.

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
	
	
	/* El constructor de la clase Hábitat: Recibe como parámetro los atributos nombre, ambientación 
	 * y capacidad máxima, los cuales corresponden respectivamente al nombre, ambientación 
	 * y capacidad máxima del hábitat a crear. A los atributo limpio e identificación se les asigna
	 * un valor automáticamente. El objeto creado va a ser añadido a la lista de hábitats de la 
	 * administración mediante el método  estático addHabitats de la clase 	Administración y se le suma 1 al 
	 * atributo cantidadHabitats para llevar la cuenta del número de hábitats del zoológico. Aunque no es asignado
	 * a nada el atributo animalesAsociados corresponde a los animales que viven dentro del habitat.
	 *  */
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
	
	//Sobrecarga del constructor de Habitat. Especial para la creacion del habitat "Jaula".
	public Habitat(String nombre) {
		this(nombre, "Ninguna", 999);
	}
	
	/* El método info() es implementado de la interfaz Entidad y definido aquí. Sirve para generar el String que será 
	 * usado para imprimir por consola los datos del hábitat en caso de ser requeridos en alguna de las funcionalidades 
	 * de la aplicación.
	 */
	public String info() {
		String retorno;
		if (animalesAsociados.isEmpty()==true) {
			retorno="Identificación: " + String.valueOf(this.getIdentificacion()) +
					"\nNombre: " + this.getNombre() +
					"\nAmbientación: " + this.getAmbientacion() +
					"\nCantidad de Animales actual: " + String.valueOf(this.cantidadAnimales()) +
					"\nCapacidad máxima : " + String.valueOf(this.getCapacidadMaxima()) + " animales";
			return retorno;
			} else {
				retorno="Identificación: " + String.valueOf(this.getIdentificacion()) +
						"\nNombre: " + this.getNombre() +
						"\nAmbientación: " + this.getAmbientacion() +
						"\nCantidad de Animales actual: " + String.valueOf(this.cantidadAnimales()) +
						"\nCapacidad máxima : " + String.valueOf(this.getCapacidadMaxima()) + " animales"+
						"\nEspecie que lo habita: "+animalesAsociados.get(0).getEspecie().getNombre();
				return retorno;
				
			}
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
	 
	 //Método con el cual se retorna el número de animales que vieven dentro del habitat.
	 public int cantidadAnimales() {
		 return animalesAsociados.size();
	 }
	 
	 //Método con el cual se agrega objetos tipo Animal a la lista correspondiente al atributo animalesAsociados.
	 public void addAnimalesAsociados(Animal animal) {
		 animalesAsociados.add(animal);
	 }
	 
	 //Método con el cual se elimina objetos tipo Animal de la lista correspondiente al atributo animalesAsociados.
	 public void removeAnimalesAsociados(Animal animal){
		 animalesAsociados.remove(animalesAsociados.indexOf(animal));
	 }
}
