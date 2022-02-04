"""CLASE CREADA POR JOSÉ DAVID CARDONA

La clase administración se crea con el fin de llevar las cuentas ecónomicas del zoológico, además
del conteo de todo lo que el mismo tiene. Para ello está el atributo caja que es el dinero con el
que cuenta el zoológico en el banco, y los atributos de animales (Animales con los que cuenta el
zoológico), visitantes (Visitantes que ha tenido el zoológico), habitats (Hábitats con los que cuenta
el zoológico, especies (Especies con las que cuenta el zoológico), veterinarios (Nómina de todos
los veterinarios con los que cuenta el zoológico), y cuidadores (Nómina de todos los cuidadores con
los que cuenta el zoológico). Hay que tener en cuenta que solo puede exisir un objeto de esta clase
pues la aplicación está diseñada para la administración de un solo zoológico."""

from gestorAplicacion.especie import Especie

class Administracion:
    _ganancias=False
    _caja=0 #Es el dinero con el que cuenta el zoologico en el banco
    _animales=[] #Es una lista de todos los animales que tiene el zoológico
    _cuidadores=[] #Es una lista de todos los cuidadores que tiene el zoológico
    _especies=[Especie.MAMIFERO, Especie.AVE, Especie.REPTIL, Especie.PEZ, Especie.ANFIBIO] #Es una lista de todas las especies que tiene el zoológico
    _habitats=[] #Es una lista de todos los habitats que tiene el zoológico
    _veterinarios=[] #Es una lista de todos los veterinarios que tiene el zoológico
    _visitantes=[] #Es una lista de todos los visitantes que tiene el zoológico
    

#Constructor de la clase Administración: Recibe como parámetro el atributo caja, el cual corresponde 
#al dinero con el que cuenta el zoológico en el banco.
     
    def __init__(self,caja=0):
        Administracion._caja=caja


#Este método no recibe parámetros y su función es la de calcular el pago total para todos los empleados
#del zoológico. Esto lo hace recorriendo las listas de trabajadores que hay (veterinarios, cuidadores) luego
#obtiene el atributo sueldo y lo suma a una variable pago. A su vez les cambia el estado del atributo pagado a true
#Luego de obtener el pago total, este se descuenta a lo que hay en la caja. 
#Tiene como retorno el valor total de pago a empleados.
    
    @classmethod
    def pagoNomina(cls):
        pago=0
        empleados=[]
        for veterinario in cls._veterinarios:
            empleados.append(veterinario)
        for cuidador in cls._cuidadores:
            empleados.append(cuidador) #Se agregan en una lista empleados, a todos los trabajadores del zoologico (Veterinarios y Cuidadores)
        for empleado in empleados:
            if (empleado.isPagado()==False): #Se comprueba que no le hayan pagado a los empleados
                pago+=empleado.getSueldo(); #Se emplea ligadura dinámica. Entra por método de Veterinario y Cuidador y no por el de Empleado.
                empleado.setPagado(True) #Se le suma al valor del sueldo, lo que se le debe pagar al empleado y se cambia el atributo pagado
        cls._caja-=pago #Se le quita a la caja el valor que debe pagar a los empleados
        Administracion._ganancias=True
        return pago #Retorna el monto total a pagar
    
#Este método recibe como parámetro un animal y su función es trasladar el animal afuera del zoológico, por lo que
#hace que el animal deje de existir, queda con apuntador a null, y el mismo se elimina de las listas donde estaba
#asociado. Eso mismo lo hace el método morir de la clase Animal, por tanto se invoca este método.
#No posee retorno.

    @classmethod
    def trasladarAnimal(self,animal):
        animal.morir() #Invoca el método morir de la clase animal
	
#Este método tiene como parámetros una identificación, la especie, el hábitat de la especie, el género, la edad y el peso
#del animal que se queiere adquirir y su función es la de crear un objeto animal con las anteriores características.
#No posee retorno. 

    @classmethod
    def adquirirAnimal(self,especie,habitatEspecie,genero,edad,peso):
        from gestorAplicacion.animal import Animal
        Animal(especie,habitatEspecie,genero,edad,peso) #Crea un objeto animal
	
#Este método no recibe parámetros y su función es la de calcular la ganancia por días del zoológico.
#Para esto recorrera la lista de visitantes, obtendra el valor de precioBoleta y se lo sumará a una variable
#llamada ganancias. Esto tiene en cuenta el atributo pagado de visitantes y cambia su estado, para que no se repitan
#ganancias.
#Tiene como retorno el valor de las ganancias.
	
    @classmethod
    def calculoGanancias(cls):
        ganancias=0
        for visitante in cls._visitantes:
            if visitante.isPagado()==False:
                ganancias+=visitante.getPrecioBoleta()
                visitante.setPagado(True)
        cls._caja+=ganancias
        return ganancias

#Este método recibe como parámetros la identificación, el nombre, el sueldo y la especie del cuidador que se quiere
#contratar y su función es la creación de un objeto cuidador con las características de los parámetros.
#Tiene como retorno el objeto Cuidador creado.*/
    
    @classmethod
    def contratarCuidador(cls,nombre,sueldo,especieAsignada):
        from gestorAplicacion.cuidador import Cuidador
        return Cuidador(nombre,sueldo,especieAsignada)
	
