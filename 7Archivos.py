#Crear un archivo en modo de texto:

f = open("centigrados.txt", "x")

#Crear una lista con los datos a guardar en el archivo
datos = ["25°C\n", "14°C\n", "0.25°C\n", "-45°C\n"]

#Escribo los datos en el archivo (forma 1 de agregar datos)
for dato in datos:
    f.write(dato)

#Cierro el archivo
f.close()

#Abro el archivo para agregar datos (append) (forma 2 de agregar datos)
f = open("centigrados.txt","a")
datos = ["17.25°C\n", "-18°C\n"]
f.writelines(datos)
f.close()

#Abro en modo lectura
f = open("centigrados.txt")
datos = f.readlines()
f.close()

#Creo el archivo fernheit.txt

f = open("Farenheit.txt","x")
for linea in datos:
    temp, escala = linea.split("°")
    temp = float(temp) * 1.8 + 32
    f.write(F"{temp}°F\n")
f.close()