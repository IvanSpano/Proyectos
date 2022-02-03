import requests
 
url = "http://localhost:8880/form"
 
datos = [
    {'name':"Juan", "email":"juan@juan", "message":"Hola"},
    {'name':"Ana", "email":"juan@juan", "message":"Hola"},
    {'name':"Juana", "email":"juan@juan", "message":"Chau"},
    {'name':"Fede", "email":"tito@juan", "message":"Hola"},
    {'name':"Tito", "email":"juan@juan", "message":"Hola"},
]
 
for dato in datos:
    r = requests.post(url, data=dato)
    if "Mensaje enviado correctamente" in r.content.decode("utf-8"):
        print(f"Mensaje del usuario {dato['name']} enviado correctamente")
    else:
        print(f"Mensaje del usuario {dato['name']} no enviado")