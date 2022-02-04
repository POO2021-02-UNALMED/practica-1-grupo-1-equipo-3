# CLASE CREADA POR DAVID MATEO GARCÍA

# En esta clase se realiza la funcionalidad del traslado de animales. Trasladar un animal corresponde a 
# eliminar del sistema el objeto tipo Animal que especifique el usuario.
# 
# Son usadas las clases Especie, Animal y Administración.

from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion
from excepciones.excepcionPresenciaDatos import ExcepcionPresenciaDatos
from excepciones.excepcionTipoInt import ExcepcionTipoInt

class Traslado(Frame):
    
    def __init__(self):
        super().__init__()
        # Se establece el nombre de la funcionalidad y su descripción para ser ambos mostrados en la GUI.
        nombre = Label(master=self, text="Traslado de animales", font="Helvetica 11 bold")
        info = "Para el traslado, se eliminará del sistema al objeto tipo Animal que se haya especificado."
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=5, pady=5)
        descripcion.pack(fill=BOTH, padx=5, pady=5)

        # Se especifican los nombres de los criterios que tendrá el FieldFrame de esta funcionalidad.
        self.criterios = ["Especie", "Identificación", "Hábitat", "Género", "Edad", "Peso"]
        # Se especifican los valores que tendrá el FieldFrame de esta funcionalidad para los criterios anteriormente especificados.
        self.valores = [False, False, "", "", "", ""]
        # Igualmente, se especifican los valores que estarán habilitados para ser editados por el usuario.
        self.habilitados = [True, True, False, False, False, False]
        # Ahora, se especifican las listas de selección que usa la GUI para que el usuario elija entre los valores de la lista.
        self.combobox = [Traslado.especies(), Traslado.animales(), False, False, False, False]
        # Se crea el FieldFrame para esta funcionalidad con los parámetros anteriormente especificados.
        self.dialogos = FieldFrame(self, "Criterios", self.criterios, "Valores", self.valores, self.habilitados, self.combobox)
        self.dialogos.pack(padx=5, pady=5)
        # Se crean además, y debajo del FieldFrame, los botones de Aceptar y Borrar.
        botones = Frame(master=self)
        aceptar = Button(master=botones, text="Aceptar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.aceptar)
        aceptar.pack(side=LEFT, padx=5, pady=5)
        borrar = Button(master=botones, text="Borrar", font="Helvetica 11 bold", 
                         bg="grey", fg="white", borderwidth=3, relief="raised",
                         command=self.borrar)
        borrar.pack(side=RIGHT, padx=5, pady=5)
        botones.pack(padx=5, pady=5)
        # Por último, se asigna el comando para el combobox de Especie y para el combobox de Identificación del animal.
        comboboxEspecie = self.dialogos.getComponente("Especie")
        comboboxEspecie.bind("<<ComboboxSelected>>", lambda e: self.especieSeleccionada())
        comboboxAnimal = self.dialogos.getComponente("Identificación")
        comboboxAnimal.bind("<<ComboboxSelected>>", lambda e: self.animalSeleccionado())
    
    # Por medio del método especieSeleccionada(), cuando se elije una especie de las disponibles por medio de su combobox,
    # el combobox de Identificación listará las identificaciones de los animales que sean solo de dicha especie, 
    # esto a través del método estático animales(especie).
    def especieSeleccionada(self):
        nombreEspecie = self.dialogos.getValue("Especie")
        # Cada vez que se cambia la especie se borrarán todos los campos.
        self.borrar()
        for especie in Administracion.getEspecies():
            if especie.getNombre() == nombreEspecie:
                self.dialogos.getComponente("Identificación").configure(values=Traslado.animales(especie))
                break
        # Además, por cada vez que se cambie la especie seleccionada, como ya se limpiaron todos los demás campos, se vuelve a
        # establecer el combobox de especie con la especie que fue selecionada.
        self.dialogos.getComponente("Especie").set(nombreEspecie)
    
    # Por medio del método animalSeleccionado(), cuando se elije una identificación de las disponibles por medio de su combobox,
    # los campos de Hábitat, Género, Edad y Peso serán llenados con los valores de los atributos del animal seleccionado.      
    def animalSeleccionado(self):
        identificacion = self.dialogos.getValue("Identificación").split("(")[0].strip()
        identificacion = int(identificacion)
        habitat = self.dialogos.getComponente("Hábitat")
        genero = self.dialogos.getComponente("Género")
        edad = self.dialogos.getComponente("Edad")
        peso = self.dialogos.getComponente("Peso")
        for animal in Administracion.getAnimales():
            if animal.getIdentificacion() == identificacion:
                habitat.configure(state=NORMAL)
                habitat.delete(0,"end")
                habitat.insert(0, animal.getHabitat().getNombre())
                habitat.configure(state=DISABLED)
                genero.configure(state=NORMAL)
                genero.delete(0,"end")
                genero.insert(0, animal.getGenero())
                genero.configure(state=DISABLED)
                edad.configure(state=NORMAL)
                edad.delete(0,"end")
                edad.insert(0, str(animal.getEdad()))
                edad.configure(state=DISABLED)
                peso.configure(state=NORMAL)
                peso.delete(0,"end")
                peso.insert(0, str(animal.getPeso()))
                peso.configure(state=DISABLED)
                break

    # Por medio del método borrar() se limpian todos los campos del FieldFrame, tanto combobox como entry.
    def borrar(self):
        self.dialogos.getComponente("Especie").set("")
        self.dialogos.getComponente("Identificación").set("")
        habitat = self.dialogos.getComponente("Hábitat")
        habitat.configure(state=NORMAL)
        habitat.delete(0,"end")
        habitat.configure(state=DISABLED)
        genero = self.dialogos.getComponente("Género")
        genero.configure(state=NORMAL)
        genero.delete(0,"end")
        genero.configure(state=DISABLED)
        edad = self.dialogos.getComponente("Edad")
        edad.configure(state=NORMAL)
        edad.delete(0,"end")
        edad.configure(state=DISABLED)
        peso = self.dialogos.getComponente("Peso")
        peso.configure(state=NORMAL)
        peso.delete(0,"end")
        peso.configure(state=DISABLED)
    
    # Por medio del método aceptar() es que se obtienen los valores actuales de los campos del FieldFrame, más específicamente
    # para este caso la identificación elegida por el usuario, esto para trasladar al animal con dicha identificación.
    def aceptar(self):
        identificacion = self.dialogos.getValue("Identificación").split("(")[0].strip()
        
        # Se hace uso de la excepción sugerida para verificar si el campo de la identificación está lleno (Si ID corresponde a un valor).
        try:
            ExcepcionPresenciaDatos.presenciaDatos(["Identificación"], [identificacion])
        except ExcepcionPresenciaDatos:
            return
        
        # Y por medio de las otra excepcion sugerida para verificar el tipo de dato se comprueba si la identificación
        # no corresponde al tipo de dato que debería.
        try:
            ExcepcionTipoInt.tipoInt(["Identificación"], [identificacion])
        except ExcepcionTipoInt:
            return
        
        # Una vez hechas todas las comprobaciones, se puede proceder a obtener el objeto tipo Animal a trasladar (a borrar).
        for elem in Administracion.getAnimales():
            if elem.getIdentificacion() == int(identificacion):
                animalSeleccionado = elem
                break
    	# Se llama al método trasladarAnimal(...) de la clase Administracion, pues este método se encarga de borrar al objeto tipo
    	# Animal que el usuario seleccionó.
        Administracion.trasladarAnimal(animalSeleccionado)
        messagebox.showinfo(title="Resultado",
                            message="Animal trasladado exitosamente!")
        # Y una vez trasladado el animal se borran todos los campos del FieldFrame y se actualiza la lista de identificaciones
        # disponibles para trasladar, pues se debe excluir al animal que acaba de ser trasladado.
        self.borrar()
        self.dialogos.getComponente("Identificación").configure(values=Traslado.animales())
 
	# A través del método especies() se obtienen los nombres de las especies disponibles.
    @staticmethod
    def especies():
        especies = []
		# El siguiente for obtiene el nombre de cada objeto de Especie almacenado en la lista de especies de Administración
        for especie in Administracion.getEspecies():
            especies.append(especie.getNombre())
        return especies    
 
	# A través del método animales(...) se obtiene el animal que será trasladado.
    @staticmethod
    def animales(especie=None):
        animales = []

        if especie==None:
            # Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administración.
            for animal in Administracion.getAnimales():
                animales.append(str(animal.getIdentificacion()) + " (" + animal.getEspecie().getNombre() + ")")
        else:
            # Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administración.
            for animal in Administracion.getAnimales():
                # Esto se hace para buscar los animales correspondientes a la especie del animal que se va a trasladar, para luego listar 
                # las identificaciones de cada uno de estos animales para que el usuario seleccione uno para trasladar.
                if(animal.getEspecie() == especie):
                    animales.append(str(animal.getIdentificacion()) + " (" + animal.getEspecie().getNombre() + ")")
		
    		# En caso que no haya ni un solo animal de la especie seleccionada, se le informa al usuario.
            if(animales == []):
                messagebox.showwarning(title="Advertencia",
                                       message="No se ha encontrado ningún animal de esta especie que esté disponible para trasladar.")
        return animales