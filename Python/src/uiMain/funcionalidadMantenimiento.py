#from gestorAplicacion.animalesZoologico.animal import Animal
from gestorAplicacion.animalesZoologico.habitat import Habitat
#from gestorAplicacion.gestionZoologico.cuidador import Cuidador
from gestorAplicacion.gestionZoologico.administracion import Administracion
from main import Main

class FuncionalidadMantenimiento:

    jaula = Habitat("jaula")
    cuidadorSeleccionado = None
    habitatSeleccionado = None

    
    
    @classmethod
    def mantenimientoHabitat(cls):
        habitatsDisponibles = cls.seleccionarHabitat()
        if habitatsDisponibles:
            cuidadoresDisponibles = cls.seleccionarCuidador
            if cuidadoresDisponibles:
                cls.limpiezaHabitat()
        
        Main.continuar()

    
    
    @classmethod
    def seleccionarHabitat(cls):
        habitats = 0
        idHabitats= []
        
        print("Elija primero el habitat que desee revisar, ingresando su identificación.\n")
        print("Identificacion; Nombre; Ambientacion; Especie del Habitat; Cantidad Animales; Capacidad Maxima")

        for habitat in Administracion.getHabitats():
             if (len(habitat.getAnimalesAsociados()) != 0 ):
                
                cadena = (str(habitat.getIdentificacion()) + "; " + habitat.getNombre() + "; " + habitat.getAmbientacion() + 
                "; " + habitat.getAnimalesAsociados()[0].getEspecie().getNombre() + "; " + str(habitat.cantidadAnimales()) + "; "
                + str(habitat.getCapacidadMaxima()))
                print(cadena)

                habitats += 1
                idHabitats.append(habitat.getIdentificacion())

        if habitats == 0:
            print("\nNo se ha encontrado ningún hábitat para revisar.")
            print("MANTENIMIENTO CANCELADO\n")
            return False
        
        else:
            
            print("\n¿Cuál hábitat elije? (Identificacion) ")
            #id= int(input())
            id= Main.leerOpcion()

            while id not in idHabitats:
                print("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida.")
                print("\nPor favor seleccione un hábitat:  ")
                #id= int(input())
                id= Main.leerOpcion()
            
            for habitat in Administracion.getHabitats() :
                if id == habitat.getIdentificacion():
                    print("\nHábitat seleccionado:\n")
                    print(habitat.info())
                    cls.habitatSeleccionado = habitat
                    break
            
            return True
    
    
    @classmethod
    def seleccionarCuidador(cls):
        cuidadores = 0
        idCuidadores= []

        print("\nAhora elija el cuidador que desee que revise el hábitat, ingresando su identificación.\n")
        print("Identificación; Nombre; Especie Asignada")

        for cuidador in Administracion.getCuidadores():
            if (cuidador.getEspecieAsignada().getNombre() == cls.habitatSeleccionado.getAnimalesAsociados()[0].getEspecie().getNombre()):
                cadena = (str(cuidador.getIdentificacion()) + "; " + cuidador.getNombre() + "; " + cuidador.getEspecieAsignada().getNombre())
                print(cadena)
                cuidadores += 1
                idCuidadores.append(cuidador.getIdentificacion())
        
        if cuidadores == 0:
            print("\nNo se ha encontrado ningún cuidador para que revise el hábitat.")
            print("MANTENIMIENTO CANCELADO\n")
            return False
        
        else:
            print("\n¿Cuál cuidador elige? (Identificación) ")
            #id = int(input())
            id= Main.leerOpcion()

            while id not in idCuidadores:
                print("\nIDENTIFICACIÓN INCORRECTA: Ingrese una válida.")
                print("\n¿Cuál cuidador elije? (Identificación) ")
                #id = int(input())
                id = Main.leerOpcion() 
            
            for cuidador in Administracion.getCuidadores():
                if  id == cuidador.getIdentificacion():
                    print("Cuidador seleccionado: \n") 
                    print(cuidador.info())
                    cls.cuidadorSeleccionado = cuidador
                    break
            
            return True
    
    
    @classmethod
    def limpiezaHabitat(cls):
        idAnimalesTristes = []
        
        print("\nCuidador " + cls.cuidadorSeleccionado().getNombre + " procede a revisar el habitat con identficacion " + str(cls.habitatSeleccionado.getIdentificacion()) + ".")

        if cls.cuidadorSeleccionado.revisar(cls.habitatSeleccionado) :
            print("RESULTADO: El habitat se encuentra en buen estado.\n")
        
        else:
            print("El cuidador " + cls.cuidadorSeleccionado.getNombre() + " decide sacar a todos los animales para hacer mantenimiento al habitat")
            cls.cuidadorSeleccionado.limpiarHabitat(cls.habitatSeleccionado, cls.jaula)

            for animal in cls.habitatSeleccionado.getAnimalesAsociados():
                if animal.isEstadoAnimo == False :
                    if animal.getIdentificacion() not in idAnimalesTristes:
                        idAnimalesTristes.append(animal.getIdentificacion())
                
            
            if not idAnimalesTristes :
                print("Hacerle mantenimiento al habitat ha dado buenos resultados, no hay animales tristes en este.")
            
            else:
                print("Los animales con los siguientes números de identificacion no han mejorado sus estados de ánimo: ")
                for id in idAnimalesTristes:
                    print(id)
                print("Puede solicitar alimentarlos o que los revise un veterinario")

            


           