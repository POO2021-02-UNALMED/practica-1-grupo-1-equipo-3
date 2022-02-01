from gestorAplicacion.administracion import Administracion
from gestorAplicacion.animal import Animal
from gestorAplicacion.cuidador import Cuidador
from gestorAplicacion.habitat import Habitat
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.visitante import Visitante
import pickle

class Deserializador():
    def deserializar():
        """fichero_administracion=open("administracion","rb")
        admin=pickle.load(fichero_administracion)
        fichero_administracion.close()"""

        fichero_animales=open("animales","rb")
        animales=pickle.load(fichero_animales)
        fichero_animales.close()

        fichero_cuidadores=open("cuidadores","rb")
        cuidadores=pickle.load(fichero_cuidadores)
        fichero_cuidadores.close()

        fichero_habitats=open("habitats","rb")
        habitats=pickle.load(fichero_habitats)
        fichero_habitats.close()

        fichero_veterinarios=open("veterinarios","rb")
        veterinarios=pickle.load(fichero_veterinarios)
        fichero_veterinarios.close()

        fichero_visitantes=open("visitantes","rb")
        visitantes=pickle.load(fichero_visitantes)
        fichero_visitantes.close()