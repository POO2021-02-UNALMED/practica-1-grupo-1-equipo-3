# CLASE CREADA POR DAVID MATEO GARCÍA

# En esta clase se realiza la funcionalidad del traslado de animales. Trasladar un animal corresponde a 
# eliminar del sistema el objeto tipo Animal que especifique el usuario.
# 
# Son necesarias las clases Especie, Animal y Administración.

from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion

class Traslado(Frame):
    
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Traslado de animales", font="Helvetica 12 bold")
        info = """Para el traslado, se eliminará del sistema al objeto tipo Animal que se haya especificado.
        """
        descripcion = Label(master=self, text=info, font="Helvetica 11")
        nombre.pack(fill=BOTH, padx=10, pady=10)
        descripcion.pack(fill=BOTH, padx=10, pady=10)

        self.criterios = ["Especie", "Identificación", "Hábitat", "Género", "Edad", "Peso"]
        self.valores = [False, False, "", "", "", ""]
        self.habilitados = [True, True, False, False, False, False]
        self.combobox = [Traslado.especies(), Traslado.animales(), False, False, False, False]
        self.dialogos = FieldFrame(self, "Criterios", self.criterios, "Valores", self.valores, self.habilitados, self.combobox)
        self.dialogos.pack(padx=10, pady=10)
        botones = Frame(master=self)
        aceptar = Button(master=botones, text="Aceptar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=lambda: Traslado.aceptar(self.dialogos))
        aceptar.pack(side=LEFT, padx=10, pady=10)
        borrar = Button(master=botones, text="Borrar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=lambda: Traslado.borrar(self.dialogos))
        borrar.pack(side=RIGHT, padx=10, pady=10)
        botones.pack(padx=10, pady=10)
        self.dialogos.getComponente("Especie").bind("<<ComboboxSelected>>", lambda e: Traslado.especieSeleccionada(self.dialogos))
        self.dialogos.getComponente("Identificación").bind("<<ComboboxSelected>>", lambda e: Traslado.animalSeleccionado(self.dialogos))
 
    @staticmethod
    def especieSeleccionada(dialogos):
        nombreEspecie = dialogos.getValue("Especie")
        for especie in Administracion.getEspecies():
            if especie.getNombre() == nombreEspecie:
                dialogos.getComponente("Identificación").configure(values=Traslado.animales(especie))
                break
            
    @staticmethod
    def animalSeleccionado(dialogos):
        identificacion = dialogos.getValue("Identificación").split("(")[0].strip()
        identificacion = int(identificacion)
        habitat = dialogos.getComponente("Hábitat")
        genero = dialogos.getComponente("Género")
        edad = dialogos.getComponente("Edad")
        peso = dialogos.getComponente("Peso")
        for animal in Administracion.getAnimales():
            if animal.getIdentificacion() == identificacion:
                habitat.configure(state=NORMAL)
                habitat.delete(0,"end")
                habitat.insert(0, animal.getHabitat().getNombre())
                habitat.configure(state=DISABLED)
                genero.configure(state=NORMAL)
                genero.delete(0,"end")
                genero.insert(0, animal.getGenero())
                genero.configure(state=DISABLED)
                edad.configure(state=NORMAL)
                edad.delete(0,"end")
                edad.insert(0, str(animal.getEdad()))
                edad.configure(state=DISABLED)
                peso.configure(state=NORMAL)
                peso.delete(0,"end")
                peso.insert(0, str(animal.getPeso()))
                peso.configure(state=DISABLED)
                break
    
    @staticmethod
    def aceptar(dialogos):
        identificacion = dialogos.getValue("Identificación")
        for elem in Administracion.getAnimales():
            if elem.getIdentificacion() == identificacion:
                animalSeleccionado = elem
                break   
    	# Se llama al método adquirirAnimal(...) de la clase Administracion, pues este método se encarga de crear el objeto tipo Animal
    	# en base a los atributos que el usuario eligió e ingresó.
        try:
            Administracion.trasladarAnimal(animalSeleccionado)
            messagebox.showinfo(title="Información",
                                message="ANIMAL TRASLADADO EXITOSAMENTE!")
        except UnboundLocalError:
            error = "Todos los campos deben tener algún valor!"
            messagebox.showerror(title="Error",
                                    message=error)  
    
    @staticmethod
    def borrar(dialogos):
        dialogos.getComponente("Especie").set("")
        dialogos.getComponente("Identificación").set("")
        habitat = dialogos.getComponente("Hábitat")
        habitat.configure(state=NORMAL)
        habitat.delete(0,"end")
        habitat.configure(state=DISABLED)
        genero = dialogos.getComponente("Género")
        genero.configure(state=NORMAL)
        genero.delete(0,"end")
        genero.configure(state=DISABLED)
        edad = dialogos.getComponente("Edad")
        edad.configure(state=NORMAL)
        edad.delete(0,"end")
        edad.configure(state=DISABLED)
        peso = dialogos.getComponente("Peso")
        peso.configure(state=NORMAL)
        peso.delete(0,"end")
        peso.configure(state=DISABLED)
 
	# A través del método especies() se obtienen los nombres de las especies disponibles.
    @staticmethod
    def especies():
        especies = []
		# El siguiente for obtiene el nombre de cada objeto de Especie almacenado en la lista de especies de Administración
        for especie in Administracion.getEspecies():
            especies.append(especie.getNombre())
        return especies    
 
	# A través del método animal() se obtiene el animal que será trasladado.
    @staticmethod
    def animales(especie=None):
        animales = []

        if especie==None:
            for animal in Administracion.getAnimales():
                animales.append(str(animal.getIdentificacion()) + " (" + animal.getEspecie().getNombre() + ")")
        else:
            # Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administración.
            for animal in Administracion.getAnimales():
                # Esto se hace para buscar los animales correspondientes a la especie del animal que se va a trasladar, para luego listar 
                # las identificaciones de cada uno de estos animales para que el usuario seleccione uno para trasladar.
                if(animal.getEspecie() == especie):
                    animales.append(str(animal.getIdentificacion()) + " (" + animal.getEspecie().getNombre() + ")")
		
    		# En caso que no haya ni un solo animal de la especie seleccionada, se le informa al usuario.
            if(animales == []):
                messagebox.showwarning(title="Advertencia",
                                       message="No se ha encontrado ningún animal disponible para trasladar.")
        return animales