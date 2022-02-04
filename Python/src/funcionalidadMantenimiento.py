#CLASE CREADA POR MATEO CARVAJAL SÁNCHEZ

#En esta clase se realiza la funcionalidad de mantenimeinto de habitat. el mantenimiento 
# de un habitat corresponde a elegir un objeto tipo habitat que se quiera revisar , luego
#dependiendo del habitat escogido se podra escoger de entre unos cuantos objetos tipo cuidador 
#para que revisen el habitat.


from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.habitat import Habitat
from gestorAplicacion.administracion import Administracion

class Mantenimiento(Frame):
    
    def __init__(self):
        super().__init__()
        self.jaula = Habitat("Jaulas")
        
        nombre = Label(master=self, text="Mantenimiento de Hábitats", font="Helvetica 11 bold")
        info = """Para el mantenimiento del habitat primero seleccione la ID del habitat que quiera revisar y luego podra
elegir el id del cuidador que va el revisar el habitat. La eleccion dell cuidador depende de la especie asignada 
al habitat """
        descripcion= Label(master=self, text= info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=5, pady=5)
        descripcion.pack(fill=BOTH, padx=5, pady=5)

        self.criterios= ["ID Habitat", "ID Cuidador", "Nombre Habitat", "Ambientacion", "Especie", "Nombre Cuidador" ]
        self.valores= [False, False, "", "", "", ""]
        self.habilitados= [False, False, False, False, False, False]
        IDhabitats= [x.getIdentificacion() for x in Administracion.getHabitats() ]
        self.combobox= [IDhabitats, [], False, False, False, False]
        self.dialogos = FieldFrame(self, "Criterios", self.criterios, "Valores", self.valores, self.habilitados, self.combobox)
        self.dialogos.pack(padx=5, pady=5)
        aceptar = Button(master=self, text="Aceptar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.aceptar)
        aceptar.pack(side=LEFT, padx=5, pady=5)
        borrar = Button(master=self, text="Borrar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.borrar)
        borrar.pack(side=RIGHT, padx=5, pady=5)
        self.dialogos.getComponente("ID Habitat").bind("<<ComboboxSelected>>", lambda e: self.habitatSeleccionado())
        self.dialogos.getComponente("ID Cuidador").bind("<<ComboboxSelected>>", lambda e: self.cuidadorSeleccionado())

    def habitatSeleccionado(self):
        self.dialogos.getComponente("Nombre Cuidador").configure(state= NORMAL)
        self.dialogos.getComponente("Nombre Cuidador").delete(0,"end")
        self.dialogos.getComponente("Nombre Cuidador").configure(state= DISABLED)
        self.dialogos.getComponente("ID Cuidador")["values"] = []
        self.dialogos.getComponente("ID Cuidador").set("")

        id = int(self.dialogos.getValue("ID Habitat"))
        idCuidadores= []
        
        for i in Administracion.getHabitats():
            if id == i.getIdentificacion():
                self.habitatEscogido = i
                break
        
        self.dialogos.getComponente("Nombre Habitat").configure(state= NORMAL)
        self.dialogos.getComponente("Nombre Habitat").delete(0,"end")
        self.dialogos.getComponente("Nombre Habitat").insert(0, self.habitatEscogido.getNombre())
        self.dialogos.getComponente("Nombre Habitat").configure(state= DISABLED)
        self.dialogos.getComponente("Ambientacion").configure(state= NORMAL)
        self.dialogos.getComponente("Ambientacion").delete(0,"end")
        self.dialogos.getComponente("Ambientacion").insert(0, self.habitatEscogido.getAmbientacion())
        self.dialogos.getComponente("Ambientacion").configure(state= DISABLED)
        self.dialogos.getComponente("Especie").configure(state= NORMAL)
        self.dialogos.getComponente("Especie").delete(0, "end")
        
        if self.habitatEscogido.getAnimalesAsociados():
            self.dialogos.getComponente("Especie").insert(0, self.habitatEscogido.getAnimalesAsociados()[0].getEspecie().getNombre())
        else:
            self.dialogos.getComponente("Especie").insert(0, "Ninguna")

        self.dialogos.getComponente("Especie").configure(state= DISABLED)        
             
        c= 0
        for cuidador in Administracion.getCuidadores():
            if cuidador.getEspecieAsignada().getNombre() == self.dialogos.getValue("Especie"):
                idCuidadores.append(cuidador.getIdentificacion())
                c += 1
        if c == 0:
            messagebox.showwarning(title="Advertencia",
                                  message="No se ha encontrado ningún cuidador que pueda revisar el habitat.")
        else:
            self.dialogos.getComponente("ID Cuidador")["values"] = idCuidadores

    def cuidadorSeleccionado(self):
        idCuidador = int(self.dialogos.getValue("ID Cuidador"))
        for cuidador in Administracion.getCuidadores():
            if idCuidador == cuidador.getIdentificacion():
                self.cuidadorEscogido = cuidador
                self.dialogos.getComponente("Nombre Cuidador").configure(state= NORMAL)
                self.dialogos.getComponente("Nombre Cuidador").delete(0, "end")
                self.dialogos.getComponente("Nombre Cuidador").insert(0, cuidador.getNombre())
                self.dialogos.getComponente("Nombre Cuidador").configure(state= DISABLED)

    def borrar(self):
        self.dialogos.getComponente("ID Habitat").set("")
        self.dialogos.getComponente("ID Cuidador").set("")
        self.dialogos.getComponente("Nombre Habitat").configure(state= NORMAL)
        self.dialogos.getComponente("Nombre Habitat").delete(0, "end")
        self.dialogos.getComponente("Nombre Habitat").configure(state= DISABLED)
        self.dialogos.getComponente("Ambientacion").configure(state= NORMAL)
        self.dialogos.getComponente("Ambientacion").delete(0, "end")
        self.dialogos.getComponente("Ambientacion").configure(state= DISABLED)
        self.dialogos.getComponente("Especie").configure(state= NORMAL)
        self.dialogos.getComponente("Especie").delete(0, "end")
        self.dialogos.getComponente("Especie").configure(state= DISABLED)
        self.dialogos.getComponente("Nombre Cuidador").configure(state= NORMAL)
        self.dialogos.getComponente("Nombre Cuidador").delete(0, "end")
        self.dialogos.getComponente("Nombre Cuidador").configure(state= DISABLED)

    def aceptar(self):
        idAnimalesTristes = [] #Recogera los animales los cuales no hayan cambiado de estado animo al final del mantenimiento del habitat.

        #Se llama al metodo revisarHabitat usando a el cuidador y el habitat escogidos previamente. Esto con el fin de revisar si el habitat
        #necesita mantenimiento.
        if self.cuidadorEscogido.revisarHabitat(self.habitatEscogido) :
            messagebox.showinfo(title= "Mantenimiento", message= "El cuidador reviso este habitat y no requiere de mantenimiento")
        
        else:
            
            mensaje1 = "El cuidador " + self.cuidadorEscogido.getNombre() + " decide sacar a todos los animales del habitat para hacer mantenimiento a este"
            messagebox.showinfo(title= "Traslado a otro habitat", message= mensaje1)
            self.cuidadorEscogido.limpiarHabitat(self.habitatEscogido, self.jaula)

            for animal in self.habitatEscogido.getAnimalesAsociados():
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
        
        self.borrar()



            


           