#Este método recibe como parámetros la identificación, el nombre, el sueldo y la especialidad del veterinario 
#que se quiere contratar y su función es la creación de un objeto veterinario con las características de los 
#parámetros.
#Tiene como retorno el objeto veterinario creado.
	
    @classmethod
    def contratarVeterinario(cls,nombre,sueldo,especialidad):
        from gestorAplicacion.veterinario import Veterinario
        return Veterinario(nombre,sueldo,especialidad)

#Este método tiene como parámetro la idetificación de un cuidador, y su función es la de despedir el cuidador
#que tenga la identificación dada. Esto implica que el objeto quede apuntando a null y sea eliminado de las listas
#donde se encuentra.
#No posee retorno*/
    
    @classmethod
    def despedirCuidador(cls,identificacion):
        for cuidador in cls._cuidadores:
            if (cuidador.getIdentificacion()==identificacion):
                cls.removeCuidadores(cuidador)
                cuidador=None
                break

#Este método tiene como parámetro la idetificación de un veterinario, y su función es la de despedir al veterinario
#que tenga la identificación dada. Esto implica que el objeto quede apuntando a null y sea eliminado de las listas
#donde se encuentra.
#No posee retorno
	
    @classmethod
    def despedirVeterinario(cls,identificacion):
        for veterinario in cls._veterinarios:
            if (veterinario.getIdentificacion()==identificacion):
                cls.removeVeterinarios(veterinario)
                veterinario=None
                break

#Este método tiene como paramétro el nombre, la ambientación y la capacidad de un hábitat y su finalidad es la creación
#de un objeto hábitat.
#Tiene como retorno el objeto hábitat creado.
    
    @classmethod
    def construirHabitat(cls,nombre,ambientacion,capacidad):
        from gestorAplicacion.habitat import Habitat
        return Habitat(nombre,ambientacion,capacidad)

#Este método tiene como parámetro un objeto animal y su función es agregarlo a la lista de atributo animales.
#No posee retorno.

    @classmethod
    def addAnimales(cls,nuevo):
        cls._animales.append(nuevo)
        
#Este método tiene como parámetro un objeto visitante y su función es agregarlo a la lista de atributo visitantes.
#No posee retorno.

    @classmethod
    def addVisitantes(cls,nuevo):
        cls._visitantes.append(nuevo)
    
#Este método tiene como parámetro un objeto hábitat y su función es agregarlo a la lista de atributo hábitats.
#No posee retorno.

    @classmethod
    def addHabitats(cls,nuevo):
        cls._habitats.append(nuevo)
	
#Este método tiene como parámetro un objeto veterinario y su función es agregarlo a la lista de atributo veterinarios.
#No posee retorno.

    @classmethod
    def addVeterinarios(cls,nuevo):
        cls._veterinarios.append(nuevo)
	
#Este método tiene como parámetro un objeto cuidador y su función es agregarlo a la lista de atributo cuidadores.
#No posee retorno.

    @classmethod
    def addCuidadores(cls,nuevo):
        cls._cuidadores.append(nuevo)
	
#Este método tiene como parámetro un objeto animal y su función es eliminarlo de la lista de atributo animales.
#No posee retorno.

    @classmethod
    def removeAnimales(cls,eliminar):
        cls._animales.remove(eliminar)
	
#Este método tiene como parámetro un objeto visitante y su función es eliminarlo de la lista de atributo visitantes.
#No posee retorno.

    @classmethod
    def removeVisitantes(cls,eliminar):
        cls._visitantes.remove(eliminar)
	
#Este método tiene como parámetro un objeto hábitat y su función es eliminarlo de la lista de atributo hábitats.
#No posee retorno.

    @classmethod
    def removeHabitats(cls,eliminar):
        cls._habitats.remove(eliminar)
	

#Este método tiene como parámetro un objeto veterinario y su función es eliminarlo de la lista de atributo veterinarios.
#No posee retorno.

    @classmethod
    def removeVeterinarios(cls,eliminar):
        cls._veterinarios.remove(eliminar)

#Este método tiene como parámetro un objeto cuidador y su función es eliminarlo de la lista de atributo cuidadores.
#No posee retorno.

    @classmethod
    def removeCuidadores(cls,eliminar):
        cls._cuidadores.remove(eliminar)

#DE ACÁ PARA ABAJO ESTÁN LOS MÉTODOS GET Y SET
	
    @classmethod
    def getCaja(cls):
        return cls._caja
	
    @classmethod
    def getAnimales(cls):
        return cls._animales
	
    @classmethod
    def getVisitantes(cls):
        return cls._visitantes
	
    @classmethod
    def getHabitats(cls):
        return cls._habitats
	
    @classmethod
    def getEspecies(cls):
        return cls._especies
	
    @classmethod
    def getVeterinarios(cls):
        return cls._veterinarios
        
    @classmethod
    def getCuidadores(cls):
        return cls._cuidadores
    
    @classmethod
    def isGanancias(cls):
        return cls._ganancias

    @classmethod
    def setCaja(cls,nuevo):
        cls._caja=nuevo

    @classmethod
    def setAnimales(cls,nuevo):
        cls._animales=nuevo
	
    @classmethod
    def setVisitantes(cls,nuevo):
        cls._visitantes=nuevo

    @classmethod
    def setHabitats(cls,nuevo):
        cls._habitats=nuevo
	
    @classmethod
    def setVeterinarios(cls,nuevo):
        cls._veterinarios=nuevo
	
    @classmethod
    def setCuidadores(cls,nuevo):
        cls._cuidadores=nuevo

    @classmethod
    def setGanancias(cls,nuevo):
        cls._ganancias=nuevo
