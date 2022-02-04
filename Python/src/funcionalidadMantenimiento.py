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
from excepciones.excepcionPresenciaDatos import ExcepcionPresenciaDatos

class Mantenimiento(Frame):
    
    def __init__(self):
        super().__init__()
        self.jaula = Habitat("Jaulas")

        #Se establecen los nombres y descripciones de la funcionalidad
        nombre = Label(master=self, text="Mantenimiento de Hábitats", font="Helvetica 11 bold")
        info = """Para el mantenimiento del habitat primero seleccione la ID del habitat que quiera revisar y luego podra
elegir el id del cuidador que va el revisar el habitat. La eleccion dell cuidador depende de la especie asignada 
al habitat """
        descripcion= Label(master=self, text= info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=5, pady=5)
        descripcion.pack(fill=BOTH, padx=5, pady=5)
        
        #Se espécifican nombres de critrerios para el FieldFrame
        self.criterios= ["ID Habitat", "ID Cuidador", "Nombre Habitat", "Ambientacion", "Especie", "Nombre Cuidador" ]
        #Se especifican los valores iniciales que van a tener los criterioos del FieldFrame
        self.valores= [False, False, "", "", "", ""]
        #Se epecifican si van ha esta habilitados en caso de que sean widgets tipo entry.
        self.habilitados= [False, False, False, False, False, False]
        #Se da los valores de los widgets combobox que van a haber en el FieldFrame
        IDhabitats= [x.getIdentificacion() for x in Administracion.getHabitats() if x.getNombre() not in ["jaulas", "veterinaria"] ]
        self.combobox= [IDhabitats, [], False, False, False, False]
        #Se crea el FieldFrame con los valores anteriores
        self.dialogos = FieldFrame(self, "Criterios", self.criterios, "Valores", self.valores, self.habilitados, self.combobox)
        self.dialogos.pack(padx=5, pady=5)
        
         #Se crean los botones de aceptar y borrar que estaran abajo del FieldFrame
        aceptar = Button(master=self, text="Aceptar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.aceptar)
        aceptar.pack(side=LEFT, padx=5, pady=5)
        borrar = Button(master=self, text="Borrar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.borrar)
        borrar.pack(side=RIGHT, padx=5, pady=5)
        
        #Se asignan comandos a los combobox
        self.dialogos.getComponente("ID Habitat").bind("<<ComboboxSelected>>", lambda e: self.habitatSeleccionado())
        self.dialogos.getComponente("ID Cuidador").bind("<<ComboboxSelected>>", lambda e: self.cuidadorSeleccionado())
    
    #Funcion que se dispara cuando se selecciona una opcion del combobox de "ID Habitat"
    def habitatSeleccionado(self):
        self.dialogos.getComponente("Nombre Cuidador").configure(state= NORMAL)
        self.dialogos.getComponente("Nombre Cuidador").delete(0,"end")
        self.dialogos.getComponente("Nombre Cuidador").configure(state= DISABLED)
        self.dialogos.getComponente("ID Cuidador")["values"] = []
        self.dialogos.getComponente("ID Cuidador").set("")

        id = int(self.dialogos.getValue("ID Habitat"))
        idCuidadores= [] #Lista que albergara los ids de los cuidadores que puedan hacerse cargo del habitat 
        
        for i in Administracion.getHabitats():
            if id == i.getIdentificacion():
                self.habitatEscogido = i #Se escoge al habitat buscando la id seleccionada en la lista de habitats de la administracion
                break
        
        #Se establecen ciertos valores para los widgets entry que vienen del objeto tipo Habitat escogido
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
        
        #En especial si el habitat no tiene animales asociados a el todavia se el asigna un valor de "Ninguna" al criterio "Especie"
        if self.habitatEscogido.getAnimalesAsociados():
            self.dialogos.getComponente("Especie").insert(0, self.habitatEscogido.getAnimalesAsociados()[0].getEspecie().getNombre())
        else:
            self.dialogos.getComponente("Especie").insert(0, "Ninguna")

        self.dialogos.getComponente("Especie").configure(state= DISABLED)        

        #Si no hay cuidadores que puedan hacerse cargo de la especie asignada al habitat. Se le notifica al usuario.     
        c= 0 #Variable que indicara cuantos cuidadores se pueden hacer cargo del habitat seleccionado.
        for cuidador in Administracion.getCuidadores():
            if cuidador.getEspecieAsignada().getNombre() == self.dialogos.getValue("Especie"):
                idCuidadores.append(cuidador.getIdentificacion()) #Se le agrega a la lista de idCuidadores los id de los cuidadores viables.
                c += 1
        if c == 0: 
            messagebox.showwarning(title="Advertencia",   #Notificacion de que no hay cuidadores viables para el habitat
                                  message="No se ha encontrado ningún cuidador que pueda revisar el habitat.")
        else:
            self.dialogos.getComponente("ID Cuidador")["values"] = idCuidadores

    
    #Funcion que se dispara cuando se selecciona una opcion del combobox de "ID Cuidador"
    def cuidadorSeleccionado(self):
        idCuidador = int(self.dialogos.getValue("ID Cuidador"))
        for cuidador in Administracion.getCuidadores():
            if idCuidador == cuidador.getIdentificacion():
                
                self.cuidadorEscogido = cuidador #Se escoge al cuidador buscando la id seleccionada en la lista de cuidadores de la administracion
                
                #Se Se establece cierto valor para el criterio "Nombre Cuidador" que viene del objeto tipo Cuidador escogido
                self.dialogos.getComponente("Nombre Cuidador").configure(state= NORMAL)
                self.dialogos.getComponente("Nombre Cuidador").delete(0, "end")
                self.dialogos.getComponente("Nombre Cuidador").insert(0, cuidador.getNombre())
                self.dialogos.getComponente("Nombre Cuidador").configure(state= DISABLED)
    
    # Funcion que limipia todos los campos del FieldFrame tanto combobox como entry
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
    
    #Funcion que dispara el boton aceptar
    def aceptar(self):
        idAnimalesTristes = [] #Recogera los animales los cuales no hayan cambiado de estado animo al final del mantenimiento del habitat.
        idHabitat = self.dialogos.getValue("ID Habitat")
        idCuidador = self.dialogos.getValue("ID Cuidador")
        nombreHabitat = self.dialogos.getValue("Nombre Habitat") #Valores de entrada
        ambientacion = self.dialogos.getValue("Ambientacion")
        especie = self.dialogos.getValue("Especie")
        nombreCuidador = self.dialogos.getValue("Nombre Cuidador") 
        valores = [idHabitat, idCuidador, nombreHabitat, ambientacion, especie, nombreCuidador]
        
        #Por medio de la excepcion implementada se verifica que todos los criterios tengan valores de entrada
        try:
            ExcepcionPresenciaDatos.presenciaDatos(self.criterios, valores)
        except ExcepcionPresenciaDatos:
            return

        #Se llama al metodo revisarHabitat usando a el cuidador y el habitat escogidos previamente. Esto con el fin de revisar si el habitat
        #necesita mantenimiento.
        if self.cuidadorEscogido.revisarHabitat(self.habitatEscogido) :
            messagebox.showinfo(title= "Mantenimiento", message= "El cuidador reviso este habitat y no requiere de mantenimiento")
        
        else:
            #Si se requiere mantenimiento, el cuidador mediante el metodo limpiarHabitat hara este.
            mensaje1 = "El cuidador " + self.cuidadorEscogido.getNombre() + " decide sacar a todos los animales del habitat para hacer mantenimiento a este"
            messagebox.showinfo(title= "Traslado a otro habitat", message= mensaje1)
            self.cuidadorEscogido.limpiarHabitat(self.habitatEscogido, self.jaula)
            
            #Se recogen los id de los animales que viven dentro del habitat y que despues del matenimiento no hayan cambiado sus estados de animo.
            for animal in self.habitatEscogido.getAnimalesAsociados():
                if animal.isEstadoAnimo() == False :
                    if animal.getIdentificacion() not in idAnimalesTristes:
                        idAnimalesTristes.append(animal.getIdentificacion())
                
            
            if not idAnimalesTristes :
                #Si no hay animales que esten tristes se le notificara al usuario que el mantenimiento ha sido un exito.
                mensaje2 = "Hacerle mantenimiento al habitat ha dado buenos resultados, no hay animales tristes en este."
                messagebox.showinfo(title= "MANTENIMIENTO EXITOSO", message= mensaje2)
            
            else:
                #Si hay animales tristes se le notificara al usuario de esto y cuales son los que no han cambiado de estado de animo y ademas unas recomendaciones
                mensaje3 = ("Los animales con los siguientes números de identificacion no han mejorado sus estados de ánimo: " + 
                str(idAnimalesTristes) + ".\nPuede solicitar alimentarlos o que los revise un veterinario mediante otros procesos" )
                messagebox.showinfo(title= "MANTENIMIENTO EXITOSO", message= mensaje3)



            


           