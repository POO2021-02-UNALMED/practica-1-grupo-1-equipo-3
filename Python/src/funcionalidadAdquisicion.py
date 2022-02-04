# CLASE CREADA POR DAVID MATEO GARCÍA

# En esta clase se realiza la funcionalidad de la adquisición de animales. Adquirir un animal corresponde a crear 
# un objeto tipo Animal de acuerdo a los atributos que especifique el usuario, esto en base primero a la especie 
# que el usuario haya seleccionado, además de depender que haya un hábitat disponible para crear a dicho animal.
# 
# Son usadas las clases Especie, Habitat, Animal y Administración.

from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame
from gestorAplicacion.administracion import Administracion
from excepciones.excepcionPresenciaDatos import ExcepcionPresenciaDatos
from excepciones.excepcionTipoInt import ExcepcionTipoInt
from excepciones.excepcionTipoFloat import ExcepcionTipoFloat

class Adquisicion(Frame):
    
    def __init__(self):
        super().__init__()
        # Se establece el nombre de la funcionalidad y su descripción para ser ambos mostrados en la GUI.
        nombre = Label(master=self, text="Adquisición de animales", font="Helvetica 11 bold")
        info = """Para la adquisición deberá elegir la Especie de la que se desea adquirir el Animal.
Luego para elegir el hábitat se le presentarán en listado solo los hábitats en los que
habita la especie que se va a adquirir y en los que la cantidad de animales de dicho 
hábitat sea menor a su capacidad máxima. Luego debe especificar los atributos del 
animal a adquirir y este será asignado al hábitat elegido.
        """
        descripcion = Label(master=self, text=info, font="Helvetica 10")
        nombre.pack(fill=BOTH, padx=5, pady=5)
        descripcion.pack(fill=BOTH, padx=5, pady=5)
        
        # Se especifican los nombres de los criterios que tendrá el FieldFrame de esta funcionalidad.
        self.criterios = ["Especie", "Hábitat", "Identificación", "Género", "Edad (Años)", "Peso (Kg)"]
        # Se establece el número de identificación de la especie a adquirir de acuerdo al último número de identificación existente.
        if (Administracion.getAnimales() == []):
            valorID = 1
        else:
            valorID = Administracion.getAnimales()[-1].getIdentificacion() + 1
        # Se especifican los valores que tendrá el FieldFrame de esta funcionalidad para los criterios anteriormente especificados.
        self.valores = [False, False, valorID, False, "", ""]
        # Igualmente, se especifican los valores que estarán habilitados para ser editados por el usuario.
        self.habilitados = [True, True, False, True, True, True]
        # Ahora, se especifican las listas de selección que usa la GUI para que el usuario elija entre los valores de la lista.
        self.combobox = [Adquisicion.especies(), Adquisicion.habitats(), False, ["Macho","Hembra"], False, False]
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
        # Por último, se asigna el comando para el combobox de Especie.
        comboboxEspecie = self.dialogos.getComponente("Especie")
        comboboxEspecie.bind("<<ComboboxSelected>>", lambda e: self.especieSeleccionada())
     
    # Por medio del método especieSeleccionada(), cuando se elije una especie de las disponibles por medio de su combobox,
    # el combobox de Hábitat listará los hábitats solo para dicha especie, esto a través del método estático habitats(especie).
    def especieSeleccionada(self):
        nombreEspecie = self.dialogos.getValue("Especie")
        for especie in Administracion.getEspecies():
            if especie.getNombre() == nombreEspecie:
                especieSeleccionada = especie
                self.dialogos.getComponente("Hábitat").configure(values=Adquisicion.habitats(especie))
                break
        # Además, por cada vez que se cambie la especie seleccionada, se limpiará el valor del hábitat seleccionado.
        self.dialogos.getComponente("Hábitat").set("")
  
    # Por medio del método borrar() se limpian todos los campos del FieldFrame, tanto combobox como entry.
    def borrar(self):
        self.dialogos.getComponente("Especie").set("")
        self.dialogos.getComponente("Hábitat").set("")
        self.dialogos.getComponente("Género").set("")
        self.dialogos.getComponente("Edad (Años)").delete(0,"end")
        self.dialogos.getComponente("Peso (Kg)").delete(0,"end")  
    
    # Por medio del método aceptar() es que se obtienen los valores actuales de los campos del FieldFrame, para adquirir
    # luego un animal con los atributos elegidos por el usuario.
    def aceptar(self):
        nombreEspecie = self.dialogos.getValue("Especie")
        idHabitat = self.dialogos.getValue("Hábitat").split("-")[0].strip()
        identificacion = self.dialogos.getValue("Identificación")
        genero = self.dialogos.getValue("Género")
        edad = self.dialogos.getValue("Edad (Años)")
        peso = self.dialogos.getValue("Peso (Kg)")
        # La lista de valores almacena los valores obtenidos de los campos del FieldFrame para verificar luego que todos
        # los campos se encuentren con algún valor por medio de la excepción sugerida implementada.
        valores = [nombreEspecie, idHabitat, identificacion, genero, edad, peso]
        try:
            ExcepcionPresenciaDatos.presenciaDatos(self.criterios, valores)
        except ExcepcionPresenciaDatos:
            return
        
        # Y por medio de las otras excepciones sugeridas para verificar el tipo de dato se comprueba si alguno de los
        # valores ingresados en alguno de los campos no corresponde al tipo de dato que debería.
        try:
            ExcepcionTipoInt.tipoInt(["Hábitat", "Identificación", "Edad (Años)"], 
                                     [idHabitat, identificacion, edad])
            ExcepcionTipoFloat.tipoFloat(["Peso (Kg)"], [peso])
        except ExcepcionTipoInt:
            return
        except ExcepcionTipoFloat:
            return
        
        # Una vez hechas todas las comprobaciones, se puede proceder a convertir y obtener los datos necesarios para adquirir al animal.
        edad = int(edad)
        peso = float(peso)
        for elem in Administracion.getEspecies():
            if elem.getNombre() == nombreEspecie:
                especie = elem
                break  
        for elem in Administracion.getHabitats():
            if elem.getIdentificacion() == int(idHabitat):
                habitat = elem
                break    
		# Se llama al método adquirirAnimal(...) de la clase Administracion, pues este método se encarga de crear el objeto tipo Animal
		# en base a los atributos que el usuario eligió e ingresó.
        Administracion.adquirirAnimal(especie, habitat, genero, edad, peso);
        messagebox.showinfo(title="Resultado",
                            message="Animal adquirido exitosamente")
        # Y una vez adquirido el animal se borran todos los campos del FieldFrame y se cambia la identificación del siguiente animal a
        # adquirir, para que no se repita y corresponda al orden que se lleva, de acuerdo al ID del último animal adquirido.
        self.borrar()
        identificacion = self.dialogos.getComponente("Identificación")
        identificacion.configure(state=NORMAL)
        identificacion.delete(0,"end")
        identificacion.insert(0, Administracion.getAnimales()[-1].getIdentificacion() + 1)
        identificacion.configure(state=DISABLED)
            
    
	# A través del método especies() se obtienen los nombres de las especies disponibles.
    @staticmethod
    def especies():
        especies = []
		# El siguiente for obtiene el nombre de cada objeto de Especie almacenado en la lista de especies de Administración
        for especie in Administracion.getEspecies():
            especies.append(especie.getNombre())
        return especies
	
	# A través del método habitat(...) se obtiene la identificación y el nombre de los hábitats disponibles para depositado al animal a adquirir.
    @staticmethod
    def habitats(especie=None):
        habitats = []
        if especie==None:
    		# Con el siguiente for se obtienen cada uno de los hábitats almacenandos en la lista de habitats de la clase Administración.
            for habitat in Administracion.getHabitats():
                if habitat.getNombre() == "Veterinaria":
                    continue
                elif habitat.getNombre() == "Jaulas":
                    continue
                elif habitat.getEspecie() != None and habitat.cantidadAnimales() < habitat.getCapacidadMaxima():
                    habitats.append(str(habitat.getIdentificacion()) + " - " + habitat.getAmbientacion() + " " + habitat.getNombre() + " (" + habitat.getEspecie().getNombre() + ")")
                elif habitat.getEspecie() == None:
                    habitats.append(str(habitat.getIdentificacion()) + " - " + habitat.getAmbientacion() + " " + habitat.getNombre() + " (Sin Especie)")
        else:
    		# Con el siguiente for se obtienen cada uno de los hábitats almacenandos en la lista de habitats de la clase Administración.
            for habitat in Administracion.getHabitats():
                if habitat.getNombre() == "Veterinaria":
                    continue
                elif habitat.getNombre() == "Jaulas":
                    continue
                # Esto se hace para buscar de manera efectiva los hábitats que puedan contener la especie del animal que se va a adquirir,
                # para listar los datos de cada uno de estos hábitats para que el usuario seleccione uno.
                if habitat.getEspecie() == especie and habitat.cantidadAnimales() < habitat.getCapacidadMaxima():
                    habitats.append(str(habitat.getIdentificacion()) + " - " + habitat.getAmbientacion() + " " + habitat.getNombre() + " (" + habitat.getEspecie().getNombre() + ")")
                elif habitat.getEspecie() == None and habitat.cantidadAnimales() < habitat.getCapacidadMaxima():
                    habitats.append(str(habitat.getIdentificacion()) + " - " + habitat.getAmbientacion() + " " + habitat.getNombre() + " (Sin Especie)")
            # En caso que no haya ni un hábitat para depositar al animal, se le informa al usuario.
            if(habitats == []):
                messagebox.showwarning(title="Advertencia",
                                       message="No se ha encontrado ningún hábitat disponible para depositar al animal.")
        return habitats