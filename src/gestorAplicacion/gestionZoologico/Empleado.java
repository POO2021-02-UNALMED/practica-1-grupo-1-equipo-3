//CLASE CREADA POR DAVID MATEO GARC�A

/* La clase Empleado se crea con el fin de ser heredada por las clases Cuidador y Veterinario,
 * pues en esta clase se definen los atributos correspondientes a la identificaci�n del empleado, 
 * al nombre del empleado, al sueldo del empleado y a si este empleado se le ha pagado el sueldo
 * o est� a la espera de esto. Adem�s, esta clase define los m�todos get y set para dichos atributos.
 * La clase es definida como abstracta pues define el m�todo abstracto toString(), m�todo necesario
 * para visualizar los datos del empleado. 
 */

package gestorAplicacion.gestionZoologico;

public abstract class Empleado {
	private int identificacion;
	private String nombre;
	private int sueldo;
	private boolean pagado=false;
	
	
	/* Constructor de la clase Empleado: Recibe como par�metros los atributos identificaci�n, nombre 
	 * y sueldo, los cuales respectivamente corresponden a la identificaci�n �nica, nombre y sueldo 
	 * del empleado a ser creado. 
	 */
	public Empleado(int identificacion, String nombre, int sueldo) {
		this.identificacion = identificacion;
		this.nombre = nombre;
		this.sueldo = sueldo;
	}
	
	// M�todo abstracto declarado para ser definido por las clases Cuidador y Veterinario, que lo heredan.
	public abstract String toString();
	
	// DE AC� PARA ABAJO EST�N LOS M�TODOS GET Y SET
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
