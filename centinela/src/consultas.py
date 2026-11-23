import sqlite3

conexion = sqlite3.connect("salida/centinela.db")
cursor = conexion.cursor()

cursor.execute("""
SELECT ip, 
       SUM(CASE WHEN resultado = 'Failed' THEN 1 ELSE 0 END) AS fallidos,
       SUM(CASE WHEN resultado = 'Accepted' THEN 1 ELSE 0 END) AS correctos
FROM intentos
GROUP BY ip
ORDER BY fallidos DESC
""")

for fila in cursor.fetchall():
    print(fila)

conexion.close()