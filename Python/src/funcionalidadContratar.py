from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.especie import Especie

class Contratar(Frame):
    
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Contratar un empleado", font="Helvetica 12 bold")
        info = """Para contratar a un empleado, deberá elegir inicialmente el tipo de profesión. 
Posteriormente llene el formulario con los datos del nuevo empleado."""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=10, pady=10)
        descripcion.pack(fill=BOTH, padx=10, pady=10)

        self.criterios = ["Profesión", "Identificación", "Nombre", "Sueldo", "Especie asignada"]
        self.valores = [False, "" , "", "", False]
        self.habilitados = [True, False, True, True, True]
        self.combobox = [["Cuidador","Veterinario"], False, False, False, Contratar.especies()]
        self.dialogos = FieldFrame(self, "Criterios", self.criterios, "Valores", self.valores, self.habilitados, self.combobox)
        self.dialogos.pack(padx=10, pady=10)
        botones = Frame(master=self)
        aceptar = Button(master=botones, text="Aceptar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=lambda:Contratar.aceptar(self.dialogos))
        aceptar.pack(side=LEFT, padx=10, pady=10)
        borrar = Button(master=botones, text="Borrar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=lambda: Contratar.borrar(self.dialogos))
        borrar.pack(side=RIGHT, padx=10, pady=10)
        botones.pack(padx=10, pady=10)
        self.dialogos.getComponente("Profesión").bind("<<ComboboxSelected>>", lambda e: Contratar.profesionSeleccionada(self.dialogos))


    # A través del método especies() se obtienen los nombres de las especies disponibles.
    @staticmethod
    def especies():
        especies = []
		# El siguiente for obtiene el nombre de cada objeto de Especie almacenado en la lista de especies de Administración
        for especie in Administracion.getEspecies():
            especies.append(especie.getNombre())
        return especies

    
    @staticmethod
    def profesionSeleccionada(dialogos):
        profesion=dialogos.getValue("Profesión")
        identificacion=dialogos.getComponente("Identificación")
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


    @staticmethod
    def aceptar(dialogos):
        profesion = dialogos.getValue("Profesión")
        identificacion=dialogos.getValue("Identificación")
        nombre=dialogos.getValue("Nombre")
        sueldo=dialogos.getValue("Sueldo")
        especie=dialogos.getValue("Especie asignada")
        try:
            sueldo = int(sueldo)
            if(sueldo < 0):
                error = "SUELDO INCORRECTO: Ingrese un número que sea positivo!"
                messagebox.showerror(title="Error",
                                     message=error)
        except ValueError:
            error = "SUELDO INCORRECTO: Ingrese un número!"
            messagebox.showerror(title="Error",
                                 message=error)            
        for elem in Administracion.getEspecies():
            if elem.getNombre() == especie:
                especie = elem
                break   
		# Se llama al método adquirirAnimal(...) de la clase Administracion, pues este método se encarga de crear el objeto tipo Animal
		# en base a los atributos que el usuario eligió e ingresó.
        if profesion=="Veterinario":
            try:
                nuevo=Administracion.contratarVeterinario(nombre,sueldo,especie)
                mensaje=str("¡"+str(nombre)+" ya hace parte de la nomina de veterinarios del zoológico!\n"+
                "\nEstos son los datos del nuevo veterinario: \n"+"\n"+nuevo.info())
                messagebox.showinfo(title="Información",
                                message=mensaje)
                Contratar.borrar(dialogos)
            except UnboundLocalError:
                error = "Todos los campos deben tener algún valor!"
                messagebox.showerror(title="Error",
                                    message=error)  
        else:
            try:
                nuevo=Administracion.contratarCuidador(nombre,sueldo,especie)
                mensaje=str("¡"+str(nombre)+" ya hace parte de la nomina de cuidadores del zoológico!\n"+
                "\nEstos son los datos del nuevo cuidador: \n"+"\n"+nuevo.info())
                messagebox.showinfo(title="Información",
                                message=mensaje)
                Contratar.borrar(dialogos)
            except UnboundLocalError:
                error = "Todos los campos deben tener algún valor!"
                messagebox.showerror(title="Error",
                                    message=error)  

        
    
    @staticmethod
    def borrar(dialogos):
        dialogos.getComponente("Profesión").set("")
        identificacion=dialogos.getComponente("Identificación")
        identificacion.configure(state=NORMAL)
        identificacion.delete(0,"end")
        identificacion.configure(state=DISABLED)
        dialogos.getComponente("Nombre").delete(0,"end")
        dialogos.getComponente("Sueldo").delete(0,"end")
        dialogos.getComponente("Especie asignada").set("")