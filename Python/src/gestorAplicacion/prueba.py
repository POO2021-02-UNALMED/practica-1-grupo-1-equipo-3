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
    ve1=Veterinario("Amy",123,Especie.MAMIFERO)
    ve2=Veterinario("Paulina",4334,Especie.AVE)
    ad.despedirVeterinario("a")
    print(ad.getVeterinarios())

