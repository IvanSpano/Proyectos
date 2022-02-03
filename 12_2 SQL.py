"""Script que crea una base de datos para administrar un restaurante. Implementa dos tablas:
categorias (entradas, plato_ppal, postres)
platos (asado, empanadas, flan, milanesa)
"""

import sqlite3

conn = sqlite3.connect("restaurante.db")

query = "CREATE TABLE categorias(\
        id INTEGER PRIMARY KEY AUTINCREMENT,\
        nombre TEXT UNIQUE NOT NULL\
        )"
conn.execute(query)

query = "CREATE TABLE platos(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        nombre TEXT UNIQUE NOT NULL,\
        id_categoria INTEGER NOT NULL,\
        FOREING KEY(id_categoria) REFERENCES categorias(id)\
        )"

conn.execute(query)
conn.commit()
conn.close()