#Para intentar hacer algo que puede dar como error

#try:   
    #numero = int(input("Ingrese un entero:"))
#except ValueError:
    #print("Error, debe ingresar un entero crack")
#else:
    #print(F"El doble de {numero} es {2*numero}")

#------------------------------------------------------------------------------------------------------

#Para no dejar pasar a la persona hasta que no use bien el numero

while True:
    try:
        numero = float(input("Ingrese un nro: "))
    except ValueError:
        print("Error, no has ingresado un numero")
    except RuntimeError:
        print("Error en tiempo de ejecución")
    else: 
        break
print(F"El doble de {numero} es {2*numero}")

#------------------------------------------------------------------------------------------------------
