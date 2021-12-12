package uiMain;
import gestorAplicacion.*;
import gestorAplicacion.gestionZoologico.Empleado;
public class FuncionalidadGestion {
	static void FuncionalidadGestion() {
		if (caja<0) {
			int identificacion=entrada.nextInt();
			for(Empleado empleado:empleados) {
				if (empleado.getIdentificacion()==identificacion) {
					despedirEmpleado(empleado);
					break;}}}}
	}
}
