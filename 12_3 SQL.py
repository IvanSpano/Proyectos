import sqlite3

def mostrar_opciones():
    return """
        Menu de administración del restaurante
    *---------------------------------------------------*
        1. Agregar categoria de plato
        2. Agregar plato
        3. Mostrar menú
        4. Salir
    *---------------------------------------------------* 
        """
    
def agregar_cateogria(nombre):
    try:
        conn.execute("INSERT INTO categorias VALUES(null,?)", (nombre,))
    except sqlite3.IntegrityError:
        print(f"Error, ya existe la categoria '{nombre}'")
    else:
        conn.commit()

def agregar_plato():
    try:
        cursor.execute("SELECT * FROM categorias ORDER BY id")
    except sqlite3.OperationalError:
        print("La consulta no se ejecutó correctamente")
    else: 
        categorias = cursor.fetchall()
        if categorias:
            id_categorias = []
            print("Categorias")
            print("-------")
            print("ID | nombre")
            print("--------------")
            for ID,nombre in categorias:
                id_categorias.append(ID)
                print(f"{ID}  | {nombre}")
            
            while True:
                try:
                    ID = int(input("\nSeleccione un id: "))
                except ValueError:
                    print("Deber ingresar un entero")
                else:
                    if ID in id_categorias:
                        break
                    print("id {ID} de categoria inexistente")
            
            nombre_plato = input("Ingrese el nombre del plato: ")
            try:
                conn.execute("INSERT INTO plats VALUES(null,?,?)", (nombre_plato,ID))
            except sqlite3.IntegrityError:
                print(f"Error, ya existe el plato '{nombre_plato}'")
            else:
                conn.commit()
        else:
            print("No hay categorias de platos")

def mostrar_menu():
    query = "SELECT categorias.id, categorias.nombre, platos.id, platos.nombre FROM categorias LEFT JOIN platos\
    ON platos.id:categoria= categorias.id\
    ORDER BY categorias.id, platos.id"
    cursor.execute(query)
    platos = cursor.fetchall()
    if platos:
        print("\nID categoria   ID plato   ")
        print("-----------------------------")
        for plato in platos:
            print()
            for elemento in plato:
                if isinstance(elemento,str):
                    print("{:<12}".format(elemento),end=" ")
                elif isinstance(elemento,int):
                    print("{:>3}".format(elemento),end=" ")
        print()
    else:
        print("No hay platos en el menu")
                

conn = sqlite3.connect("restaurante.db")
cursor = conn.cursor()

while True:
    print(mostrar_opciones())

    opcion = input("Selecciones una opción: ")

    if opcion == "1":
        agregar_cateogria(input("Ingrese el nombre: "))
    elif opcion == "2":
        agregar_plato()
    elif opcion == "3":
        mostrar_menu()
    elif opcion == "4":
        conn.close()
        print("Cerrando base de datos...")
        break
    else:
        print("Opción incorrecta")