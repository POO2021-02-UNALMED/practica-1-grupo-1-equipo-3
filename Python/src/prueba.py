from gestorAplicacion.animal import Animal
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.cuidador import Cuidador
from gestorAplicacion.empleado import Empleado
from gestorAplicacion.entidad import Entidad
from gestorAplicacion.especie import Especie
from gestorAplicacion.habitat import Habitat
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.visitante import Visitante
from baseDatos.serializador import *

if __name__=="__main__":
    a = Habitat("H1", "Pradera", 2)
    b = Habitat("H2", "Jungla", 1)
    c= Habitat("H3", "Pantano", 3)
    d= Habitat("H5", "Rio", 3)
    e= Habitat("H6","Pantano",2)
    a1 = Animal(Especie.REPTIL, c, "Macho", 5, 70.0)
    a2 = Animal(Especie.REPTIL, c, "Hembra", 4, 65.0)
    a03=Animal(Especie.REPTIL,c,"Macho",2,34)
    c.setLimpio(False)
    a1.setEstadoAnimo(False)
    a03.setEstadoAnimo(False)
    a3 = Animal(Especie.ANFIBIO,e,"Macho",2,20.0)
    a4 = Animal(Especie.ANFIBIO,e,"Hembra",2,15.0)
    a3.setEstadoAnimo(False)
    a4.setEstadoAnimo(False)
    a3.setAlimentado(False)
    a4.setEstadoSalud(False)
    a5 = Animal(Especie.PEZ,d,"Macho",2,20.0)
    a6 = Animal(Especie.PEZ,d,"Macho",1,15.0)
    a7 = Animal(Especie.PEZ,d,"Hembra",1,20.0)
    d.setLimpio(False)
    a5.setEstadoAnimo(False)
    a6.setEstadoAnimo(False)
    a7.setEstadoAnimo(False)
    a7.setAlimentado(False)
    a5.setAlimentado(False)
    a5.setEstadoSalud(False)
    a6.setEstadoSalud(False)
    a8 = Animal(Especie.ANFIBIO,b,"Hembra",1,20.0)
    b.setLimpio(False)
    a8.setAlimentado(False)
    a8.setEstadoSalud(False)
    a8.setEstadoAnimo(False)
    c1 = Cuidador("Jorge", 7000, Especie.MAMIFERO)
    c2 = Cuidador("Johanna", 1000, Especie.AVE)
    c3 = Cuidador("Camila", 100000, Especie.REPTIL)
    c4 = Cuidador("David", 10000, Especie.PEZ)
    c5 = Cuidador("Juan", 5000, Especie.ANFIBIO)
    v1 = Veterinario("Elva",10000,Especie.ANFIBIO)
    v2 = Veterinario("Francisco",12000,Especie.PEZ)
    vi1 = Visitante("Jose",3,15)
    vi2 = Visitante("Diego",5,30)
    vi3 = Visitante("Valeria",6,30)

    serializar()
    
    
    
    """ad=Administracion(0)
    cu1=Cuidador("Amy",3000000,Especie.ANFIBIO)
    cu2=Cuidador("Paulina",3000000,Especie.AVE)
    ve1=Veterinario("Vale",232,Especie.PEZ)
    ve2=Veterinario("Jil",2323,Especie.MAMIFERO)
    ve3=Veterinario("Juan",3,Especie.ANFIBIO)
    h=Habitat("Juan","Jil",23)
    an1=Animal(Especie.ANFIBIO,h,"Macho",34,2)
    an1.setAlimentado(False)
    an1.setEstadoAnimo(False)
    cu1.revisarAnimal"""
    
