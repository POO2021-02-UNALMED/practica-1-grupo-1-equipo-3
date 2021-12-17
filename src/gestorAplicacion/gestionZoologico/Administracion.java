//CLASE CREADA POR JOS� DAVID CARDONA

/*La clase administraci�n se crea con el fin de llevar las cuentas ec�nomicas del zool�gico, adem�s
 del conteo de todo lo que el mismo tiene. Para ello est� el atributo caja que es el dinero con el
 que cuenta el zool�gico en el banco, y los atributos de animales (Animales con los que cuenta el
 zool�gico), visitantes (Visitantes que ha tenido el zool�gico), habitats (H�bitats con los que cuenta
 el zool�gico, especies (Especies con las que cuenta el zool�gico), veterinarios (N�mina de todos
 los veterinarios con los que cuenta el zool�gico), y cuidadores (N�mina de todos los cuidadores con
 los que cuenta el zool�gico). Hay que tener en cuenta que solo puede exisir un objeto de esta clase
 pues la aplicaci�n est� dise�ada para la administraci�n de un solo zool�gico.*/

package gestorAplicacion.gestionZoologico;

import java.util.*;
import gestorAplicacion.animalesZoologico.*;
import java.io.Serializable;

public class Administracion implements Serializable {
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static final long serialVersionUID = 1L;
	static private double caja;
	static private List<Animal> animales=new ArrayList<Animal>();
	static private List<Cuidador> cuidadores= new ArrayList<Cuidador>();
	static private List<Especie> especies= new ArrayList<Especie>();
	static private List<Habitat> habitats= new ArrayList<Habitat>();
	static private List<Veterinario> veterinarios= new ArrayList<Veterinario>();
	static private List<Visitante> visitantes=new ArrayList<Visitante>(); 
	
	/*Constructor de la clase Administraci�n: Recibe como par�metro el atributo caja, el cual corresponde 
	al dinero con el que cuenta el zool�gico en el banco.*/
	public Administracion(int caja) {
		Administracion.caja=caja;}
	
	/*Sobrecarga del constructor de la clase Administracion. Se usa el this(0) para invocar el contrsuctor incial y de esa forma asignarle 0
	 a la caja*/
	public Administracion() {
		this(0);}

	/*Este m�todo no recibe par�metros y su funci�n es la de calcular el pago total para todos los empleados
	del zool�gico. Esto lo hace recorriendo las listas de trabajadores que hay (veterinarios, cuidadores) luego
	obtiene el atributo sueldo y lo suma a una variable pago. A su vez les cambia el estado del atributo pagado a true
	Luego de obtener el pago total, este se descuenta a lo que hay en la caja. 
	Tiene como retorno el valor total de pago a empleados.*/
	public static int pagoNomina() {
		int pago=0;
		List<Empleado> empleados=new ArrayList<Empleado>();
		for (Veterinario veterinario:veterinarios) {
			empleados.add(veterinario);
			}
		for (Cuidador cuidador:cuidadores) {
			empleados.add(cuidador);
			}
		for (Empleado emple:empleados) {
			if (emple.isPagado()==false) {
				pago+=emple.getSueldo();//Se emplea ligadura din�mica. Entra por m�todo de Veterrinario y Cuidador y no por el de Empleado.
				emple.setPagado(true);
			}
		}
		caja-=pago;
		return pago;}
	
	/*Este m�todo recibe como par�metro un animal y su funci�n es trasladar el animal afuera del zool�gico, por lo que
	 hace que el animal deje de existir, queda con apuntador a null, y el mismo se elimina de las listas donde estaba
	 asociado. Eso mismo lo hace el m�todo morir de la clase Animal, por tanto se invoca este m�todo.
	 No posee retorno.*/ 
	public static void trasladarAnimal(Animal animal) {
		animal.morir();}
	
	/*Este m�todo tiene como par�metros una identificaci�n, la especie, el h�bitat de la especie, el g�nero, la edad y el peso
	 del animal que se queiere adquirir y su funci�n es la de crear un objeto animal con las anteriores caracter�sticas.
	 No posee retorno. */
	public static void adquirirAnimal(Especie especie, Habitat habitatEspecie, String genero, int edad, float peso) {
		Animal animalAdquirido = new Animal(especie,habitatEspecie,genero,edad,peso);}
	
	/*Este m�todo no recibe par�metros y su funci�n es la de calcular la ganancia por d�as del zool�gico.
	 Para esto recorrera la lista de visitantes, obtendra el valor de precioBoleta y se lo sumar� a una variable
	 llamada ganancias. Esto tiene en cuenta el atributo pagado de visitantes y cambia su estado, para que no se repitan
	 ganancias.
	 Tiene como retorno el valor de las ganancias. */
	public static double calculoGanancias() {
		double ganancias=0;
		for (Visitante visitante:visitantes) {
			if (visitante.isPagado()==false) {  //Condicional agregado para que no se agreguen dos veces las ganancias, en caso de invocar seguidamente este m�todo.
				ganancias+=visitante.getPrecioBoleta();
				visitante.setPagado(true);}}
		caja=caja+ganancias;
		return ganancias;}
	
