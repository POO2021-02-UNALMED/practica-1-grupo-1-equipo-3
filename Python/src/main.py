# main.py
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from funcionalidadMantenimiento import Mantenimiento
from funcionalidadCurar import Curar
from funcionalidadCuidar import Cuidar
from funcionalidadAdquisicion import Adquisicion
from funcionalidadTraslado import Traslado
from funcionalidadGestion import Gestion
from funcionalidadDespedir import Despedir
from funcionalidadContratar import Contratar
from funcionalidadConstruir import Construir
from funcionalidadDatosTrabajadores import Trabajador
from funcionalidadDatosAnimales import Animales
from funcionalidadDatosHabitats import Habitats
from funcionalidadDatosVisitantes import Visitantes
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.animal import Animal
from gestorAplicacion.cuidador import Cuidador
from gestorAplicacion.especie import Especie
from gestorAplicacion.habitat import Habitat
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.visitante import Visitante
from baseDatos.deserializador import *
from baseDatos.serializador import *
from excepciones.excepcionPresenciaArchivo import ExcepcionPresenciaArchivos


# Funcion inicio que verifica que existan los archivos donde va a actuar el deserializador y serializador
def inicio():
    try:
        ExcepcionPresenciaArchivos.presenciaArchivos(["baseDatos\\temp\\administracion", "baseDatos\\temp\\animales", 
        "baseDatos\\temp\\cuidadores","baseDatos\\temp\\habitats", "baseDatos\\temp\\veterinarios", "baseDatos\\temp\\visitantes"] )
        deserializar()
    except ExcepcionPresenciaArchivos:
        return

inicio()

# A continuación se encuentran los objetos que fueron guardados originalmente en la persistencia inicial.

"""a = Habitat("H1", "Pradera", 2)
    b = Habitat("H2", "Jungla", 1)
    c= Habitat("H3", "Pantano", 3)
    d= Habitat("H5", "Rio", 3)
    e= Habitat("H6","Pantano",2)
    a1 = Animal(Especie.REPTIL, c, "Macho", 5, 70.0)
    a2 = Animal(Especie.REPTIL, c, "Hembra", 4, 65.0)
    a2.setAlimentado(False)
    a2.setEstadoAnimo(False)
    a3 = Animal(Especie.ANFIBIO,e,"Macho",2,20.0)
    a4 = Animal(Especie.ANFIBIO,e,"Hembra",2,15.0)
    a3.setEstadoAnimo(False)
    a4.setEstadoAnimo(False)
    a3.setAlimentado(False)
    a4.setEstadoSalud(False)
    a5 = Animal(Especie.PEZ,d,"Macho",2,20.0)
    a6 = Animal(Especie.PEZ,d,"Macho",1,15.0)
    a7 = Animal(Especie.PEZ,d,"Hembra",1,20.0)
    d.setLimpio(False)
    a5.setEstadoAnimo(False)
    a6.setEstadoAnimo(False)
    a7.setEstadoAnimo(False)
    a7.setAlimentado(False)
    a5.setAlimentado(False)
    a5.setEstadoSalud(False)
    a6.setEstadoSalud(False)
    a8 = Animal(Especie.ANFIBIO,b,"Hembra",1,20.0)
    c1 = Cuidador("Jorge", 7000, Especie.MAMIFERO)
    c2 = Cuidador("Johanna", 1000, Especie.AVE)
    c3 = Cuidador("Camila", 100000, Especie.REPTIL)
    c4 = Cuidador("David", 10000, Especie.PEZ)
    c5 = Cuidador("Juan", 5000, Especie.ANFIBIO)
    v1 = Veterinario("Elva",10000,Especie.ANFIBIO)
    v2 = Veterinario("Francisco",12000,Especie.PEZ)
    vi1 = Visitante("Jose",3,15)
    vi2 = Visitante("Diego",5,30)
    vi3 = Visitante("Valeria",6,30)"""

