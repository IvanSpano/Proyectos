import requests
from pprint import pprint
 
url = "http://localhost:5000/alumno"
 
while True:
    print("""
        Administración remota
    ===================================
        1. Agregar un alumno
        2. Modificar datos de un alumno
        3. Listar alumnos
        4. Eliminar un alumno
        5. Salir
    """)
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        cursos = input("Cursos: ")
        datos = {'nombre':nombre, 'cursos':cursos}
        r = requests.post(url, json=datos)
        print("Código de respuesta:", r.status_code)
        print("Respuesta:", r.json())
            
    
    elif opcion == "2":
        id_alumno = int(input("ID: "))
        datos = {'id':id_alumno, 'nombre':None, 'cursos':None}
        
        cambiar = input('¿Desea cambiar el nombre(s/N)?: ')
        if cambiar.lower() == "s":
            datos['nombre'] = input("Nuevo nombre: ")
        
        cambiar = input('¿Desea cambiar los cursos(s/N)?: ')
        if cambiar.casefold() == "s":
            datos['cursos'] = input("Nuevos cursos: ")
        
        r = requests.put(url, json=datos)
        print("Código de respuesta:", r.status_code)
        print("Respuesta:", r.json())
        
    
    
    elif opcion == "3":
        r = requests.get(url)
        if r.status_code == 200:
            alumnos = r.json()['alumnos']
            if not alumnos:
                print("No hay alumnos")
            else:
                pprint(r.json())
        else:
            print("No se pudo descargar la lista de alumnos")
            print("Código de respuesta:", r.status_code)
    
    
    elif opcion == "4":
        id_alumno = int(input("ID: "))
        datos = {'id':id_alumno}
        r = requests.delete(url, json=datos)
        print("Código de respuesta:", r.status_code)
        print("Respuesta:", r.json())
        
    
    elif opcion == "5":
        print("Finalizando sesión...")
        break
        
        
    else:
        print("Opción incorrecta")