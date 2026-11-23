# Centinela

Analizador de logs de seguridad. Lee los registros de acceso SSH de un servidor, detecta ataques y redacta el informe del incidente.

## Qué lo hace diferente

- **Fuerza bruta exitosa:** no solo avisa de intentos fallidos, detecta cuando el atacante logró entrar.
- **Comportamiento normal por usuario:** aprende horarios e IPs de cada usuario y alerta lo que se sale de lo normal.
- **Estándares de la industria:** alertas etiquetadas con MITRE ATT&CK y reglas en formato Sigma.
- **Informe con IA local:** genera el borrador del informe de incidente en español con Ollama, sin enviar datos a internet.

## Estructura

```
centinela/
├── logs/       Logs de ejemplo (datos inventados)
├── src/        Código del programa
├── reglas/     Reglas de detección (formato Sigma)
├── tests/      Pruebas automáticas
└── salida/     Base de datos e informes generados (no se suben a GitHub)
```

## Plan

**Base**
- [x] Leer el log y contar intentos fallidos
- [ ] Separar cada línea en datos (fecha, usuario, IP, resultado)
- [ ] Guardar en SQLite y consultar con SQL

**Detección**
- [ ] Fuerza bruta y fuerza bruta exitosa
- [ ] Comportamiento normal por usuario
- [ ] Etiquetas MITRE ATT&CK y reglas Sigma

**Informe**
- [ ] Borrador del informe de incidente con IA local (Ollama)

**Extra**
- [ ] Pruebas automáticas y GitHub Actions
- [ ] Docker

## Cómo usarlo

```bash
cd centinela
python src/lector.py
```
