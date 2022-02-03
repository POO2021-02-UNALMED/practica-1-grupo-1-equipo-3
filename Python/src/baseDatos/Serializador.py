from gestorAplicacion.administracion import Administracion

import pickle

def serializar():
    serializarAdmin()
    serializarAnimales()
    serializarCuidadores()
    serializarVeterinarios()
    serializarHabitats()
    serializarVisitantes()
    
def serializarAdmin():
    admin=Administracion(0)
    fichero_admin=open("admin","wb")
    pickle.dump(admin,fichero_admin)
    fichero_admin.close()

def serializarAnimales():
    fichero_animales=open("animales","wb")
    pickle.dump(Administracion.getAnimales(),fichero_animales)
    fichero_animales.close()

def serializarCuidadores():
    fichero_cuidadores=open("cuidadores","wb")
    pickle.dump(Administracion.getCuidadores(),fichero_cuidadores)
    fichero_cuidadores.close()

def serializarVeterinarios():
    fichero_veterinarios=open("veterinarios","wb")
    pickle.dump(Administracion.getVeterinarios(),fichero_veterinarios)
    fichero_veterinarios.close()

def serializarHabitats():
    fichero_habitats=open("habitats","wb")
    pickle.dump(Administracion.getHabitats(),fichero_habitats)
    fichero_habitats.close()

def serializarVisitantes():
    fichero_visitantes=open("visitantes","wb")
    pickle.dump(Administracion.getVisitantes(),fichero_visitantes)
    fichero_visitantes.close()

