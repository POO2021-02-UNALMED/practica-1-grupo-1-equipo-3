package gestorAplicacion.gestionZoologico;

import gestorAplicacion.animalesZoologico.Animal;
import gestorAplicacion.animalesZoologico.Especie;

public class Veterinario extends Empleado {
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static final long serialVersionUID=1L;
    private Especie especialidad;


    public Veterinario(int identificacion, String nombre, int sueldo, Especie especialidad) {
        super(identificacion, nombre, sueldo);
        this.especialidad = especialidad;
        especialidad.addVeterinarioAsignado(this);
        Administracion.addVeterinarios(this);
    }

    public boolean revisarAnimal(Animal animal) {
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

    @Override
    public String toString() {
        return ("Tipo de empleado: VETERINARIO" + 
				"\nIdentificaci�n: " + this.getIdentificacion() + 
				"\nNombre: " + this.getNombre() + 
				"\nSueldo: " + this.getSueldo() + 
				"\nEspecie asignada: " + this.getEspecialidad());
    }
    
}
