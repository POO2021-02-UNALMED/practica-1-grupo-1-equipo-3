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