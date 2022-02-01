"""CLASE CREADA POR JOSÉ DAVID CARDONA

En esta clase se realiza la funcionalidad de la gestión administrativa del zoológico, la cual se encargará de calcular las ganancias, y pagar
a los empleados. En caso de que en la caja haya un valor negativo, querrá decir que no había dinero suficiente para pagar a los empleados y
fue necesario sacar un prestamo. Será necesario despedir a un empleado para que el zoológico se recupere económicamente posteriormente.
 
Son necesarias las clases Veterinario, Cuidador, Visitante y Administración."""

from tkinter import *
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.animal import Animal
from gestorAplicacion.cuidador import Cuidador
from gestorAplicacion.habitat import Habitat
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.visitante import Visitante


class FuncionalidadGestion():

    @classmethod
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
