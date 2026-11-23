# Centinela - Paso 1: leer el archivo de log

# 1. Abrimos el archivo y leemos todas sus lineas
with open("logs/auth_ejemplo.log", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

# 2. Contamos cuantas lineas hay
print(f"El log tiene {len(lineas)} lineas")

# 3. Contamos cuantos intentos fallaron
fallidos = 0
for linea in lineas:
    if "Failed password" in linea:
        fallidos = fallidos + 1

print(f"Intentos fallidos: {fallidos}")
