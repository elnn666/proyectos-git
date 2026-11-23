with open("logs/auth_ejemplo.log", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    partes = linea.split()
    print(partes[2],  partes[5], partes[8], partes[10])

fallidos = {}
correctos = {}

for linea in lineas:
    ip = linea.split()[10]
    if "Failed" in linea:
        fallidos[ip] = fallidos.get(ip, 0) + 1
    else:
        correctos[ip] = correctos.get(ip, 0) + 1

print("Fallidos:", fallidos)
print("Correctos:", correctos)