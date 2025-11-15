# Productor–Consumidor en Python (Versión con Timeouts)

Este proyecto implementa una versión sencilla del patrón Productor–Consumidor en Python utilizando hilos (`threading`) y una cola segura (`queue.Queue`). El sistema simula cómo varios productores generan elementos y cómo varios consumidores los procesan de manera concurrente.

La comunicación entre hilos se realiza mediante una cola compartida y los consumidores utilizan un `timeout` para determinar el final de su trabajo cuando ya no se produzcan más elementos.

---

## Descripción general

-   Se crean dos productores, cada uno generando cinco elementos.
-   Se crean tres consumidores, que retiran elementos de la cola mientras haya disponibles.
-   La cola tiene un tamaño máximo de 10 elementos.
-   Los consumidores utilizan `queue.get(timeout=2)` para finalizar cuando la cola se mantiene vacía por un tiempo.
-   Los hilos se ejecutan en paralelo para simular concurrencia real.

Este enfoque evita el uso de sentinelas (`None`) y permite finalizar el consumo de forma natural mediante timeouts.

---

## Estructura del código

### `productor(nombre)`

Genera cinco elementos y los inserta en la cola.  
Imprime información sobre cada producción.

### `consumidor(id_con)`

Toma elementos de la cola utilizando un timeout.  
Si no se recibe ningún elemento dentro del intervalo de espera, el consumidor termina su ejecución.

### `main()`

-   Crea y arranca los hilos de productores y consumidores.
-   Espera a que todos los hilos finalicen usando `join()`.
-   Imprime un mensaje indicando que el procesamiento ha terminado.

---

## Ejemplo de salida

El orden de los mensajes puede variar debido a la ejecución concurrente.

```
Iniciando productor [0]...
Iniciando productor [1]...
Consumidor [0] iniciado :)
Consumidor [1] iniciado :)
Consumidor [2] iniciado :)
Productor [0] hizo un [0 - Helado - 0]
Consumidor [0] esta comiendo [0 - Helado - 0]
...
Consumidor [1] vio que no hay mas heladitos disponibles :c
Consumidor [1] no comera mas helados
Procesamiento completado

```
