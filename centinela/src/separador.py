with open("logs/openssh_loghub_2k.log", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    if "Failed password" not in linea and "Accepted password" not in linea:
        continue
    partes = linea.split()
    ip = partes[partes.index("from") + 1]
    print(partes[2],  partes[5], ip)

fallidos = {}
correctos = {}

for linea in lineas:
    if "Failed password" not in linea and "Accepted password" not in linea:
        continue
    partes = linea.split()
    ip = partes[partes.index("from") + 1]
    if "Failed" in linea:
        fallidos[ip] = fallidos.get(ip, 0) + 1
    else:
        correctos[ip] = correctos.get(ip, 0) + 1

print("Fallidos:", fallidos)
print("Correctos:", correctos)