# Productor--Consumidor en Python (Version con Timeouts)

> [!NOTE]
> Este proyecto tambien contiene un directorio MVC_Productores_y_Consumidores/ pero este no forma parte del taller, fue elaborado solamente para fines didactos y
> practicar la estructura MVC pero para programas AUTOMATIZADOS

Este proyecto implementa el patron **Productor--Consumidor** usando
`threading` y `queue.Queue`. La idea es simular como dos productores
generan heladitos y tres consumidores los procesan al mismo tiempo. Todo
se hace de forma concurrente y usando un `timeout` para que los
consumidores sepan cuando ya no quedan mas tareas.

Tambien use este video de apoyo para darme una idea intuitiva sobre el manejo de hilos y la cola (buffer)

<p align="center">
  <a href="https://www.youtube.com/watch?v=gI0BtbmIYUs">
    <img src="https://img.youtube.com/vi/gI0BtbmIYUs/hqdefault.jpg" alt="Demo en YouTube">
  </a>
</p>

---

## Descripcion general

-   Dos productores generan 10 helados en total.
-   Tres consumidores los procesan mientras haya elementos en la cola.
-   La cola tiene un tamaño maximo de 10.
-   Los consumidores usan `get(timeout=2)` para terminar cuando la cola
    queda vacia por un rato.
-   Al final se muestran las tareas producidas, las consumidas y el
    tiempo total de ejecucion.

---

## Como funciona el codigo

### `productor(nombre)`

Genera 5 helados, los coloca en la cola y muestra mensajes sobre lo que
va haciendo.

### `consumidor(id_con)`

Saca helados de la cola hasta que no llegan mas (timeout). Tambien
muestra si esta comiendo o si ya no hay tareas.

### `main()`

Crea los hilos, los arranca, espera a que todos terminen y muestra los
resultados finales.

---

## Ejemplo de salida

    Iniciando productor [0]...
    Iniciando productor [1]...
    Consumidor [0] iniciado :)
    Consumidor [1] iniciado :)
    Consumidor [2] iniciado :)
    Productor [0] hizo un [(P0)-Helado-0]
    Consumidor [0] esta comiendo [(P0)-Helado-0]
    ...
    ===== RESULTADOS =====
    Total de tareas producidas: 10
    Total de tareas consumidas: 10
    Tiempo total de ejecucion: 3.814 segundos
    Procesamiento completado

---

# Segunda version: ThreadPoolExecutor

Tambien se hizo una version usando **ThreadPoolExecutor**, que maneja
automaticamente un pool de hilos. Aqui no hay productores y consumidores
separados, sino tareas que representan helados y son ejecutadas por los
hilos del pool.

Ejemplo:

    [(H0)-Helado] iniciando preparacion...
    Resultado -> (H0)-Helado completado
    ...
    Tiempo total: 3.806 segundos

---

# Analisis rapido

-   En la version Productor--Consumidor se puede ver claramente como se
    comunican los hilos usando la cola.
-   En la version con ThreadPoolExecutor el codigo queda mas limpio y
    Python se encarga de manejar los hilos.
-   Los tiempos salen parecidos porque la mayor parte del tiempo se va
    en `sleep()`, que simula operaciones de E/S.
-   Para aplicaciones reales, el executor es mas practico porque
    reutiliza hilos y escala mejor.

---

# Estructura del proyecto

    .
    ├── estrucura_base.py
    ├── ThreadPoolExecutor_helados.py
    ├── MVC_Productores_y_Consumidores/
    └── README.md
