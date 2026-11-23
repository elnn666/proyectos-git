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

cursor.execute("DELETE FROM intentos")

with open("logs/auth_ejemplo.log", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    partes = linea.split()
    fecha = partes [0] + " " + partes[1]
    hora = partes[2]
    resultado = partes [5]
    usuario = partes [8]
    ip = partes [10]

    cursor.execute(
       "INSERT INTO intentos (fecha, hora, resultado, usuario, ip) VALUES (?, ?, ?, ?, ?)",
       (fecha, hora, resultado, usuario, ip)
    )

conexion.commit()
conexion.close()
print(f"Se han insertado {len(lineas)} intentos")