	/*Este m�todo recibe como par�metros la identificaci�n, el nombre, el sueldo y la especie del cuidador que se quiere
	 contratar y su funci�n es la creaci�n de un objeto cuidador con las caracter�sticas de los par�metros.
	 Tiene como retorno el objeto Cuidador creado.*/
	public static Cuidador contratarCuidador(String nombre, int sueldo, Especie especieAsignada) {
		Cuidador nuevo=new Cuidador(nombre,sueldo,especieAsignada);
		return nuevo;}
	
	/*Este m�todo recibe como par�metros la identificaci�n, el nombre, el sueldo y la especialidad del veterinario 
	 que se quiere contratar y su funci�n es la creaci�n de un objeto veterinario con las caracter�sticas de los 
	 par�metros.
	 Tiene como retorno el objeto veterinario creado.*/
	public static Veterinario contratarVeterinario(String nombre, int sueldo, Especie especialidad) {
		Veterinario nuevo=new Veterinario(nombre,sueldo,especialidad);
		return nuevo;}

	/*Este m�todo tiene como par�metro la idetificaci�n de un cuidador, y su funci�n es la de despedir el cuidador
	 que tenga la identificaci�n dada. Esto implica que el objeto quede apuntando a null y sea eliminado de las listas
	 donde se encuentra.
	 No posee retorno*/
	public static void despedirCuidador(int identificacion) {
		for (Cuidador cuidador:cuidadores) {
			if (cuidador.getIdentificacion()==identificacion) {
				removeCuidadores(cuidador);
				cuidador=null;
				break;
			}
		}
	}
	
	/*Este m�todo tiene como par�metro la idetificaci�n de un veterinario, y su funci�n es la de despedir al veterinario
	 que tenga la identificaci�n dada. Esto implica que el objeto quede apuntando a null y sea eliminado de las listas
	 donde se encuentra.
	 No posee retorno*/
	public static void despedirVeterinario(int identificacion) {
		for (Veterinario veterinario:veterinarios) {
			if (veterinario.getIdentificacion()==identificacion) {
				removeVeterinarios(veterinario);
				veterinario=null;
				break;}}}
	
	public static Habitat construirHabitat(String nombre, String ambientacion, int capacidad) {
		Habitat nuevo=new Habitat(nombre,ambientacion,capacidad);
		return nuevo;}
	
	/*Este m�todo tiene como par�metro un objeto animal y su funci�n es agregarlo a la lista de atributo animales.
	 No posee retorno.*/
	public static void addAnimales(Animal nuevo) {
		animales.add(nuevo);}
	
	/*Este m�todo tiene como par�metro un objeto visitante y su funci�n es agregarlo a la lista de atributo visitantes.
	 No posee retorno.*/
	public static void addVisitantes(Visitante nuevo) {
		visitantes.add(nuevo);}
	
	/*Este m�todo tiene como par�metro un objeto h�bitat y su funci�n es agregarlo a la lista de atributo h�bitats.
	 No posee retorno.*/
	public static void addHabitats(Habitat nuevo) {
		habitats.add(nuevo);}
	
	/*Este m�todo tiene como par�metro un objeto especie y su funci�n es agregarlo a la lista de atributo especies.
	 No posee retorno.*/
	public static void addEspecies(Especie nuevo) {
		especies.add(nuevo);}
	
	/*Este m�todo tiene como par�metro un objeto veterinario y su funci�n es agregarlo a la lista de atributo veterinarios.
	 No posee retorno.*/
	public static void addVeterinarios(Veterinario nuevo) {
		veterinarios.add(nuevo);}
	
	/*Este m�todo tiene como par�metro un objeto cuidador y su funci�n es agregarlo a la lista de atributo cuidadores.
	 No posee retorno.*/
	public static void addCuidadores(Cuidador nuevo) {
		cuidadores.add(nuevo);}
	
	/*Este m�todo tiene como par�metro un objeto animal y su funci�n es eliminarlo de la lista de atributo animales.
	 No posee retorno.*/
	public static void removeAnimales(Animal eliminar) {
		animales.remove(animales.indexOf(eliminar));}
	
	/*Este m�todo tiene como par�metro un objeto visitante y su funci�n es eliminarlo de la lista de atributo visitantes.
	 No posee retorno.*/
	public static void removeVisitantes(Visitante eliminar) {
		visitantes.remove(visitantes.indexOf(eliminar));}
	
	/*Este m�todo tiene como par�metro un objeto h�bitat y su funci�n es eliminarlo de la lista de atributo h�bitats.
	 No posee retorno.*/
	public static void removeHabitats(Habitat eliminar) {
		habitats.remove(habitats.indexOf(eliminar));}
	
	/*Este m�todo tiene como par�metro un objeto especie y su funci�n es eliminarlo de la lista de atributo especies.
	 No posee retorno.*/
	public static void removeEspecies(Especie eliminar) {
		especies.remove(especies.indexOf(eliminar));}
	
	/*Este m�todo tiene como par�metro un objeto veterinario y su funci�n es eliminarlo de la lista de atributo veterinarios.
	 No posee retorno.*/
	public static void removeVeterinarios(Veterinario eliminar) {
		veterinarios.remove(veterinarios.indexOf(eliminar));}
	
	/*Este m�todo tiene como par�metro un objeto cuidador y su funci�n es eliminarlo de la lista de atributo cuidadores.
	 No posee retorno.*/
	public static void removeCuidadores(Cuidador eliminar) {
		cuidadores.remove(cuidadores.indexOf(eliminar));}
	
	// DE AC� PARA ABAJO EST�N LOS M�TODOS GET Y SET
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
