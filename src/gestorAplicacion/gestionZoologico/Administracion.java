package gestorAplicacion.gestionZoologico;

import java.util.*;
import gestorAplicacion.animalesZoologico.*;

public class Administracion {
	private double caja;
	static private List<Animal> animales=new ArrayList<Animal>();
	static private List<Empleado> empleados=new ArrayList<Empleado>();
	static private List<Visitante> visitantes=new ArrayList<Visitante>();
	static private List<Habitat> habitats= new ArrayList<Habitat>();
	static private List<Especie> especies= new ArrayList<Especie>();
	static private List<Veterinario> veterinarios= new ArrayList<Veterinario>();
	static private List<Cuidador> cuidadores= new ArrayList<Cuidador>();
	

	public Administracion(int caja) {
		this.caja=caja;}
	
	public void pagoNomina() {
		double pago=0;
		double ganancias=calculoGanancias();
		caja=caja+ganancias;
		for (Empleado empleado:empleados) {
			pago=pago+empleado.getSueldo();
		}
		caja=caja-pago;}
	
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
			Animal x=new Animal(identificacion,especie,null,genero,edad,peso);
			especie.getCuidadorAsignado().get(0).moverAnimal(x,habitatEspecie);
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
	
	public static void addEspecies(Especie nuevo) {
		especies.add(nuevo);}
	
	public static void addVeterinarios(Veterinario nuevo) {
		veterinarios.add(nuevo);}
	
	public static void addCuidadores(Cuidador nuevo) {
		cuidadores.add(nuevo);}
	
	public static void removeAnimales(Animal eliminar) {
		animales.remove(animales.indexOf(eliminar));}
	
	public static void removeEmpleados(Empleado eliminar) {
		empleados.remove(empleados.indexOf(eliminar));}
	
	public static void removeVisitantes(Visitante eliminar) {
		visitantes.remove(visitantes.indexOf(eliminar));}
	
	public static void removeHabitats(Habitat eliminar) {
		habitats.remove(habitats.indexOf(eliminar));}
	
	public static void removeEspecies(Especie eliminar) {
		especies.remove(especies.indexOf(eliminar));}
	
	public static void removeVeterinarios(Veterinario eliminar) {
		veterinarios.remove(veterinarios.indexOf(eliminar));}
	
	public static void removeCuidadores(Cuidador eliminar) {
		cuidadores.remove(cuidadores.indexOf(eliminar));}
	
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
	
	public static List<Especie> getEspecies() {
		return especies;}
	
	public static List<Veterinario> getVeterinarios() {
		return veterinarios;}
	
	public static List<Cuidador> getCuidadores() {
		return cuidadores;}
	
	public void setCaja(double nuevo) {
		caja=nuevo;}
	
	public static void setAnimales(List<Animal> nuevo) {
		animales=nuevo;}
	
	public static void setEmpleados(List<Empleado> nuevo) {
		empleados=nuevo;}
	
	public static void setVisitantes(List<Visitante> nuevo) {
		visitantes=nuevo;}
	
	public static void setHabitats(List<Habitat> nuevo) {
		habitats=nuevo;}
	
	public static void setEspecies(List<Especie> nuevo) {
		especies=nuevo;}
	
	public static void setVeterinarios(List<Veterinario> nuevo) {
		veterinarios=nuevo;}
	
	public static void setCuidadores(List<Cuidador> nuevo) {
		cuidadores=nuevo;}}
