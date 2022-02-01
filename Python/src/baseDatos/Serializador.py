from gestorAplicacion.administracion import Administracion
from gestorAplicacion.animal import Animal
from gestorAplicacion.cuidador import Cuidador
from gestorAplicacion.habitat import Habitat
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.visitante import Visitante
import pickle


class Serializador():
    def serializar():
        """admin=open("administracion","wb")
        pickle.dump(Administracion,admin)
        admin.close()"""

        fichero_animales=open("animales","wb")
        pickle.dump(Administracion.getAnimales,fichero_animales)
        fichero_animales.close()

        fichero_cuidadores=open("cuidadores","wb")
        pickle.dump(Administracion.getCuidadores,fichero_cuidadores)
        fichero_cuidadores.close()

        fichero_habitats=open("habitats","wb")
        pickle.dump(Administracion.getHabitats,fichero_habitats)
        fichero_habitats.close()

        fichero_veterinarios=open("veterinarios","wb")
        pickle.dump(Administracion.getVeterinarios,fichero_veterinarios)
        fichero_veterinarios.close()

        fichero_visitantes=open("visitantes","wb")
        pickle.dump(Administracion.getVisitantes,fichero_visitantes)
        fichero_visitantes.close()
        