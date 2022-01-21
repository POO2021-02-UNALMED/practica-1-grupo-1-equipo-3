package uiMain;

import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;
import java.io.Serializable;
import baseDatos.Deserializador;
import baseDatos.Serializador;

import java.util.Scanner;

public class Main implements Serializable {
	// Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static final long serialVersionUID = 1L;
	static Scanner sc= new Scanner(System.in);
	
	static int leerOpcion() {
		return sc.nextInt();}
	
	static String leerString() {
		return sc.next();}
	/* El método salirDelSistema() permite guardar en los archivos las listas de animales, visitantes, habitat, especies, veterinarios y cuidadores
	 * del objeto admin del tipo Administracion. */
	private static void salirDelSistema() {
		System.out.println("¡Gracias por haber usado nuestra aplicación! Vuelva pronto.\n");
		Serializador.serializar();
		System.exit(0);
	}
	
	static void continuar(){
		System.out.println("Presione \"ENTER\" para continuar...");
		Scanner continuar = new Scanner(System.in);
		continuar.nextLine();
	}
	
	public static void main(String args[]) {
		/* La siguiente línea permite cargar las listas de animales, visitantes, habitat, especies, veterinarios y cuidadores
		 * al objeto Administracion creado. */

		Deserializador.deserializar();
		// A continuación se encuentran los objetos que fueron guardados originalmente en la persistencia inicial.
/*		Administracion admin = new Administracion();
		Habitat a = new Habitat("H1", "Pradera", 2);
		Habitat b = new Habitat("H2", "Jungla", 1);
		Habitat c= new Habitat("H3", "Pantano", 3);
		Habitat d= new Habitat("H5", "Rio", 3);
		Habitat e= new Habitat("H6","Pantano",2);
		c.setLimpio(false);
		Animal a1 = new Animal(Especie.REPTIL, c, "M", 5, 70);
		Animal a2 = new Animal(Especie.REPTIL, c, "F", 4, 65);
		a1.setEstadoAnimo(false);
		a2.setEstadoAnimo(false);
		Animal a3 = new Animal(Especie.ANFIBIO,e,"M",2,20);
		Animal a4 = new Animal(Especie.ANFIBIO,e,"F",2,15);
		a3.setEstadoAnimo(false);
		a4.setEstadoAnimo(false);
		a3.setAlimentado(false);
		a4.setEstadoSalud(false);
		Animal a5 = new Animal(Especie.PEZ,d,"M",2,20);
		Animal a6 = new Animal(Especie.PEZ,d,"M",1,15);
		Animal a7 = new Animal(Especie.PEZ,d,"F",1,20);
		d.setLimpio(false);
		a5.setEstadoAnimo(false);
		a6.setEstadoAnimo(false);
		a7.setEstadoAnimo(false);
		a7.setAlimentado(false);
		a5.setAlimentado(false);
		a5.setEstadoSalud(false);
		a6.setEstadoSalud(false);
		Animal a8 = new Animal(Especie.ANFIBIO,b,"F",1,20);
		Cuidador c1 = new Cuidador("Jorge", 7000, Especie.MAMIFERO);
		Cuidador c2 = new Cuidador("Johanna", 1000, Especie.AVE);
		Cuidador c3 = new Cuidador("Camila", 100000, Especie.REPTIL);
		Cuidador c4 = new Cuidador("David", 10000, Especie.PEZ);
		Cuidador c5 = new Cuidador("Juan", 5000, Especie.ANFIBIO);
		Veterinario v1= new Veterinario("Elva",10000,Especie.ANFIBIO);
		Veterinario v2= new Veterinario("Francisco",12000,Especie.PEZ);
		Visitante vi1= new Visitante("Jose",3,15);
		Visitante vi2= new Visitante("Diego",5,30);
		Visitante vi3= new Visitante("Valeria",6,30);
*/		int opcion;
		do {
			System.out.println("\n¡Bienvenido al sistema gestor de tu Zoológico!\n");
			System.out.println("A continuación te presentamos funcionalidades disponibles:\n");
			System.out.println("1. Mantenimiento de los habitats");
			System.out.println("2. Curar a los animales");
			System.out.println("3. Cuidar a los animales");
			System.out.println("4. Gestión administrativa del Zoológico");
			System.out.println("5. Adquisición y traslado de animales");
			System.out.println("6. Otras funcionalidades");
			System.out.println("7. Salir del programa");
			System.out.print("\n¿Cuál quieres realizar? ");
			opcion=leerOpcion();
			System.out.println();
			switch(opcion) {
				case 1: FuncionalidadMantenimiento.mantenimientoHabitat(); break;
				case 2: FuncionalidadCurar.curarAnimal(); break;
				case 3: FuncionalidadCuidar.cuidarAnimal(); break;
				case 4: FuncionalidadGestion.gestionAdministrativa(); break;
				case 5: FuncionalidadAdquisicionTraslado.adquisicionTraslado(); break;
				case 6: FuncionalidadOtras.funcionalidades(); break;
				case 7: salirDelSistema(); break;
				default: System.out.println("Opción incorrecta. Solo opciones del 1 al 7."); break;}
		} while(opcion!=7);
	}
}