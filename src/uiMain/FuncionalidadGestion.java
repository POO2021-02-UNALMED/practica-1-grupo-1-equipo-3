//CLASE CREADA POR JOSÉ DAVID CARDONA

/*En esta clase se realiza la funcionalidad de la gestión administrativa del zoológico, la cual se encargará de calcular las ganancias, y pagar
 a los empleados. En caso de que en la caja haya un valor negativo, querrá decir que no había dinero suficiente para pagar a los empleados y
 fue necesario sacar un prestamo, y será necesario despedir a un empleado para que el zoológico se recupere económicamente posteriormente.
 
 Son necesarias las clases Veterinario, Cuidador, Visitante y Administración.*/



package uiMain;
import java.util.*;
import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;
public class FuncionalidadGestion {
	static void gestionAdministrativa() {
		//Inicialmente se muestran los visitantes que ha tenido el zoológico en el día, y luego invoca el método calculoGanancias() donde muestra las ganancias obtenidas por la entrada de los visitantes, y se suman esas ganancias a la caja.
		System.out.println("El zoológico ha recibido a "+Visitante.getTotalVisitantes()+" visitantes en el día de hoy, y ha obtenido ganancias por un total de "+Administracion.calculoGanancias()+"$.");
		//Se muestra el dinero con el que cuenta el zoológico en el banco
		System.out.println("\nEn total el zoológico dispone de "+Administracion.getCaja()+"$ de presupuesto en el banco.");
		//Se invoca el método pagarEmpelados con el cual se cambia el estado de pagado de los empleados para asi indicar que ya se les pagó
		pagarEmpleados();}
	
	static void pagarEmpleados() {
		boolean estado=false;
		int identificacion=0;
		List<Integer> identificaciones= new ArrayList<Integer>();
		//Se invoca el método pagoNomina de la clase administración el cual calcula cual es el monto toal a pagar, y luego este se le resta a lo que tiene el zoológico en el banco. Además cambia el atributo pagado de los empelados para así saber que ya se les pagó
		System.out.println("\nEs tiempo de pagarle a nuestros empleados. El total a pagar es de "+Administracion.pagoNomina()+"$.");
		System.out.println("\nProcederemos con el pago.");
		System.out.println("\n...");
		//En caso de que luego de realizar el pago la caja quede con un valor negativo querra decir que fue necesario sacar un prestamo para pagar a los empelados y entrará a esta condición
		if (Administracion.getCaja()<1) {
			System.out.println("\nLe informamos que no ha tenido dinero suficiente para pagar, y hemos tenido que realizar un prestamo por un valor de "+Administracion.getCaja()*-1+"$.");
			//Es necesario despedir a un empleado y para esto se muestran los empleados con lo que cuenta el zoológico.
			System.out.println("\nEs necesario despedir a alguno de nuestros empleados. A continuación le mostraremos la nómina de empleados:");
			for (Cuidador cuidador:Administracion.getCuidadores()) {
				System.out.println("\n"+cuidador.toString());}
			for (Veterinario veterinario:Administracion.getVeterinarios()) {
				System.out.println("\n"+veterinario.toString());}
			System.out.println("\n¿Se ha decidido por uno de los empleados? A continuación ingrese el número de identificación del empleado que desea despedir:");
			//Se pide al usuario que ingrese la identificación del empleado al que se va a despedir
			while (estado==false){
				identificacion=Main.sc.nextInt();
				//Si la identificacion corresponde a la de algún cuidador, invoca el método de despedirCuidador de la clase Administracion para así eliminarlo.
				for (Cuidador cuidador:Administracion.getCuidadores()) {
					identificaciones.add(cuidador.getIdentificacion());
					if (cuidador.getIdentificacion()==identificacion) {
						Administracion.despedirCuidador(identificacion);
						System.out.println(cuidador.getNombre()+" hacia parte de la nómina de cuidadores del zoológico. Ha sido despedido.");
						estado=true;
						break;}}
				//Si la identificacion corresponde a la de algún veterinario, invoca el método de despedirVeterinario de la clase Administracion para así eliminarlo.
				for (Veterinario veterinario:Administracion.getVeterinarios()) {
					identificaciones.add(veterinario.getIdentificacion());
					if (veterinario.getIdentificacion()==identificacion) {
						Administracion.despedirVeterinario(identificacion);
						System.out.println(veterinario.getNombre()+" hacia parte de la nómina de veterinarios del zoológico. Ha sido despedido.");
						estado=true;
						break;}}
				//En caso de que se ingrese una identificacion que no corresponde a algun empelado de la nomina,volverá a pedir la identificación hasta que se ingrese una correcta
				if (identificaciones.contains(identificacion)==false) {
					System.out.println("\nNinguno de nuestros empleados tiene esa identificación. Por favor vuelva a ingresar una válida.");
				}
			}
			System.out.println("\nCon esto el zoógico se recuperará económicamente.");
			System.out.println("\n...");
		} else { //En caso de que la caja no haya quedado negativa, no pasará nada
			System.out.println("\nLe hemos pagado a todos los empleados. El nuevo presupuesto que dispone el zoológico en el banco es de "+Administracion.getCaja()+"$.");}}}