"""Serializador creado por: JOSÉ DAVID CARDONA SOTO
Este módulo fue hecho con la finalidad de crear la función para serilizar los objetos creados, para
así luego poder ser deserializados y usados en el main de nuestra aplicación. Cada tipo de objeto
es serializado por aparte, en su función correspondiente, y luego invocado en la función serializar"""

from gestorAplicacion.administracion import Administracion
import os
import pathlib

import pickle

#Se llaman a todas las funciones de serilización
def serializar():
    serializarAdmin()
    serializarAnimales()
    serializarCuidadores()
    serializarVeterinarios()
    serializarHabitats()
    serializarVisitantes()
    
def serializarAdmin():
    #Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de administracion
    fichero_admin=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\administracion"),"wb") 
    #Indicamos el dato que será serializado. En este caso el valor de la caja de Administración
    pickle.dump(Administracion.getCaja(),fichero_admin)
    #Se cierra el archivo creado
    fichero_admin.close()

def serializarAnimales():
    #Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de animales
    fichero_animales=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\animales"),"wb")
    #Indicamos el dato que será serializado. En este caso la lista de animales del zoológico
    pickle.dump(Administracion.getAnimales(),fichero_animales)
    #Se cierra el archivo creado
    fichero_animales.close()

def serializarCuidadores():
    #Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de cuidadores
    fichero_cuidadores=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\cuidadores"),"wb")
    #Indicamos el dato que será serializado. En este caso la lista de cuidadores del zoológico
    pickle.dump(Administracion.getCuidadores(),fichero_cuidadores)
    #Se cierra el archivo creado
    fichero_cuidadores.close()

def serializarVeterinarios():
    #Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de veterinarios
    fichero_veterinarios=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\veterinarios"),"wb")
    #Indicamos el dato que será serializado. En este caso la lista de veterinarios del zoológico
    pickle.dump(Administracion.getVeterinarios(),fichero_veterinarios)
    #Se cierra el archivo creado
    fichero_veterinarios.close()

def serializarHabitats():
    #Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de habitats
    fichero_habitats=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\habitats"),"wb")
    #Indicamos el dato que será serializado. En este caso la lista de habitats del zoológico
    pickle.dump(Administracion.getHabitats(),fichero_habitats)
    #Se cierra el archivo creado
    fichero_habitats.close()

def serializarVisitantes():
    #Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de visitantes
    fichero_visitantes=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\visitantes"),"wb")
    #Indicamos el dato que será serializado. En este caso la lista de visitants del zoológico
    pickle.dump(Administracion.getVisitantes(),fichero_visitantes)
    #Se cierra el archivo creado
    fichero_visitantes.close()

