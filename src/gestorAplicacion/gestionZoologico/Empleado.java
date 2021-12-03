package gestorAplicacion.gestionZoologico;

public abstract class Empleado {
	private int identificacion;
	private String nombre;
	private int sueldo;
	
	public Empleado(int identificacion, String nombre, int sueldo) {
		this.identificacion = identificacion;
		this.nombre = nombre;
		this.sueldo = sueldo;
//		Administracion.addEmpleados(this);
	}
	
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
	
	public abstract String toString();
}
