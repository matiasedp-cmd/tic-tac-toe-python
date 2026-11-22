# ❌⭕ Tic-Tac-Toe (Ta-Te-Ti) en Python

Proyecto final del curso **Python Essentials 1 (Fundamentos de Python 1)** de **Cisco Networking Academy**. Implementación completa del clásico juego de consola *Tic-Tac-Toe* utilizando exclusivamente la biblioteca estándar de Python.

---

## 📋 Características

* **Tablero dinámico en consola:** Representación visual de matriz `3x3` mediante listas anidadas (`tablero[fila][columna]`), con la máquina (`X`) iniciando siempre en el centro.
* **Validación robusta de entradas:** Manejo de excepciones (`try-except`) para evitar cierres por caracteres no numéricos, números fuera de rango (`1-9`) o intentos de ocupar casillas ya tomadas.
* **Detección automática de resultados:** Verificación de victorias en filas, columnas y diagonales para ambos jugadores (`O` y `X`), además de detección de empates.
* **Sistema de revancha:** Opción al finalizar cada partida para reiniciar el tablero y volver a jugar o salir del programa de forma limpia.

---

## 🛠️ Requisitos y ejecución

No requiere instalación de dependencias externas, solo **Python 3.x**.

1. Clona el repositorio:
   ```bash
   git clone https://github.com
   cd tic-tac-toe-python
   ```

2. Ejecuta el juego:
   ```bash
   python tic_tac_toe.py
   ```

---

## 🧩 Estructura del código

| Función | Descripción |
| :--- | :--- |
| `mostrar_tablero(tablero)` | Dibuja el estado actual del tablero `3x3` en la terminal. |
| `ingresar_movimiento(tablero)` | Solicita, valida y registra la jugada del usuario (`O`). |
| `listar_campos_libres(tablero)` | Devuelve una lista de tuplas `(fila, columna)` con las casillas disponibles. |
| `victoria_para(tablero, signo)` | Evalúa si el jugador indicado completó una línea horizontal, vertical o diagonal. |
| `dibujar_movimiento(tablero)` | Genera un movimiento aleatorio válido para la máquina (`X`). |
| `jugar()` | Controla el flujo completo de una partida individual. |

---

## 🚀 Flujo de desarrollo

El proyecto se construyó de manera modular utilizando ramas y Pull Requests bajo la convención **Conventional Commits**:
1. Estructura inicial del tablero y renderizado visual.
2. Captura y validación del movimiento del usuario.
3. Lógica de victoria, turnos de la máquina y bucle principal.
4. Mejoras de interfaz en consola y bucle de reinicio de partida.
