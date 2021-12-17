//CLASE CREADA POR JOS� DAVID CARDONA

/*La clase visitante se crea con el fin de saber quienes son las personas que ingresan a visitar el zool�gico. Se cuenta con el atributo
 identificacion, nombre, estrato socioecon�mico, edad, precio boleta, el atributo est�tico totalVisitantes que lleva cuentas del n�mero
 de visitantes que han ingresado el zool�gico y el atributo pagado para saber si ya pag� su boleta (Necesario en el m�todo calcularGanancias
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

	/*Constructor de la clase Visitante que recibe como par�metros la identificaci�n, el nombre, el estrato y la edad del visitante.*/
	public Visitante(String nombre, int estrato, int edad) {
		if(Administracion.getVisitantes().isEmpty()) {
			this.identificacion = 1;
		} else {
			this.identificacion = Administracion.getVisitantes().get(Administracion.getVisitantes().size() - 1).getIdentificacion() + 1;
		}
		this.nombre=nombre;
		this.estrato=estrato;
		this.edad=edad;
		precioBoleta=calcularPrecioBoleta(); //El atributo de precio boleta est� dado por el m�todo calcularPrecioBoleta
		Administracion.addVisitantes(this); //Cada que se crea un objeto visitante, se agrega al atributo visitantes de la clase adminitracion. Necesario para el calculo de ganancias
	}
		
	/* El m�todo info() es implementado de la interfaz Entidad y definido aqu�. Sirve para generar el String que ser� 
	 * usado para imprimir por consola los datos del visitante en caso de ser requeridos en alguna de las funcionalidades 
	 * de la aplicaci�n.
	 */
	public String info() {
        return ("Identificaci�n: " + String.valueOf(this.getIdentificacion()) + 
				"\nNombre: " + this.getNombre() + 
				"\nEstrato: " + String.valueOf(this.getEstrato()) + 
				"\nEdad: " + String.valueOf(this.getEdad()) +
				"\nPrecio de boleta: " + String.valueOf(this.getPrecioBoleta()));
    }
	
	/*Este m�todo no recibe par�metros y su funci�n es la destrucci�n del objeto visitante que lo invoc� con el proposito de indicar que sali�
	 del zool�gico. Elimina a ese objeto de la lista de visitantes solo cuando halla pagado el precio de su boleta.
	 No tiene ning�n retorno.*/
	public void salidaVisitante() {
		if (pagado==true) {
			Visitante este=this;
			Administracion.removeVisitantes(this);
			este=null;}
		}
	
	/*Este metodo no recibe par�metros y su funci�n es la de calcular el atributo precioBoleta del visitante. Para esto es tenido en cuenta el
	 estrato y la edad; Dependiendo de los valores en estos dos par�metros, el precio variar�.
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
	
	// DE AC� PARA ABAJO ES�N LOS M�TODOS GET Y SET
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

