package gestorAplicacion.gestionZoologico;

public class Visitante {
	private int identificacion;
	private String nombre;
	private int estrato;
	private int edad;
	private double precioBoleta;
	private static int totalVisitantes;

	public Visitante(int identificacion, String nombre, int estrato, int edad) {
		this.identificacion=identificacion;
		this.nombre=nombre;
		this.estrato=estrato;
		this.edad=edad;
		totalVisitantes++;
		Administracion.addVisitantes(this);}
	
	public void salidaVisitante() {
		Visitante este=this;
		totalVisitantes--;
		Administracion.removeVisitantes(this);
		este=null;}
	
	public void calcularPrecioBoleta() {
		if (edad<15) {
			precioBoleta=10000;
			if (estrato<=3) {
				precioBoleta=precioBoleta*0.7;
			}
		}
		else {
			precioBoleta=20000;
			if (estrato<=3) {
				precioBoleta=precioBoleta*0.8;}}}	
	
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
		return totalVisitantes;}
	
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
	
	public static void setTotalVisitantes(int nuevo) {
		totalVisitantes=nuevo;}}

