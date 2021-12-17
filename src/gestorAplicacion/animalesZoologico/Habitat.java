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
	
	
	/* El constructor de la clase H�bitat: Recibe como par�metro los atributos nombre, ambientaci�n 
	 * y capacidad m�xima, los cuales corresponden respectivamente al nombre, ambientaci�n 
	 * y capacidad m�xima del h�bitat a crear. A los atributo limpio e identificaci�n se les asigna
	 * un valor autom�ticamente. El objeto creado va a ser a�adido a la lista de h�bitats de la 
	 * administraci�n mediante el m�todo  est�tico addHabitats de la clase 	Administraci�n y se le suma 1 al 
	 * atributo cantidadHabitats para llevar la cuenta del n�mero de h�bitats del zool�gico. Aunque no es asignado
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
	
	/* El m�todo info() es implementado de la interfaz Entidad y definido aqu�. Sirve para generar el String que ser� 
	 * usado para imprimir por consola los datos del h�bitat en caso de ser requeridos en alguna de las funcionalidades 
	 * de la aplicaci�n.
	 */
	public String info() {
		String retorno;
		if (animalesAsociados.isEmpty()==true) {
			retorno="Identificaci�n: " + String.valueOf(this.getIdentificacion()) +
					"\nNombre: " + this.getNombre() +
					"\nAmbientaci�n: " + this.getAmbientacion() +
					"\nCantidad de Animales actual: " + String.valueOf(this.cantidadAnimales()) +
					"\nCapacidad m�xima : " + String.valueOf(this.getCapacidadMaxima()) + " animales";
			return retorno;
			} else {
				retorno="Identificaci�n: " + String.valueOf(this.getIdentificacion()) +
						"\nNombre: " + this.getNombre() +
						"\nAmbientaci�n: " + this.getAmbientacion() +
						"\nCantidad de Animales actual: " + String.valueOf(this.cantidadAnimales()) +
						"\nCapacidad m�xima : " + String.valueOf(this.getCapacidadMaxima()) + " animales"+
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
	 
	 //M�todo con el cual se retorna el n�mero de animales que vieven dentro del habitat.
	 public int cantidadAnimales() {
		 return animalesAsociados.size();
	 }
	 
	 //M�todo con el cual se agrega objetos tipo Animal a la lista correspondiente al atributo animalesAsociados.
	 public void addAnimalesAsociados(Animal animal) {
		 animalesAsociados.add(animal);
	 }
	 
	 //M�todo con el cual se elimina objetos tipo Animal de la lista correspondiente al atributo animalesAsociados.
	 public void removeAnimalesAsociados(Animal animal){
		 animalesAsociados.remove(animalesAsociados.indexOf(animal));
	 }
}
