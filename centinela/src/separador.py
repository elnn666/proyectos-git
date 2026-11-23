linea = "Nov 20 03:10:00 servidor sshd[1300]: Failed password for root from 203.0.113.77 port 41300 ssh2"

partes = linea.split()

print(partes)
print(partes[2])
print(partes[8])
print(partes[10])