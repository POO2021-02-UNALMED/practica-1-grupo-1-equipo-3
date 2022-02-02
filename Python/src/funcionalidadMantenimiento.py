#CLASE CREADA POR MATEO CARVAJAL SÁNCHEZ

#En esta clase se realiza la funcionalidad de mantenimeinto de habitat. el mantenimiento 
# de un habitat corresponde a elegir un objeto tipo habitat que se quiera revisar , luego
#dependiendo del habitat escogido se podra escoger de entre unos cuantos objetos tipo cuidador 
#para que revisen el habitat.


#from gestorAplicacion.animalesZoologico.animal import Animal
from cgitb import text
from email import message
from gestorAplicacion.habitat import Habitat
#from gestorAplicacion.gestionZoologico.cuidador import Cuidador
from gestorAplicacion.administracion import Administracion
#from main import Main, descripcion
from tkinter import *
from fieldFrame import FieldFrame
from tkinter import messagebox


class Mantenimiento(Frame):

    jaula = Habitat("jaula")
    cuidadorEscogido = None
    habitatEscogido = None
    dialogos= None
    
    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Mantenimiento de Hábitats", font="Helvetica 12 bold")
        info = """Para el mantenimiento del habitat primero seleccione la ID del habitat que quiera revisar y luego podra
         elegir el id del cuidador que va el revisar el habitat. La eleccion dell cuidador depende de la especie asignada 
         al habitat """
        descripcion= Label(master=self, text= info, font="Helvetica 12 bold")
        nombre.pack(fill=BOTH, padx=10, pady=10)
        descripcion.pack(fill=BOTH, padx=10, pady=10)

        criterios= ["ID Habitat", "ID Cuidador","Nombre Habitat", "Ambientacion", "Especie", "Nombre Cuidador" ]
        valores= [False, False, "", "", "", ""]
        habilitados= [False, False, False, False, False, False]
        IDhabitats= [x.getIdentificacion() for x in Administracion.getHabitats() ]
        combobox= [IDhabitats, [], False, False, False, False]
        Mantenimiento.dialogos = FieldFrame(self, "Criterios", criterios, "Valores", valores, habilitados, combobox)
        Mantenimiento.dialogos.pack(fill=BOTH, padx=10, pady=10)
        aceptar = Button(master=self, text="Aceptar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=Mantenimiento.aceptar)
        aceptar.pack(side=LEFT, padx=10, pady=10)
        borrar = Button(master=self, text="Borrar", font="Helvetica 12 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=Mantenimiento.borrar)
        borrar.pack(side=RIGHT, padx=10, pady=10)
        idCuidadoresBox=  Mantenimiento.dialogos.getComponente("ID Cuidador")
        #idCuidadoresBox["state"] = "disabled"
        Mantenimiento.dialogos.getComponente("ID Habitat").bind("<<ComboboxSelected>>", Mantenimiento.habitatSeleccionado)
        Mantenimiento.dialogos.getComponente("ID Cuidador").bind("<<ComboboxSelected>>", Mantenimiento.cuidadorSeleccionado)

    
    
   

    @classmethod
    def habitatSeleccionado(cls, e):
        cls.dialogos.getComponente("Nombre Cuidador").configure(state= NORMAL)
        cls.dialogos.getComponente("Nombre Cuidador").delete(0,"end")
        cls.dialogos.getComponente("Nombre Cuidador").configure(state= DISABLED)
        cls.dialogos.getComponente("ID Cuidador")["values"] = []
        cls.dialogos.getComponente("ID Cuidador").set("")

        id = int(cls.dialogos.getValue("ID Habitat"))
        idCuidadores= []
        
        for i in Administracion.getHabitats():
            if id == i.getIdentificacion():
                cls.habitatEscogido = i
                break
        
        cls.dialogos.getComponente("Nombre Habitat").configure(state= NORMAL)
        cls.dialogos.getComponente("Nombre Habitat").delete(0,"end")
        cls.dialogos.getComponente("Nombre Habitat").insert(0, cls.habitatEscogido.getNombre())
        cls.dialogos.getComponente("Nombre Habitat").configure(state= DISABLED)
        cls.dialogos.getComponente("Ambientacion").configure(state= NORMAL)
        cls.dialogos.getComponente("Ambientacion").delete(0,"end")
        cls.dialogos.getComponente("Ambientacion").insert(0, cls.habitatEscogido.getAmbientacion())
        cls.dialogos.getComponente("Ambientacion").configure(state= DISABLED)
        cls.dialogos.getComponente("Especie").configure(state= NORMAL)
        cls.dialogos.getComponente("Especie").delete(0, "end")
        
        if cls.habitatEscogido.getAnimalesAsociados():
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
                
                


    @classmethod
    def cuidadorSeleccionado(cls, e):
        idCuidador = int(cls.dialogos.getValue("ID Cuidador"))
        for cuidador in Administracion.getCuidadores():
            if idCuidador == cuidador.getIdentificacion():
                cls.cuidadorEscogido = cuidador
                cls.dialogos.getComponente("Nombre Cuidador").configure(state= NORMAL)
                cls.dialogos.getComponente("Nombre Cuidador").delete(0, "end")
                cls.dialogos.getComponente("Nombre Cuidador").insert(0, cuidador.getNombre())
                cls.dialogos.getComponente("Nombre Cuidador").configure(state= DISABLED)

    @classmethod
    def borrar(cls):
        cls.dialogos.getComponente("ID Habitat").set("")
        cls.dialogos.getComponente("ID Cuidador").set("")
        cls.dialogos.getComponente("Nombre Habitat").configure(state= NORMAL)
        cls.dialogos.getComponente("Nombre Habitat").delete(0, "end")
        cls.dialogos.getComponente("Nombre Habitat").configure(state= DISABLED)
        cls.dialogos.getComponente("Ambientacion").configure(state= NORMAL)
        cls.dialogos.getComponente("Ambientacion").delete(0, "end")
        cls.dialogos.getComponente("Ambientacion").configure(state= DISABLED)
        cls.dialogos.getComponente("Especie").configure(state= NORMAL)
        cls.dialogos.getComponente("Especie").delete(0, "end")
        cls.dialogos.getComponente("Especie").configure(state= DISABLED)
        cls.dialogos.getComponente("Nombre Cuidador").configure(state= NORMAL)
        cls.dialogos.getComponente("Nombre Cuidador").delete(0, "end")
        cls.dialogos.getComponente("Nombre Cuidador").configure(state= DISABLED)
    
    classmethod

        
    
 
    
    @classmethod
    def aceptar(cls):
        idAnimalesTristes = [] #Recogera los animales los cuales no hayan cambiado de estado animo al final del mantenimiento del habitat.

        #Se llama al metodo revisarHabitat usando a el cuidador y el habitat escogidos previamente. Esto con el fin de revisar si el habitat
        #necesita mantenimiento.
        if cls.cuidadorEscogido.revisarHabitat(cls.habitatEscogido) :
            messagebox.showinfo(title= "Mantenimiento", message= "El cuidador reviso este habitat y no requiere de mantenimiento")
        
        else:
            
            mensaje1 = "El cuidador " + cls.cuidadorEscogido.getNombre() + " decide sacar a todos los animales del habitat para hacer mantenimiento a este"
            messagebox.showinfo(title= "Traslado a otro habitat", message= mensaje1)
            cls.cuidadorEscogido.limpiarHabitat(cls.habitatEscogido, cls.jaula)

            for animal in cls.habitatEscogido.getAnimalesAsociados():
                if animal.isEstadoAnimo() == False :
                    if animal.getIdentificacion() not in idAnimalesTristes:
                        idAnimalesTristes.append(animal.getIdentificacion())
                
            
            if not idAnimalesTristes :
                
                mensaje2 = "Hacerle mantenimiento al habitat ha dado buenos resultados, no hay animales tristes en este."
                messagebox.showinfo(title= "MANTENIMIENTO EXITOSO", message= mensaje2)
            
            else:
                
                mensaje3 = ("Los animales con los siguientes números de identificacion no han mejorado sus estados de ánimo: " + 
                str(idAnimalesTristes) + ".\nPuede solicitar alimentarlos o que los revise un veterinario mediante otros procesos" )
                messagebox.showinfo(title= "MANTENIMIENTO EXITOSO", message= mensaje3)



            


           