ventana = Tk()
ventana.title("Sistema gestor de zoológico")
ventana.geometry("+10+10")
ventana.resizable(False, False)
ventana.option_add("*tearOff", FALSE)
#ventana.iconbitmap("../Imagenes/Z.ico")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# Con la siguiente función se ocultan todos los frames de la aplicación, esto para la correcta transición entre menús.
def ocultarTodo():
    ventanaInicio.pack_forget()
    ventanaUsuario.pack_forget()
    ventanaMantenimiento.pack_forget()
    ventanaCurar.pack_forget()
    ventanaCuidar.pack_forget()
    ventanaAdquision.pack_forget()
    ventanaTraslado.pack_forget()
    ventanaGestion.pack_forget()
    ventanaDespedir.pack_forget()
    ventanaContratar.pack_forget()
    ventanaConstruir.pack_forget()
    ventanaTrabajador.pack_forget()
    ventanaAnimales.pack_forget()
    ventanaHabitats.pack_forget()
    ventanaVisitantes.pack_forget()

# Con la siguiente función se borran los campos de FieldFrame para todas las funcionalidades, además que se ocultan
# todas las tablas Treeview de las funcionalidades de consulta.
def borrarTodo():
    ventanaMantenimiento.borrar()
    ventanaCurar.borrar()
    ventanaCuidar.borrar()
    ventanaAdquision.borrar()
    ventanaTraslado.borrar()
    #ventanaGestion.borrar()
    ventanaDespedir.borrar()
    ventanaContratar.borrar()
    ventanaConstruir.borrar()
    ventanaTrabajador.ocultarTabla()
    ventanaAnimales.ocultarTabla()
    ventanaHabitats.ocultarTabla()
    ventanaVisitantes.ocultarTabla()

# COMANDOS RELATIVOS A LA VENTANA DE INICIO:

# Con estas variables se define la hoja de vida de los autores de la aplicación que será mostrada en la ventana de Inicio.
VidaDavid="""Nombre: David Mateo García Vallejo"""
VidaJose="""Nombre: José David Cardona Soto"""
VidaJuan="""Nombre: Juan José Monsalve Marín"""
VidaMateo="""Nombre: Mateo Carvajal Sánchez"""

# Por medio de la siguiente función se cambia la imagen relativa al sistema (Imágenes de animales).
posicionImagen=1
def cambiarImagen(e):
    global posicionImagen
    posicionImagen += 1
    if posicionImagen == 6:
        posicionImagen = 1
    FotoAnimal=(Image.open("Imagenes/Animales/" + str(posicionImagen) + ".jpg")).resize((400,400), Image.ANTIALIAS)
    FotoAnimal = ImageTk.PhotoImage(FotoAnimal)
    """LabelFotoAnimal.configure(image=FotoAnimal)
    LabelFotoAnimal.image=FotoAnimal"""

# Por medio de la siguiente función se cambia la hoja de vida y las imágenes asociadas a cada autor de la aplicación.
posicionVida=0
def cambiarVida(e):
    global posicionVida
    posicionVida += 1
    if posicionVida == 4:
        posicionVida = 0
    ListaFotos=["David","Jose","Juan","Mateo"]
    Foto1 =(Image.open("Imagenes/" + ListaFotos[posicionVida] + "/1.jpg")).resize((200,200), Image.ANTIALIAS)
    Foto1 = ImageTk.PhotoImage(Foto1)
    Foto2 =(Image.open("Imagenes/" + ListaFotos[posicionVida] + "/2.jpg")).resize((200,200), Image.ANTIALIAS)
    Foto2 = ImageTk.PhotoImage(Foto2)
    Foto3 =(Image.open("Imagenes/" + ListaFotos[posicionVida] + "/3.jpg")).resize((200,200), Image.ANTIALIAS)
    Foto3 = ImageTk.PhotoImage(Foto3)
    Foto4 =(Image.open("Imagenes/" + ListaFotos[posicionVida] + "/4.jpg")).resize((200,200), Image.ANTIALIAS)
    Foto4 = ImageTk.PhotoImage(Foto4)
    """LabelFoto1.configure(image=Foto1)
    LabelFoto1.image=Foto1
    LabelFoto2.configure(image=Foto2)
    LabelFoto2.image=Foto2
    LabelFoto3.configure(image=Foto3)
    LabelFoto3.image=Foto3
    LabelFoto4.configure(image=Foto4)
    LabelFoto4.image=Foto4"""
    if posicionVida==0:
        CuerpoVida.config(text=VidaDavid)
    elif posicionVida==1:
        CuerpoVida.config(text=VidaJose)
    elif posicionVida==2:
        CuerpoVida.config(text=VidaJuan)
    elif posicionVida==3:
        CuerpoVida.config(text=VidaMateo)

