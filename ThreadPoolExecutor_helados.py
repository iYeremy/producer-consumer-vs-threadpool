"""
Ejercicio: Uso de ThreadPoolExecutor para procesar tareas concurrentes.
Cada tarea simula preparar un helado con una duracion aleatoria.
Se muestran conforme van terminando.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

# Colores ANSI
VERDE = "\033[32m"
AZUL = "\033[34m"
AMARILLO = "\033[33m"
RESET = "\033[0m"


def preparar_helado(nombre):
    """Simula preparar un helado con una duracion aleatoria."""
    duracion = random.uniform(0.5, 1.5)
    print(f"{AZUL}[{nombre}] iniciando preparacion (duracion {duracion:.2f}s){RESET}")
    time.sleep(duracion)
    return f"{nombre} completado"


def main():
    # Creamos un conjunto de tareas
    helados = [f"(H{i})-Helado" for i in range(10)]

    inicio = time.time()

    with ThreadPoolExecutor(max_workers=3) as executor:
        futuros = [executor.submit(preparar_helado, h) for h in helados]

        # Mostrar resultados a medida que terminan
        for futuro in as_completed(futuros):
            resultado = futuro.result()
            print(f"{VERDE}Resultado -> {resultado}{RESET}")

    fin = time.time()

    print(f"{AMARILLO}Tiempo total de ejecucion: {fin - inicio:.3f} segundos{RESET}")
    print(f"{AMARILLO}Ejecucion finalizada.{RESET}")


if __name__ == "__main__":
    main()
