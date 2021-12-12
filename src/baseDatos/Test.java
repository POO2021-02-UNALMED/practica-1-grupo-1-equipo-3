package seria;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.ArrayList;

public class Test implements Serializable{

	String texto;
	
	public static ArrayList<Test> lista =  new ArrayList<>();
	
	public Test(String texto) {
		this.texto = texto;
		lista.add(this);
	}
	
	private static final long serialVersionUID = 1L;

	public static void main(String[] args){
		Test t1 = new Test("Hola");
		Test t2 = new Test("como");
		Test t3 = new Test("estas");
		
		metodo();
		
		metodo1();
        
	}
	
	//Serializando objeto por objeto
	public static void metodo() {
		
		//Serializar
		FileOutputStream fileOut;
		try {
			fileOut = new FileOutputStream(System.getProperty("user.dir") + "\\tmp\\testLista.txt");
			
			ObjectOutputStream out = new ObjectOutputStream(fileOut);
			
			for (Test test : lista) {
				out.writeObject(test);
			}
			
			out.close();
			fileOut.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		//Deserializar
		
		FileInputStream fileIn;
		try {
			fileIn = new FileInputStream(System.getProperty("user.dir") + "/tmp/testLista.txt");
			
			ObjectInputStream in = new ObjectInputStream(fileIn);
			
			ArrayList<Test> listado =  new ArrayList<>();
			
			try {
				Object obj = in.readObject();
				
				while(obj != null) {
					
					listado.add((Test)obj);
					
					obj = in.readObject();
				}
			} catch (EOFException e) {
				// TODO Auto-generated catch block
			}
			
			//
			for (Test test : listado) {
				System.out.println(test.texto);
			}
			
	        in.close();
	        fileIn.close();
	        
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	//Serializando el ArrayList y leyendolo de nuevo
	public static void metodo1() {
		
		//Serializar
		FileOutputStream fileOut;
		try {
			fileOut = new FileOutputStream(System.getProperty("user.dir") + "\\tmp\\testLista2.txt");
			
			ObjectOutputStream out = new ObjectOutputStream(fileOut);
			
			
			out.writeObject(lista);
			out.close();
			fileOut.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		//Deserializar
		
		FileInputStream fileIn;
		try {
			fileIn = new FileInputStream(System.getProperty("user.dir") + "/tmp/testLista2.txt");
			
			ObjectInputStream in = new ObjectInputStream(fileIn);
			
			ArrayList<Test> listado;
			
			listado = (ArrayList<Test>) in.readObject();
			
			//Recorro el ArrayList
			for (Test test : listado) {
				System.out.println(test.texto);
			}
			
	        in.close();
	        fileIn.close();
	        
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
