"""CLASE CREADA POR JOSÉ DAVID CARDONA

En esta clase se realiza la funcionalidad de la gestión administrativa del zoológico, la cual se encargará de calcular las ganancias, y pagar
a los empleados. En caso de que en la caja haya un valor negativo, querrá decir que no había dinero suficiente para pagar a los empleados y
fue necesario sacar un prestamo. Será necesario despedir a un empleado para que el zoológico se recupere económicamente posteriormente.
 
Son necesarias las clases Veterinario, Cuidador, Visitante y Administración."""

from tkinter import *
from fieldFrame import FieldFrame
from tkinter import messagebox
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.animal import Animal
from gestorAplicacion.cuidador import Cuidador
from gestorAplicacion.habitat import Habitat
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.visitante import Visitante


class Gestion(Frame):

    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Gestión administrativa", font="Helvetica 11 bold")
        info = """Nos encargaremos de pagarle a cada uno de nuestros empleados, su respectivo sueldo. Para ello 
calcularemos las ganancias que hemos generado el día de hoy, y se lo sumaremos al presupuesto 
que posee el zoológico en el banco. Usa el botón pagar para hacer todo esto.

En caso de que no tengamos dinero suficiente para pagarle a los empleados, será necesario 
que despida a uno de estos para así recuperarnos económicamente, y para ello se habilitará 
el botón despedir."""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=5, pady=5)
        descripcion.pack(fill=BOTH, padx=5, pady=5)

        botones = Frame(master=self)
        pagar = Button(master=botones, text="Pagar a empleados", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.pagar)
        pagar.pack(side=LEFT, padx=5, pady=5)
        
        botones.pack(padx=5, pady=5)

    """@staticmethod"""
    def pagar(self):
        if Administracion.isGanancias()==True:
            mensaje=("Ya hemos pagado a todos los empleados por el día de hoy.\n"+
            "\nVuelva a ejecutar esta función el día de mañana cuando hayamos recibido más visitantes.")
            messagebox.showerror(title="Error",message=mensaje)
        else:
            mensaje=("Hemos recibido a "+str(len(Administracion.getVisitantes()))+" visitantes el día de hoy y estos "+
            "han generado ganancias por un valor de "+str(Gestion.sumaBoletas())+"$."+
            " En el banco habían "+str(Administracion.getCaja())+"$ guardados. Ahora cuenta con "+str(Administracion.getCaja()+Gestion.sumaBoletas())+"$."
            "\n\nContamos con "+str(Gestion.empleados())+" empleados en la nómina. El monto total a pagar por la suma de sueldos es de"+
            Gestion.montoPagar()+" $."+"\n\nProcederemos con el pago.")
            messagebox.showinfo(title="Información",message=mensaje)
            Administracion.calculoGanancias()
            Administracion.pagoNomina()
            if (Administracion.getCaja()<0):
                mensaje=("Le informamos que no ha tenido dinero suficiente para pagar,"+" y hemos tenido que realizar un prestamo por un valor de "+str(Administracion.getCaja()*-1)+"$."+
                "\n\nEs necesario que despida a uno de nuestros empelados. Para ello se en el menú de procesos y consultas, dirijase a otrasfuncionalidades y luego en la opción de despedir empelado. ")
                messagebox.showwarning(title="Dinero insuficiente",message=mensaje)
                
            else:
                mensaje=("¡Pago exitoso!\n\nEl zoológico ha quedado con un presupuesto de "+str(Administracion.getCaja())+"$ en el banco.")
                messagebox.showinfo(title="Información",message=mensaje)



    @staticmethod
    def sumaBoletas():
        respuesta=0
        for inv in Administracion.getVisitantes():
            respuesta+=inv.getPrecioBoleta()
        return respuesta

    @staticmethod
    def montoPagar():
        pago=0
        for vet in Administracion.getVeterinarios():
            pago+=vet.getSueldo()
        for cui in Administracion.getCuidadores():
            pago+=cui.getSueldo()
        return str(pago)

    @staticmethod
    def empleados():
        perso=0
        for vet in Administracion.getVeterinarios():
            perso+=1
        for cui in Administracion.getCuidadores():
            perso+=1
        return str(perso)