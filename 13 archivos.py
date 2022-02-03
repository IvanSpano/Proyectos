"""
Ejercicio: script que recibe como argumento una ruta a una carpeta y una
extension y muestra todos los archivos existentes
Ej:
 python buscar_archivos.py <ruta> <extension>
 
python C:\\Users\\Usuario .py
saludar.py
otro.py
....
 
"""
import sys
import os
 
hallados = False
 
# verifico la cantidad de argumentos
if len(sys.argv) != 3:
    sys.exit("Error en cantidad de argumentos: ejecute 'python buscar_archivos.py <ruta> <extension>'")
 
# asigno los argumentos
ruta, extension = sys.argv[1:]
 
# verifico que exista la ruta
if not os.path.exists(ruta):
    sys.exit(f"No existe la ruta {ruta}")
    
# busco en forma recursiva dentro de la ruta
# os.walk() devuelve 3 valores en cada iteracion del for:
# a) el nombre de la carpeta actual,
# b) una lista de subcapetas dentro de la carpeta actual
# c) una lista de archivos dentro de la carpeta actual
for carpeta_actual, lista_carpetas, lista_archivos in os.walk(ruta):
    for archivo in lista_archivos:
        if archivo.endswith(extension):
            print(os.path.join(carpeta_actual,archivo))
            hallados = True
 
if not hallados:
    print(f"No se hallaron archivos con extension {extension} en {ruta}")