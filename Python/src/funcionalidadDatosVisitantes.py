from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion

class Visitantes(Frame):
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Consultar visitantes del zoológico", font="Helvetica 12 bold")
        info = """A través de esta funcionalidad y presionando el botón consultar, podrá ver
en pantalla los datos de los visitantes que han visitado el día de hoy el zoológico"""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=10, pady=10)
        descripcion.pack(fill=BOTH, padx=10, pady=10)
        botones = Frame(master=self)
        consultar = Button(master=botones, text="Consultar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=lambda:Visitantes.consultar())
        consultar.pack(padx=10, pady=10)
        botones.pack(padx=10, pady=10)
    
    @staticmethod
    def consultar():
        n_visitantes=len(Administracion.getVisitantes())
        mensaje=str(n_visitantes)+" personas han visitado el zoológico el día hoy.\nEstos son los datos de los VISITANTES:"
        for an in Administracion.getVisitantes():
            mensaje=mensaje+"\n"+an.info()
        messagebox.showinfo(title="Información",message=mensaje)