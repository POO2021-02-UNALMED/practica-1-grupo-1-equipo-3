from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.title("Sistema gestor de zoológico")
ventana.resizable(False, False)
    
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
    FotoAnimal=(Image.open("./Fotos/Animales/" + str(posicionImagen) + ".jpg")).resize((400,400), Image.ANTIALIAS)
    FotoAnimal = ImageTk.PhotoImage(FotoAnimal)
    LabelFotoAnimal.configure(image=FotoAnimal)
    LabelFotoAnimal.image=FotoAnimal
    
posicionVida=0
def cambiarVida(e):
    global posicionVida
    posicionVida += 1
    if posicionVida == 4:
        posicionVida = 0
    ListaFotos=["David","Jose","Juan","Mateo"]
    Foto1 =(Image.open("./Fotos/" + ListaFotos[posicionVida] + "/1.jpg")).resize((200,200), Image.ANTIALIAS)
    Foto1 = ImageTk.PhotoImage(Foto1)
    Foto2 =(Image.open("./Fotos/" + ListaFotos[posicionVida] + "/2.jpg")).resize((200,200), Image.ANTIALIAS)
    Foto2 = ImageTk.PhotoImage(Foto2)
    Foto3 =(Image.open("./Fotos/" + ListaFotos[posicionVida] + "/3.jpg")).resize((200,200), Image.ANTIALIAS)
    Foto3 = ImageTk.PhotoImage(Foto3)
    Foto4 =(Image.open("./Fotos/" + ListaFotos[posicionVida] + "/4.jpg")).resize((200,200), Image.ANTIALIAS)
    Foto4 = ImageTk.PhotoImage(Foto4)
    LabelFoto1.configure(image=Foto1)
    LabelFoto1.image=Foto1
    LabelFoto2.configure(image=Foto2)
    LabelFoto2.image=Foto2
    LabelFoto3.configure(image=Foto3)
    LabelFoto3.image=Foto3
    LabelFoto4.configure(image=Foto4)
    LabelFoto4.image=Foto4
    if posicionVida==0:
        CuerpoVida.config(text=VidaDavid)
    elif posicionVida==1:
        CuerpoVida.config(text=VidaJose)
    elif posicionVida==2:
        CuerpoVida.config(text=VidaJuan)
    elif posicionVida==3:
        CuerpoVida.config(text=VidaMateo)

Scene = Frame()
P1 = Frame(master=Scene, highlightbackground="black", highlightthickness=2)
P2 = Frame(master=Scene, highlightbackground="black", highlightthickness=2)
P3 = Frame(master=P1, highlightbackground="black", highlightthickness=2)
P4 = Frame(master=P1, highlightbackground="black", highlightthickness=2)
P5 = Frame(master=P2, highlightbackground="black", highlightthickness=2)
P6 = Frame(master=P2, highlightbackground="black", highlightthickness=2)

Inicio = Button(master=Scene, text="Inicio", fg="red", font="Helvetica 14 bold",
                borderwidth=5, relief="groove")
Saludo = Label(master=P3, text="""Bienvenido al sistema de gestion de zoológico, que lo ayudará 
a administrar facilmente todo lo que tiene que ver con este.""", 
                               font="Helvetica 12")
Ingreso = Button(master=P4, text="Ingresar", font="Helvetica 14 bold", 
                 bg="grey", fg="white", borderwidth=5, relief="groove")

TituloVida = Label(master=P5, text="Breve biografía de los autores", 
                   font="Helvetica 14 bold")
CuerpoVida = Label(master=P5, text=VidaDavid, font="Helvetica 12", 
                  anchor=W)
PieVida = Label(master=P5, text="Clic sobre la biografía para cambiar de autor",
                font="Helvetica 8 italic", fg="blue")

FotoAnimal=(Image.open("./Fotos/Animales/1.jpg")).resize((400,400), Image.ANTIALIAS)
FotoAnimal = ImageTk.PhotoImage(FotoAnimal)
Foto1 =(Image.open("./Fotos/David/1.jpg")).resize((200,200), Image.ANTIALIAS)
Foto1 = ImageTk.PhotoImage(Foto1)
Foto2 =(Image.open("./Fotos/David/2.jpg")).resize((200,200), Image.ANTIALIAS)
Foto2 = ImageTk.PhotoImage(Foto2)
Foto3 =(Image.open("./Fotos/David/3.jpg")).resize((200,200), Image.ANTIALIAS)
Foto3 = ImageTk.PhotoImage(Foto3)
Foto4 =(Image.open("./Fotos/David/4.jpg")).resize((200,200), Image.ANTIALIAS)
Foto4 = ImageTk.PhotoImage(Foto4)

LabelFotoAnimal = Label(master=P4, image=FotoAnimal, borderwidth=5, relief="ridge")
LabelFoto1 = Label(master=P6, image=Foto1, borderwidth=5, relief="ridge")
LabelFoto1.grid(column=0, row=0, padx=3, pady=3)
LabelFoto2 = Label(master=P6, image=Foto2, borderwidth=5, relief="ridge")
LabelFoto2.grid(column=1, row=0, padx=3, pady=3)
LabelFoto3 = Label(master=P6, image=Foto3, borderwidth=5, relief="ridge")
LabelFoto3.grid(column=0, row=1, padx=3, pady=3)
LabelFoto4 = Label(master=P6, image=Foto4, borderwidth=5, relief="ridge")
LabelFoto4.grid(column=1, row=1, padx=3, pady=3)

Scene.pack()
Inicio.pack(padx=10, anchor=NW)
P1.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
P2.pack(side=RIGHT, fill=BOTH, padx=10, pady=10)
P3.pack(side=TOP, fill=BOTH, padx=10, pady=10)
P4.pack(side=BOTTOM, fill=BOTH, padx=10, pady=10)
P5.pack(side=TOP, fill=BOTH, padx=10, pady=10)
P6.pack(side=BOTTOM, fill=BOTH, padx=10, pady=10)
Saludo.pack(padx=10, pady=10)
Ingreso.pack(side=BOTTOM, padx=10, pady=10)
LabelFotoAnimal.pack(side=TOP, padx=10, pady=10)
TituloVida.pack(padx=10, pady=10)
CuerpoVida.pack(padx=10, pady=10)
PieVida.pack(padx=10, pady=10)

CuerpoVida.bind("<Button-1>", cambiarVida)
LabelFotoAnimal.bind("<Enter>", cambiarImagen)

ventana.mainloop()