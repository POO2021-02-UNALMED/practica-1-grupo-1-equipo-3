"""CLASE CREADA POR JOSÉ DAVID CARDONA

En esta clase se realiza otras funcionalidades distintas a las 5 principales. Cuenta con la posibilidad de contratar
y despedir empleados, construir nuevo habitats, y consultar datos del zoológico como la nómina de trabajadores, los
visitantes que ha recebido, la información de los animales.

Son necesarias las clases Veterinario, Cuidador, Visitante y Administración."""

from gestorAplicacion.animalesZoologico import habitat
from gestorAplicacion.gestionZoologico import *
from gestorAplicacion.animalesZoologico import *
from gestorAplicacion.gestionZoologico.administracion import Administracion
class FuncionalidadOtras:
    
    @classmethod
    def funcionalidades(cls):
        while(True):
            print("Elija que desea hacer:\n")
            print("1. Contratar a un empleado")
            print("2. Despedir a un empleado")
            print("3. Construcción de un nuevo hábitat")
            print("4. Consultar datos del zoológico")
            opcion=input("\n¿Cuál quiere realizar? A continuación ingrese su opción: ")
            if opcion==1:
                while(True):
                    print("Puede elegir entre:\n")
                    print("1. Contratar cuidador")
                    print("2. Contratar veterinario")
                    op1=input("\n¿Cuál quiere realizar? A continuación ingrese su opción: ")
                    if op1==1:
                        FuncionalidadOtras.contratarCuidador()
                        break
                    elif op1==2:
                        FuncionalidadOtras.contratarVeterinario()
                        break
                    else:
                        print("OPCIÓN INCORRECTA: Solo opciones 1 y 2. Vuelva a ingresar una opción válida")
            elif opcion==2:
                while(True):
                    print("Puede elegir entre:\n")
                    print("1. Despedir cuidador")
                    print("2. Despedir veterinario")
                    op2=input("\n¿Cuál quiere realizar? A continuación ingrese su opción: ")
                    if op2==1:
                        FuncionalidadOtras.despedirCuidador()
                        break
                    elif op2==2:
                        FuncionalidadOtras.despedirVeterinario()
                        break
                    else:
                        print("OPCIÓN INCORRECTA: Solo opciones 1 y 2. Vuelva a ingresar una opción válida")
            elif opcion==3:
                FuncionalidadOtras.crearHabitat()
            elif opcion==4:
                while(True):
                    print("Puede elegir entre:\n")
                    print("1. Consultar datos animales")
                    print("2. Consultar datos hábitats")
                    print("3. Consultar datos cuidadores")
                    print("4. Consultar datos veterinarios")
                    print("5. Consultar datos visitantes")
                    op4=input("\n¿Cuál quiere realizar? A continuación ingrese su opción: ")
                    if op4==1:
                        FuncionalidadOtras.animales()
                        break
                    elif op4==2:
                        FuncionalidadOtras.habitats()
                        break
                    elif op4==3:
                        FuncionalidadOtras.cuidadores()
                        break
                    elif op4==4:
                        FuncionalidadOtras.veterinarios()
                        break
                    elif op4==5:
                        FuncionalidadOtras.visitantes()
                        break
                    else:
                        print("OPCIÓN INCORRECTA: Solo opciones del 1 al 5. Vuelva a ingresar una opción válida")
            else:
                print("OPCIÓN INCORRECTA: Solo opciones del 1 al 4. Vuelva a ingresar una opción válida")
    
    @classmethod
    def contratarCuidador(cls):
        nombre=input("Ingrese el nombre del cuidador al que quiere contratar: ")
        print()
        sueldo=input("Ahora ingrese el sueldo del cuidador (NÚMERO ENTERO): ")
        print()
        print("A continuácion se muestran las especies para que posteriormente sea ingresado el nombre de la especie.")
        for espe in Administracion.getEspecies():
            print("\n"+espe.info())
        print()
        especie=input("Por último ingrese el nombre de la especie de la que se va a encargar el cuidador: ")
        for espe in Administracion.getEspecies():
            if (espe.getNombre()==especie):
                especialidad=espe
                break
        nuevo=Administracion.contratarCuidador(nombre,sueldo,especialidad)
        print()
        print("¡"+nuevo.getNombre()+" ya hace parte de la nomina de cuidadores del zoológico!\n")
        print("Estas son las características del nuevo cuidador:\n")
        print(nuevo.info())
        print()
    
    @classmethod
    def contratarVeterinario():
        nombre=input("Ingrese el nombre del veterinario al que quiere contratar: ")
        print()
        sueldo=input("Ahora ingrese el sueldo del veterinario (NÚMERO ENTERO): ")
        print()
        print("A continuácion se muestran las especies para que posteriormente sea ingresado el nombre de la especie.")
        for espe in Administracion.getEspecies():
            print("\n"+espe.info())
        print()
        especie=input("Por último ingrese el nombre de la especie de la que el veterinario está especializado: ")
        for espe in Administracion.getEspecies():
            if (espe.getNombre()==especie):
                especialidad=espe
                break
        nuevo=Administracion.contratarVeterinario(nombre,sueldo,especialidad)
        print()
        print("¡"+nuevo.getNombre()+" ya hace parte de la nomina de veterinarios del zoológico!\n")
        print("Estas son las características del nuevo veterinario:\n")
        print(nuevo.info())
        print()

    @classmethod
    def despedirCuidador():
        print("A continuación le mostraremos la nómina de cuidadores del zoológico:")
        for cuidador in Administracion.getCuidadores():
            print("\n"+cuidador.info())
        while(True):
            id=input("¿Ya se decidió por el cuidador que quiere despedir? A continuación ingrese el número de identificación del cuidador: ")
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
    def despedirVeterinario():
        print("A continuación le mostraremos la nómina de veterinarios del zoológico:")
        for cuidador in Administracion.getVeterinarios():
            print("\n"+cuidador.info())
        while(True):
            id=input("¿Ya se decidió por el veterinario que quiere despedir? A continuación ingrese el número de identificación del veterinario: ")
            for cuidador in Administracion.getVeterinarios():
                if (id==cuidador.getIdentificacion()): #Si hay una identificación que coincide con la ingresada, se despedirá al cuidador
                    Administracion.despedirVeterinario(id)
                    print(cuidador.getNombre()+" hacia parte de la nómina de veterinarios del zoológico. Ha sido despedid@.")
                    print("\nCon esto el zoológico se recuperará económicamente.")
                    print()
                    break
            #En caso de no encontrar a alguien con esa identificación, se repetirá el proceso
            print("\nNinguno de nuestros veterinarios tiene esa identificación. Por favor ingrese una identificación válida.")
    
    @classmethod
    def crearHabitat():
        print("Iniciaremos la construcción de un nuevo hábitat.\n")
        nombre=input("Ingrese el nombre del hábitat: ")
        print()
        ambientacion=input("Ahora ingrese la ambientación que va a tener el hábitat: ")
        print()
        capacidad=input("Por último ingrese la capacidad máxima de animales que puede albergar:")
        print("\n...")
        nuevo=Administracion.construirHabitat(nombre,ambientacion,capacidad)
        print("\n¡Se ha construido el nuevo hábitat!\n")
        print("Este posee las siguientes características: ")
        print("\n"+nuevo.info())
        print()

    @classmethod
    def animales():
        print("Este es el listado de animales con los que cuenta el zoológico:")
        for animales in Administracion.getAnimales():
            print()
            print(animales.info())
        print()
    
    @classmethod
    def habitats():
        print("Este es el listado de hábitats con los que cuenta el zoológico:")
        for habitats in Administracion.getHabitats():
            print()
            print(habitats.info())
        print()
    
    @classmethod
    def cuidadores():
        print("Esta es la nómina de cuidadores del zoológico: ")
        for cuidador in Administracion.getCuidadores():
            print()
            print(cuidador.info())
        print()
	
    @classmethod
    def veterinarios():
        print("Esta es la nómina de veterinarios del zoológico: ")
        for cuidador in Administracion.getVeterinarios():
            print()
            print(cuidador.info())
        print()
	
    @classmethod
    def visitantes():
        print("Este es el listado de personas que han visitado el zoológico en el día de hoy: ")
        for visitante in Administracion.getVisitantes():
            print()
            print(visitante.info())
        print()