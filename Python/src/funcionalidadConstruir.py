from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.especie import Especie
from excepciones.excepcionPresenciaDatos import ExcepcionPresenciaDatos
from excepciones.excepcionTipoInt import ExcepcionTipoInt
from excepciones.excepcionTipoString import ExcepcionTipoString

class Construir(Frame):
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Construir un nuevo hábitat", font="Helvetica 11 bold")
        info = """Para construir un nuevo hábitat ingrese el nombre, la ambientación y la capacidad
máxima del hábitat"""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=5, pady=5)
        descripcion.pack(fill=BOTH, padx=5, pady=5)

        self.criterios = ["Nombre", "Ambientación", "Capacidad máxima"]
        self.valores = ["", "", ""]
        self.habilitados = [True, True, True]
        self.combobox = [False, False, False]
        self.dialogos = FieldFrame(self, "Criterios", self.criterios, "Valores", self.valores, self.habilitados, self.combobox)
        self.dialogos.pack(padx=5, pady=5)
        botones = Frame(master=self)
        aceptar = Button(master=botones, text="Aceptar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.aceptar)
        aceptar.pack(side=LEFT, padx=5, pady=5)
        borrar = Button(master=botones, text="Borrar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.borrar)
        borrar.pack(side=RIGHT, padx=5, pady=5)
        botones.pack(padx=5, pady=5)
        
    def aceptar(self):
        nombre = self.dialogos.getValue("Nombre")
        ambientacion=self.dialogos.getValue("Ambientación")
        capacidad=self.dialogos.getValue("Capacidad máxima")
        valores= [nombre, ambientacion, capacidad]

        try:   
            ExcepcionPresenciaDatos.presenciaDatos(self.criterios, valores)
        except ExcepcionPresenciaDatos:
            return
        finally:
            try:
                capacidad= int(capacidad)
                ExcepcionTipoInt.tipoInt(["Capacidad máxima"], [capacidad])
            except ValueError:
                error = "CAPACIDAD MÁXIMA INCORRECTA: Ingrese un número!"
                messagebox.showerror(title="Error", 
                                     message=error)
                return                     
            except ExcepcionTipoInt:
                return
            finally:
                try:
                    ExcepcionTipoString.tipoString(["Nombre", "Ambientación"], [nombre, ambientacion])
                except ExcepcionTipoString: 
                    return
                
                   
        nuevo=Administracion.construirHabitat(nombre,ambientacion,capacidad)
        mensaje=str("¡Se ha construido el nuevo hábitat!\n"+
        "\nEste posee las siguientes características: \n"+"\n"+nuevo.info())
        messagebox.showinfo(title="Información",
                        message=mensaje)
        self.borrar()
        
        
        
        
        
        
        
        

       #try:
       #    capacidad = int(capacidad)
       #    if(capacidad < 0):
       #        error = "CAPACIDAD MÁXIMA INCORRECTA: Ingrese un número que sea positivo!"
       #        messagebox.showerror(title="Error",
       #                             message=error)
       #except ValueError:
       #    error = "CAPACIDAD MÁXIMA INCORRECTA: Ingrese un número!"
       #    messagebox.showerror(title="Error",
       #                         message=error)            
       #try:
       #    nuevo=Administracion.construirHabitat(nombre,ambientacion,capacidad)
       #    mensaje=str("¡Se ha construido el nuevo hábitat!\n"+
       #    "\nEste posee las siguientes características: \n"+"\n"+nuevo.info())
       #    messagebox.showinfo(title="Información",
       #                    message=mensaje)
       #    
       #except UnboundLocalError:
       #    error = "Todos los campos deben tener algún valor!"
       #    messagebox.showerror(title="Error",
       #                        message=error)  

    def borrar(self):
        self.dialogos.getComponente("Nombre").delete(0,"end")
        self.dialogos.getComponente("Ambientación").delete(0,"end")
        self.dialogos.getComponente("Capacidad máxima").delete(0,"end")