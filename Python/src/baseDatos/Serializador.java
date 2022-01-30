package baseDatos;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;

import gestorAplicacion.gestionZoologico.Administracion;

public class Serializador {
	// Este atributo es para definir la ruta al directorio temp que contiene las clases.
	private static File rutaTemp = new File("src\\baseDatos\\temp");
	
	// El método serializar(...) es el encargado de serializar las listas de todos los objetos que están en la clase Administracion
	public static void serializar() {
		FileOutputStream fos;
		ObjectOutputStream oos;
		File [] archivos = rutaTemp.listFiles();
		PrintWriter pw;
		
		/* El siguiente ciclo for borra el contenido de los archivos al momento de guardar los objetos, esto para evitar que haya
		 * reduncancia en los archivos y futuras complicaciones para buscar. */
		for(File archivo : archivos) {
			try {
				/* Al crear el siguiente objeto tipo PrintWriter y pasarle como parámetro la ruta de cada archivo, borrará lo
				 * que haya en cada archivo automáticamente. */
				pw = new PrintWriter(archivo);
			} catch (FileNotFoundException excepcion) {
				excepcion.printStackTrace();
			}
		}
		
		for(File archivo : archivos) {
			if (archivo.getAbsolutePath().contains("administracion")) {
				try {
					fos = new FileOutputStream(archivo);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Administracion.getCaja());
				} catch(FileNotFoundException excepcion) {
					excepcion.printStackTrace();
				} catch(IOException excepcion) {
					excepcion.printStackTrace();
				}
			} else if (archivo.getAbsolutePath().contains("animales")) {
				try {
					fos = new FileOutputStream(archivo);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Administracion.getAnimales());
				} catch(FileNotFoundException excepcion) {
					excepcion.printStackTrace();
				} catch(IOException excepcion) {
					excepcion.printStackTrace();
				}
			} else if(archivo.getAbsolutePath().contains("cuidadores")) {
				try {
					fos = new FileOutputStream(archivo);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Administracion.getCuidadores());
				} catch(FileNotFoundException excepcion) {
					excepcion.printStackTrace();
				} catch(IOException excepcion) {
					excepcion.printStackTrace();
				}
			} else if(archivo.getAbsolutePath().contains("habitats")) {
				try {
					fos = new FileOutputStream(archivo);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Administracion.getHabitats());
				} catch(FileNotFoundException excepcion) {
					excepcion.printStackTrace();
				} catch(IOException excepcion) {
					excepcion.printStackTrace();
				}
			} else if(archivo.getAbsolutePath().contains("veterinarios")) {
				try {
					fos = new FileOutputStream(archivo);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Administracion.getVeterinarios());
				} catch(FileNotFoundException excepcion) {
					excepcion.printStackTrace();
				} catch(IOException excepcion) {
					excepcion.printStackTrace();
				}
			} else if(archivo.getAbsolutePath().contains("visitantes")) {
				try {
					fos = new FileOutputStream(archivo);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Administracion.getVisitantes());
				} catch(FileNotFoundException excepcion) {
					excepcion.printStackTrace();
				} catch(IOException excepcion) {
					excepcion.printStackTrace();
				}
			}
		}
	}
}
