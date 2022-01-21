//CLASE CREADA POR MATEO CARVAJAL.

package gestorAplicacion.animalesZoologico;

import gestorAplicacion.gestionZoologico.Administracion;
import gestorAplicacion.gestionZoologico.Entidad;
import java.io.Serializable;

public class Animal implements Serializable, Entidad {
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
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
	
	/*Constructor de la clase Animal: Recibe como parametros los atributos especie, habitat, 
	 * genero, edad y pesoque corresponden respectivamente a la especie, habitat, genero, 
	 * edad y peso del animal a crear. A los atributos estadoAnimo, estadoSalud, alimentado
	 * y identificacion se les asigna un valor automaticamente. El objeto creado va a ser 
	 * añadido a la lista de animales de la administracion mediante el medoto estatico 
	 * de la clase Adminsitracion addAnimalesAsociados(). Ademas se le sumara 1 al atributo
	 * totalAnimales para lleavr la cuenta de los animales que hay dentro del zoologico.*/
	public Animal(Especie especie, Habitat habitat, String genero, int edad, float peso) {
		if(Administracion.getAnimales().isEmpty()) {
			this.identificacion = 1;
		} else {
			this.identificacion = Administracion.getAnimales().get(Administracion.getAnimales().size() - 1).getIdentificacion() + 1;
		}
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
	
	/* El método info() es implementado de la interfaz Entidad y definido aquí. Sirve para generar el String que será 
	 * usado para imprimir por consola los datos del animal en caso de ser requeridos en alguna de las funcionalidades 
	 * de la aplicación.
	 */
	public String info() {
		return ("Identificación: " + String.valueOf(this.getIdentificacion()) + 
				"\nEspecie: " + this.getEspecie().getNombre() + 
				"\nHábitat: " + this.getHabitat().getNombre() + "(" + this.getHabitat().getAmbientacion() + ")" + 
				"\nGénero: " + this.getGenero() +
				"\nEdad: " + String.valueOf(this.getEdad()) + " años" +
				"\nPeso: " + String.valueOf(this.getPeso())) + " Kg";
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
	
	/*Este metodo elimina todas las referencias que pueden haber del objeto tipo animal y resta uno al atributo totalAnimales*/
	public void morir() {
		Animal este=this;
		totalAnimales--;
		habitat.removeAnimalesAsociados(this);
		Administracion.removeAnimales(this);
		este = null;
		
	}
}
