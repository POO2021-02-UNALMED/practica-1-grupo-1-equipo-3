// INTERFAZ CREADA POR DAVID MATEO GARC�A

/* Esta interfaz es utilidad para forzar la definici�n del m�todo info() en las clases que la implemente.
 * Las clases que implementan esta interfaz son: Cuidador, Veterinario, Visitante, Animal, Especie y Habitat. */

package gestorAplicacion.gestionZoologico;

public interface Entidad {
	String info();
}