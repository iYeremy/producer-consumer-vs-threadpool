"""
Ejercicio: Uso de ThreadPoolExecutor para simular la carga de mundos en un videojuego.
Cada tarea representa el proceso de preparar un mundo hasta que los jugadores puedan entrar.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

# Colores ANSI
VERDE = "\033[32m"
AZUL = "\033[34m"
AMARILLO = "\033[33m"
RESET = "\033[0m"

MENSAJES_CARGA = [
    "Cargando terreno",
    "Rellenando mares",
    "Despertando fauna",
    "Iluminando cavernas",
    "Regando junglas",
    "Afinando musica del bioma",
    "Elevando islas flotantes",
]


def cargar_mundo(nombre):
    """Simula las etapas que debe pasar un mundo antes de estar disponible."""
    pasos = random.sample(MENSAJES_CARGA, k=3)
    tiempo_total = 0.0
    for paso in pasos:
        duracion = random.uniform(0.3, 0.8)
        tiempo_total += duracion
        print(f"{AZUL}[{nombre}] {paso}...{RESET}")
        time.sleep(duracion)
    return f"{nombre} listo en {tiempo_total:.2f}s"


def main():
    mundos = [f"Mundo-{i}" for i in range(10)]

    inicio = time.time()

    with ThreadPoolExecutor(max_workers=3) as executor:
        futuros = [executor.submit(cargar_mundo, mundo) for mundo in mundos]

        for futuro in as_completed(futuros):
            resultado = futuro.result()
            print(f"{VERDE}Resultado -> {resultado}{RESET}")

    fin = time.time()

    print(f"{AMARILLO}Tiempo total de ejecucion: {fin - inicio:.3f} segundos{RESET}")
    print(f"{AMARILLO}Cargador de mundos finalizado.{RESET}")


if __name__ == "__main__":
    main()
