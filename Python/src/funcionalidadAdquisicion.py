# CLASE CREADA POR DAVID MATEO GARCÍA

# En esta clase se realiza la funcionalidad de la adquisición de animales. Adquirir un animal corresponde a crear 
# un objeto tipo Animal de acuerdo a los atributos que especifique el usuario, esto en base primero a la especie 
# que el usuario haya seleccionado, además de depender que haya un hábitat disponible para crear a dicho animal.
# 
# Son necesarias las clases Especie, Habitat, Animal y Administración.

from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion

class Adquisicion(Frame):
    
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Adquisición de animales", font="Helvetica 12 bold")
        info = """Para la adquisición deberá elegir la Especie de la que se desea adquirir el Animal. Luego para 
elegir el hábitat se le presentarán en listado solo los hábitats en los que habita la especie que se va a 
adquirir y en los que la cantidad de animales de dicho hábitat sea menor a su capacidad máxima. Luego 
debe especificar los atributos del animal a adquirir y este será asignado al hábitat elegido.
        """
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=10, pady=10)
        descripcion.pack(fill=BOTH, padx=10, pady=10)

        self.criterios = ["Especie", "Hábitat", "Identificación", "Género", "Edad (Años)", "Peso (Kg)"]
        if (not Administracion.getAnimales()):
            valorID = 1
        else:
            valorID = Administracion.getAnimales()[-1].getIdentificacion() + 1
        self.valores = [False, False, valorID, False, "", ""]
        self.habilitados = [True, True, False, True, True, True]
        self.combobox = [Adquisicion.especies(), Adquisicion.habitats(), False, ["Macho","Hembra"], False, False]
        self.dialogos = FieldFrame(self, "Criterios", self.criterios, "Valores", self.valores, self.habilitados, self.combobox)
        self.dialogos.pack(padx=10, pady=10)
        botones = Frame(master=self)
        aceptar = Button(master=botones, text="Aceptar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=lambda:Adquisicion.aceptar(self.dialogos))
        aceptar.pack(side=LEFT, padx=10, pady=10)
        borrar = Button(master=botones, text="Borrar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=lambda: Adquisicion.borrar(self.dialogos))
        borrar.pack(side=RIGHT, padx=10, pady=10)
        botones.pack(padx=10, pady=10)
        comboboxEspecie = self.dialogos.getComponente("Especie")
        comboboxEspecie.bind("<<ComboboxSelected>>", lambda e: Adquisicion.especieSeleccionada(self.dialogos))
        
    @staticmethod
    def especieSeleccionada(dialogos):
        nombreEspecie = dialogos.getValue("Especie")
        for especie in Administracion.getEspecies():
            if especie.getNombre() == nombreEspecie:
                dialogos.getComponente("Hábitat").configure(values=Adquisicion.habitats(especie))
                break
    
    @staticmethod
    def aceptar(dialogos):
        nombreEspecie = dialogos.getValue("Especie")
        idHabitat = dialogos.getValue("Hábitat").split("-")[0].strip()
        genero = dialogos.getValue("Género")
        edad = dialogos.getValue("Edad (Años)")
        try:
            edad = int(edad)
            if(edad < 0):
                error = "EDAD INCORRECTA: Ingrese un número que sea positivo!"
                messagebox.showerror(title="Error",
                                     message=error)
        except ValueError:
            error = "EDAD INCORRECTA: Ingrese un número!"
            messagebox.showerror(title="Error",
                                 message=error)            
        peso = dialogos.getValue("Peso (Kg)")
        try:
            peso = float(peso)
            if(peso < 0.0):
                error = "PESO INCORRECTO: Ingrese un número que sea positivo!"
                messagebox.showerror(title="Error",
                                     message=error)
        except ValueError:
            error = "PESO INCORRECTO: Ingrese un número!"
            messagebox.showerror(title="Error",
                                    message=error)            
        for elem in Administracion.getEspecies():
            if elem.getNombre() == nombreEspecie:
                especie = elem
                break   
        for elem in Administracion.getHabitats():
            try:
                if elem.getIdentificacion() == int(idHabitat):
                    habitat = elem
                    break
            except ValueError:
                break
		# Se llama al método adquirirAnimal(...) de la clase Administracion, pues este método se encarga de crear el objeto tipo Animal
		# en base a los atributos que el usuario eligió e ingresó.
        try:
            Administracion.adquirirAnimal(especie, habitat, genero, edad, peso);
            messagebox.showinfo(title="Información",
                                message="ANIMAL ADQUIRIDO EXITOSAMENTE!")
        except UnboundLocalError:
            error = "Todos los campos deben tener algún valor!"
            messagebox.showerror(title="Error",
                                    message=error)  
    
    @staticmethod
    def borrar(dialogos):
        dialogos.getComponente("Especie").set("")
        dialogos.getComponente("Hábitat").set("")
        dialogos.getComponente("Género").set("")
        dialogos.getComponente("Edad (Años)").delete(0,"end")
        dialogos.getComponente("Peso (Kg)").delete(0,"end")
    
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
    def habitats(especie=None):
        habitats = []
        if especie==None:
    		# Con el siguiente for se obtienen cada uno de los hábitats almacenandos en la lista de habitats de la clase Administración.
            for habitat in Administracion.getHabitats():
                if habitat.getEspecie() != None and habitat.cantidadAnimales() < habitat.getCapacidadMaxima():
                    habitats.append(str(habitat.getIdentificacion()) + " - " + habitat.getAmbientacion() + " " + habitat.getNombre() + " (" + habitat.getEspecie().getNombre() + ")")
                elif habitat.getEspecie() == None:
                    habitats.append(str(habitat.getIdentificacion()) + " - " + habitat.getAmbientacion() + " " + habitat.getNombre() + " (Sin Especie)")
        else:
    		# Con el siguiente for se obtienen cada uno de los hábitats almacenandos en la lista de habitats de la clase Administración.
            for habitat in Administracion.getHabitats():
                # Esto se hace para buscar de manera efectiva los hábitats que puedan contener la especie del animal que se va a adquirir,
                # para listar los datos de cada uno de estos hábitats para que el usuario seleccione uno.
                if habitat.getEspecie() == especie.getNombre() and habitat.cantidadAnimales() < habitat.getCapacidadMaxima():
                    habitats.append(str(habitat.getIdentificacion()) + " - " + habitat.getAmbientacion() + " " + habitat.getNombre() + " (" + habitat.getEspecie().getNombre() + ")")
            # En caso que no haya ni un hábitat para depositar al animal, se le informa al usuario.
        if(habitats == []):
            messagebox.showwarning(title="Advertencia",
                                   message="No se ha encontrado ningún hábitat disponible para depositar al animal.")
        return habitats