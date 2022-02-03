dic = {}
continuar = 1
legajo = ""
nombre = ""
while continuar != 0:
    print("ingrese un numero de legajo: ")
    legajo = input()
    if legajo in dic:
        print("Error, legajo ya existente")
    else:
        print("ingrese un nombre: ")
        nombre = input()
        dic.update({legajo:nombre})
        print("Diccionario actual: ", dic)