# La siguiente función es llamada cuando se accede al menú de "Descripción" de la ventana de Inicio. Por medio de esta
# se muestra al usuario la descripción de la aplicación.
def descripcion():
    descripcion = "En el sistema gestor de zoológico podrá administrar todo lo que tiene que ver con su zoológico: Calcular las ganancias del día; pagar a sus empleados; llevar conteo de los visitantes, de los animales, de los empleados, de las especies, y de los hábitats."
    messagebox.showinfo(title="Descripción de la aplicación",
                        message=descripcion)

# La siguiente función es llamada cuando se accede al menú de "Salir" de la ventana de Inicio. Por medio de esta es que
# antes de cerrarse la ventana se serializan los objetos.
def salirInicio():
    salir = messagebox.askyesno(title="Salir",
                                message="¿Confirma que desea salir de la aplicación?",
                                detail="Clic en Sí para salir")
    if salir:
        serializar()
        ventana.destroy()
        serializar()

# La siguiente función es llamada cuando se presiona el botón Ingresar de la ventana de Inicio. Por medio de esta
# el usuario puede acceder a la ventana de Usuario, desde donde puede hacer uso de las distintas funcionalidades.
def ingresar():
    ocultarTodo()
    borrarTodo()
    ventanaUsuario.pack()
    ventana["menu"] = menuVentanaUsuario

# COMANDOS RELATIVOS A LA VENTANA DEL USUARIO:

# La función mantenimiento() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad.
def mantenimiento():
    ocultarTodo()
    borrarTodo()
    ventanaMantenimiento.pack()

# La función curar() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad.
def curar():
    ocultarTodo()
    borrarTodo()
    ventanaCurar.pack()

# La función cuidar() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad.
def cuidar():
    ocultarTodo()
    borrarTodo()
    ventanaCuidar.pack()

# La función adquisicion() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad.
def adquisicion():
    ocultarTodo()
    borrarTodo()
    ventanaAdquision.pack()

# La función traslado() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad.
def traslado():
    ocultarTodo()
    borrarTodo()
    ventanaTraslado.pack()

# La función gestion() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad.
def gestion():
    ocultarTodo()
    borrarTodo()
    ventanaGestion.pack()

# La función despedir() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad.
def despedir():
    ocultarTodo()
    borrarTodo()
    ventanaDespedir.pack()

# La función contratar() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad (Crear Empleados).
def contratar():
    ocultarTodo()
    borrarTodo()
    ventanaContratar.pack()

# La función construir() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad (Crear Hábitat).
def construir():
    ocultarTodo()
    borrarTodo()
    ventanaConstruir.pack()

# La función trabajador() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad (Consultar Empleados).
def trabajador():
    ocultarTodo()
    borrarTodo()
    ventanaTrabajador.pack()

# La función animales() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad (Consultar Animales).
def animales():
    ocultarTodo()
    borrarTodo()
    ventanaAnimales.pack()

# La función habitats() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad (Consultar Hábitats).
def habitats():
    ocultarTodo()
    borrarTodo()
    ventanaHabitats.pack()

# La función visitantes() sirve para hacer la transición desde el menú a la ventana de dicha funcionalidad (Consultar Visitantes).
def visitantes():
    ocultarTodo()
    borrarTodo()
    ventanaVisitantes.pack()

