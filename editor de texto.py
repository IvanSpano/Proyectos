from tkinter import *
from tkinter import filedialog as FileDialog

#funciones menu de archivos

def nuevo():
    global ruta
    mensaje.set("Nuevo archivo")
    texto.delete(1.0, END)
    root.title("Mi Editor")
    ruta = ""

def abrir():
    global ruta
    mensaje.set("Abrir archivo")
    ruta = FileDialog.askopenfilename(
        initialdir=".",
        filetypes = (
            ("Archivos de texto", "*.txt"),
            ("Archivo Python", "*.py"),
            ("Todos los archivos", "*.*")
        ),
        title="Abrir un archivo"
    )
    # si la ruta es válida, abrimos el contenido en modo lectura
    if ruta != "":
        f = open(ruta)
        contenido = f.read()  # leo el archivo
        texto.delete(1.0, END)  # borro el contenido del editor
        texto.insert('insert', contenido) # pego el contenido del archivo
        f.close()
        root.title(f"{ruta} - Mi Editor")
        mensaje.set("Archivo abierto")

def guardar():
    global ruta
    mensaje.set("Guardando archivo...")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        # abrimos un archivo en modo w+ para lectura y escritura
        # Si el archivo existe, lo sobreescribe. Si no existe, crea
        # uno nuevo para lectura y escritura
        f = open(ruta, "w+")
        f.write(contenido)
        f.close()
        mensaje.set("Archivo guardado")
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set("Guardar archivo como...")
    f = FileDialog.asksaveasfile(
            title = " Guardar archivo como",
            mode = "w",
            filetypes = (
            ("Archivos de texto", "*.txt"),
            ("Archivo Python", "*.py"),
            ("Todos los archivos", "*.*")
        ),
            defaultextension = ".txt"
        )
    if f is not None:
        ruta = f.name
        contenido = texto.get(1.0, 'end-1c')
        f = open(ruta, "w+")
        f.write(contenido)
        f.close()
        mensaje.set("Archivo guardado")
    else:
        mensaje.set("Se ha cancelado el guardado del archivo")
        ruta = ""

# funciones menu editar 
def undo():
    texto.event_generate("<<Undo>>")
    
def redo():
    texto.event_generate("<<Redo>>")
    
def cortar():
    texto.event_generate("<<Cut>>")
    
def copiar():
    texto.event_generate("<<Copy>>")
 
def pegar():
    texto.event_generate("<<Paste>>")

root = Tk()
root.title("Mi editor de texto")

#########################
#creo una variable global para almacenar la ruta de los archivos
ruta = ''

#creo la barra de menu
menubar = Menu(root)

#menu archivo
archivo = Menu(menubar, tearoff=0)
archivo.add_command(label="Nuevo", command=nuevo)
archivo.add_command(label="Abrir", command=abrir)
archivo.add_command(label="Guardar", command=guardar)
archivo.add_command(label="Guardar como", command=guardar_como)
archivo.add_separator()
archivo.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=archivo)

# agrego la barra de manu a la ventana
root.config(menu=menubar)

# menu editar
# iconos a mostrar en el menu
undo_image=PhotoImage(file='undo.png')
redo_image=PhotoImage(file='redo.png')
paste_image=PhotoImage(file='paste.png')
cut_image=PhotoImage(file='cut.png')
 
editar = Menu(menubar, tearoff=0)
editar.add_command(label="Deshacer", accelerator='Ctrl+Z', compound='left', image=undo_image, command=undo)
editar.add_command(label="Rehacer", accelerator='Shift+Ctrl+Z', compound='left', image=redo_image, command=redo)
editar.add_command(label="Cortar", accelerator='Ctrl+X', compound='left', image=cut_image, command=cortar)
editar.add_command(label="Copiar", accelerator='Ctrl+C', command=copiar)
editar.add_command(label="Pegar", accelerator='Ctrl+V', compound='left', image=paste_image, command=pegar)
menubar.add_cascade(label="Editar", menu=editar)

# scrollbar
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

# zona de escribir
texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(
        padx=6, pady=6, bd=0,
        font=('arial',12),
        bg='beige',
        undo=True, maxundo=20,
        yscrollcommand=scroll.set
        )
scroll.config(command=texto.yview)

scroll.config(command=texto.yview)
 
# mensajes en barra inferior
mensaje = StringVar()
mensaje.set("Bienvenidos a Mi Editor")
barra_inferior = Label(root, textvar=mensaje, justify='right')
barra_inferior.pack(side='left')

root.mainloop()