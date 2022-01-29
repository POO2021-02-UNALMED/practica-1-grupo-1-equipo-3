from tkinter import *
from tkinter import messagebox

class FieldFrame(Frame):
    datos = {}
    
    def __init__(self, tituloCriterios, criterios, tituloValores, valores, habilitado):
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores
        self.habilitado = habilitado
    
    def getValue(self, criterio):
        return datos[criterio]