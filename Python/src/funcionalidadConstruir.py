from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.especie import Especie

class Construir(Frame):
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Construir un nuevo hábitat", font="Helvetica 12 bold")
        info = """Para construir un nuevo hábitat ingrese el nombre, la ambientación y la capacidad
máxima del hábitat"""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=10, pady=10)
        descripcion.pack(fill=BOTH, padx=10, pady=10)

        self.criterios = ["Nombre", "Ambientación", "Capacidad máxima"]
        self.valores = ["", "", ""]
        self.habilitados = [True, True, True]
        self.combobox = [False, False, False]
        self.dialogos = FieldFrame(self, "Criterios", self.criterios, "Valores", self.valores, self.habilitados, self.combobox)
        self.dialogos.pack(padx=10, pady=10)
        botones = Frame(master=self)
        aceptar = Button(master=botones, text="Aceptar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=lambda:Construir.aceptar(self.dialogos))
        aceptar.pack(side=LEFT, padx=10, pady=10)
        borrar = Button(master=botones, text="Borrar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=lambda: Construir.borrar(self.dialogos))
        borrar.pack(side=RIGHT, padx=10, pady=10)
        botones.pack(padx=10, pady=10)
        
    @staticmethod
    def aceptar(dialogos):
        nombre = dialogos.getValue("Nombre")
        ambientacion=dialogos.getValue("Ambientación")
        capacidad=dialogos.getValue("Capacidad máxima")
        try:
            capacidad = int(capacidad)
            if(capacidad < 0):
                error = "CAPACIDAD MÁXIMA INCORRECTA: Ingrese un número que sea positivo!"
                messagebox.showerror(title="Error",
                                     message=error)
        except ValueError:
            error = "CAPACIDAD MÁXIMA INCORRECTA: Ingrese un número!"
            messagebox.showerror(title="Error",
                                 message=error)            
        try:
            nuevo=Administracion.construirHabitat(nombre,ambientacion,capacidad)
            mensaje=str("¡Se ha construido el nuevo hábitat!\n"+
            "\nEste posee las siguientes características: \n"+"\n"+nuevo.info())
            messagebox.showinfo(title="Información",
                            message=mensaje)
            Construir.borrar(dialogos)
        except UnboundLocalError:
            error = "Todos los campos deben tener algún valor!"
            messagebox.showerror(title="Error",
                                message=error)  

        
    
    @staticmethod
    def borrar(dialogos):
        dialogos.getComponente("Nombre").delete(0,"end")
        dialogos.getComponente("Ambientación").delete(0,"end")
        dialogos.getComponente("Capacidad máxima").delete(0,"end")