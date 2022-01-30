package baseDatos;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;

import java.util.List;

import gestorAplicacion.animalesZoologico.*;
import gestorAplicacion.gestionZoologico.*;

public class Deserializador {
	// Este atributo es para definir la ruta al directorio temp que contiene las clases.
	private static File rutaTemp = new File("src\\baseDatos\\temp");
	
	/* El método deserializar(...) es el encargado de cargar las listas de objetos que hay almacenados (serializados)
	 * en los archivos del directorio temp. */
	public static void deserializar() {
		File [] archivos = rutaTemp.listFiles();
		FileInputStream fis;
		ObjectInputStream ois;
		
		for(File archivo : archivos) {
			if(archivo.getAbsolutePath().contains("administracion")) {
				try {
					fis = new FileInputStream(archivo);
					ois = new ObjectInputStream(fis);
					Administracion.setCaja((double) ois.readObject());
				} catch(FileNotFoundException excepcion) {
					excepcion.printStackTrace();
				} catch(IOException excepcion) {
					excepcion.printStackTrace();
				} catch(ClassNotFoundException excepcion) {
					excepcion.printStackTrace();
				}
			} else if(archivo.getAbsolutePath().contains("animales")) {
				try {
					fis = new FileInputStream(archivo);
					ois = new ObjectInputStream(fis);
					Administracion.setAnimales((List<Animal>) ois.readObject());
				} catch(FileNotFoundException excepcion) {
					excepcion.printStackTrace();
				} catch(IOException excepcion) {
					excepcion.printStackTrace();
				} catch(ClassNotFoundException excepcion) {
					excepcion.printStackTrace();
				}
			} else if(archivo.getAbsolutePath().contains("cuidadores")) {
				try {
					fis = new FileInputStream(archivo);
					ois = new ObjectInputStream(fis);
					Administracion.setCuidadores((List<Cuidador>) ois.readObject());
				} catch(FileNotFoundException excepcion) {
					excepcion.printStackTrace();
				} catch(IOException excepcion) {
					excepcion.printStackTrace();
				} catch(ClassNotFoundException excepcion) {
					excepcion.printStackTrace();
				}
			} else if(archivo.getAbsolutePath().contains("habitats")) {
				try {
					fis = new FileInputStream(archivo);
					ois = new ObjectInputStream(fis);
					Administracion.setHabitats((List<Habitat>) ois.readObject());
				} catch(FileNotFoundException excepcion) {
					excepcion.printStackTrace();
				} catch(IOException excepcion) {
					excepcion.printStackTrace();
				} catch(ClassNotFoundException excepcion) {
					excepcion.printStackTrace();
				}
			} else if(archivo.getAbsolutePath().contains("veterinarios")) {
				try {
					fis = new FileInputStream(archivo);
					ois = new ObjectInputStream(fis);
					Administracion.setVeterinarios((List<Veterinario>) ois.readObject());
				} catch(FileNotFoundException excepcion) {
					excepcion.printStackTrace();
				} catch(IOException excepcion) {
					excepcion.printStackTrace();
				} catch(ClassNotFoundException excepcion) {
					excepcion.printStackTrace();
				}
			} else if(archivo.getAbsolutePath().contains("visitantes")) {
				try {
					fis = new FileInputStream(archivo);
					ois = new ObjectInputStream(fis);
					Administracion.setVisitantes((List<Visitante>) ois.readObject());
				} catch(FileNotFoundException excepcion) {
					excepcion.printStackTrace();
				} catch(IOException excepcion) {
					excepcion.printStackTrace();
				} catch(ClassNotFoundException excepcion) {
					excepcion.printStackTrace();
				}
			}
		}
	}
}
