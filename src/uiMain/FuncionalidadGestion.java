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
		//Inicialmente se muestran los visitantes que ha tenido el zool�gico en el d�a, y luego invoca el m�todo calculoGanancias() donde muestra las ganancias obtenidas por la entrada de los visitantes, y se suman esas ganancias a la caja.
		System.out.println("El zool�gico ha recibido a "+Visitante.getTotalVisitantes()+" visitantes en el d�a de hoy, y ha obtenido ganancias por un total de "+Administracion.calculoGanancias()+"$.");
		//Se muestra el dinero con el que cuenta el zool�gico en el banco
		System.out.println("\nEn total el zool�gico dispone de "+Administracion.getCaja()+"$ de presupuesto en el banco.");
		//Se invoca el m�todo pagarEmpelados con el cual se cambia el estado de pagado de los empleados para asi indicar que ya se les pag�
		pagarEmpleados();
	}
	static void pagarEmpleados() {
		boolean estado=false;
		int identificacion=0;
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
				System.out.println("\n"+cuidador.info());
			}
			for (Veterinario veterinario:Administracion.getVeterinarios()) {
				System.out.println("\n"+veterinario.info());
			}
			System.out.println("\n�Se ha decidido por uno de los empleados? A continuaci�n ingrese el n�mero de identificaci�n del empleado que desea despedir:");
			//Se pide al usuario que ingrese la identificaci�n del empleado al que se va a despedir
			while (estado==false){
				identificacion=Main.sc.nextInt();
				//Si la identificacion corresponde a la de alg�n cuidador, invoca el m�todo de despedirCuidador de la clase Administracion para as� eliminarlo.
				for (Cuidador cuidador:Administracion.getCuidadores()) {
					identificaciones.add(cuidador.getIdentificacion());
					if (cuidador.getIdentificacion()==identificacion) {
						Administracion.despedirCuidador(identificacion);
						System.out.println(cuidador.getNombre()+" hacia parte de la n�mina de cuidadores del zool�gico. Ha sido despedido.");
						estado=true;
						break;
					}
				}
				//Si la identificacion corresponde a la de alg�n veterinario, invoca el m�todo de despedirVeterinario de la clase Administracion para as� eliminarlo.
				for (Veterinario veterinario:Administracion.getVeterinarios()) {
					identificaciones.add(veterinario.getIdentificacion());
					if (veterinario.getIdentificacion()==identificacion) {
						Administracion.despedirVeterinario(identificacion);
						System.out.println(veterinario.getNombre()+" hacia parte de la n�mina de veterinarios del zool�gico. Ha sido despedido.");
						estado=true;
						break;
					}
				}
				//En caso de que se ingrese una identificacion que no corresponde a algun empelado de la nomina,volver� a pedir la identificaci�n hasta que se ingrese una correcta
				if (identificaciones.contains(identificacion)==false) {
					System.out.println("\nNinguno de nuestros empleados tiene esa identificaci�n. Por favor vuelva a ingresar una v�lida.");
				}
			}
			System.out.println("\nCon esto el zo�gico se recuperar� econ�micamente.");
			System.out.println("\n...");
		} else { //En caso de que la caja no haya quedado negativa, no pasar� nada
			System.out.println("\nLe hemos pagado a todos los empleados. El nuevo presupuesto que dispone el zool�gico en el banco es de "+Administracion.getCaja()+"$.");
		}
	}
}