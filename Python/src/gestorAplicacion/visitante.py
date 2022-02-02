"""CLASE CREADA POR JOSÉ DAVID CARDONA

La clase visitante se crea con el fin de saber quienes son las personas que ingresan a visitar el zoológico. Se cuenta con el atributo
identificacion, nombre, estrato socioeconómico, edad, precio boleta, el atributo estático totalVisitantes que lleva cuentas del número
de visitantes que han ingresado el zoológico y el atributo pagado para saber si ya pagó su boleta (Necesario en el método calcularGanancias
de la clase Administracion para no sumar varias veces el precio de la boleta de un mismo visitante)
"""

from gestorAplicacion.entidad import Entidad

class Visitante(Entidad):

#Constructor de la clase visitante que recibe como parámetros el nombre, el estrato y la edad del visitante,
#además asigana el precioBoleta y la identificacion dependiendo de unas condiciones
    _totalVisitantes=0
    def __init__(self,nombre,estrato,edad):
        from gestorAplicacion.administracion import Administracion
        self._nombre=nombre
        self._estrato=estrato
        self._edad=edad
        self._pagado=False
        if (len(Administracion.getVisitantes())==0): #La asignacion de identificaciones es automatica para no generar futos errores por identificaciones iguales
            self._identificacion=1
        else:
            self._identificacion=Administracion.getVisitantes()[-1].getIdentificacion()+1
        self._precioBoleta=self.calcularPrecioBoleta()
        Administracion.addVisitantes(self)
        Visitante._totalVisitantes+=1
		
#El método info() es implementado de la interfaz Entidad y definido aquí. Sirve para generar el String que será 
#usado para imprimir por consola los datos del visitante en caso de ser requeridos en alguna de las funcionalidades 
#de la aplicación.

    def info(self):
        return ("\nIdentificacion: "+str(self._identificacion)+"\nNombre: "+self._nombre+"\nEstrato: "+str(self._estrato)+"\nEdad: "+str(self._edad)+"\nPrecio de boleta: "+str(self._precioBoleta)+"$")

#Este método no recibe parámetros y su función es la destrucción del objeto visitante que lo invocó con el proposito de indicar que salió
#del zoológico. Elimina a ese objeto de la lista de visitantes solo cuando halla pagado el precio de su boleta.
#No tiene ningún retorno.

    def salidaVisitante(self):
        from gestorAplicacion.administracion import Administracion
        if self._pagado==True:
            Administracion.removeVisitantes(self)
            self=None
            Visitante._totalVisitantes-=1

#Este metodo no recibe parámetros y su función es la de calcular el atributo precioBoleta del visitante. Para esto es tenido en cuenta el
#estrato y la edad; Dependiendo de los valores en estos dos parámetros, el precio variará.
#Tiene como retorno el valor de precioBoleta

    def calcularPrecioBoleta(self):
        if (self._edad<15):
            self._precioBoleta=10000
            if (self._estrato<=3):
                self._precioBoleta=int(self._precioBoleta*0.7)
        else:
            self._precioBoleta=20000
            if (self._estrato<=3)		:
                self._precioBoleta=int(self._precioBoleta*0.8)
        return self._precioBoleta
	
#DE ACÁ PARA ABAJO ESÁN LOS MÉTODOS GET Y SET

    def getIdentificacion(self):
        return self._identificacion
	
    def getNombre(self):
        return self._nombre
	
    def getEstrato(self):
        return self._estrato
	
    def getEdad(self):
        return self._edad
	
    def getPrecioBoleta(self):
        return self._precioBoleta
	
    @classmethod 
    def getTotalVisitantes(cls):
        return cls._totalVisitantes
	
    def isPagado(self):
        return self._pagado
	
    def setIdentificacion(self,nuevo):
        self._identificacion=nuevo

    def setNombre(self,nuevo):
        self._nombre=nuevo

    def setEstrato(self,nuevo):
        self._estrato=nuevo
	
    def setEdad(self,nuevo):
        self._edad=nuevo
	

    def setPrecioBoleta(self,nuevo):
        self._nombre=nuevo
	
    def setPagado(self,nuevo):
        self._pagado=nuevo