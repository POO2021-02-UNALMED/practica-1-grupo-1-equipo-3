//CLASE CREADA POR DAVID MATEO GARCÍA

/* La clase Empleado se crea con el fin de ser heredada por las clases Cuidador y Veterinario,
 * pues en esta clase se definen los atributos correspondientes a la identificación del empleado, 
 * al nombre del empleado, al sueldo del empleado y a si este empleado se le ha pagado el sueldo
 * o está a la espera de esto. Además, esta clase define los métodos get y set para dichos atributos.
 * La clase es definida como abstracta pues define el método abstracto toString(), método necesario
 * para visualizar los datos del empleado. 
 */

package gestorAplicacion.gestionZoologico;

import gestorAplicacion.animalesZoologico.Animal;
import java.io.Serializable;

public abstract class Empleado implements Serializable, Entidad {
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static final long serialVersionUID=1L;
	protected int identificacion;
	protected String nombre;
	protected int sueldo;
	protected boolean pagado=false;
	
	
	/* Constructor de la clase Empleado: Recibe como parámetros los atributos identificación, nombre 
	 * y sueldo, los cuales respectivamente corresponden a la identificación única, nombre y sueldo 
	 * del empleado a ser creado. 
	 */
	public Empleado(int identificacion, String nombre, int sueldo) {
		this.identificacion = identificacion;
		this.nombre = nombre;
		this.sueldo = sueldo;
	}
	
	// Método abstracto declarado para ser definido por las clases Cuidador y Veterinario, que lo heredan.
	protected abstract boolean revisar(Animal animal);
	
	public String info() {//Para la ligadura dinámica
		return "\nIdentificación: " + String.valueOf(this.getIdentificacion()) + 
				"\nNombre: " + this.getNombre() + 
				"\nSueldo: " + String.valueOf(this.getSueldo());
	}
	
	// DE ACÁ PARA ABAJO ESTÁN LOS MÉTODOS GET Y SET
	public int getIdentificacion() {
		return this.identificacion;
	}
	
	public void setIdentificacion(int identificacion) {
		this.identificacion = identificacion;
	}
	
	public String getNombre() {
		return this.nombre;
	}
	
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	public int getSueldo() {
		return this.sueldo;
	}
	
	public void setSueldo(int sueldo) {
		this.sueldo = sueldo;
	}
	
	public boolean isPagado() {
		return pagado;
	}
	
	public void setPagado(boolean estado) {
		pagado=estado;}
}
