// CLASE CREADA POR DAVID MATEO GARC�A

/* La clase Cuidador se crea con el fin de manejar los objetos correspondientes a los cuidadores 
 * del zool�gico. En esta clase se define el atributo especieAsignada, correspondiente a la especie 
 * que el cuidador tiene asignada. Adem�s se definen los m�todos get y set para ese atributo y los 
 * m�todos necesarios para implementar las funcionalidades que requieran de alg�n cuidador. 
 */

package gestorAplicacion.gestionZoologico;

import gestorAplicacion.animalesZoologico.*;
import java.util.*;

public class Cuidador extends Empleado {
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static final long serialVersionUID=1L;
	private Especie especieAsignada;
	
	/* Constructor de la clase Cuidador: Recibe como par�metros los atributos identificaci�n, nombre, sueldo 
	 * y especieAsignada, los cuales respectivamente corresponden a la identificaci�n �nica, nombre, sueldo 
	 * y especieAsignada del cuidador a ser creado. Los primeros tres atributos son pasados a la clase padre 
	 * de esta clase, la clase Empleado, y el cuarto se asigna normalmente al cuidador creado. Luego se relaciona 
	 * con al objeto de la especie asignada al cuidador dicho objeto cuidador, e igualmente el cuidador se asocia 
	 * con el objeto �nico de tipo Administracion, esto a trav�s de las listas que estas clases manejan y por medio
	 * de los m�todos addCuidadorAsignado de la clase Especie y addCuidadores de la clase Administracion. 
	 */
	public Cuidador(String nombre, int sueldo, Especie especieAsignada) {
		super((Administracion.getCuidadores().isEmpty()) ? 1 : 
				Administracion.getCuidadores().get(Administracion.getCuidadores().size() - 1).getIdentificacion() + 1, 
				nombre, sueldo);
		this.especieAsignada = especieAsignada;
		Administracion.addCuidadores(this);
	}

	
	
	/* El m�todo info() es implementado de la interfaz Entidad y definido aqu�. Sirve para generar el String que ser� 
	 * usado para imprimir por consola los datos del cuidador en caso de ser requeridos en alguna de las funcionalidades 
	 * de la aplicaci�n.
	 */
	public String info() {
		return ("Tipo de empleado: CUIDADOR" + 
				"\nIdentificaci�n: " + String.valueOf(this.getIdentificacion()) + 
				"\nNombre: " + this.getNombre() + 
				"\nSueldo: " + String.valueOf(this.getSueldo()) + 
				"\nEspecie asignada: " + this.getEspecieAsignada().getNombre());
	}
	
	/* El m�todo alimentarAnimal() simplemente cambia a true el estado del atributo "alimentado" del objeto tipo Animal 
	 * que se le pasa como par�metro.
	 */
	public void alimentarAnimal(Animal animal) {
		animal.setAlimentado(true);
	}
	
	/* El m�todo moverAnimal() recibe como primer par�metro el objeto tipo Animal que el cuidador debe mover y como 
	 * segundo par�metro el h�bitat al que ser� movido dicho objeto animal. Con estos par�metros el m�todo se encarga
	 * de cortar la relaci�n entre el animal y su anterior h�bitat por medio del atributo de lista "animalesAsociados" 
	 * de la clase Habitat, para luego asignar al animal su nuevo h�bitat, correspondiente al pasado como par�metro.
	 */
	public void moverAnimal(Animal animal, Habitat lugar) {
		animal.getHabitat().removeAnimalesAsociados(animal);
		animal.setHabitat(lugar);
		lugar.addAnimalesAsociados(animal);
	}
	
	/* Este m�todo revisar() es heredado de la clase abstracta padre Empleado y definido aqu�, adem�s que aplica la 
	 * sobrecarga de m�todos. La siguiente es la primera definici�n del m�todo, que recibe como par�metro un objeto 
	 * tipo Animal y que en base a ese objeto retorna su atributo "estadoAnimo".
	 */
	public boolean revisar(Animal animal) {
		return animal.isEstadoAnimo();
	}
	
	/* La siguiente es la segunda definici�n del m�todo sobrecargado, que recibe como par�metro un objeto tipo Habitat 
	 * y que en base a ese objeto retorna su atributo "limpio".
	 */
	public boolean revisar(Habitat habitat) {
		return habitat.isLimpio();
	}
	
	/* El siguiente m�todo limpiarHabitat() recibo como primer par�metro el objeto tipo Habitat a limpiar y como segundo
	 * par�metro el objeto tipo Habitat correspondiente al h�bitat/zona a donde ser�n movidos los animales durante la
	 * limpieza. El m�todo consiste en que, de acuerdo a los objetos tipo Animal almacenados en el atributo de lista
	 * "animalesAsociados" del objeto tipo Habitat que se pas� como primer par�metro, los animales son movidos por el
	 * objeto tipo Cuidador sobre el cual se est� invocando el m�todo a un h�bitat temporal pasado como segundo par�metro, 
	 * esto para cambiar el estado del atributo "limpio" del h�bitat que se pas� como primer par�metro a true y regresar
	 * a los animales a dicho h�bitat.
	 */
	public void limpiarHabitat(Habitat habitat, Habitat jaulas) {
		List<Animal> animales = habitat.getAnimalesAsociados();
		
		for(Animal animal : animales) {
			this.moverAnimal(animal, jaulas);
		}
		
		habitat.setLimpio(true);
		
		for(Animal animal : animales) {
			/* El siguiente if se encarga, para cada animal, de cambiar su atributo de "estadoAnimo" a true en caso que los dos 
			 * atributos de esta clase necesarios para este cambio se encuentren en true, o sea, "alimentado" y "estadoSalud".
			 * Otro atributo requerido para esto es el atributo "limpio" relacionado con el h�bitat con que dicho animal est�
			 * asociado, que en este caso se asume como true pues el h�bitat acabe de ser limpiado.
			 */
			if(animal.isAlimentado() && animal.isEstadoSalud()) {
				animal.setEstadoAnimo(true);
			}
			this.moverAnimal(animal, habitat);
		}
	}
	
	// DE AC� PARA ABAJO EST�N LOS M�TODOS GET Y SET
	public Especie getEspecieAsignada() {
		return this.especieAsignada;
	}
	
	public void setEspecieAsignada(Especie especieAsignada) {
		this.especieAsignada = especieAsignada;
	}
}
