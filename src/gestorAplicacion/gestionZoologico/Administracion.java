package gestorAplicacion.gestionZoologico;

import java.util.*;
import gestorAplicacion.animalesZoologico.*;

public class Administracion {
	private double caja;
	static private List<Animal> animales=new ArrayList<Animal>();
	static private List<Empleado> empleados=new ArrayList<Empleado>();
	static private List<Visitante> visitantes=new ArrayList<Visitante>();
	static private List<Habitat> habitats= new ArrayList<Habitat>();
	
	public Administracion(int caja) {
		this.caja=caja;}
	
	public void pagoNomina() {
		Scanner entrada=new Scanner(System.in);
		double pago=0;
		double ganancias=calculoGanancias();
		caja=caja+ganancias;
		for (Empleado empleado:empleados) {
			pago=pago+empleado.getSueldo();
		}
		caja=caja-pago;
		if (caja<0) {
			int identificacion=entrada.nextInt();
			for(Empleado empleado:empleados) {
				if (empleado.getIdentificacion()==identificacion) {
					despedirEmpleado(empleado);
					break;}}}}
	
	public void trasladarAnimal(Animal animal) {
		removeAnimales(animal);
		animal=null;}
	
	public void adquirirAnimal(Especie especie) {
		Scanner entrada=new Scanner(System.in);
		Habitat habitatEspecie=null;
		for (Animal animal:animales) {
			if (animal.getEspecie()==especie) {
				habitatEspecie=animal.getHabitat();
				break;}}
		if (habitatEspecie.cantidadAnimales()<habitatEspecie.getCapacidadMaxima()) {
			int identificacion=entrada.nextInt();
			String genero=entrada.nextLine();
			int edad=entrada.nextInt();
			float peso=entrada.nextFloat();
			String estadoA=entrada.nextLine();
			boolean estadoS=entrada.nextBoolean();
			boolean alimentado=entrada.nextBoolean();
			Animal x=new Animal(identificacion,especie,null,genero,edad,peso,estadoA,estadoS,alimentado);
			//especie.getCuidadorAsignado().get(0).moverAnimal(x,habitatEspecie);
			}
	}
	
	public double calculoGanancias() {
		double ganancias=0;
		for (Visitante visitante:visitantes) {
			ganancias=ganancias+visitante.getPrecioBoleta();
			removeVisitantes(visitante);}
		return ganancias;}
	
	public void contratarCuidador() {
		//Cuidador x=new Cuidador();
	}
	
	public void contratarVeterinario() {
		//Veterinario y=new Veterinario();
	}

	public void despedirEmpleado(Empleado empleado) {
		removeEmpleados(empleado);
		empleado=null;}
	
	public static void addAnimales(Animal nuevo) {
		animales.add(nuevo);}
	
	public static void addEmpleados(Empleado nuevo) {
		empleados.add(nuevo);}
	
	public static void addVisitantes(Visitante nuevo) {
		visitantes.add(nuevo);}
	
	public static void addHabitats(Habitat nuevo) {
		habitats.add(nuevo);}
	
	public static void removeAnimales(Animal eliminar) {
		animales.remove(animales.indexOf(eliminar));}
	
	public static void removeEmpleados(Empleado eliminar) {
		empleados.remove(empleados.indexOf(eliminar));}
	
	public static void removeVisitantes(Visitante eliminar) {
		visitantes.remove(visitantes.indexOf(eliminar));}
	
	public static void removeHabitats(Habitat eliminar) {
		habitats.remove(habitats.indexOf(eliminar));}
	
	public double getCaja() {
		return caja;}
	
	public static List<Animal> getAnimales() {
		return animales;}
	
	public static List<Empleado> getEmpleados() {
		return empleados;}
	
	public static List<Visitante> getVisitantes() {
		return visitantes;}
	
	public static List<Habitat> getHabitats() {
		return habitats;}
	
	public void setCaja(double nuevo) {
		caja=nuevo;}
	
	public static void setAnimales(List<Animal> nuevo) {
		animales=nuevo;}
	
	public static void setEmpleados(List<Empleado> nuevo) {
		empleados=nuevo;}
	
	public static void setVisitantes(List<Visitante> nuevo) {
		visitantes=nuevo;}
	
	public static void setHabitats(List<Habitat> nuevo) {
		habitats=nuevo;}}
