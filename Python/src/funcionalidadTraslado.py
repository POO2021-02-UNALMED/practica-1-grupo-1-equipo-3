# CLASE CREADA POR DAVID MATEO GARCÍA

# En esta clase se realiza la funcionalidad del traslado de animales. Trasladar un animal corresponde a 
# eliminar del sistema el objeto tipo Animal que especifique el usuario.
# 
# Son usadas las clases Especie, Animal y Administración.

from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion

class Traslado(Frame):
    
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Traslado de animales", font="Helvetica 12 bold")
        info = "Para el traslado, se eliminará del sistema al objeto tipo Animal que se haya especificado."
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
                         command=self.aceptar)
        aceptar.pack(side=LEFT, padx=10, pady=10)
        borrar = Button(master=botones, text="Borrar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.borrar)
        borrar.pack(side=RIGHT, padx=10, pady=10)
        botones.pack(padx=10, pady=10)
        comboboxEspecie = self.dialogos.getComponente("Especie")
        comboboxEspecie.bind("<<ComboboxSelected>>", lambda e: self.especieSeleccionada())
        comboboxAnimal = self.dialogos.getComponente("Identificación")
        comboboxAnimal.bind("<<ComboboxSelected>>", lambda e: self.animalSeleccionado())
 
    def especieSeleccionada(self):
        nombreEspecie = self.dialogos.getValue("Especie")
        self.borrar()
        for especie in Administracion.getEspecies():
            if especie.getNombre() == nombreEspecie:
                self.dialogos.getComponente("Identificación").configure(values=Traslado.animales(especie))
                break
        self.dialogos.getComponente("Especie").set(nombreEspecie)
            
    def animalSeleccionado(self):
        identificacion = self.dialogos.getValue("Identificación").split("(")[0].strip()
        identificacion = int(identificacion)
        habitat = self.dialogos.getComponente("Hábitat")
        genero = self.dialogos.getComponente("Género")
        edad = self.dialogos.getComponente("Edad")
        peso = self.dialogos.getComponente("Peso")
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

    def borrar(self):
        self.dialogos.getComponente("Especie").set("")
        self.dialogos.getComponente("Identificación").set("")
        habitat = self.dialogos.getComponente("Hábitat")
        habitat.configure(state=NORMAL)
        habitat.delete(0,"end")
        habitat.configure(state=DISABLED)
        genero = self.dialogos.getComponente("Género")
        genero.configure(state=NORMAL)
        genero.delete(0,"end")
        genero.configure(state=DISABLED)
        edad = self.dialogos.getComponente("Edad")
        edad.configure(state=NORMAL)
        edad.delete(0,"end")
        edad.configure(state=DISABLED)
        peso = self.dialogos.getComponente("Peso")
        peso.configure(state=NORMAL)
        peso.delete(0,"end")
        peso.configure(state=DISABLED)
    
    def aceptar(self):
        identificacion = self.dialogos.getValue("Identificación").split("(")[0].strip()
        for elem in Administracion.getAnimales():
            try:
                if elem.getIdentificacion() == int(identificacion):
                    animalSeleccionado = elem
                    break   
            except ValueError:
                break
    	# Se llama al método adquirirAnimal(...) de la clase Administracion, pues este método se encarga de crear el objeto tipo Animal
    	# en base a los atributos que el usuario eligió e ingresó.
        try:
            Administracion.trasladarAnimal(animalSeleccionado)
            messagebox.showinfo(title="Resultado",
                                message="Animal trasladado exitosamente!")
            self.borrar()
            self.dialogos.getComponente("Identificación").configure(values=Traslado.animales())
        except UnboundLocalError:
            error = "Debe seleccionar como mínimo la identificación del animal"
            messagebox.showerror(title="Error",
                                    message=error)
 
	# A través del método especies() se obtienen los nombres de las especies disponibles.
    @staticmethod
    def especies():
        especies = []
		# El siguiente for obtiene el nombre de cada objeto de Especie almacenado en la lista de especies de Administración
        for especie in Administracion.getEspecies():
            especies.append(especie.getNombre())
        return especies    
 
	# A través del método animales(...) se obtiene el animal que será trasladado.
    @staticmethod
    def animales(especie=None):
        animales = []

        if especie==None:
            # Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administración.
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
                                       message="No se ha encontrado ningún animal de esta especie que esté disponible para trasladar.")
        return animales