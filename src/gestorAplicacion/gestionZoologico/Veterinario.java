// CLASE CREADA POR Juan José Monsalve Marín

/* 
La clase Veterinario se crea con la finalidad de definir los diferentes atributos y métodos de los objetos de tipo veterinario. 
En esta clase se define el atributo “especialidad” el cual corresponde a la especie que cada veterinario esta especializado 
en tratar. Se definen los métodos de “revisar”, el cual se encarga de verificar el estado de salud de los animales del 
zoológico y se define el método “curarAnimal” el cual se encarga de que se implemento los cuidados y procedimientos 
necesarios para curar al animal. Esta clase hereda de "Empleado"
*/

package gestorAplicacion.gestionZoologico;

import gestorAplicacion.animalesZoologico.Animal;
import gestorAplicacion.animalesZoologico.Especie;

public class Veterinario extends Empleado {
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static final long serialVersionUID=1L;
    private Especie especialidad;

    /*  
    Constructor de la clase Veterinario: recibe como parámetros los atributos identificación, nombre y sueldo 
    los cuales hereda de la clase empleado. Por su parte recibe el parámetro especialidad de tipo especie.
    */
    public Veterinario(int identificacion, String nombre, int sueldo, Especie especialidad) {
        super(identificacion, nombre, sueldo);
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
    El método revisar(Animal animal) es el método encargado de verificar el estado de saludo de los animales del zoológico. 
    Este método admite como parámetro un objeto de tipo “Animal” y con este verifica el estado de salud de los animales.  
    */
    public boolean revisar(Animal animal) {
        if (animal.isEstadoSalud() == false) { return false;} 
        else {return true;}
    }

    /*
    El método curarAnimal(Animal animal) se encarga de cambiar el estado de salud de un animal  del zoológico cuando se encuentra enfermo(false), 
    luego de que un veterinario realice todos los procedimientos necesarios para curar al animal. Este método admite como parámetro un objeto de tipo animal.  
    */
    public void curarAnimal(Animal animal) {
        animal.setEstadoSalud(true);
    }

    // Se definen los métodos set y get del atributo “especialidad” de tipo animal.
    public Especie getEspecialidad() {
        return especialidad;
    }

    public void setEspecialidad(Especie especialidad) {
        this.especialidad = especialidad;
    }    
}
