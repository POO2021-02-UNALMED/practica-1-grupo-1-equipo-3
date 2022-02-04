"""Deserializador creado por: JOSÉ DAVID CARDONA SOTO
Este módulo fue hecho con la finalidad de crear la función para deserializar los objetos guardados, para
así luego  usados en el main de nuestra aplicación."""

from gestorAplicacion.administracion import Administracion
from gestorAplicacion.animal import Animal
from gestorAplicacion.cuidador import Cuidador
from gestorAplicacion.habitat import Habitat
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.visitante import Visitante
import pickle
import os
import pathlib

#Se llaman a todas las funciones de deserialización
def deserializar():
    deserializarAdministracion()
    deserializarAnimales()
    deserializarCuidadores()
    deserializarHabitats()
    deserializarVeterinarios()
    deserializarVisitantes()

def deserializarAdministracion():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de administracion
    fichero_administracion=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\administracion"),"rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso el valor de la caja de Administración
    Administracion.setCaja(pickle.load(fichero_administracion))
    #Se cierra el archivo abierto
    fichero_administracion.close()

def deserializarAnimales():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de animales
    fichero_animales=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\animales"),"rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de animales
    Administracion.setAnimales(pickle.load(fichero_animales))
    #Se cierra el archivo abierto
    fichero_animales.close()

def deserializarCuidadores():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de cuidadores
    fichero_cuidadores=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\cuidadores"),"rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de cuidadores
    Administracion.setCuidadores(pickle.load(fichero_cuidadores))
    #Se cierra el archivo abierto
    fichero_cuidadores.close()

def deserializarHabitats():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de habitats
    fichero_habitats=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\habitats"),"rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de habitats
    Administracion.setHabitats(pickle.load(fichero_habitats))
    #Se cierra el archivo abierto
    fichero_habitats.close()

def deserializarVeterinarios():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de veterinarios
    fichero_veterinarios=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\veterinarios"),"rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de veterinarios
    Administracion.setVeterinarios(pickle.load(fichero_veterinarios))
    #Se cierra el archivo abierto
    fichero_veterinarios.close()

def deserializarVisitantes():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de visitantes
    fichero_visitantes=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\visitantes"),"rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de visitantes
    Administracion.setVisitantes(pickle.load(fichero_visitantes))
    #Se cierra el archivo abierto
    fichero_visitantes.close()