# La siguiente función es llamada cuando se accede al menú de "Aplicación" de la ventana de Usuario. Por medio de esta
# se muestra al usuario NUEVAMENTE la descripción de la aplicación.
def aplicacion():
    descripcion = "En el sistema gestor de zoológico podrá administrar todo lo que tiene que ver con su zoológico: Calcular las ganancias del día; pagar a sus empleados; llevar conteo de los visitantes, de los animales, de los empleados, de las especies, y de los hábitats."
    messagebox.showinfo(title="Información básica de la aplicación",
                        message=descripcion)

# La siguiente función es llamada cuando se accede al menú de "Salir" de la ventana de Usuario. Por medio de esta
# se regresa a la ventana de Inicio.
def salirUsuario():
    salir = messagebox.askyesno(title="Salir",
                                message="¿Confirma que desea regresar a la ventana de inicio?",
                                detail="Clic en Sí para regresar")
    if salir:
        ocultarTodo()
        ventanaInicio.pack()
        ventana["menu"] = menuVentanaInicio

# La siguiente función es llamada cuando se accede al menú de "Acerca De" de la ventana de Usuario. Por medio de esta
# se muestra al usuario los autores de la aplicación.
def ayuda():
    autores = """Autores:

- David Mateo García Vallejo
- José David Cardona Soto
- Juan José Monsalve Marín
- Mateo Carvajal Sánchez
    """
    messagebox.showinfo(title="Acerca de la aplicación",
                        message=autores) 

# COMPONENTES DEL MENÚ DE LA VENTANA DE INICIO:

menuVentanaInicio = Menu(ventana, font="Helvetica 12 bold", fg="red")
menuInicio = Menu(menuVentanaInicio, font="Helvetica 12",)
menuVentanaInicio.add_cascade(menu=menuInicio, label="Inicio")
menuInicio.add_command(label="Descripción", command=descripcion)
menuInicio.add_command(label="Salir", command=salirInicio)
ventana["menu"] = menuVentanaInicio

# COMPONENTES DEL MENÚ DE LA VENTANA DEL USUARIO:

menuVentanaUsuario = Menu(ventana, font="Helvetica 12 bold")
menuArchivo = Menu(menuVentanaUsuario, font="Helvetica 12")
menuVentanaUsuario.add_cascade(menu=menuArchivo, label="Archivo")
menuArchivo.add_command(label="Aplicación", command=aplicacion)
menuArchivo.add_command(label="Salir", command=salirUsuario)
menuProcesos = Menu(menuVentanaUsuario, font="Helvetica 12")
menuVentanaUsuario.add_cascade(menu=menuProcesos, label="Procesos y consultas")
menuProcesos.add_command(label="Mantenimiento de hábitats", command=mantenimiento)
menuProcesos.add_command(label="Curar animales", command=curar)
menuProcesos.add_command(label="Cuidar animales", command=cuidar)
menuAdquisicionTraslado = Menu(menuProcesos, font="Helvetica 12")
menuProcesos.add_cascade(menu=menuAdquisicionTraslado, label="Adquisición y traslado de animales")
menuAdquisicionTraslado.add_command(label="Adquirir animales", command=adquisicion)
menuAdquisicionTraslado.add_command(label="Trasladar animales", command=traslado)
menuProcesos.add_command(label="Gestión administrativa", command=gestion)

menuOtras = Menu(menuProcesos, font="Helvetica 12")
menuProcesos.add_cascade(menu=menuOtras, label="Otras funcionalidades")
menuOtras.add_command(label="Contratar un empleado", command=contratar)
menuOtras.add_command(label="Despedir un empleado",command=despedir)
menuOtras.add_command(label="Construir un habitat", command=construir)
menuConsultas= Menu(menuOtras, font="Helvetica 12")
menuOtras.add_cascade(menu=menuConsultas, label="Consultar datos del zoológico")
menuConsultas.add_command(label="Nómina de empleados", command=trabajador)
menuConsultas.add_command(label="Animales actuales", command=animales)
menuConsultas.add_command(label="Hábitats actuales", command=habitats)
menuConsultas.add_command(label="Visitantes recibidos", command=visitantes)

