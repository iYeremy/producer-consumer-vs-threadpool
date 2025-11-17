import threading, queue, time, random

# Colores ANSI
VERDE = "\033[32m"
AZUL = "\033[34m"
ROJO = "\033[31m"
AMARILLO = "\033[33m"
RESET = "\033[0m"

cola = queue.Queue(maxsize=10)

FASES_CARGA = [
    "Modelando terreno",
    "Rellenando mares",
    "Trazando cavernas",
    "Plantando bosques",
    "Encendiendo volcanes",
    "Agitando la atmosfera",
    "Despertando criaturas",
]

mundos_generados = []
entradas_jugadores = []

def generador_mundo(nombre) -> None:
    print(f"{VERDE}Servidor [{nombre}] preparando mundos...{RESET}")
    for i in range(5):
        fase = random.choice(FASES_CARGA)
        item = f"[Servidor-{nombre}] Mundo-{i} :: {fase}"
        cola.put(item)  # bloquea si esta llena la cola
        mundos_generados.append(item)
        print(f"{VERDE}{item} completado y listo para jugadores.{RESET}")
        time.sleep(random.uniform(0.2, 0.6))
    print(f"{VERDE}Servidor [{nombre}] ya dejo todos los mundos en cola.{RESET}")

def jugador_esperando(id_con) -> None:
    print(f"{AZUL}Explorador [{id_con}] esperando mundos disponibles...{RESET}")
    while True:
        try:
            item = cola.get(timeout=2)
        except queue.Empty:
            print(f"{ROJO}Explorador [{id_con}] volvio al menu: no quedan mundos nuevos por cargar.{RESET}")
            break
        print(f"{AZUL}Explorador [{id_con}] entro cuando '{item}' termino de cargarse.{RESET}")
        entradas_jugadores.append(item)
        time.sleep(random.uniform(0.2, 0.4))
        cola.task_done()  # se libero la entrada para el siguiente
    print(f"{ROJO}Explorador [{id_con}] cerrando sesion de espera.{RESET}")

def main():
    inicio = time.time()

    servidores = [threading.Thread(target=generador_mundo, args=(i,)) for i in range(2)]
    exploradores = [threading.Thread(target=jugador_esperando, args=(i,)) for i in range(3)]

    for h in servidores + exploradores:
        h.start()
    for h in servidores + exploradores:
        h.join()

    fin = time.time()

    print("\n===== RESULTADOS =====")
    print(f"{AMARILLO}Fases de carga generadas: {len(mundos_generados)}{RESET}")
    print(f"{AMARILLO}Entradas exitosas de jugadores: {len(entradas_jugadores)}{RESET}")
    print(f"{AMARILLO}Tiempo total de ejecución: {round(fin - inicio, 3)} segundos{RESET}")
    print(f"{AMARILLO}Cola de mundos vacia. Listo para nuevas sesiones.{RESET}")
    print("Procesamiento completado")

if __name__ == "__main__":
    main()
