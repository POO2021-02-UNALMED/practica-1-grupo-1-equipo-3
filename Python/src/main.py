# main.py
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from funcionalidadMantenimiento import Mantenimiento
#from funcionalidadCurar import Curar
#from funcionalidadCuidar import Cuidar
from funcionalidadAdquisicion import Adquisicion
from funcionalidadTraslado import Traslado
from funcionalidadGestion import Gestion
from funcionalidadDespedir import Despedir
from funcionalidadContratar import Contratar
from funcionalidadConstruir import Construir
from funcionalidadDatosTrabajadores import Trabajador
from funcionalidadDatosAnimales import Animales
from funcionalidadDatosHabitats import Habitats
from gestorAplicacion.administracion import Administracion
from gestorAplicacion.animal import Animal
from gestorAplicacion.cuidador import Cuidador
from gestorAplicacion.especie import Especie
from gestorAplicacion.habitat import Habitat
from gestorAplicacion.veterinario import Veterinario
from gestorAplicacion.visitante import Visitante

#A continuación se encuentran los objetos que fueron guardados originalmente en la persistencia inicial.
admin = Administracion()
a = Habitat("H1", "Pradera", 2)
b = Habitat("H2", "Jungla", 1)
c= Habitat("H3", "Pantano", 3)
d= Habitat("H5", "Rio", 3)
e= Habitat("H6","Pantano",2)
c.setLimpio(False)
a1 = Animal(Especie.REPTIL, c, "Macho", 5, 70)
a2 = Animal(Especie.REPTIL, c, "Hembra", 4, 65)
a1.setEstadoAnimo(False)
a2.setEstadoAnimo(False)
a3 = Animal(Especie.ANFIBIO,e,"Macho",2,20)
a4 = Animal(Especie.ANFIBIO,e,"Hembra",2,15)
a3.setEstadoAnimo(False)
a4.setEstadoAnimo(False)
a3.setAlimentado(False)
a4.setEstadoSalud(False)
a5 = Animal(Especie.PEZ,d,"Macho",2,20)
a6 = Animal(Especie.PEZ,d,"Macho",1,15)
a7 = Animal(Especie.PEZ,d,"Hembra",1,20)
d.setLimpio(False)
a5.setEstadoAnimo(False)
a6.setEstadoAnimo(False)
a7.setEstadoAnimo(False)
a7.setAlimentado(False)
a5.setAlimentado(False)
a5.setEstadoSalud(False)
a6.setEstadoSalud(False)
a8 = Animal(Especie.ANFIBIO,b,"Hembra",1,20)
c1 = Cuidador("Jorge", 7000, Especie.MAMIFERO)
c2 = Cuidador("Johanna", 1000, Especie.AVE)
c3 = Cuidador("Camila", 100000, Especie.REPTIL)
c4 = Cuidador("David", 10000, Especie.PEZ)
c5 = Cuidador("Juan", 5000, Especie.ANFIBIO)
v1 = Veterinario("Elva",10000,Especie.ANFIBIO)
v2 = Veterinario("Francisco",12000,Especie.PEZ)
vi1 = Visitante("Jose",3,15)
vi2 = Visitante("Diego",5,30)
vi3 = Visitante("Valeria",6,30)

ventana = Tk()
ventana.title("Sistema gestor de zoológico")
ventana.geometry("+100+100")
ventana.resizable(False, False)
ventana.option_add("*tearOff", FALSE)
#ventana.iconbitmap("../Imagenes/Z.ico")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

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

# COMANDOS RELATIVOS A LA VENTANA DE INICIO:

VidaDavid="""Nombre: David Mateo García Vallejo"""
VidaJose="""Nombre: José David Cardona Soto"""
VidaJuan="""Nombre: Juan José Monsalve Marín"""
VidaMateo="""Nombre: Mateo Carvajal Sánchez"""

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

def descripcion():
    descripcion = "En el sistema gestor de zoológico podrá administrar todo lo que tiene que ver con su zoológico: Calcular las ganancias del día; pagar a sus empleados; llevar conteo de los visitantes, de los animales, de los empleados, de las especies, y de los hábitats."
    messagebox.showinfo(title="Descripción de la aplicación",
                        message=descripcion)

def salirInicio():
    salir = messagebox.askyesno(title="Salir",
                                message="¿Confirma que desea salir de la aplicación?",
                                detail="Clic en Sí para salir")
    if salir:
        ventana.destroy()

def ingresar():
    ocultarTodo()
    ventanaUsuario.pack()
    ventana["menu"] = menuVentanaUsuario

# COMANDOS RELATIVOS A LA VENTANA DEL USUARIO:

def mantenimiento():
    ocultarTodo()
    ventanaMantenimiento.pack()

def curar():
    ocultarTodo()
    ventanaCurar.pack()

def cuidar():
    ocultarTodo()
    ventanaCuidar.pack()

def adquisicion():
    ocultarTodo()
    ventanaAdquision.pack()

def traslado():
    ocultarTodo()
    ventanaTraslado.pack()

def gestion():
    ocultarTodo()
    ventanaGestion.pack()
    
def despedir():
    ocultarTodo()
    ventanaDespedir.pack()

def contratar():
    ocultarTodo()
    ventanaContratar.pack()

def construir():
    ocultarTodo()
    ventanaConstruir.pack()

def trabajador():
    ocultarTodo()
    ventanaTrabajador.pack()

def animales():
    ocultarTodo()
    ventanaAnimales.pack()

def habitats():
    ocultarTodo()
    ventanaHabitats.pack()

def consultar():
    ocultarTodo()
 
