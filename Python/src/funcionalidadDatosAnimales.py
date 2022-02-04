# CLASE CREADA POR DAVID MATEO GARCÍA Y JOSÉ DAVID CARDONA

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.administracion import Administracion

class Animales(Frame):
    def __init__(self):
        super().__init__()
        # Se establece el nombre de la funcionalidad y su descripción para ser ambos mostrados en la GUI.
        nombre = Label(master=self, text="Consultar animales del zoológico", font="Helvetica 11 bold")
        info = """A través de esta funcionalidad y presionando el botón consultar, podrá ver
en pantalla los datos de los diferentes animales del zoológico"""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=5, pady=5)
        descripcion.pack(fill=BOTH, padx=5, pady=5)
        
        # Se crea el botón de Consultar para obtener por medio de este la tabla de los animales.
        botones = Frame(master=self)
        consultar = Button(master=botones, text="Consultar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.consultar)
        consultar.pack(padx=5, pady=5)
        # Se crea el label que contendrá el mensaje con la cantidad de animales con los que se cuenta.
        self.labelCantidad = Label(master=botones, font="Helvetica 10 bold", anchor=CENTER)
        botones.pack(padx=5, pady=5)
        
        # Se crea la tabla de los animales.
        self.frameTabla = Frame(master=self)
        self.tabla = ttk.Treeview(master=self.frameTabla, columns=(1, 2, 3, 4, 5, 6), show='headings')
        self.tabla.pack(side=LEFT)
        # Se especifican los escabezados de la tabla.
        encabezados = ("Identificación", "Especie", "Hábitat", "Género", "Edad", "Peso")
        # De acuerdo a los encabezados especificados, estos son ingresados como encabezados de la tabla.
        for i in range(len(encabezados)):
            self.tabla.column(i+1, anchor=CENTER)
            self.tabla.heading(i+1, text=encabezados[i])
        # Se añade una scroll bar a la tabla para ser usado en caso que los datos consultados superen la altura estándar de la tabla.
        bardesp = Scrollbar(self.frameTabla, orient=VERTICAL)
        bardesp.pack(side=RIGHT, fill=Y)
        # Se configura la tabla con el scroll bar y viceversa.
        self.tabla.config(yscrollcommand=bardesp.set)
        bardesp.config(command=self.tabla.yview)
    
    # Por medio del método consultar() se arma la tabla con los datos consultados.
    def consultar(self):
        # Se establece el mensaje con la cantidad de animales con los que se cuenta.
        mensaje="Actualmente el zoológico cuenta con "+str(len(Administracion.getAnimales()))+" ANIMALES. Los siguientes son los datos de los animales."
        self.labelCantidad.configure(text=mensaje)
        # Primero se eliminan los anteriores datos con los que cuenta la última tabla que se armó, 
        # esto debido a que puede ser el caso en que haya nuevos datos disponibles para consultar.
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        # Ahora, se obtienen cada uno de los datos de los animales existentes para ser ingresados en la tabla por filas.
        for animal in Administracion.getAnimales():
            datos = (str(animal.getIdentificacion()), animal.getEspecie().getNombre(),
                     animal.getHabitat().getNombre(), animal.getGenero(),
                     str(animal.getEdad()), str(animal.getPeso()))
            self.tabla.insert(parent="", index="end", values=datos)
        # Por último se habilita para ser visualizada la tabla y el mensaje de la cantidad de animales con los que se cuenta.
        self.labelCantidad.pack(padx=5, pady=5)
        self.frameTabla.pack(padx=5, pady=5)
     
    # Por medio del método ocultarTabla() se deshabilita la visualización de las tablas cuando se cambia de menú.
    def ocultarTabla(self):
        self.labelCantidad.pack_forget()
        self.frameTabla.pack_forget()
