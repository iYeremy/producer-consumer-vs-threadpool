# Productor--Consumidor en Python (Version con Timeouts)

> [!NOTE]
> Este proyecto tambien contiene un directorio MVC_Productores_y_Consumidores/ pero este no forma parte del taller, fue elaborado solamente para fines didactos y
> practicar la estructura MVC pero para programas AUTOMATIZADOS

Este proyecto implementa el patron **Productor--Consumidor** usando `threading` y `queue.Queue`. La idea es simular como dos servidores multijugador van generando mundos y tres exploradores (clientes) se conectan tan pronto como un mundo termina la secuencia de carga. Todo se hace de forma concurrente y usando un `timeout` para que los jugadores sepan cuando ya no quedan mas mundos en cola.

Tambien use este video de apoyo para darme una idea intuitiva sobre el manejo de hilos y la cola (buffer)

<p align="center">
  <a href="https://www.youtube.com/watch?v=gI0BtbmIYUs">
    <img src="https://img.youtube.com/vi/gI0BtbmIYUs/hqdefault.jpg" alt="Demo en YouTube">
  </a>
</p>

---

## Descripcion general

-   Dos servidores generan 10 mundos procedimentales (5 cada uno).
-   Tres exploradores se conectan cuando detectan que un mundo termino su secuencia de carga.
-   La cola tiene un tamano maximo de 10 sesiones de mundo listas para entrar.
-   Los exploradores usan `get(timeout=2)` para abandonar la espera cuando no hay mas mundos disponibles.
-   Al final se muestran cuantos mundos se generaron, cuantas entradas de jugadores se registraron y el tiempo total de ejecucion.

---

## Como funciona el codigo

### `generador_mundo(nombre)`

Simula un servidor preparando mundos. Cada iteracion toma una fase de carga aleatoria (modelar terreno, despertar criaturas, etc.), la coloca en la cola compartida y registra que el mundo esta listo para jugadores.

### `jugador_esperando(id_con)`

Representa a un explorador en la cola de espera. Toma mundos de la cola, imprime cuando logra entrar y abandona la sesion si pasan 2 segundos sin novedades.

### `main()`

Crea los hilos de servidores y exploradores, inicia todos, espera a que terminen y luego imprime estadisticas de cuantas fases se procesaron y cuanto tiempo tomo el ciclo completo.

---

## Ejemplo de salida

```
Servidor [0] preparando mundos...
Servidor [1] preparando mundos...
Explorador [0] esperando mundos disponibles...
Explorador [1] esperando mundos disponibles...
Explorador [2] esperando mundos disponibles...
[Servidor-0] Mundo-0 :: Plantando bosques completado y listo para jugadores.
Explorador [0] entro cuando '[Servidor-0] Mundo-0 :: Plantando bosques' termino de cargarse.
...
===== RESULTADOS =====
Fases de carga generadas: 10
Entradas exitosas de jugadores: 10
Tiempo total de ejecucion: 3.481 segundos
Cola de mundos vacia. Listo para nuevas sesiones.
Procesamiento completado
```

---

# Segunda version: ThreadPoolExecutor

Tambien se hizo una version usando **ThreadPoolExecutor**, que maneja automaticamente un pool de hilos. Cada tarea ahora representa la carga completa de un mundo y se le asigna a un trabajador del pool hasta que todos los mundos quedan listos para abanico de jugadores.

Ejemplo:

```
[Mundo-0] Cargando terreno...
[Mundo-0] Regando junglas...
[Mundo-0] Afinando musica del bioma...
Resultado -> Mundo-0 listo en 1.36s
...
Tiempo total de ejecucion: 4.012 segundos
Cargador de mundos finalizado.
```

---

# Analisis rapido

-   En la version Productor--Consumidor se observa claramente como los servidores depositan trabajos en la cola y como los exploradores van entrando apenas hay cupo.
-   En la version con ThreadPoolExecutor el mismo concepto de "preparar mundos" se modela como tareas independientes que el executor distribuye sobre un conjunto fijo de hilos.
-   Los tiempos de ejecucion son parecidos porque la mayor parte del tiempo se invierte en `sleep()`, que aqui simula operaciones de I/O o procesos de carga.
-   Para aplicaciones reales, el executor simplifica la administracion de hilos y es mas facil de escalar cuando el numero de mundos o servidores crece.

---

## Reflexion sobre modularidad y posible uso de MVC

Aunque este taller funciona bien con un solo script, vale la pena pensar como se organizaria si el sistema creciera. En proyectos mas grandes, separar responsabilidades suele hacer el codigo mas claro y mas facil de mantener.

Una opcion seria usar una estructura inspirada en el patron MVC:

-   **Modelo:** incluiria la logica de generacion de mundos, la cola compartida y el manejo de estados de carga.
-   **Controlador:** coordina el flujo del programa, la creacion de hilos y el control general del proceso de carga y de entrada de jugadores.
-   **Vista:** se encarga de mostrar mensajes, formato de salida y cualquier interaccion visible para los operadores o jugadores.

Para este taller no es necesario implementar esta estructura (igualmente agregue una version de MVC), pero pensar en modularidad ayuda a entender como escalar el diseno si se agregan mas tipos de mundos, varias colas o diferentes interfaces.

# Estructura del proyecto

```
.
├── estrucura_base.py
├── ThreadPoolExecutor_helados.py
├── MVC_Productores_y_Consumidores/
└── README.md
```
