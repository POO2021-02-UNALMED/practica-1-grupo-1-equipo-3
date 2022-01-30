# CLASE CREADA POR DAVID MATEO GARCÍA

# En esta clase se realiza la funcionalidad de la adquisición y el traslado de animales. Adquirir un animal corresponde a
# crear un objeto tipo Animal de acuerdo a los atributos que especifique el usuario, esto en base primero a la especie que
# el usuario haya seleccionado, además de depender que haya un hábitat disponible para crear a dicho animal. Por otro lado, 
# trasladar un animal corresponde a eliminar del sistema el objeto tipo Animal que especifique el usuario.
# 
# Son necesarias las clases Especie, Habitat, Animal y Administración.

from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from ..gestorAplicacion.gestionZoologico.administracion import Administracion
from ..gestorAplicacion.animalesZoologico.especie import Especie
from ..gestorAplicacion.animalesZoologico.habitat import Habitat
from ..gestorAplicacion.animalesZoologico.animal import Animal

class Adquisicion(Frame):
	
    def __init__():
        super().__init__()
        nombre = Label(master=self, text="Adquisición de animales", font="Helvetica 12 bold")
        info = """
        Para la adquisición deberá elegir la Especie de la que se desea adquirir el Animal. Luego para elegir 
        el hábitat se le presentarán en listado solo los hábitats en los que habita la especie que se va a 
        adquirir y en los que la cantidad de animales de dicho hábitat sea menor a su capacidad máxima. Luego 
        debe especificar los atributos del animal a adquirir y este será asignado al hábitat elegido.
        """
        descripcion = Label(master=self, text=info, font="Helvetica 11")
        nombre.pack(fill=BOTH, padx=10, pady=10)
        descripcion.pack(fill=BOTH, padx=10, pady=10)

        criterios = ["Especie", "Hábitat", "Identificación", "Género", "Edad (Años)", "Peso (Kg)"]
        if (not Administracion.getAnimales()):
            valorID = 1
        else:
            valorID = Administracion.getAnimales[-1].getIdentificacion() + 1
        valores = [False, False, valorID, False, "", ""]
        habilitados = [True, True, False, True, True, True]
        combobox = [Adquisicion.especies(), Adquisicion.habitats(), False, ["Macho","Hembra"], False, False]
        dialogos = FieldFrame(self, "Criterios", criterios, "Valores", valores, habilitados, combobox)
        dialogos.pack(fill=BOTH, padx=10, pady=10)
        aceptar = Button(master=self, text="Aceptar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=Adquisicion.aceptar)
        aceptar.pack(side=LEFT, padx=10, pady=10)
        borrar = Button(master=self, text="Borrar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=Adquisicion.borrar)
        borrar.pack(side=RIGHT, padx=10, pady=10)
        FieldFrame.dialogos.getComponente("Especie").bind("<<ComboboxSelected>>", Adquisicion.especieSeleccionada)
        
    @staticmethod
    def especieSeleccionada(e):
        nombreEspecie = FieldFrame.dialogos.getValue("Especie")
        for especie in Administracion.getEspecies():
            if especie.getNombre() == nombreEspecie:
                FieldFrame.dialogos.getComponente("Hábitat").configure(values=Adquisicion.habitats(especie))
                break
    
    @staticmethod
    def aceptar():
        nombreEspecie = FieldFrame.dialogos.getValue("Especie")
        idHabitat = FieldFrame.dialogos.getValue("Hábitat").split("-")[0].strip()
        genero = FieldFrame.dialogos.getValue("Género")
        edad = int(FieldFrame.dialogos.getValue("Edad (Años)"))
        peso = float(FieldFrame.dialogos.getValue("Peso (Kg)"))
        for elem in Administracion.getEspecies():
            if elem.getNombre() == nombreEspecie:
                especie = elem
                break   
        for elem in Administracion.getHabitats():
            if elem.getIdentificacion() == int(idHabitat):
                habitat = elem
                break  
        if(edad < 0 or type(edad) != int):
            error = "EDAD INCORRECTA: Ingrese un número que sea positivo!"
            messagebox.showerror(title="Error",
                                 message=error)
            return
        if(peso < 0.0 or type(peso) != float):
            error = "PESO INCORRECTO: Ingrese un número que sea positivo!"
            messagebox.showerror(title="Error",
                                 message=error)
            return
		# Se llama al método adquirirAnimal(...) de la clase Administracion, pues este método se encarga de crear el objeto tipo Animal
		# en base a los atributos que el usuario eligió e ingresó.
        Administracion.adquirirAnimal(especie, habitat, genero, edad, peso);
        messagebox.showinfo(title="Información",
                            message="ANIMAL ADQUIRIDO EXITOSAMENTE!")
    
    @staticmethod
    def borrar():
        FieldFrame.dialogos.getComponente("Especie").set("")
        FieldFrame.dialogos.getComponente("Hábitat").set("")
        FieldFrame.dialogos.getComponente("Género").delete(0,"end")
        FieldFrame.dialogos.getComponente("Edad (Años)").delete(0,"end")
        FieldFrame.dialogos.getComponente("Peso (Kg)").delete(0,"end")
    
	# A través del método especies() se obtienen los nombres de las especies disponibles.
    @staticmethod
    def especies():
        especies = []
		# El siguiente for obtiene el nombre de cada objeto de Especie almacenado en la lista de especies de Administración
        for especie in Administracion.getEspecies():
            especies.append(especie.getNombre())
        return especies
	
	# A través del método habitat(...) se obtiene la identificación y el nombre de los hábitats disponibles para depositado al animal a adquirir.
    @staticmethod
    def habitat(especie=None):
        habitats = []
        if especie==None:
    		# Con el siguiente for se obtienen cada uno de los hábitats almacenandos en la lista de habitats de la clase Administración.
            for habitat in Administracion.getHabitats():
                if habitat.cantidadAnimales() < habitat.getCapacidadMaxima():
                    habitats.append(habitat.getIdentificacion() + " - " + habitat.getNombre() + " (" + habitat.getEspecie() + ")")
        else:
    		# Con el siguiente for se obtienen cada uno de los hábitats almacenandos en la lista de habitats de la clase Administración.
            for habitat in Administracion.getHabitats():
                if habitat.getAnimalesAsociados() == []:
                    if habitat.cantidadAnimales() < habitat.getCapacidadMaxima():
                        habitats.append(habitat.getIdentificacion() + " - " + habitat.getNombre() + " (Sin Especie)")                
                else:
        			# Además, con el siguiente for, se obtiene cada uno de los animales asociados a cada uno de los hábitats obtenidos con el anterior for que
        			# hayan contenido al menos un animal.
                    for animal in habitat.getAnimalesAsociados():
        				# Todo esto se hace para buscar de manera efectiva los hábitats que puedan contener la especie del animal que se va a adquirir,
        				# para luego listar los datos de cada uno de estos hábitats para que el usuario seleccione uno.
                        if animal.getEspecie() == especie and habitat.cantidadAnimales() < habitat.getCapacidadMaxima():
                            habitats.append(habitat.getIdentificacion() + " - " + habitat.getNombre() + " (" + habitat.getEspecie() + ")")
                            break	
		# En caso que no haya ni un hábitat para depositar al animal, se le informa al usuario.
        if(habitats == []):
            messagebox.showwarning(title="Advertencia",
                                   message="No se ha encontrado ningún hábitat disponible para depositar al animal.")
        return habitats
        
class Traslado(Frame):
    
    def __init__():
        super().__init__()
        nombre = Label(master=self, text="Traslado de animales", font="Helvetica 12 bold")
        info = """
        Para el traslado, se eliminará del sistema al objeto tipo Animal que se haya especificado.
        """
        descripcion = Label(master=self, text=info, font="Helvetica 11")
        nombre.pack(fill=BOTH, padx=10, pady=10)
        descripcion.pack(fill=BOTH, padx=10, pady=10)

        criterios = ["Especie", "Identificación", "Hábitat", "Género", "Edad", "Peso"]
        valores = [False, False, "", "", "", ""]
        habilitados = [True, True, False, False, False, False]
        combobox = [Adquisicion.especies(), False, False, False, False, False]
        dialogos = FieldFrame(self, "Criterios", criterios, "Valores", valores, habilitados, combobox)
        dialogos.pack(fill=BOTH, padx=10, pady=10)
        aceptar = Button(master=self, text="Aceptar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=Traslado.aceptar)
        aceptar.pack(side=LEFT, padx=10, pady=10)
        borrar = Button(master=self, text="Borrar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=Traslado.borrar)
        borrar.pack(side=RIGHT, padx=10, pady=10)
        FieldFrame.dialogos.getComponente("Especie").bind("<<ComboboxSelected>>", Traslado.especieSeleccionada)
        FieldFrame.dialogos.getComponente("Identificación").bind("<<ComboboxSelected>>", Traslado.animalSeleccionado)
 
    @staticmethod
    def especieSeleccionada(e):
        nombreEspecie = FieldFrame.dialogos.getValue("Especie")
        for especie in Administracion.getEspecies():
            if especie.getNombre() == nombreEspecie:
                FieldFrame.dialogos.getComponente("Identificación").configure(values=Traslado.animales(especie))
                break
            
    @staticmethod
    def animalSeleccionado(e):
        identificacion = FieldFrame.dialogos.getValue("Identificación")
        for animal in Administracion.getAnimales():
            if animal.getIdentificacion() == identificacion:
                FieldFrame.dialogos.getComponente("Hábitat").delete(0,"end")
                FieldFrame.dialogos.getComponente("Hábitat").insert(0, animal.getHabitat())
                FieldFrame.dialogos.getComponente("Género").delete(0,"end")
                FieldFrame.dialogos.getComponente("Género").insert(0, animal.getGenero())
                FieldFrame.dialogos.getComponente("Edad").delete(0,"end")
                FieldFrame.dialogos.getComponente("Edad").insert(0, animal.getEdad())
                FieldFrame.dialogos.getComponente("Peso").delete(0,"end")
                FieldFrame.dialogos.getComponente("Peso").insert(0, animal.getPeso())
                break
    
    @staticmethod
    def aceptar():
        identificacion = FieldFrame.dialogos.getValue("Identificacion")
        for elem in Administracion.getAnimales():
            if elem.getIdentificacion() == identificacion:
                animalSeleccionado = elem
                break   
    	# Se llama al método adquirirAnimal(...) de la clase Administracion, pues este método se encarga de crear el objeto tipo Animal
    	# en base a los atributos que el usuario eligió e ingresó.
        Administracion.trasladarAnimal(animalSeleccionado)
        messagebox.showinfo(title="Información",
                            message="ANIMAL TRASLADADO EXITOSAMENTE!")
    
    @staticmethod
    def borrar():
        FieldFrame.dialogos.getComponente("Especie").set("")
        FieldFrame.dialogos.getComponente("Identificación").set("")
        FieldFrame.dialogos.getComponente("Hábitat").delete(0,"end")
        FieldFrame.dialogos.getComponente("Género").delete(0,"end")
        FieldFrame.dialogos.getComponente("Edad").delete(0,"end")
        FieldFrame.dialogos.getComponente("Peso").delete(0,"end")       
 
	# A través del método animal() se obtiene el animal que será trasladado.
    @staticmethod
    def animal(especie=None):
        animales = []

        if especie==None:
            for animal in Administracion.getAnimales():
                animales.append(animal)
        else:
            # Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administración.
            for animal in Administracion.getAnimales():
                # Esto se hace para buscar los animales correspondientes a la especie del animal que se va a trasladar, para luego listar 
                # las identificaciones de cada uno de estos animales para que el usuario seleccione uno para trasladar.
                if(animal.getEspecie() == especie):
                    animales.append(animal)
		
		# En caso que no haya ni un solo animal de la especie seleccionada, se le informa al usuario.
        if(animales == []):
            messagebox.showwarning(title="Advertencia",
                                   message="No se ha encontrado ningún animal disponible para trasladar.")
        return animales