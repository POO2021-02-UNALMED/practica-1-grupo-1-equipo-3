from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion

class Trabajador(Frame):
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Consultar nómina de empleados", font="Helvetica 12 bold")
        info = """A través de esta funcionalidad y presionando el botón consultar, podrá ver
en pantalla los datos de los diferentes empleados activos del zoológico"""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=10, pady=10)
        descripcion.pack(fill=BOTH, padx=10, pady=10)
        botones = Frame(master=self)
        consultar = Button(master=botones, text="Consultar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=lambda:Trabajador.consultar())
        consultar.pack(padx=10, pady=10)
        botones.pack(padx=10, pady=10)
    
    @staticmethod
    def consultar():
        n_veterinarios=len(Administracion.getVeterinarios())
        n_cuidadores=len(Administracion.getCuidadores())
        mensaje="Actualmente el zoológico cuenta con "+str(n_veterinarios)+" VETERINARIOS\ny "+str(n_cuidadores)+" CUIDADORES. Estos son los datos de nuestros VETERINARIOS:"
        for vet in Administracion.getVeterinarios():
            mensaje=mensaje+"\n"+vet.info()
        mensaje=mensaje+"\n\nAhora mostraremos los datos de nuestros CUIDADORES:"
        for cui in Administracion.getCuidadores():
            mensaje=mensaje+"\n"+cui.info()
        messagebox.showinfo(title="Información",message=mensaje)
