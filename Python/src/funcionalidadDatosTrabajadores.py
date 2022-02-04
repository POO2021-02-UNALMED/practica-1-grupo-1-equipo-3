# CLASE CREADA POR DAVID MATEO GARCÍA Y JOSÉ DAVID CARDONA

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.administracion import Administracion

class Trabajador(Frame):
    def __init__(self):
        super().__init__()
        # Se establece el nombre de la funcionalidad y su descripción para ser ambos mostrados en la GUI.
        nombre = Label(master=self, text="Consultar nómina de empleados", font="Helvetica 11 bold")
        info = """A través de esta funcionalidad y presionando el botón consultar, podrá ver
en pantalla los datos de los diferentes empleados activos del zoológico"""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=5, pady=5)
        descripcion.pack(fill=BOTH, padx=5, pady=5)
        
        # Se crea el botón de Consultar para obtener por medio de este la tabla de los empleados.
        botones = Frame(master=self)
        consultar = Button(master=botones, text="Consultar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.consultar)
        consultar.pack(padx=5, pady=5)
        # Se crea el label que contendrá el mensaje con la cantidad de cuidadores y veterinarios con los que se cuenta.
        self.labelCantidad = Label(master=botones, font="Helvetica 10 bold", anchor=CENTER)
        botones.pack(padx=5, pady=5)
        
        # Se crea la tabla de los cuidadores.
        self.frameTablaCuidadores = Frame(master=self)
        self.tablaCuidadores = ttk.Treeview(master=self.frameTablaCuidadores, columns=(1, 2, 3, 4), show='headings')
        self.tablaCuidadores.pack(side=LEFT)
        # Se especifican los escabezados de la tabla de los cuidadores.
        encabezados = ("Identificación", "Nombre", "Sueldo", "Especie Asignada")
        # De acuerdo a los encabezados especificados, estos son ingresados como encabezados de la tabla de los cuidadores.
        for i in range(len(encabezados)):
            self.tablaCuidadores.column(i+1, anchor=CENTER)
            self.tablaCuidadores.heading(i+1, text=encabezados[i])
        # Se añade una scroll bar a la tabla de los cuidadores para ser usado en caso que los datos consultados superen la altura estándar de la tabla.
        bardesp = Scrollbar(self.frameTablaCuidadores, orient=VERTICAL)
        bardesp.pack(side=RIGHT, fill=Y)
        # Se configura la tabla de los cuidadores con el scroll bar y viceversa.
        self.tablaCuidadores.config(yscrollcommand=bardesp.set)
        bardesp.config(command=self.tablaCuidadores.yview)
        
        # Se crea el label que contendrá el mensaje de título para la tabla de los veterinarios.
        self.labelVeterinarios = Label(master=self, text="Los siguientes son los datos de nuestros VETERINARIOS.", font="Helvetica 10 bold", anchor=CENTER)
        # Se crea la tabla de los veterinarios.
        self.frameTablaVeterinarios = Frame(master=self)
        self.tablaVeterinarios = ttk.Treeview(master=self.frameTablaVeterinarios, columns=(1, 2, 3, 4), show='headings')
        self.tablaVeterinarios.pack(side=LEFT)
        # De acuerdo a los encabezados especificados, estos son ingresados como encabezados de la tabla de los veterinarios.
        encabezados = ("Identificación", "Nombre", "Sueldo", "Especie Asignada")
        # De acuerdo a los encabezados especificados, estos son ingresados como encabezados de la tabla de los veterinarios.
        for i in range(len(encabezados)):
            self.tablaVeterinarios.column(i+1, anchor=CENTER)
            self.tablaVeterinarios.heading(i+1, text=encabezados[i])
        # Se añade una scroll bar a la tabla de los veterinarios para ser usado en caso que los datos consultados superen la altura estándar de la tabla.
        bardesp = Scrollbar(self.frameTablaVeterinarios, orient=VERTICAL)
        bardesp.pack(side=RIGHT, fill=Y)
        # Se configura la tabla de los veterinarios con el scroll bar y viceversa.
        self.tablaVeterinarios.config(yscrollcommand=bardesp.set)
        bardesp.config(command=self.tablaVeterinarios.yview)
    
    # Por medio del método consultar() se arma la tabla con los datos consultados.
    def consultar(self):
        # Se establece el mensaje con la cantidad de cuidadores y veterinarios con los que se cuenta.
        mensaje="Actualmente el zoológico cuenta con "+str(len(Administracion.getCuidadores()))+" CUIDADORES y "+str(len(Administracion.getVeterinarios()))+" VETERINARIOS.\n\nLos siguientes son los datos de nuestros CUIDADORES."
        self.labelCantidad.configure(text=mensaje)
        # Primero se eliminan los anteriores datos con los que cuenta la última tabla de los cuidadores que se armó, 
        # esto debido a que puede ser el caso en que haya nuevos datos disponibles para consultar.
        for i in self.tablaCuidadores.get_children():
            self.tablaCuidadores.delete(i)
        # Ahora, se obtienen cada uno de los datos de los cuidadores existentes para ser ingresados en la tabla de los cuidadores por filas.
        for cuidador in Administracion.getCuidadores():
            datos = (str(cuidador.getIdentificacion()), cuidador.getNombre(),
                     str(cuidador.getSueldo()), cuidador.getEspecieAsignada().getNombre())
            self.tablaCuidadores.insert(parent="", index="end", values=datos)
        # Y se habilita para ser visualizada la tabla de los cuidadores y el mensaje de la cantidad de cuidadores y veterinarios con los que se cuenta.
        self.labelCantidad.pack(padx=5, pady=5)
        self.frameTablaCuidadores.pack(padx=5, pady=5)
        
        # Primero se eliminan los anteriores datos con los que cuenta la última tabla de los veterinarios que se armó, 
        # esto debido a que puede ser el caso en que haya nuevos datos disponibles para consultar.
        for i in self.tablaVeterinarios.get_children():
            self.tablaVeterinarios.delete(i)
        # Ahora, se obtienen cada uno de los datos de los veterinarios existentes para ser ingresados en la tabla de los veterinarios por filas.
        for veterinario in Administracion.getVeterinarios():
            datos = (str(veterinario.getIdentificacion()), veterinario.getNombre(),
                     str(veterinario.getSueldo()), veterinario.getEspecieAsignada().getNombre())
            self.tablaVeterinarios.insert(parent="", index="end", values=datos)
        # Y se habilita para ser visualizada la tabla de los veterinarios y el título para esta tabla.
        self.labelVeterinarios.pack(padx=5, pady=5)
        self.frameTablaVeterinarios.pack(padx=5, pady=5)
    
    # Por medio del método ocultarTabla() se deshabilita la visualización de las tablas cuando se cambia de menú.
    def ocultarTabla(self):
        self.frameTablaVeterinarios.pack_forget()
        self.labelVeterinarios.pack_forget()
        self.frameTablaCuidadores.pack_forget()
        self.labelCantidad.pack_forget()
        
