import sqlite3

conexion = sqlite3.connect("salida/centinela.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS intentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    hora TEXT,
    resultado TEXT,
    usuario TEXT,
    ip TEXT

)
""")

conexion.commit()
conexion.close()
print("Base de datos creada")