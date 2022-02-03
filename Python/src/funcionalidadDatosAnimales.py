from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.animal import Animal

class Animales(Frame):
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Consultar animales del zoológico", font="Helvetica 11 bold")
        info = """A través de esta funcionalidad y presionando el botón consultar, podrá ver
en pantalla los datos de los diferentes animales del zoológico"""
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
        
        self.frameTabla = Frame(master=self)
        self.tabla = ttk.Treeview(master=self.frameTabla, columns=(1, 2, 3, 4, 5, 6), show='headings')
        self.tabla.pack(side=LEFT)
        encabezados = ("Identificación", "Especie", "Hábitat", "Género", "Edad", "Peso")
        for i in range(len(encabezados)):
            self.tabla.column(i+1, anchor=CENTER)
            self.tabla.heading(i+1, text=encabezados[i])
        bardesp = Scrollbar(self.frameTabla, orient=VERTICAL)
        bardesp.pack(side=RIGHT, fill=Y)
        self.tabla.config(yscrollcommand=bardesp.set)
        bardesp.config(command=self.tabla.yview)
        
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        style.configure("Treeview.Heading", font="Helvetica 10 bold")
        style.configure("Treeview", font="Helvetica 10")
    
    def consultar(self):
        mensaje="Actualmente el zoológico cuenta con "+str(len(Administracion.getAnimales()))+" ANIMALES. Los siguientes son los datos de los animales."
        self.labelCantidad.configure(text=mensaje)
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        for animal in Administracion.getAnimales():
            datos = (str(animal.getIdentificacion()), animal.getEspecie().getNombre(),
                     animal.getHabitat().getNombre(), animal.getGenero(),
                     str(animal.getEdad()), str(animal.getPeso()))
            self.tabla.insert(parent="", index="end", values=datos)
        self.labelCantidad.pack(padx=5, pady=5)
        self.frameTabla.pack(padx=5, pady=5)
        
    def ocultarTabla(self):
        self.labelCantidad.pack_forget()
        self.frameTabla.pack_forget()
