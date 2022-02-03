#script que calcula las raices de una ecuación cuadratica en el campo de los reales

import datetime

def validar_numeros(p):
    while True:
        try:
            numero = float(input(f"Ingrese el término {p}: "))
        except ValueError:
            print("Error, debe ingresar un numero")
        else:
            if p == "a" and not numero:
                print("Erro, 'a' debe ser no nulo")
            else: 
                return numero

def ingresar_datos():
    a = validar_numeros("a")
    b = validar_numeros("b")
    c = validar_numeros("c")
    return [a,b,c]

def calcular_raices(a,b,c):
    from math import sqrt
    delta = b**2 - 4*a*c

    if not delta:
        raiz = -1*b/(2*a)
        return raiz
    elif delta > 0:
        raiz1 = (-1*b + sqrt(delta)) / (2*a)
        raiz2 = (-1*b - sqrt(delta)) / (2*a)
        return [raiz1, raiz2]
    else:
        return "No existen raices\n"

def grabar_datos(a,b,c,raices):
    try:
        f = open("Raices.txt", "a")
    except Exception:
        print("Error, no se pudo abrir el archivo 'raices.txt'")
    else:
        f.write(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S") + "\n")
        f.write("Parámetros de la parábola:\n")
        f.write(f"Témino cuadrático: {a}\n")
        f.write(f"Témino lineal: {b}\n")
        f.write(f"Témino independiente: {c}\n")

        if isinstance(raices, float):
            f.write("Existe una solución única: {:.2f}\n".format(raices))
        elif isinstance(raices, list):
            f.write("Existe dos soluciones: {:.2f} y {:.2f}\n".format(raices[0], raices[1]))
        else:
            f.write(raices + "\n")
    finally:
        f.close()
    
def imprimir_raices(raices):
    if isinstance(raices, float):
        print("Existe una solución única: {:.2f}".format(raices))
    elif isinstance(raices, list):
        print("Existe dos soluciones: {:.2f} y {:.2f}".format(raices[0], raices[1]))
    else:
        print(raices)

print("Calculo de raíces de una parábola")

while True:
    a,b,c = ingresar_datos()
    raices = calcular_raices(a,b,c)
    grabar_datos(a,b,c, raices)
    imprimir_raices(raices)

    opcion = input("\nPresione cualquier tecla para continuar o '1' para salir: ")
    if opcion == "1":
        print("Gracias por usar este programa...")
        break