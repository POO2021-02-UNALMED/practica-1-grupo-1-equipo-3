//CLASE CREADA POR JOSÉ DAVID CARDONA

/*La clase visitante se crea con el fin de saber quienes son las personas que ingresan a visitar el zoológico. Se cuenta con el atributo
 identificacion, nombre, estrato socioeconómico, edad, precio boleta, el atributo estático totalVisitantes que lleva cuentas del número
 de visitantes que han ingresado el zoológico y el atributo pagado para saber si ya pagó su boleta (Necesario en el método calcularGanancias
 de la clase Administracion para no sumar varias veces el precio de la boleta de un mismo visitante)*/

package gestorAplicacion.gestionZoologico;

import java.io.Serializable;

public class Visitante implements Serializable, Entidad {
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static final long serialVersionUID=1L;
	private int identificacion;
	private String nombre;
	private int estrato;
	private int edad;
	private double precioBoleta;
	private boolean pagado=false;

	/*Constructor de la clase Visitante que recibe como parámetros la identificación, el nombre, el estrato y la edad del visitante.*/
	public Visitante(String nombre, int estrato, int edad) {
		if(Administracion.getVisitantes().isEmpty()) {
			this.identificacion = 1;
		} else {
			this.identificacion = Administracion.getVisitantes().get(Administracion.getVisitantes().size() - 1).getIdentificacion() + 1;
		}
		this.nombre=nombre;
		this.estrato=estrato;
		this.edad=edad;
		precioBoleta=calcularPrecioBoleta(); //El atributo de precio boleta está dado por el método calcularPrecioBoleta
		Administracion.addVisitantes(this); //Cada que se crea un objeto visitante, se agrega al atributo visitantes de la clase adminitracion. Necesario para el calculo de ganancias
	}
		
	/* El método info() es implementado de la interfaz Entidad y definido aquí. Sirve para generar el String que será 
	 * usado para imprimir por consola los datos del visitante en caso de ser requeridos en alguna de las funcionalidades 
	 * de la aplicación.
	 */
	public String info() {
        return ("Identificación: " + String.valueOf(this.getIdentificacion()) + 
				"\nNombre: " + this.getNombre() + 
				"\nEstrato: " + String.valueOf(this.getEstrato()) + 
				"\nEdad: " + String.valueOf(this.getEdad()) +
				"\nPrecio de boleta: " + String.valueOf(this.getPrecioBoleta()));
    }
	
	/*Este método no recibe parámetros y su función es la destrucción del objeto visitante que lo invocó con el proposito de indicar que salió
	 del zoológico. Elimina a ese objeto de la lista de visitantes solo cuando halla pagado el precio de su boleta.
	 No tiene ningún retorno.*/
	public void salidaVisitante() {
		if (pagado==true) {
			Visitante este=this;
			Administracion.removeVisitantes(this);
			este=null;}
		}
	
	/*Este metodo no recibe parámetros y su función es la de calcular el atributo precioBoleta del visitante. Para esto es tenido en cuenta el
	 estrato y la edad; Dependiendo de los valores en estos dos parámetros, el precio variará.
	 Tiene como retorno el valor de precioBoleta */ 
	public double calcularPrecioBoleta() {
		if (edad<15) {
			precioBoleta=10000;
			if (estrato<=3) {
				precioBoleta=precioBoleta*0.7;
			}
		}
		else {
			precioBoleta=20000;
			if (estrato<=3) {
				precioBoleta=precioBoleta*0.8;}
			}
		return precioBoleta;}	
	
	// DE ACÁ PARA ABAJO ESÁN LOS MÉTODOS GET Y SET
	public int getIdentificacion() {
		return identificacion;}
	
	public String getNombre() {
		return nombre;}
	
	public int getEstrato() {
		return estrato;}
	
	public int getEdad() {
		return edad;}
	
	public double getPrecioBoleta() {
		return precioBoleta;}
	
	public static int getTotalVisitantes() {
		return Administracion.getVisitantes().size();}
	
	public boolean isPagado() {
		return pagado;}
	
	public void setIdentificacion(int nuevo) {
		identificacion=nuevo;}
	
	public void setNombre(String nuevo) {
		nombre=nuevo;}
	
	public void setEstrato(int nuevo) {
		estrato=nuevo;}
	
	public void setEdad(int nuevo) {
		edad=nuevo;}
	
	public void setPrecioBoleta(double nuevo) {
		precioBoleta=nuevo;}
	
	public void setPagado(boolean nuevo) {
		pagado=nuevo;}}

