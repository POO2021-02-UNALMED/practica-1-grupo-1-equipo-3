from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.animal import Animal
from gestorAplicacion.cuidador import Cuidador

class Curar(Frame):

    #jaula = Habitat("jaula")
    cuidadorEscogido = None
    veterinarioEscogido = None
    animalEscogido = None
    dialogos= None

    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Curar Animales", font="Helvetica 12 bold")
        info = """Para curar un animal primero seleccione el animal enfermo, luego seleccionar el ID del cuidador que 
                  trasladara el animal y luego podra elegir el id del veterinario que va a revisar el animal. 
                  La eleccion del cuidador y veterinario depende de la especie """
        descripcion= Label(master=self, text= info, font="Helvetica 12 bold")
        nombre.pack(fill=BOTH, padx=10, pady=10)
        descripcion.pack(fill=BOTH, padx=10, pady=10)

        criterios= ["ID Animal", "ID Cuidador", "ID Veterinario", "Especie", "Nombre Cuidador", "Nombre Veterinario"]
        valores= [False, False, False, "", "", ""]
        habilitados= [False, False, False, False, False, False]
        animales= [x.getIdentificacion() for x in Administracion.getAnimales()]
        combobox= [animales, [], [], False, False, False]
        Curar.dialogos = FieldFrame(self, "Criterios", criterios, "Valores", valores, habilitados, combobox)
        Curar.dialogos.pack(fill=BOTH, padx=10, pady=10)

        aceptar = Button(master=self, text="Aceptar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=Curar.aceptar)
        aceptar.pack(side=LEFT, padx=10, pady=10)

        borrar = Button(master=self, text="Borrar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=Curar.borrar)
        borrar.pack(side=RIGHT, padx=10, pady=10)

        idAnimalesBox=  Curar.dialogos.getComponente("ID Animal")
        #idCuidadoresBox["state"] = "disabled"
        #Curar.dialogos.getComponente("ID Animal").bind("<<ComboboxSelected>>", Curar.habitatSeleccionado)
        #Curar.dialogos.getComponente("ID Cuidador").bind("<<ComboboxSelected>>", Curar.cuidadorSeleccionado)
        #Curar.dialogos.getComponente("ID Veterinario").bind("<<ComboboxSelected>>", Curar.cuidadorSeleccionado)

    @classmethod
    def aceptar(cls):
        pass

    @classmethod
    def borrar(cls):
        pass

    @classmethod
    def animalSeleccionado(cls, e):
        
        cls.dialogos.getComponente("Nombre Cuidador").configure(state= NORMAL)
        cls.dialogos.getComponente("Nombre Cuidador").delete(0,"end")
        cls.dialogos.getComponente("Nombre Cuidador").configure(state= DISABLED)
        cls.dialogos.getComponente("ID Cuidador")["values"] = []
        cls.dialogos.getComponente("ID Cuidador").set("")
        
        id = int(cls.dialogos.getValue("ID Animal"))
        idCuidadores= []
        
        for i in Administracion.getAnimales():
            if id == i.getIdentificacion():
                cls.animalEscogido = i
                break

        cls.dialogos.getComponente("Especie").configure(state= NORMAL)
        cls.dialogos.getComponente("Especie").delete(0, "end")


        if cls.animalEscogido:
            cls.dialogos.getComponente("Especie").insert(0, cls.habitatEscogido.getAnimalesAsociados()[0].getEspecie().getNombre())
        else:
            cls.dialogos.getComponente("Especie").insert(0, "Ninguna")

        cls.dialogos.getComponente("Especie").configure(state= DISABLED)        
             
        c= 0
        for cuidador in Administracion.getCuidadores():
            if cuidador.getEspecieAsignada().getNombre() == cls.dialogos.getValue("Especie"):
                idCuidadores.append(cuidador.getIdentificacion())
                c += 1
        if c == 0:
            messagebox.showwarning(title="Advertencia",
                                  message="No se ha encontrado ningún cuidador que pueda revisar el habitat.")
        else:
            cls.dialogos.getComponente("ID Cuidador")["values"] = idCuidadores
            #cls.dialogos.getComponente("ID Cuidador")["state"] = "normal"

    
        

        

    
        
        
        
        