from gestorAplicacion.animal import Animal
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.cuidador import Cuidador
from gestorAplicacion.empleado import Empleado
from gestorAplicacion.entidad import Entidad
from gestorAplicacion.especie import Especie
from gestorAplicacion.habitat import Habitat
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.visitante import Visitante

if __name__=="__main__":
    ad=Administracion(0)
    cu1=Cuidador("Amy",3000000,Especie.ANFIBIO)
    cu2=Cuidador("Paulina",3000000,Especie.AVE)
    h=Habitat("Juan","Jil",23)
    h2=Habitat("Jil","asl",11)
    for h in ad.getHabitats():
        print(h.info())
