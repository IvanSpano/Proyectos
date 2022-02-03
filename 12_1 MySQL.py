"""
Como seria con MySQL. Tendriamos que importar el módulo PyMySQL
python -m pip install PyMySQL
"""

import pymysql

#Creo una conexión con una base de datos.Si la base no existe, la crea. Si la base existe, la abre.
conn = pymysql.connect(
            host="localhost",
            user="nombre del usuario",
            passwd="contraseña",
            db="database.db")

#Creo una variable para hacer una consulta SQL
cursor = conn.cursor()

#Creo una tabla (o sea, ejecuto mi primer consulta SQL )
try:
    cursor.execute("CREATE TABLE IF NOT EXISTS personas(nombre VARCHAR(45), edad INT)")
except pymysql.ProgrammingError:
    print("Error de sintaxis")
#Guardar los cambios
conn.commit()

#Creo una tupla de datos para cargar en la tabla personas
datos = (
    ("Juan",19),
    ("Ana", 22),
    ("Roque", 45),
    ("Lisa", 27)
)

#Agrego los datos en la tabla
for nombre, edad in datos:
    cursor.execute("INSERT INTO personas VALUES(%s,%s)",(nombre, edad))

#Guardar los cambios
conn.commit()

#Leo los datos y luego los imprimo
cursor.execute("SELECT * FROM personas")
datos = cursor.fetchall() #Cursor.fetchone() devuelve un solo dato
print(datos)

#Cierro la base de datos
conn.close()

"""
un error que puede salir es: pymysql.err.InternalError; cuando quiero crear algo que ya existe(tabla, columna)
"""