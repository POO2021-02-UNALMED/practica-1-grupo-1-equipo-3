from mailbox import NoSuchMailboxError
from tkinter import *
from tkinter import messagebox
from excepciones.excepcionPresenciaDatos import ExcepcionPresenciaDatos
from excepciones.excepcionTipoInt import ExcepcionTipoInt
from excepciones.excepcionTipoString import ExcepcionTipoString
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.especie import Especie

class Contratar(Frame):
    
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Contratar un empleado", font="Helvetica 11 bold")
        info = """Para contratar a un empleado, deberá elegir inicialmente el tipo de profesión. 
Posteriormente llene el formulario con los datos del nuevo empleado."""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=5, pady=5)
        descripcion.pack(fill=BOTH, padx=5, pady=5)

        self.criterios = ["Profesión", "Identificación", "Nombre", "Sueldo", "Especie asignada"]
        self.valores = [False, "" , "", "", False]
        self.habilitados = [True, False, True, True, True]
        self.combobox = [["Cuidador","Veterinario"], False, False, False, Contratar.especies()]
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
        self.dialogos.getComponente("Profesión").bind("<<ComboboxSelected>>", lambda e: self.profesionSeleccionada())


    # A través del método especies() se obtienen los nombres de las especies disponibles.
    @staticmethod
    def especies():
        especies = []
		# El siguiente for obtiene el nombre de cada objeto de Especie almacenado en la lista de especies de Administración
        for especie in Administracion.getEspecies():
            especies.append(especie.getNombre())
        return especies

    def profesionSeleccionada(self):
        profesion=self.dialogos.getValue("Profesión")
        identificacion=self.dialogos.getComponente("Identificación")
        if profesion=="Veterinario":
            if len(Administracion.getVeterinarios())==0:
                identificacion.configure(state=NORMAL)
                identificacion.delete(0,"end")
                identificacion.insert(0, 1)
                identificacion.configure(state=DISABLED)
            else:
                identificacion.configure(state=NORMAL)
                identificacion.delete(0,"end")
                identificacion.insert(0, Administracion.getVeterinarios()[-1].getIdentificacion() + 1)
                identificacion.configure(state=DISABLED)
        else:
            if len(Administracion.getCuidadores())==0:
                identificacion.configure(state=NORMAL)
                identificacion.delete(0,"end")
                identificacion.insert(0, 1)
                identificacion.configure(state=DISABLED)
            else:
                identificacion.configure(state=NORMAL)
                identificacion.delete(0,"end")
                identificacion.insert(0, Administracion.getCuidadores()[-1].getIdentificacion() + 1)
                identificacion.configure(state=DISABLED)

    def aceptar(self):
        profesion = self.dialogos.getValue("Profesión")
        identificacion=self.dialogos.getValue("Identificación")
        nombre=self.dialogos.getValue("Nombre")
        sueldo=self.dialogos.getValue("Sueldo")
        especie=self.dialogos.getValue("Especie asignada")
        valores= [profesion, identificacion, nombre, sueldo, especie]
        try:
            ExcepcionPresenciaDatos.presenciaDatos(self.criterios, valores)
        except ExcepcionPresenciaDatos:
            return
        finally:
            try:
                sueldo = int(sueldo)
                ExcepcionTipoInt.tipoInt(["Sueldo"], [sueldo])
            except ValueError:
                error = "SUELDO INCORRECTO: Ingrese un número!"
                messagebox.showerror(title="Error",
                                     message=error)
                return
            except ExcepcionTipoInt:
                return
            finally:
                try:
                    ExcepcionTipoString.tipoString(["Nombre"],[nombre]) 
                except ExcepcionTipoString:
                    return            
                    
        for elem in Administracion.getEspecies():
            if elem.getNombre() == especie:
                especie = elem
                break   
		#Se llama al método adquirirAnimal(...) de la clase Administracion, pues este método se encarga de crear el objeto tipo Animal
		# en base a los atributos que el usuario eligió e ingresó.
        if profesion=="Veterinario":
            try:
                nuevo=Administracion.contratarVeterinario(nombre,sueldo,especie)
                mensaje=str("¡"+str(nombre)+" ya hace parte de la nomina de veterinarios del zoológico!\n"+
                "\nEstos son los datos del nuevo veterinario: \n"+nuevo.info())
                messagebox.showinfo(title="Información",
                                message=mensaje)
                self.borrar()
            except UnboundLocalError:
                error = "Todos los campos deben tener algún valor!"
                messagebox.showerror(title="Error",
                                    message=error)  
        else:
            try:
                nuevo=Administracion.contratarCuidador(nombre,sueldo,especie)
                mensaje=str("¡"+str(nombre)+" ya hace parte de la nomina de cuidadores del zoológico!\n"+
                "\nEstos son los datos del nuevo cuidador: \n"+nuevo.info())
                messagebox.showinfo(title="Información",
                                message=mensaje)
                self.borrar()
            except UnboundLocalError:
                error = "Todos los campos deben tener algún valor!"
                messagebox.showerror(title="Error",
                                    message=error)  

    def borrar(self):
        self.dialogos.getComponente("Profesión").set("")
        identificacion=self.dialogos.getComponente("Identificación")
        identificacion.configure(state=NORMAL)
        identificacion.delete(0,"end")
        identificacion.configure(state=DISABLED)
        self.dialogos.getComponente("Nombre").delete(0,"end")
        self.dialogos.getComponente("Sueldo").delete(0,"end")
        self.dialogos.getComponente("Especie asignada").set("")