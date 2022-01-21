//CLASE CREADA POR JOSÉ DAVID CARDONA

/*En esta clase se realiza la funcionalidad de la gestión administrativa del zoológico, la cual se encargará de calcular las ganancias, y pagar
 a los empleados. En caso de que en la caja haya un valor negativo, querrá decir que no había dinero suficiente para pagar a los empleados y
 fue necesario sacar un prestamo, y será necesario despedir a un empleado para que el zoológico se recupere económicamente posteriormente.
 
 Son necesarias las clases Veterinario, Cuidador, Visitante y Administración.*/

package uiMain;

import java.util.*;
import gestorAplicacion.gestionZoologico.*;

public class FuncionalidadGestion {
	static void gestionAdministrativa() {
		if (Administracion.calculoGanancias()==0 && Administracion.pagoNomina()==0) {
			System.out.println("Ya fueron calculadas las ganancias por el día de hoy, y todos nuestro empleados han recibido su paga.");
			System.out.println();
			Main.continuar();
		} else {
		//Inicialmente se muestran los visitantes que ha tenido el zoológico en el día, y luego invoca el método calculoGanancias() donde muestra las ganancias obtenidas por la entrada de los visitantes, y se suman esas ganancias a la caja.
		System.out.println("El zoológico ha recibido a "+Visitante.getTotalVisitantes()+" visitantes en el día de hoy, y ha obtenido ganancias por un total de "+sumaBoletas()+"$.");
		//Se muestra el dinero con el que cuenta el zoológico en el banco
		System.out.println("\nEn total el zoológico dispone de "+Administracion.getCaja()+"$ de presupuesto en el banco.");
		//Se invoca el método pagarEmpelados con el cual se cambia el estado de pagado de los empleados para asi indicar que ya se les pagó
		pagarEmpleados();}
	
	}
	static double sumaBoletas() {
		double respuesta=0;
		for (Visitante visi:Administracion.getVisitantes()) {
			respuesta+=visi.getPrecioBoleta();
		}
		return respuesta;
	}
	static void pagarEmpleados() {
		boolean estado=false;
		int identificacion=0;
		int opcion=0;
		List<Empleado> empleados=new ArrayList<Empleado>();
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
				empleados.add(cuidador);
			}
			for (Veterinario veterinario:Administracion.getVeterinarios()) {
				empleados.add(veterinario);
			}
			for (Empleado empleado:empleados) {
				System.out.println("\n"+empleado.info());
			}
			System.out.println("\n¿Se ha decidido por uno de los empleados? Elija una de las siguientes opciones: ");
			System.out.println();
			System.out.println("1. Despedir a un Cuidador");
			System.out.println("2. Despedir a un Veterinario");
			System.out.println();
			System.out.println("Ingrese su opción: ");
			opcion = Main.leerOpcion();
			System.out.println();
			switch(opcion) {
				case 1:{
					despedirCuidador();break;
				}
				case 2:{
					despedirVeterinario();break;
				}default: System.out.println("OPCIÓN INCORRECTA: Solo opciones 1 y 2."); break;
			}
			//Se pide al usuario que ingrese la identificación del empleado al que se va a despedir
			
			
		} else { //En caso de que la caja no haya quedado negativa, no pasará nada
			System.out.println("\nLe hemos pagado a todos los empleados. El nuevo presupuesto que dispone el zoológico en el banco es de "+Administracion.getCaja()+"$.");
			System.out.println();
			Main.continuar();
		}
	}
	
	static void despedirCuidador() {
		int id;
		boolean estado=false;
		List<Integer> identificaciones= new ArrayList<Integer>();
		System.out.println("A continuación ingrese el número de identificación del cuidador:" );
		while (estado==false){
			id=Main.sc.nextInt();
			for (Cuidador cuidador:Administracion.getCuidadores()) {
				identificaciones.add(cuidador.getIdentificacion());
				if (cuidador.getIdentificacion()==id) {
					Administracion.despedirCuidador(id);
					System.out.println(cuidador.getNombre()+" hacia parte de la nómina de cuidadores del zoológico. Ha sido despedid@.");
					System.out.println("\nCon esto el zoógico se recuperará económicamente.");
					System.out.println();
					Main.continuar();
					estado=true;
					break;
				}
			}
			//En caso de que se ingrese una identificacion que no corresponde a algun empelado de la nomina,volverá a pedir la identificación hasta que se ingrese una correcta
			if (identificaciones.contains(id)==false) {
				System.out.println("\nNinguno de nuestros cuidadores tiene esa identificación. Por favor vuelva a ingresar una identificación válida.");
			}
		}
	}
	
	static void despedirVeterinario() {
		int id;
		boolean estado=false;
		List<Integer> identificaciones= new ArrayList<Integer>();
		System.out.println("A continuación ingrese el número de identificación del veterinario:" );
		while (estado==false){
			id=Main.sc.nextInt();
			for (Veterinario veterinario:Administracion.getVeterinarios()) {
				identificaciones.add(veterinario.getIdentificacion());
				if (veterinario.getIdentificacion()==id) {
					Administracion.despedirVeterinario(id);
					System.out.println(veterinario.getNombre()+" hacia parte de la nómina de veterinarios del zoológico. Ha sido despedid@.");
					System.out.println("\nCon esto el zoógico se recuperará económicamente.");
					System.out.println();
					Main.continuar();
					estado=true;
					break;
				}
			}
			//En caso de que se ingrese una identificacion que no corresponde a algun empelado de la nomina,volverá a pedir la identificación hasta que se ingrese una correcta
			if (identificaciones.contains(id)==false) {
				System.out.println("\nNinguno de nuestros veterinarios tiene esa identificación. Por favor vuelva a ingresar una identificación válida.");
			}
		}
	}
}