menuAyuda = Menu(menuVentanaUsuario, font="Helvetica 12")
menuVentanaUsuario.add_cascade(menu=menuAyuda, label="Ayuda")
menuAyuda.add_command(label="Acerca de", command=ayuda)

# COMPONENTES DE LA VENTANA DE INICIO:

# Se crean cada uno de los frames especificados para la ventana de Inicio.
ventanaInicio = Frame()
P1 = Frame(master=ventanaInicio, highlightbackground="black", highlightthickness=2)
P2 = Frame(master=ventanaInicio, highlightbackground="black", highlightthickness=2)
P3 = Frame(master=P1, highlightbackground="black", highlightthickness=2)
P4 = Frame(master=P1, highlightbackground="black", highlightthickness=2)
P5 = Frame(master=P2, highlightbackground="black", highlightthickness=2)
P6 = Frame(master=P2, highlightbackground="black", highlightthickness=2)

# Se crea el Label de bienvenida a la aplicación.
Saludo = Label(master=P3, text="""Bienvenido al sistema de gestion de zoológico, que lo ayudará 
a administrar facilmente todo lo que tiene que ver con este.""", font="Helvetica 12")
# Se crea el botón "Ingresar", que al ser presionado permitirá al usuario acceder a las funcionalidades.
Ingreso = Button(master=P4, text="Ingresar", font="Helvetica 14 bold", 
                 bg="grey", fg="white", borderwidth=5, relief="groove",
                 command=ingresar)

# Se crea el título para las hojas de vida de los autores.
TituloVida = Label(master=P5, text="Breve biografía de los autores", 
                   font="Helvetica 14 bold")
# Se crea el Label para el texto de las hojas de vida de los autores.
CuerpoVida = Label(master=P5, text=VidaDavid, font="Helvetica 12", 
                   anchor=W)
# Se crea el Label que contendrá las instrucciones para cambiar entre hojas de vida de los autores.
PieVida = Label(master=P5, text="Clic sobre la biografía para cambiar de autor",
                font="Helvetica 8 italic", fg="blue")

# Se localizan las imágenes iniciales para las relacionadas con la aplicación y para las de hojas de vida de los autores.
"""FotoAnimal=(Image.open("Imagenes/Animales/1.jpg")).resize((400,400), Image.ANTIALIAS)
FotoAnimal = ImageTk.PhotoImage(FotoAnimal)
Foto1 =(Image.open("Imagenes/David/1.jpg")).resize((200,200), Image.ANTIALIAS)
Foto1 = ImageTk.PhotoImage(Foto1)
Foto2 =(Image.open("Imagenes/David/2.jpg")).resize((200,200), Image.ANTIALIAS)
Foto2 = ImageTk.PhotoImage(Foto2)
Foto3 =(Image.open("Imagenes/David/3.jpg")).resize((200,200), Image.ANTIALIAS)
Foto3 = ImageTk.PhotoImage(Foto3)
Foto4 =(Image.open("Imagenes/David/4.jpg")).resize((200,200), Image.ANTIALIAS)
Foto4 = ImageTk.PhotoImage(Foto4)

# Se crean los Label para las imágenes relacionadas con la aplicación y para las de hojas de vida de los autores.
LabelFotoAnimal = Label(master=P4, image=FotoAnimal, borderwidth=5, relief="ridge")
LabelFoto1 = Label(master=P6, image=Foto1, borderwidth=5, relief="ridge")
LabelFoto1.grid(column=0, row=0, padx=3, pady=3)
LabelFoto2 = Label(master=P6, image=Foto2, borderwidth=5, relief="ridge")
LabelFoto2.grid(column=1, row=0, padx=3, pady=3)
LabelFoto3 = Label(master=P6, image=Foto3, borderwidth=5, relief="ridge")
LabelFoto3.grid(column=0, row=1, padx=3, pady=3)
LabelFoto4 = Label(master=P6, image=Foto4, borderwidth=5, relief="ridge")
LabelFoto4.grid(column=1, row=1, padx=3, pady=3)"""

