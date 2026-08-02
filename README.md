# Black Mamba AI Copilot

Sistema experimental de copiloto asistido por IA para Microsoft Flight Simulator.

## Objetivo

Construir un sistema modular que:

- lea telemetría desde Microsoft Flight Simulator mediante SimConnect;
- detecte eventos de vuelo y desviaciones operativas;
- genere alertas y recomendaciones en tiempo real;
- registre cada sesión;
- produzca un reporte técnico después del vuelo.

## Alcance del MVP

1. Conexión a SimConnect.
2. Lectura de telemetría básica:
   - altitud;
   - velocidad indicada;
   - rumbo;
   - pitch y bank;
   - posición;
   - combustible;
   - estado del tren de aterrizaje.
3. Motor de reglas para eventos iniciales:
   - overspeed;
   - stall warning;
   - combustible bajo;
   - aproximación inestable;
   - desviación de rumbo.
4. Salida por consola.
5. Registro de telemetría en JSONL.

## Arquitectura

```text
Microsoft Flight Simulator
        ↓ SimConnect
Telemetry Adapter
        ↓
Normalized Flight State
        ↓
Rules Engine
        ↓
Alerts / Logs / Future Voice UI
```

## Estructura inicial

```text
flight-simu/
├── README.md
├── requirements.txt
├── .gitignore
└── src/
    ├── main.py
    ├── telemetry.py
    ├── rules.py
    └── models.py
```

## Estado

Proyecto en fase de arranque.

## Roadmap

- [x] Definir arquitectura inicial.
- [ ] Conectar con SimConnect.
- [ ] Normalizar telemetría.
- [ ] Implementar reglas básicas.
- [ ] Añadir voz en tiempo real.
- [ ] Crear reporte post-vuelo.
- [ ] Añadir panel web.

## Seguridad

Este proyecto es para simulación. No debe utilizarse como sustituto de procedimientos reales de aviación, entrenamiento certificado ni sistemas de seguridad aeronáutica.
