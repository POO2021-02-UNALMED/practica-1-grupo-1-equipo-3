from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion

class Trabajador(Frame):
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Consultar nómina de empleados", font="Helvetica 11 bold")
        info = """A través de esta funcionalidad y presionando el botón consultar, podrá ver
en pantalla los datos de los diferentes empleados activos del zoológico"""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=5, pady=5)
        descripcion.pack(fill=BOTH, padx=5, pady=5)
        botones = Frame(master=self)
        consultar = Button(master=botones, text="Consultar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.consultar)
        consultar.pack(padx=5, pady=5)
        self.labelCantidad = Label(master=botones, font="Helvetica 10 bold", anchor=CENTER)
        botones.pack(padx=5, pady=5)
        
        self.frameTablaCuidadores = Frame(master=self)
        self.tablaCuidadores = ttk.Treeview(master=self.frameTablaCuidadores, columns=(1, 2, 3, 4), show='headings')
        self.tablaCuidadores.pack(side=LEFT)
        encabezados = ("Identificación", "Nombre", "Sueldo", "Especie Asignada")
        for i in range(len(encabezados)):
            self.tablaCuidadores.column(i+1, anchor=CENTER)
            self.tablaCuidadores.heading(i+1, text=encabezados[i])
        bardesp = Scrollbar(self.frameTablaCuidadores, orient=VERTICAL)
        bardesp.pack(side=RIGHT, fill=Y)
        self.tablaCuidadores.config(yscrollcommand=bardesp.set)
        bardesp.config(command=self.tablaCuidadores.yview)
        
        self.labelVeterinarios = Label(master=self, text="Los siguientes son los datos de nuestros VETERINARIOS.", font="Helvetica 10 bold", anchor=CENTER)
        self.frameTablaVeterinarios = Frame(master=self)
        self.tablaVeterinarios = ttk.Treeview(master=self.frameTablaVeterinarios, columns=(1, 2, 3, 4), show='headings')
        self.tablaVeterinarios.pack(side=LEFT)
        encabezados = ("Identificación", "Nombre", "Sueldo", "Especie Asignada")
        for i in range(len(encabezados)):
            self.tablaVeterinarios.column(i+1, anchor=CENTER)
            self.tablaVeterinarios.heading(i+1, text=encabezados[i])
        bardesp = Scrollbar(self.frameTablaVeterinarios, orient=VERTICAL)
        bardesp.pack(side=RIGHT, fill=Y)
        self.tablaVeterinarios.config(yscrollcommand=bardesp.set)
        bardesp.config(command=self.tablaVeterinarios.yview)
        
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        style.configure("Treeview.Heading", font="Helvetica 10 bold")
        style.configure("Treeview", font="Helvetica 10")
    
    def consultar(self):
        mensaje="Actualmente el zoológico cuenta con "+str(len(Administracion.getCuidadores()))+" CUIDADORES y "+str(len(Administracion.getVeterinarios()))+" VETERINARIOS.\n\nLos siguientes son los datos de nuestros CUIDADORES."
        self.labelCantidad.configure(text=mensaje)
        for i in self.tablaCuidadores.get_children():
            self.tablaCuidadores.delete(i)
        for cuidador in Administracion.getCuidadores():
            datos = (str(cuidador.getIdentificacion()), cuidador.getNombre(),
                     str(cuidador.getSueldo()), cuidador.getEspecieAsignada().getNombre())
            self.tablaCuidadores.insert(parent="", index="end", values=datos)
        self.labelCantidad.pack(padx=5, pady=5)
        self.frameTablaCuidadores.pack(padx=5, pady=5)
        
        self.labelVeterinarios.configure()
        for i in self.tablaVeterinarios.get_children():
            self.tablaVeterinarios.delete(i)
        for veterinario in Administracion.getVeterinarios():
            datos = (str(veterinario.getIdentificacion()), veterinario.getNombre(),
                     str(veterinario.getSueldo()), veterinario.getEspecieAsignada().getNombre())
            self.tablaVeterinarios.insert(parent="", index="end", values=datos)
        self.labelVeterinarios.pack(padx=5, pady=5)
        self.frameTablaVeterinarios.pack(padx=5, pady=5)
        
    def ocultarTabla(self):
        self.frameTablaVeterinarios.pack_forget()
        self.labelVeterinarios.pack_forget()
        self.frameTablaCuidadores.pack_forget()
        self.labelCantidad.pack_forget()
        
