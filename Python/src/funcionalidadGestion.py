"""CLASE CREADA POR JOSÉ DAVID CARDONA

En esta clase se realiza la funcionalidad de la gestión administrativa del zoológico, la cual se encargará de calcular las ganancias, y pagar
a los empleados. En caso de que en la caja haya un valor negativo, querrá decir que no había dinero suficiente para pagar a los empleados y
fue necesario sacar un prestamo. Será necesario despedir a un empleado para que el zoológico se recupere económicamente posteriormente.
 
Son necesarias las clases Veterinario, Cuidador, Visitante y Administración."""

from cgitb import text
from email import message
from tkinter import *
from turtle import title
from fieldFrame import FieldFrame
from tkinter import messagebox
from idlelib.tooltip import Hovertip
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.animal import Animal
from gestorAplicacion.cuidador import Cuidador
from gestorAplicacion.habitat import Habitat
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.visitante import Visitante


class Gestion(Frame):

    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Gestión administrativa", font="Helvetica 12 bold")
        info = """Nos encargaremos de pagarle a cada uno de nuestros empleados, su respectivo sueldo. Para ello 
calcularemos las ganancias que hemos generado el día de hoy, y se lo sumaremos al presupuesto 
que posee el zoológico en el banco. Usa el botón pagar para hacer todo esto.

En caso de que no tengamos dinero suficiente para pagarle a los empleados, será necesario 
que despida a uno de estos para así recuperarnos económicamente, y para ello se habilitará 
el botón despedir."""
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=10, pady=10)
        descripcion.pack(fill=BOTH, padx=10, pady=10)

        botones = Frame(master=self)
        pagar = Button(master=botones, text="Pagar a empleados", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.pagar)
        pagar.pack(side=LEFT, padx=10, pady=10)
        
        botones.pack(padx=10, pady=10)

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


"""    @classmethod
    def sumaBoletas(cls):
        #Este método es usado para saber cuantas ganancias le han generado al zoológico los visitantes en un día
        respuesta=0
        for visitante in Administracion.getVisitantes:
            respuesta+=visitante.getPrecioBoleta()
        return respuesta

    @classmethod
    def gestionAdministrativa(cls):
        if (Administracion.calculoGanancias()==0 and Administracion.pagoNomina()==0):
            #Esta funcionalidad esta diseñada para ser ejecutada una sola vez. En caso de que ya haya sido ejecuta, el calculo de ganancias y el pago a nomina serán 0 y se mostrará el siguiente mensaje
            print("Ya fueron calculadas las ganancias por el día de hoy y todos nuestros empleados han recibido su paga.")
            print()
        else:
            #En caso de no haber sido ejecutada anteriormente, mostrará el total de visitantes en un día y las ganancias que estos han dado
            print("El zoologico ha recibido a "+str(Visitante.getTotalVisitantes())+" visitantes en el día de hoy y ha obtenido ganancias por un total de "+str(FuncionalidadGestion.sumaBoletas())+"$.")
            #Se procede a mostrar lo que tiene el zoológico en el banco
            print("\nEn total el zoológico dispone de "+str(Administracion.getCaja()+"$ de presupuesto en el banco."))
            #Se invoca el método de pagarEmpleados, el cual dependiendo de lo que haya que pagar y lo que se tenga en el banco, realizará algunas cosas
            FuncionalidadGestion.pagarEmpleados()

    @classmethod
    def pagarEmpleados(cls):
        empleados=[]
        #Se invoca el método pagoNomina de la clase administración el cual calcula cual es el monto toal a pagar, y luego este se le resta a lo que tiene el zoológico en el banco. Además cambia el atributo pagado de los empelados para así saber que ya se les pagó
        print("\nEs tiempo de pagarle a nuestros empleados. El total a pagar es de "+str(Administracion.pagoNomina())+"$.")
        print("\nProcederemos con el pago.")
        print("\n...")
		#En caso de que luego de realizar el pago la caja quede con un valor negativo querra decir que fue necesario sacar un prestamo para pagar a los empelados y entrará a esta condición
        if (Administracion.getCaja()<1):
            print("\nLe informamos que no ha tenido dinero suficiente para pagar, y hemos tenido que realizar un prestamo por un valor de "+str(Administracion.getCaja()*-1)+"$.")
			#Es necesario despedir a un empleado y para esto se muestran los empleados con lo que cuenta el zoológico.
            print("\nEs necesario despedir a alguno de nuestros empleados. A continuación le mostraremos la nómina de empleados:")
            for cuidador in Administracion.getCuidadores:
                empleados.append(cuidador)
            for veterinario in Administracion.getVeterinarios:
                empleados.append(veterinario)
            for empleado in empleados:
                print("\n"+empleado.info())

            while(True):
                print("\n¿Se ha decidido por uno de los empleados? Elija una de las siguientes opciones: ")
                print("1. Despedir a un Cuidador")
                print("2. Despedir a un Veterinario")
                print()
                opcion=input("Ingrese la opción escogida: ")
                print()
                if opcion==1:
                    FuncionalidadGestion.despedirCuidador()
                    break
                elif opcion==2:
                    FuncionalidadGestion.despedirVeterinario()
                    break
                else:
                    print("OPCIÓN INCORRECTA: Solo opciones 1 y 2.")
        else:
            #En caso de que la caja no haya quedado negativa, no ocurrirá nada fuera de lo normal y se imprimirá eñ siguiente mensaje
            print("\nLe hemos pagado a todos los empleados. El nuevo presupuesto que dispone el zoológico en el banco es de "+str(Administracion.getCaja())+"$.")
            print()
	
    @classmethod
    #Este método tiene como finalidad despedir a un cuidador de la nómina de cuidadores
    def despedirCuidador(cls):
        while(True):
            id=input("A continuación ingrese el número de identificación del cuidador: ")
            for cuidador in Administracion.getCuidadores():
                if (id==cuidador.getIdentificacion()): #Si hay una identificación que coincide con la ingresada, se despedirá al cuidador
                    Administracion.despedirCuidador(id)
                    print(cuidador.getNombre()+" hacia parte de la nómina de cuidadores del zoológico. Ha sido despedid@.")
                    print("\nCon esto el zoológico se recuperará económicamente.")
                    print()
                    break
            #En caso de no encontrar a alguien con esa identificación, se repetirá el proceso
            print("\nNinguno de nuestros cuidadores tiene esa identificación. Por favor ingrese una identificación válida.")

    @classmethod
    def despedirVeterinario(cls):
        id=0
        while(True):
            id=input("A continuación ingrese el número de identificación del veterinario: ")
            for cuidador in Administracion.getVeterinarios():
                if (id==cuidador.getIdentificacion()): #Si hay una identificación que coincide con la ingresada, se despedirá al cuidador
                    Administracion.despedirVeterinario(id)
                    print(cuidador.getNombre()+" hacia parte de la nómina de veterinarios del zoológico. Ha sido despedid@.")
                    print("\nCon esto el zoológico se recuperará económicamente.")
                    print()
                    break
            #En caso de no encontrar a alguien con esa identificación, se repetirá el proceso
            print("\nNinguno de nuestros veterinarios tiene esa identificación. Por favor ingrese una identificación válida.")
"""