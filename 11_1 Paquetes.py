"""
Modulo: Cualquier archivo .py
Biblioteca: Conjunto de módulos
Paquete: Conjunto de modulos y/o bibliotecas que conforman alguna utilidad (ej un editor de texto) para distribuir su uso. Un paquete se distingue porque tiene un módulo que se llama __init__.py (generalmente vacio)

Namespace: espacio de nombres, se refiere al lugar donde se define una funcion

ej paquete_____ menu.py
        |______ cuadratica.py (validar_numeros, ingresar_datos,etc)
        |______ excel.py
        |______ __init__.py
        |______ subpaquete
                    |______ cuadratica.py
                    |______ modulo2.py
                    |______ __init__.py
        |______ modulo1.py
"""

# si solo quiero usar validar_numeros:
# from paquete.cuadratica import validar_numeros
# namespace: paquete.cuadratica

#-------------------------------------------------------------------------------------------

#programa que calcula el volumen de un dado

from cubo import cubo as volumen

lado = int(input("Ingrese el lado del dado: "))
print(f"El volumen del dado es {volumen(lado)}")