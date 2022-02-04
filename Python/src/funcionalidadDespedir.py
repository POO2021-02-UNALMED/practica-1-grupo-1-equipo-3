from tkinter import *
from fieldFrame import FieldFrame
from tkinter import messagebox
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.cuidador import Cuidador
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.especie import Especie
from excepciones.excepcionPresenciaDatos import ExcepcionPresenciaDatos
 
class Despedir(Frame):
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Despedir un empleado", font="Helvetica 11 bold")
        info = """Seleccionando la profesión y posteriormente la identificación de alguno 
de nuestros empleados. Este será despedido."""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=5, pady=5)
        descripcion.pack(fill=BOTH, padx=5, pady=5)

        self.criterios = ["Profesión","Identificación", "Nombre", "Sueldo", "Especie asignada"]
        self.valores = [False,False, "", "", "", "", ""]
        self.habilitados = [True,True, False, False, False, False, False]
        self.combobox = [["Cuidador","Veterinario"],Despedir.identificaciones(), False, False, False, False, False]
        self.dialogos = FieldFrame(self, "Criterios", self.criterios, "Valores", self.valores, self.habilitados, self.combobox)
        self.dialogos.pack(padx=5, pady=5)
        botones = Frame(master=self)
        aceptar = Button(master=botones, text="Aceptar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command= self.aceptar)
        aceptar.pack(side=LEFT, padx=5, pady=5)
        borrar = Button(master=botones, text="Borrar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command= self.borrar)
        borrar.pack(side=RIGHT, padx=5, pady=5)
        botones.pack(padx=5, pady=5)
        self.dialogos.getComponente("Profesión").bind("<<ComboboxSelected>>", lambda e: self.profesionSeleccionada())
        self.dialogos.getComponente("Identificación").bind("<<ComboboxSelected>>", lambda e: self.empleadoSeleccionado())

    def profesionSeleccionada(self):
        profesion=self.dialogos.getValue("Profesión")
        if profesion=="Veterinario":
            self.dialogos.getComponente("Identificación").configure(values=Despedir.identificacionesVeterinarios())
        else:
            self.dialogos.getComponente("Identificación").configure(values=Despedir.identificacionesCuidadores())
            
    def empleadoSeleccionado(self):
        profesion=self.dialogos.getValue("Profesión")
        identificacion = self.dialogos.getValue("Identificación")
        identificacion = int(identificacion)
        nombre = self.dialogos.getComponente("Nombre")
        sueldo = self.dialogos.getComponente("Sueldo")
        especie = self.dialogos.getComponente("Especie asignada")
        if profesion=="Cuidador":
            for cuidador in Administracion.getCuidadores():
              if cuidador.getIdentificacion() == identificacion:
                    nombre.configure(state=NORMAL)
                    nombre.delete(0,"end")
                    nombre.insert(0, cuidador.getNombre())
                    nombre.configure(state=DISABLED)
                    sueldo.configure(state=NORMAL)
                    sueldo.delete(0,"end")
                    sueldo.insert(0, str(cuidador.getSueldo()))
                    sueldo.configure(state=DISABLED)
                    especie.configure(state=NORMAL)
                    especie.delete(0,"end")
                    especie.insert(0, cuidador.getEspecieAsignada().getNombre())
                    especie.configure(state=DISABLED)
                    break
        else :
            for veterinario in Administracion.getVeterinarios():
                if veterinario.getIdentificacion() == identificacion:
                    nombre.configure(state=NORMAL)
                    nombre.delete(0,"end")
                    nombre.insert(0, veterinario.getNombre())
                    nombre.configure(state=DISABLED)
                    sueldo.configure(state=NORMAL)
                    sueldo.delete(0,"end")
                    sueldo.insert(0, str(veterinario.getSueldo()))
                    sueldo.configure(state=DISABLED)
                    especie.configure(state=NORMAL)
                    especie.delete(0,"end")
                    especie.insert(0, veterinario.getEspecieAsignada().getNombre())
                    especie.configure(state=DISABLED)
                    break

    def aceptar(self):
        profesion=self.dialogos.getValue("Profesión")
        identificacion = self.dialogos.getValue("Identificación")
        nombre = self.dialogos.getValue("Nombre")
        sueldo = self.dialogos.getValue("Sueldo")
        especie = self.dialogos.getValue("Especie asignada") 
        valores= [profesion, identificacion, nombre, sueldo, especie]

        try:
            ExcepcionPresenciaDatos.presenciaDatos(self.criterios, valores)
        except ExcepcionPresenciaDatos:
            return

        if profesion=="Veterinario":
            try:
                Administracion.despedirVeterinario(int(identificacion))
                mensaje=str(str(nombre)+" hacia parte de la nomina de veterinarios del zoológico. Ha sido despedid@.")
                messagebox.showinfo(title="Información",
                                message=mensaje)
                self.borrar()
            except:
                error = "Seleccione una identificación"
                messagebox.showerror(title="Error",
                                    message=error) 
        else:
            try:
                mensaje=str(nombre+" hacia parte de la nomina de cuidadores del zoológico. Ha sido despedid@.")
                Administracion.despedirCuidador(int(identificacion))
                messagebox.showinfo(title="Información",
                                message=mensaje)
                self.borrar()
            except:
                error = "Seleccione una identificación"
                messagebox.showerror(title="Error",
                                    message=error)
        
    def borrar(self):
        self.dialogos.getComponente("Profesión").set("")
        self.dialogos.getComponente("Identificación").set("")
        nombre = self.dialogos.getComponente("Nombre")
        nombre.configure(state=NORMAL)
        nombre.delete(0,"end")
        nombre.configure(state=DISABLED)
        sueldo = self.dialogos.getComponente("Sueldo")
        sueldo.configure(state=NORMAL)
        sueldo.delete(0,"end")
        sueldo.configure(state=DISABLED)
        especie = self.dialogos.getComponente("Especie asignada")
        especie.configure(state=NORMAL)
        especie.delete(0,"end")
        especie.configure(state=DISABLED)
    
    @staticmethod
    def identificacionesVeterinarios():
        ids=[]
        for veterinario in Administracion.getVeterinarios():
            ids.append(veterinario.getIdentificacion())
        return ids
    
    @staticmethod
    def identificacionesCuidadores():
        ids=[]
        for cuidador in Administracion.getCuidadores():
            ids.append(cuidador.getIdentificacion())
        return ids

    @staticmethod
    def identificaciones():
        ids=[]
        for cuidador in Administracion.getCuidadores():
            ids.append(cuidador.getIdentificacion())
        for veterinario in Administracion.getVeterinarios():
            ids.append(veterinario.getIdentificacion())
        return ids
        