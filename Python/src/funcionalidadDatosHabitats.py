from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion

class Habitats(Frame):
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Consultar hábitats del zoológico", font="Helvetica 12 bold")
        info = """A través de esta funcionalidad y presionando el botón consultar, podrá ver
en pantalla los datos de los diferentes hábitats del zoológico"""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=10, pady=10)
        descripcion.pack(fill=BOTH, padx=10, pady=10)
        botones = Frame(master=self)
        consultar = Button(master=botones, text="Consultar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=lambda:Habitats.consultar())
        consultar.pack(padx=10, pady=10)
        botones.pack(padx=10, pady=10)
    
    @staticmethod
    def consultar():
        n_habitats=len(Administracion.getHabitats())
        mensaje="Actualmente el zoológico cuenta con "+str(n_habitats)+" HÁBITATS.\nEstos son los datos de los hábitats:"
        for an in Administracion.getHabitats():
            mensaje=mensaje+"\n"+an.info()
        messagebox.showinfo(title="Información",message=mensaje,)