def aplicacion():
    descripcion = "En el sistema gestor de zoológico podrá administrar todo lo que tiene que ver con su zoológico: Calcular las ganancias del día; pagar a sus empleados; llevar conteo de los visitantes, de los animales, de los empleados, de las especies, y de los hábitats."
    messagebox.showinfo(title="Información básica de la aplicación",
                        message=descripcion)

def salirUsuario():
    salir = messagebox.askyesno(title="Salir",
                                message="¿Confirma que desea regresar a la ventana de inicio?",
                                detail="Clic en Sí para regresar")
    if salir:
        ocultarTodo()
        ventanaInicio.pack()
        ventana["menu"] = menuVentanaInicio

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
menuConsultas.add_command(label="Visitantes recibidos", command=consultar)



menuAyuda = Menu(menuVentanaUsuario, font="Helvetica 12")
menuVentanaUsuario.add_cascade(menu=menuAyuda, label="Ayuda")
menuAyuda.add_command(label="Acerca de", command=ayuda)

# COMPONENTES DE LA VENTANA DE INICIO:

ventanaInicio = Frame()
P1 = Frame(master=ventanaInicio, highlightbackground="black", highlightthickness=2)
P2 = Frame(master=ventanaInicio, highlightbackground="black", highlightthickness=2)
P3 = Frame(master=P1, highlightbackground="black", highlightthickness=2)
P4 = Frame(master=P1, highlightbackground="black", highlightthickness=2)
P5 = Frame(master=P2, highlightbackground="black", highlightthickness=2)
P6 = Frame(master=P2, highlightbackground="black", highlightthickness=2)

Saludo = Label(master=P3, text="""Bienvenido al sistema de gestion de zoológico, que lo ayudará 
a administrar facilmente todo lo que tiene que ver con este.""", font="Helvetica 12")
Ingreso = Button(master=P4, text="Ingresar", font="Helvetica 14 bold", 
                 bg="grey", fg="white", borderwidth=5, relief="groove",
                 command=ingresar)

TituloVida = Label(master=P5, text="Breve biografía de los autores", 
                   font="Helvetica 14 bold")
CuerpoVida = Label(master=P5, text=VidaDavid, font="Helvetica 12", 
                   anchor=W)
PieVida = Label(master=P5, text="Clic sobre la biografía para cambiar de autor",
                font="Helvetica 8 italic", fg="blue")

"""FotoAnimal=(Image.open("Imagenes/Animales/1.jpg")).resize((400,400), Image.ANTIALIAS)
FotoAnimal = ImageTk.PhotoImage(FotoAnimal)
Foto1 =(Image.open("Imagenes/David/1.jpg")).resize((200,200), Image.ANTIALIAS)
Foto1 = ImageTk.PhotoImage(Foto1)
Foto2 =(Image.open("Imagenes/David/2.jpg")).resize((200,200), Image.ANTIALIAS)
Foto2 = ImageTk.PhotoImage(Foto2)
Foto3 =(Image.open("Imagenes/David/3.jpg")).resize((200,200), Image.ANTIALIAS)
Foto3 = ImageTk.PhotoImage(Foto3)
Foto4 =(Image.open("Imagenes/David/4.jpg")).resize((200,200), Image.ANTIALIAS)
Foto4 = ImageTk.PhotoImage(Foto4)"""

"""LabelFotoAnimal = Label(master=P4, image=FotoAnimal, borderwidth=5, relief="ridge")
LabelFoto1 = Label(master=P6, image=Foto1, borderwidth=5, relief="ridge")
LabelFoto1.grid(column=0, row=0, padx=3, pady=3)
LabelFoto2 = Label(master=P6, image=Foto2, borderwidth=5, relief="ridge")
LabelFoto2.grid(column=1, row=0, padx=3, pady=3)
LabelFoto3 = Label(master=P6, image=Foto3, borderwidth=5, relief="ridge")
LabelFoto3.grid(column=0, row=1, padx=3, pady=3)
LabelFoto4 = Label(master=P6, image=Foto4, borderwidth=5, relief="ridge")
LabelFoto4.grid(column=1, row=1, padx=3, pady=3)"""

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

CuerpoVida.bind("<Button-1>", cambiarVida)
#LabelFotoAnimal.bind("<Enter>", cambiarImagen)  

# COMPONENTES DE LA VENTANA DEL USUARIO:

tutorial = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris convallis nisl sit amet diam convallis, 
vitae malesuada est sodales. In at lectus eget orci pellentesque euismod. Curabitur justo lacus, volutpat 
nec arcu eget, placerat porttitor enim. In lorem arcu, malesuada sed vulputate at, tempus sit amet felis. 
Etiam sed odio sed erat ornare auctor non non enim. Pellentesque non eros ut sapien ornare maximus. Ut et 
venenatis orci, sit amet congue est. Duis sit amet tincidunt purus. Ut ac scelerisque risus. Etiam scelerisque 
tortor eu orci posuere porta. Praesent at dictum est. Aliquam a mauris diam. Donec euismod mi leo. Phasellus 
sed urna leo. Nulla facilisi.
"""    

ventanaUsuario = Frame()
tituloInfo = Label(master=ventanaUsuario, text="¿Cómo usar esta aplicación y qué puede hacer con ella?", font="Helvetica 12 bold")
info = Label(master=ventanaUsuario, text=tutorial, font="Helvetica 11")
tituloInfo.pack(fill=BOTH, padx=10, pady=10)
info.pack(fill=BOTH, padx=10, pady=10)

# FUNCIONALIDAD DE MANTENIMIENTO:

ventanaMantenimiento =  Mantenimiento()
ventanaMantenimiento.pack_forget()

# FUNCIONALIDAD DE CURAR:

ventanaCurar = Frame() # Curar()
ventanaCurar.pack_forget()

# FUNCIONALIDAD DE CUIDAR:

ventanaCuidar = Frame() # Cuidar()
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


ventana.mainloop()