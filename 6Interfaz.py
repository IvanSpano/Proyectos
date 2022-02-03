def menu(titulo, *args, **kwargs): 
    print(titulo)
    for i in range(len(args)):
        print(f"{i+1}) {args[i]}")
    opc = int(input("Selecciona una opción: "))
    while opc != 5:
        if 1 <= opc <= len(args):
            print(f"Seleccionaste la opción {args[opc-1]}")
        else:
            print("Opción no válida, vuelva a intentarlo")
            if "error" in kwargs:
                print({kwargs["error"]})
        if opc == 1:
            ("Ingrese los números que desea sumar: ")
        
    

menu("Operaciones aritméticas", "Suma", "Resta", "Multiplicación","División", error="Esta opción no es válida")
