# Centinela

Analizador de logs de seguridad. Lee los registros de acceso SSH de un servidor y detecta actividad sospechosa.

## Estado

- [x] Paso 1: leer el log y contar intentos fallidos
- [ ] Paso 2: separar cada línea en datos (fecha, usuario, IP, resultado)
- [ ] Paso 3: guardar en SQLite y consultar con SQL
- [ ] Paso 4: reglas de alerta (fuerza bruta, horarios raros)
- [ ] Paso 5: reporte con gráficas
- [ ] Paso 6: Docker

## Cómo usarlo

```bash
cd centinela
python centinela.py
```
