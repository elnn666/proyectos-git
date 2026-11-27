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

with open("logs/openssh_loghub_2k.log", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

guardados = 0

for linea in lineas:
    if "Failed password" not in linea and "Accepted password" not in linea:
        continue
    partes = linea.split()
    fecha = partes [0] + " " + partes[1]
    hora = partes[2]
    if "Failed" in linea:
        resultado = "Failed"
    else:
        resultado = "Accepted"
    usuario = partes[partes.index("from") - 1]
    ip = partes[partes.index("from") + 1]

    cursor.execute(
       "INSERT INTO intentos (fecha, hora, resultado, usuario, ip) VALUES (?, ?, ?, ?, ?)",
       (fecha, hora, resultado, usuario, ip)
    )
    guardados = guardados + 1
conexion.commit()
conexion.close()
print(f"Se leyeron {len(lineas)} lineas y se guardaron {guardados} intentos")