"""
DB-API (API estandar de Python para base de datos)

MySQL  mysql--conector--python, PyMySQL, MySQLdb
PostgreSQL --> psycopg pg8000
SQLite --> un archivo sqlite3 (NO SE INSTALA)
SQL server --> pymssql, pyodbc
Oracle --> cx_Oracle
"""

import sqlite3

#Creo una conexión con una base de datos.Si la base no existe, la crea. Si la base existe, la abre.
conn = sqlite3.connect("database.sqlite")

#Creo una variable para hacer una consulta SQL
cursor = conn.cursor()

#Creo una tabla (o sea, ejecuto mi primer consulta SQL )
try:
    cursor.execute("CREATE TABLE IF NOT EXISTS personas(nombre TEXT, edad NUMERIC)")
except sqlite3.OperationalError:
    print("Error: ¿Ya existia la tabla?")
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
    cursor.execute("INSERT INTO personas VALUES(?,?)",(nombre, edad))

#Guardar los cambios
conn.commit()

#Leo los datos y luego los imprimo
cursor.execute("SELECT * FROM personas")
datos = cursor.fetchall() #Cursor.fetchone() devuelve un solo dato
print(datos)

#Cierro la base de datos
conn.close()