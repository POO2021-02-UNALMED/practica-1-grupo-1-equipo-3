package gestorAplicacion.gestionZoologico;

import java.util.*;
import gestorAplicacion.animalesZoologico.*;

public class Administracion {
	static private double caja;
	static private List<Animal> animales=new ArrayList<Animal>();
	static private List<Visitante> visitantes=new ArrayList<Visitante>();
	static public List<Visitante> visitantesBoletas=new ArrayList<Visitante>();
	static private List<Habitat> habitats= new ArrayList<Habitat>();
	static private List<Especie> especies= new ArrayList<Especie>(Arrays.asList(Especie.MAMIFERO, Especie.AVE, Especie.REPTIL, Especie.PEZ, Especie.ANFIBIO));
	static private List<Veterinario> veterinarios= new ArrayList<Veterinario>();
	static private List<Cuidador> cuidadores= new ArrayList<Cuidador>();
	

	public Administracion(int caja) {
		this.caja=caja;}
	
	public static int pagoNomina() {
		int pago=0;
		for (Veterinario veterinario:veterinarios) {
			if (veterinario.isPagado()==false) {
				pago=pago+veterinario.getSueldo();
				veterinario.setPagado(true);
			}}
		for (Cuidador cuidador:cuidadores) {
			if (cuidador.isPagado()==false) {
				pago=pago+cuidador.getSueldo();
				cuidador.setPagado(true);
			}}
		caja-=pago;
		return pago;}
	
	public static void trasladarAnimal(Animal animal) {
		animal.morir();}
	
	
	public static void adquirirAnimal(int identificacion, Especie especie, Habitat habitatEspecie, String genero, int edad, float peso) {
		Animal animalAdquirido=new Animal(identificacion,especie,null,genero,edad,peso);
		especie.getCuidadorAsignado().get(0).moverAnimal(animalAdquirido,habitatEspecie);
	}
	
	public static double calculoGanancias() {
		double ganancias=0;
		for (Visitante visitante:visitantesBoletas) {
			ganancias+=visitante.getPrecioBoleta();
			visitante=null;
			}
		visitantesBoletas.clear();
		caja=caja+ganancias;
		return ganancias;}
	
	
	public void contratarCuidador() {
		
	}
	
	public void contratarVeterinario() {
		
	}

	public static void despedirCuidador(int identificacion) {
		for (Cuidador cuidador:cuidadores) {
			if (cuidador.getIdentificacion()==identificacion) {
				removeCuidadores(cuidador);
				cuidador=null;
				break;}}}
	
	public static void despedirVeterinario(int identificacion) {
		for (Veterinario veterinario:veterinarios) {
			if (veterinario.getIdentificacion()==identificacion) {
				removeVeterinarios(veterinario);
				veterinario=null;
				break;}}}
	
	public static void addAnimales(Animal nuevo) {
		animales.add(nuevo);}
	
	public static void addVisitantes(Visitante nuevo) {
		visitantes.add(nuevo);}
	
	public static void addVisitantesBoletas(Visitante nuevo) {
		visitantesBoletas.add(nuevo);}
	
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
	
	public static void removeVisitantes(Visitante eliminar) {
		visitantes.remove(visitantes.indexOf(eliminar));}
	
	public static void removeVisitantesBoletas(Visitante eliminar) {
		visitantesBoletas.remove(visitantesBoletas.indexOf(eliminar));}
	
	public static void removeHabitats(Habitat eliminar) {
		habitats.remove(habitats.indexOf(eliminar));}
	
	public static void removeEspecies(Especie eliminar) {
		especies.remove(especies.indexOf(eliminar));}
	
	public static void removeVeterinarios(Veterinario eliminar) {
		veterinarios.remove(veterinarios.indexOf(eliminar));}
	
	public static void removeCuidadores(Cuidador eliminar) {
		cuidadores.remove(cuidadores.indexOf(eliminar));}
	
	public static double getCaja() {
		return caja;}
	
	public static List<Animal> getAnimales() {
		return animales;}
	
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
	
	public static void setCaja(double nuevo) {
		caja=nuevo;}
	
	public static void setAnimales(List<Animal> nuevo) {
		animales=nuevo;}
	
	
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
