# Padel Performance Analytics & Scouting System 📊

### Optimización del rendimiento deportivo mediante análisis de datos 

Este proyecto nace de la necesidad de profesionalizar el scouting en el pádel. Desarrollé un sistema integral que transforma las anotaciones crudas de los partidos en dashboards accionables para entrenadores y jugadores profesionales.

#### 🚀 Funcionalidades Clave:
- **Cargador Inteligente (Python):** Script que procesa archivos de texto con nomenclatura técnica (ej: `er1`, `wr1`, `spg`) y los transforma en datos estructurados.
- **Base de Datos Relacional (SQL):** Arquitectura diseñada para cruzar variables tácticas (dirección, intención, calidad de bola) con resultados emocionales y psicológicos.
- **Visualización Estratégica (Tableau):** Dashboards que identifican patrones de error y zonas de éxito bajo presión.

#### 🛠️ Tecnologías utilizadas:
- **Lenguaje:** Python (Pandas para limpieza de datos).
- **Base de Datos:** Azure SQL Database.
- **BI:** Tableau Desktop.

#### 📈 Impacto del Proyecto:
El sistema permite identificar, por ejemplo, la efectividad de los golpes según la "Calidad de Bola" recibida (Fácil, Media, Difícil), permitiendo al equipo técnico ajustar los entrenamientos basados en datos reales, no solo en sensaciones.<br>


🎯 Dashboard de Influencia y Peso en el Marcador

Este tablero responde a la pregunta estratégica: ¿Qué tanta injerencia tiene el jugador en la resolución de los puntos?

Métrica Clave: Indice de resolución = (Puntos Finalizados / Total Puntos Jugados).

Insight: No medimos solo la calidad técnica, sino el protagonismo real en el resultado.

Objetivo: Identificar desde qué zonas el jugador tiene mayor impacto resolutivo y en qué momentos del partido su presencia se vuelve determinante para cerrar el marcador. <br><br>


<img width="540" height="291" alt="Captura de pantalla 2026-03-01 a la(s) 7 11 30 p  m" src="https://github.com/user-attachments/assets/2c5ee127-de0a-4ff5-84b0-e368350ada72" /> <br><br>



Dashboard de Precisión Crítica (Efectividad en la Toma de Decisiones)
Este análisis responde a la pregunta clave: ¿Qué tan efectivo es el jugador cuando asume el riesgo de finalizar el punto?

Métrica Clave: Precisión Crítica = Winners / (Winners + Errores No Forzados).

Interpretación Directa: Por ejemplo, el 80,77% detectado en el segundo partido indica que, cuando el jugador decide tomar la iniciativa para cerrar, 8 de cada 10 veces lo hace de manera efectiva.

Criterio Técnico:

Incluye: Solo situaciones donde el punto termina directamente por acción del jugador (Winner o Error No Forzado).

Excluye: Errores forzados (donde la decisión está condicionada por el rival) y puntos donde el jugador no interviene en el cierre. <br><br>



<img width="559" height="296" alt="Captura de pantalla 2026-03-01 a la(s) 7 14 36 p  m" src="https://github.com/user-attachments/assets/2098aa3c-37d0-4f73-a42a-b0074e28f667" /><br><br>

🎯 Dashboard de Performance Bajo Presión
Aquí tenés el texto pulido para que lo pongas en tu README junto a esa imagen:

Este gráfico de “Momentos críticos del partido” permite auditar:

Toma de decisiones: Qué golpe elige el jugador cuando el marcador está ajustado (ej: 30-40 o ventajas).

Efectividad Psicológica: El resultado real (Winner vs. Error) en situaciones de alta tensión.

Patrones de Juego: Identificar si el jugador tiende a arriesgar (Smash/Volea) o a asegurar (Bloqueo/Globo) en momentos clave. <br><br>

<img width="606" height="874" alt="Captura de pantalla 2026-03-01 a la(s) 7 19 51 p  m" src="https://github.com/user-attachments/assets/3074d7ca-e956-4c8f-ac45-a53498af76a0" />



