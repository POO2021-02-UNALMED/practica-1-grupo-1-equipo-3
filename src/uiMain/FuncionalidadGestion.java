package uiMain;
import java.util.*;
import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;
public class FuncionalidadGestion {
	static void gestionAdministrativa() {
		System.out.println("El zoológico ha recibido a "+Administracion.getVisitantes().size()+" visitantes en el día de hoy, y ha obtenido ganancias por un total de "+Administracion.calculoGanancias()+"$.");
		System.out.println("\nEn total el zoológico dispone de "+Administracion.getCaja()+"$ de presupuesto en el banco.");
		pagarEmpleados();}
	
	static void pagarEmpleados() {
		boolean estado=false;
		int identificacion=0;
		List<Integer> identificaciones= new ArrayList<Integer>();
		System.out.println("\nEs tiempo de pagarle a nuestros empleados. El total a pagar es de "+Administracion.pagoNomina()+"$.");
		System.out.println("\nProcederemos con el pago.");
		System.out.println("\n...");
		if (Administracion.getCaja()<1) {
			System.out.println("\nLe informamos que no ha tenido dinero suficiente para pagar, y hemos tenido que realizar un prestamo por un valor de "+Administracion.getCaja()*-1+"$.");
			System.out.println("\nEs necesario despedir a alguno de nuestros empleados. A continuación le mostraremos la nómina de empleados:");
			for (Cuidador cuidador:Administracion.getCuidadores()) {
				System.out.println("\n"+cuidador.toString());}
			for (Veterinario veterinario:Administracion.getVeterinarios()) {
				System.out.println("\n"+veterinario.toString());}
			System.out.println("\n¿Se ha decidido por uno de los empleados? A continuación ingrese el número de identificación del empleado que desea despedir:");
			while (estado==false){
				identificacion=Main.sc.nextInt();
				for (Cuidador cuidador:Administracion.getCuidadores()) {
					identificaciones.add(cuidador.getIdentificacion());
					if (cuidador.getIdentificacion()==identificacion) {
						Administracion.despedirCuidador(identificacion);
						System.out.println(cuidador.getNombre()+" hacia parte de la nómina de cuidadores del zoológico. Ha sido despedido.");
						estado=true;
						break;}}
				for (Veterinario veterinario:Administracion.getVeterinarios()) {
					identificaciones.add(veterinario.getIdentificacion());
					if (veterinario.getIdentificacion()==identificacion) {
						Administracion.despedirVeterinario(identificacion);
						System.out.println(veterinario.getNombre()+" hacia parte de la nómina de veterinarios del zoológico. Ha sido despedido.");
						estado=true;
						break;}}
				if (identificaciones.contains(identificacion)==false) {
					System.out.println("\nNinguno de nuestros empleados tiene esa identificación. Por favor vuelva a ingresar una válida.");
				}
			}
			System.out.println("\nCon esto el zoógico se recuperará económicamente.");
			System.out.println("\n...");
		} else {
			System.out.println("\nLe hemos pagado a todos los empleados. El nuevo presupuesto que dispone el zoológico en el banco es de "+Administracion.getCaja()+"$.");}}}