# Se visualizan todos los elementos anteriormente creados.
ventanaInicio.pack()
P1.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
P2.pack(side=RIGHT, fill=BOTH, padx=10, pady=10)
P3.pack(side=TOP, fill=BOTH, padx=10, pady=10)
P4.pack(side=BOTTOM, fill=BOTH, padx=10, pady=10)
P5.pack(side=TOP, fill=BOTH, padx=10, pady=10)
P6.pack(side=BOTTOM, fill=BOTH, padx=10, pady=10)
Saludo.pack(padx=10, pady=10)
Ingreso.pack(side=BOTTOM, padx=10, pady=10)
#LabelFotoAnimal.pack(side=TOP, padx=10, pady=10)
TituloVida.pack(padx=10, pady=10)
CuerpoVida.pack(padx=10, pady=10)
PieVida.pack(padx=10, pady=10)

# Se asignan los comandos para cambiar de hoja de vida y de imagen relacionada a la aplicación.
CuerpoVida.bind("<Button-1>", cambiarVida)
#LabelFotoAnimal.bind("<Enter>", cambiarImagen)  

# COMPONENTES DE LA VENTANA DEL USUARIO:

# Se define el mensaje que aparecerá cuando se accede a la ventana de Usuario desde la ventana de Inicio.
tutorial = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris convallis nisl sit amet diam convallis, 
vitae malesuada est sodales. In at lectus eget orci pellentesque euismod. Curabitur justo lacus, volutpat 
nec arcu eget, placerat porttitor enim. In lorem arcu, malesuada sed vulputate at, tempus sit amet felis. 
Etiam sed odio sed erat ornare auctor non non enim. Pellentesque non eros ut sapien ornare maximus. Ut et 
venenatis orci, sit amet congue est. Duis sit amet tincidunt purus. Ut ac scelerisque risus. Etiam scelerisque 
tortor eu orci posuere porta. Praesent at dictum est. Aliquam a mauris diam. Donec euismod mi leo. Phasellus 
sed urna leo. Nulla facilisi.
"""    

# Se crea la ventana de usuario, así como la sección de qué se puede hacer con la aplicación.
ventanaUsuario = Frame()
tituloInfo = Label(master=ventanaUsuario, text="¿Cómo usar esta aplicación y qué puede hacer con ella?", font="Helvetica 12 bold")
info = Label(master=ventanaUsuario, text=tutorial, font="Helvetica 11")
tituloInfo.pack(fill=BOTH, padx=10, pady=10)
info.pack(fill=BOTH, padx=10, pady=10)

# FUNCIONALIDAD DE MANTENIMIENTO:

ventanaMantenimiento =  Mantenimiento()
ventanaMantenimiento.pack_forget()

# FUNCIONALIDAD DE CURAR:

ventanaCurar = Curar() # Curar()
ventanaCurar.pack_forget()

# FUNCIONALIDAD DE CUIDAR:

ventanaCuidar = Cuidar()
ventanaCuidar.pack_forget()

# FUNCIONALIDAD DE ADQUISICIÓN Y TRASLADO:

ventanaAdquision = Adquisicion()
ventanaAdquision.pack_forget()

ventanaTraslado = Traslado()
ventanaTraslado.pack_forget()

# FUNCIONALIDAD DE GESTIÓN:

ventanaGestion = Gestion()
ventanaGestion.pack_forget()

# OTRAS FUNCIONALIDADES:

ventanaDespedir = Despedir()
ventanaDespedir.pack_forget()

ventanaContratar = Contratar()
ventanaContratar.pack_forget()

ventanaConstruir = Construir()
ventanaConstruir.pack_forget()

ventanaTrabajador = Trabajador()
ventanaTrabajador.pack_forget()

ventanaAnimales = Animales()
ventanaAnimales.pack_forget()

ventanaHabitats = Habitats()
ventanaHabitats.pack_forget()

ventanaVisitantes = Visitantes()
ventanaVisitantes.pack_forget()

# Las siguiente líneas son para definir el estilo para ciertos elementos y tablas que usa la aplicación.
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")
style.configure("Treeview.Heading", font="Helvetica 10 bold")
style.configure("Treeview", font="Helvetica 10")

ventana.mainloop()