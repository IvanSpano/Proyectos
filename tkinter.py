#script que implementa un formulario
import tkinter as tk
from tkinter import ttk
from pprint import pprint

""" personas = [ {"nombre":"juan", "email":"juan@juan","tel":"(011)122121", "nac":"argentino"}
{"nombre":"Ana", "email":"Ana@Ana","tel":"(011)123221", "nac":"argentino"}
]
"""

personas = []

def guardar_datos():
    global personas
    nombre = caja_nombre.get()
    email = caja_email.get()
    nac = caja_nac.get()
    tel = caja_tel.get()
    persona = {"nombre":nombre, "email":email,"tel":tel, "nac":nac}
    personas.append(persona)
    pprint(personas)
    caja_nombre.delete(0, tk.END)
    caja_email.delete(0, tk.END)
    caja_nac.delete(0, tk.END)
    caja_tel.delete(0, tk.END)

#tkinter se usa para crear interfaz gráfica
ventana = tk.Tk()    #crea una ventana
ventana.title("Mi primera app")    #le pone un titulo a la ventana
ventana.config(width=300, height=400, bg="blue")

#ventana.resizable(0,0)   #si quisiera un tamaño fijo

##### campos del formulario #####

#campo nombre
caja_nombre = tk.Entry()
caja_nombre.place(x=100, y=30, widht=100, height=25)
etiqueta = ttk.Label(text="Nombre")
etiqueta.place(x=10, y=30)

#campo email
caja_email = tk.Entry()
caja_email.place(x=100, y=80, widht=100, height=25)
etiqueta = ttk.Label(text="Email")
etiqueta.place(x=10, y=80)

#campo nacionalidad
caja_nac = tk.Entry()
caja_nac.place(x=100, y=130, widht=100, height=25)
etiqueta = ttk.Label(text="Nacionalidad")
etiqueta.place(x=10, y=130)

#campo telefono
caja_tel = tk.Entry()
caja_tel.place(x=100, y=180, widht=100, height=25)
etiqueta = ttk.Label(text="telefono")
etiqueta.place(x=10, y=180)

#############################################################

### botón para guardar datos ###

boton = ttk.Button(text="GUARDAR", command=guardar_datos)
boton.place(x=120, y=220, widht=100, height=50)

ventana.mainloop()    #para mantener la ventana abierta