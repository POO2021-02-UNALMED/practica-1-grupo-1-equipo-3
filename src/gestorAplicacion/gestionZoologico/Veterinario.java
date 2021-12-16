package gestorAplicacion.gestionZoologico;

import gestorAplicacion.animalesZoologico.Animal;
import gestorAplicacion.animalesZoologico.Especie;

public class Veterinario extends Empleado {
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static final long serialVersionUID=1L;
    private Especie especialidad;


    public Veterinario(String nombre, int sueldo, Especie especialidad) {
        super(Administracion.getVeterinarios().size() + 1, nombre, sueldo);
        this.especialidad = especialidad;
        Administracion.addVeterinarios(this);
    }
    
    /* El método info() es implementado de la interfaz Entidad y definido aquí. Sirve para generar el String que será 
	 * usado para imprimir por consola los datos del veterinario en caso de ser requeridos en alguna de las funcionalidades 
	 * de la aplicación.
	 */
    public String info() {
        return ("Tipo de empleado: VETERINARIO" + 
				"\nIdentificación: " + String.valueOf(this.getIdentificacion()) + 
				"\nNombre: " + this.getNombre() + 
				"\nSueldo: " + String.valueOf(this.getSueldo()) + 
				"\nEspecie asignada: " + this.getEspecialidad().getNombre());
    }

    public boolean revisar(Animal animal) {
        if (animal.isEstadoSalud() == false) { return false;} 
        else {return true;}
    }

    public void curarAnimal(Animal animal) {
        animal.setEstadoSalud(true);
    }

    public Especie getEspecialidad() {
        return especialidad;
    }

    public void setEspecialidad(Especie especialidad) {
        this.especialidad = especialidad;
    }    
}
