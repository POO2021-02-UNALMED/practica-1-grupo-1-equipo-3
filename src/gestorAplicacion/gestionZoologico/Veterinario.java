// CLASE CREADA POR JUAN JOS� MONSALVE MAR�N

/* 
La clase Veterinario se crea con la finalidad de definir los diferentes atributos y m�todos de los objetos de tipo veterinario. 
En esta clase se define el atributo "especialidad" el cual corresponde a la especie que cada veterinario esta especializado 
en tratar. Se definen los m�todos de revisar(), el cual se encarga de verificar el estado de salud de los animales del 
zool�gico y se define el m�todo curarAnimal() el cual se encarga de que se implementen los cuidados y procedimientos 
necesarios para curar al animal. Esta clase hereda de la clase Empleado
*/

package gestorAplicacion.gestionZoologico;

import gestorAplicacion.animalesZoologico.Animal;
import gestorAplicacion.animalesZoologico.Especie;

public class Veterinario extends Empleado {
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static final long serialVersionUID=1L;
    private Especie especialidad;

    /*  
    Constructor de la clase Veterinario: recibe como par�metros los atributos identificaci�n, nombre y sueldo 
    los cuales hereda de la clase empleado. Por su parte recibe el par�metro especialidad de tipo especie.
    */
    public Veterinario(String nombre, int sueldo, Especie especialidad) {
    	super((Administracion.getVeterinarios().isEmpty()) ? 1 : 
				Administracion.getVeterinarios().get(Administracion.getVeterinarios().size() - 1).getIdentificacion() + 1, 
				nombre, sueldo);
        this.especialidad = especialidad;
        Administracion.addVeterinarios(this);
    }
    
    /* El m�todo info() es implementado de la interfaz Entidad y definido aqu�. Sirve para generar el String que ser� 
	 * usado para imprimir por consola los datos del veterinario en caso de ser requeridos en alguna de las funcionalidades 
	 * de la aplicaci�n.
	 */
    public String info() {
        return ("Tipo de empleado: VETERINARIO" + 
				"\nIdentificaci�n: " + String.valueOf(this.getIdentificacion()) + 
				"\nNombre: " + this.getNombre() + 
				"\nSueldo: " + String.valueOf(this.getSueldo()) + 
				"\nEspecie asignada: " + this.getEspecialidad().getNombre());
    }
    
    /*
    El m�todo revisar(Animal animal) es el m�todo encargado de verificar el estado de saludo de los animales del zool�gico. 
    Este m�todo admite como par�metro un objeto de tipo Animal y con este verifica el estado de salud de los animales.  
    */
    public boolean revisar(Animal animal) {
        if (animal.isEstadoSalud() == false) { return false;} 
        else {return true;}
    }
    
    /*
    El m�todo curarAnimal(Animal animal) se encarga de cambiar el estado de salud de un animal  del zool�gico cuando se encuentra enfermo (false), 
    luego de que un veterinario realice todos los procedimientos necesarios para curar al animal. Este m�todo admite como par��metro un objeto de tipo animal.  
    */
    public void curarAnimal(Animal animal) {
        animal.setEstadoSalud(true);
    }
    
    // De aqu� en adelante se definen los m�todos set y get del atributo "especialidad".
    public Especie getEspecialidad() {
        return especialidad;
    }

    public void setEspecialidad(Especie especialidad) {
        this.especialidad = especialidad;
    }    
}
