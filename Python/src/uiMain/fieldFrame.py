from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class FieldFrame(Frame):
    
    def __init__(self, ventana, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None, combobox=None):
        super().__init__(ventana, highlightbackground="black", highlightthickness=2)
        self.componentes = []
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores
        self.habilitado = habilitado
        self.combobox = combobox
        labelTituloCriterios = Label(master=self, text=tituloCriterios, font="Helvetica 10 bold")
        labelTituloCriterios.grid(column=0, row=0, padx=20, pady=10)
        labelTituloValores = Label(master=self, text=tituloValores, font="Helvetica 10 bold")
        labelTituloValores.grid(column=1, row=0, padx=20, pady=10)
        for i in range(1, len(criterios)+1):
            labelCriterio = Label(master=self, text=criterios[i-1], font="Helvetica 10", anchor=W)
            labelCriterio.grid(column=0, row=i, padx=20, pady=10, sticky=W)
            if not combobox[i-1]:
                if valores==None:
                    entryValor = Entry(master=self, font="Helvetica 10", bd=5)
                    entryValor.grid(column=1, row=i, padx=20, pady=10, sticky=E)
                    componentes.append(entryValor)
                    if not habilitado[i-1]:
                        entryValor.configure(state=DISABLED)
                else:
                    entryValor = Entry(master=self, font="Helvetica 10", bd=5)
                    entryValor.grid(column=1, row=i, padx=20, pady=10, sticky=E)
                    entryValor.insert(0, valores[i-1])
                    componentes.append(entryValor)
                    if not habilitado[i-1]:
                        entryValor.configure(state=DISABLED)
            else:
                comboboxValor = ttk.Combobox(master=self, values=combobox[i-1])
                componentes.append(entryValor)
    
    @staticmethod
    def getValue(self, criterio):
        indice = self.criterios.index(criterio)
        return self.componentes[indice].get()
    
    @staticmethod
    def getComponente(self, criterio):
        indice = self.criterios.index(criterio)
        return self.componentes[indice]
        