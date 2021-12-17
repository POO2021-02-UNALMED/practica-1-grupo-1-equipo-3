//CLASE CREADA POR JOS� DAVID CARDONA

/*En esta clase se realiza la funcionalidad de la gesti�n administrativa del zool�gico, la cual se encargar� de calcular las ganancias, y pagar
 a los empleados. En caso de que en la caja haya un valor negativo, querr� decir que no hab�a dinero suficiente para pagar a los empleados y
 fue necesario sacar un prestamo, y ser� necesario despedir a un empleado para que el zool�gico se recupere econ�micamente posteriormente.
 
 Son necesarias las clases Veterinario, Cuidador, Visitante y Administraci�n.*/

package uiMain;

import java.util.*;
import gestorAplicacion.gestionZoologico.*;

public class FuncionalidadGestion {
	static void gestionAdministrativa() {
		if (Administracion.calculoGanancias()==0 && Administracion.pagoNomina()==0) {
			System.out.println("Ya fueron calculadas las ganancias por el d�a de hoy, y todos nuestro empleados han recibido su paga.");
			System.out.println();
			Main.continuar();
		} else {
		//Inicialmente se muestran los visitantes que ha tenido el zool�gico en el d�a, y luego invoca el m�todo calculoGanancias() donde muestra las ganancias obtenidas por la entrada de los visitantes, y se suman esas ganancias a la caja.
		System.out.println("El zool�gico ha recibido a "+Visitante.getTotalVisitantes()+" visitantes en el d�a de hoy, y ha obtenido ganancias por un total de "+sumaBoletas()+"$.");
		//Se muestra el dinero con el que cuenta el zool�gico en el banco
		System.out.println("\nEn total el zool�gico dispone de "+Administracion.getCaja()+"$ de presupuesto en el banco.");
		//Se invoca el m�todo pagarEmpelados con el cual se cambia el estado de pagado de los empleados para asi indicar que ya se les pag�
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
		//Se invoca el m�todo pagoNomina de la clase administraci�n el cual calcula cual es el monto toal a pagar, y luego este se le resta a lo que tiene el zool�gico en el banco. Adem�s cambia el atributo pagado de los empelados para as� saber que ya se les pag�
		System.out.println("\nEs tiempo de pagarle a nuestros empleados. El total a pagar es de "+Administracion.pagoNomina()+"$.");
		System.out.println("\nProcederemos con el pago.");
		System.out.println("\n...");
		//En caso de que luego de realizar el pago la caja quede con un valor negativo querra decir que fue necesario sacar un prestamo para pagar a los empelados y entrar� a esta condici�n
		if (Administracion.getCaja()<1) {
			System.out.println("\nLe informamos que no ha tenido dinero suficiente para pagar, y hemos tenido que realizar un prestamo por un valor de "+Administracion.getCaja()*-1+"$.");
			//Es necesario despedir a un empleado y para esto se muestran los empleados con lo que cuenta el zool�gico.
			System.out.println("\nEs necesario despedir a alguno de nuestros empleados. A continuaci�n le mostraremos la n�mina de empleados:");
			for (Cuidador cuidador:Administracion.getCuidadores()) {
				empleados.add(cuidador);
			}
			for (Veterinario veterinario:Administracion.getVeterinarios()) {
				empleados.add(veterinario);
			}
			for (Empleado empleado:empleados) {
				System.out.println("\n"+empleado.info());
			}
			System.out.println("\n�Se ha decidido por uno de los empleados? Elija una de las siguientes opciones: ");
			System.out.println();
			System.out.println("1. Despedir a un Cuidador");
			System.out.println("2. Despedir a un Veterinario");
			System.out.println();
			System.out.println("Ingrese su opci�n: ");
			opcion = Main.leerOpcion();
			System.out.println();
			switch(opcion) {
				case 1:{
					despedirCuidador();break;
				}
				case 2:{
					despedirVeterinario();break;
				}default: System.out.println("OPCI�N INCORRECTA: Solo opciones 1 y 2."); break;
			}
			//Se pide al usuario que ingrese la identificaci�n del empleado al que se va a despedir
			
			
		} else { //En caso de que la caja no haya quedado negativa, no pasar� nada
			System.out.println("\nLe hemos pagado a todos los empleados. El nuevo presupuesto que dispone el zool�gico en el banco es de "+Administracion.getCaja()+"$.");
			System.out.println();
			Main.continuar();
		}
	}
	
	static void despedirCuidador() {
		int id;
		boolean estado=false;
		List<Integer> identificaciones= new ArrayList<Integer>();
		System.out.println("A continuaci�n ingrese el n�mero de identificaci�n del cuidador:" );
		while (estado==false){
			id=Main.sc.nextInt();
			for (Cuidador cuidador:Administracion.getCuidadores()) {
				identificaciones.add(cuidador.getIdentificacion());
				if (cuidador.getIdentificacion()==id) {
					Administracion.despedirCuidador(id);
					System.out.println(cuidador.getNombre()+" hacia parte de la n�mina de cuidadores del zool�gico. Ha sido despedid@.");
					System.out.println("\nCon esto el zo�gico se recuperar� econ�micamente.");
					System.out.println();
					Main.continuar();
					estado=true;
					break;
				}
			}
			//En caso de que se ingrese una identificacion que no corresponde a algun empelado de la nomina,volver� a pedir la identificaci�n hasta que se ingrese una correcta
			if (identificaciones.contains(id)==false) {
				System.out.println("\nNinguno de nuestros cuidadores tiene esa identificaci�n. Por favor vuelva a ingresar una identificaci�n v�lida.");
			}
		}
	}
	
	static void despedirVeterinario() {
		int id;
		boolean estado=false;
		List<Integer> identificaciones= new ArrayList<Integer>();
		System.out.println("A continuaci�n ingrese el n�mero de identificaci�n del veterinario:" );
		while (estado==false){
			id=Main.sc.nextInt();
			for (Veterinario veterinario:Administracion.getVeterinarios()) {
				identificaciones.add(veterinario.getIdentificacion());
				if (veterinario.getIdentificacion()==id) {
					Administracion.despedirVeterinario(id);
					System.out.println(veterinario.getNombre()+" hacia parte de la n�mina de veterinarios del zool�gico. Ha sido despedid@.");
					System.out.println("\nCon esto el zo�gico se recuperar� econ�micamente.");
					System.out.println();
					Main.continuar();
					estado=true;
					break;
				}
			}
			//En caso de que se ingrese una identificacion que no corresponde a algun empelado de la nomina,volver� a pedir la identificaci�n hasta que se ingrese una correcta
			if (identificaciones.contains(id)==false) {
				System.out.println("\nNinguno de nuestros veterinarios tiene esa identificaci�n. Por favor vuelva a ingresar una identificaci�n v�lida.");
			}
		}
	}
}