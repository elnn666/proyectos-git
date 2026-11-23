import sqlite3

conexion = sqlite3.connect("salida/centinela.db")
cursor = conexion.cursor()

cursor.execute("""
SELECT ip, COUNT(*) AS fallidos
FROM intentos
WHERE resultado = 'Accepted'
GROUP BY ip
ORDER BY fallidos DESC
""")

for fila in cursor.fetchall():
    print(fila)

conexion.close()
