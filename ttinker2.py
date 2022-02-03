import tkinter as tk
from tkinter import ttk

def seleccionar_lista():
    valor = lista.get(lista.curselection())
    print(valor)

def seleccionar_combo():
    valor = combo.get()
    print(valor)

ventana = tk.Tk()
ventana.title("mi ventana")
ventana.config(widht=400, height=600)

#lista (listbox)
lista = tk.Listbox()
lista.insert(0,"Ale", "Juana","Ana","Tito","Luisa")
lista.place(x=10, y=20)
boton = ttk.Button(text="Seleccionar", command=seleccionar_lista)
boton.place(x=10, y=200)

#lista desplegable(combobox)
combo = ttk.Combobox(state="readonly", values=["Ale","Juana","Ana","Tito","Luisa"])
combo.place(x=10, y=250)
boton = ttk.Button(text="Seleccionar", command=seleccionar_combo)
boton.place(x=10, y=280)

#casilla de verificación
estado = tk.BooleanVar()
estado.set("True")
casilla = ttk.Checkbutton(text="Acepto las condiciones", variable=estado)
casilla.place(x=250, y=30)

#imagen (dentro de una etiqueta)
imagen = tk.PhotoImage(file="Imagen1.png")
etiqueta = ttk.Label(image=imagen)
etiqueta.place(relx=0.5, rely= 0.5,relwidth=0.5, relheight=0.5)

#barra de progreso
barra = ttk.Progressbar(maximun=100)
barra.place(x=10, y=350, width=200)
#barra.step(99.9) para que la barra empiece llena
barra.start()


ventana.mainloop()