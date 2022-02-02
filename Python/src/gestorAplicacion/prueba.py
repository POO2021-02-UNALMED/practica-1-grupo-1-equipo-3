from animal import Animal
from habitat import Habitat
from especie import Especie
from empleado import Empleado
from veterinario import Veterinario
from cuidador import Cuidador
from visitante import Visitante
from administracion import Administracion

if __name__=="__main__":
    ad=Administracion(0)
    cu1=Cuidador("Amy",3000000,Especie.ANFIBIO)
    cu2=Cuidador("Paulina",3000000,Especie.AVE)
    for cui in ad.getCuidadores():
        print(cui.info())


