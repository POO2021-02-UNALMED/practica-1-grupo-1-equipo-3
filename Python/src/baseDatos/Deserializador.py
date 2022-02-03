from gestorAplicacion.administracion import Administracion
from gestorAplicacion.animal import Animal
from gestorAplicacion.cuidador import Cuidador
from gestorAplicacion.habitat import Habitat
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.visitante import Visitante
import pickle
import os
import pathlib

def deserializar():
    #deserializarAdministracion()
    deserializarAnimales()
    deserializarCuidadores()
    deserializarHabitats()
    deserializarVeterinarios()
    deserializarVisitantes()

def deserializarAdministracion():
    fichero_administracion=open(pathlib.Path(__file__).parent.absolute(), "temp\\administracion","rb")
    admi=pickle.load(fichero_administracion)
    fichero_administracion.close()

def deserializarAnimales():
    fichero_animales=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\animales"),"rb")
    Administracion.setAnimales(pickle.load(fichero_animales))
    fichero_animales.close()

def deserializarCuidadores():
    fichero_cuidadores=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\cuidadores"),"rb")
    Administracion.setCuidadores(pickle.load(fichero_cuidadores))
    fichero_cuidadores.close()

def deserializarHabitats():
    fichero_habitats=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\habitats"),"rb")
    Administracion.setHabitats(pickle.load(fichero_habitats))
    fichero_habitats.close()

def deserializarVeterinarios():
    fichero_veterinarios=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\veterinarios"),"rb")
    Administracion.setVeterinarios(pickle.load(fichero_veterinarios))
    fichero_veterinarios.close()

def deserializarVisitantes():
    fichero_visitantes=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\visitantes"),"rb")
    Administracion.setVisitantes(pickle.load(fichero_visitantes))
    fichero_visitantes.close()