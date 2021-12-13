package uiMain;
import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;
public class FuncionalidadGestion {
	static void gestionAdministrativa() {
		System.out.println("El zoológico ha recibido a"+Administracion.getVisitantes().size()+" visitantes en el día de hoy, y ha obtenido ganancias por un total de "+Administracion.calculoGanancias()+"$.");
		System.out.println("\nEn total el zoológico dispone de "+Administracion.getCaja()+"$ de presupuesto en el banco.");
		pagarEmpleados();
		System.out.print("Presione Enter para continuar...");
		Main.sc.nextLine();}
	
	static void pagarEmpleados() {
		double caja=0;
		int identificacion=0;
		System.out.println("\nEs tiempo de pagarles a nuestros empleados.");
		System.out.println("\nEl total a pagar es de "+Administracion.pagoNomina()+"$. Procederemos con el pago.");
		caja=Administracion.getCaja();
		if (caja<1) {
			System.out.println("Le informamos que no ha tenido dinero suficiente para pagar, y hemos tenido que realizar un prestamo por"+caja*-1+"$");
			System.out.println("\nEs necesario despedir a alguno de nuestros empleados. A continuación le mostraremos la nómina de empleados:");
			for (Cuidador cuidador:Administracion.getCuidadores()) {
				cuidador.toString();}
			for (Veterinario veterinario:Administracion.getVeterinarios()) {
				veterinario.toString();}
			System.out.println("\n¿Se ha decidido por uno de los empleados? A continuación ingrese el número de identificación del empleado que desea despedir:\n");
			identificacion=Main.sc.nextInt();
			for (Cuidador cuidador:Administracion.getCuidadores()) {
				if (cuidador.getIdentificacion()==identificacion) {
					Administracion.despedirCuidador(identificacion);
					System.out.println(cuidador.getNombre()+" hacia parte de la nómina de cuidadores del zoológico. Ha sido despedido.");
					break;}}
			for (Veterinario veterinario:Administracion.getVeterinarios()) {
				if (veterinario.getIdentificacion()==identificacion) {
					Administracion.despedirVeterinario(identificacion);
					System.out.println(veterinario.getNombre()+" hacia parte de la nómina de veterinarios del zoológico. Ha sido despedido.");
					break;}}
			System.out.println("\nCon esto el zoógico se recuperará económicamente.");
		} else {
			System.out.println("Le hemos pagado a todos los empleados. El nuevo presupuesto que dispone el zoológico en el banco es de "+caja+"$.");}}}
