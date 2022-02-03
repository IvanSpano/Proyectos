import os
from datetime import datetime
from tabulate import tabulate
 
directorio = input("Ingrese el directorio: ")
 
############ lista de los archivos ######
print("\nArchivos:")
print("---------------------------------")
for entrada in os.scandir(directorio):
    if entrada.is_file():
        print(entrada.name)
 
############ lista de las subcarpetas ######
print("\nCarpetas:")
print("---------------------------------")
for entrada in os.scandir(directorio):
    if entrada.is_dir():
        print(entrada.name)
 
########## mostrar archivos con tamaño y ultima modificación
# creo una variable tabla para poder imprimir los datos
tabla = []
for entrada in os.scandir(directorio):
    if entrada.is_file():
        info = entrada.stat() 
        tamaño = info.st_size
        
        if tamaño < 1024:
            tamaño = f"{tamaño} B"
        
        elif 1024 < tamaño < 1024**2:
            tamaño = "{:.1f} KB".format(tamaño/1024)
            
        else:
            tamaño = "{:.1f} MB".format(tamaño/(1024**2))
            
        ult_modificacion = datetime.utcfromtimestamp(info.st_mtime).strftime('%d-%b-%y %H:%M')
        
        # agrego los datos del archivo a la tabla
        tabla.append([entrada.name, tamaño, ult_modificacion])
        
print(tabulate(
                tabla,
                headers = ["Archivos","Tamaño","Ultima modificación"],
                tablefmt = 'grid',
                colalign = ['left', 'right', 'center']
        )
    )