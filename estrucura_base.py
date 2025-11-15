import threading, queue, time, random

# Colores ANSI
VERDE = "\033[32m"
AZUL = "\033[34m"
ROJO = "\033[31m"
AMARILLO = "\033[33m"
RESET = "\033[0m"

cola = queue.Queue(maxsize=10)

def productor(nombre) -> None:
    print(f"{VERDE}Iniciando productor [{nombre}]...{RESET}")
    for i in range(5):
        item = f"[(P{nombre})-Helado-{i}]"
        cola.put(item) # bloquea si esta llena la cola
        print(f"{VERDE}Productor [{nombre}] hizo un {item}{RESET}")
        time.sleep(random.uniform(0.2, 0.6))
    print(f"{VERDE}Productor {nombre} finalizo produccion{RESET}")

def consumidor(id_con) -> None:
    print(f"{AZUL}Consumidor [{id_con}] iniciado :){RESET}")
    while True:
        try:
            item = cola.get(timeout=2)
        except queue.Empty:
            print(f"{ROJO} Consumidor [{id_con}] vio que no hay mas heladitos disponibles :c{RESET}")
            break
        print(f"{AZUL}Consumidor [{id_con}] esta comiendo {item}{RESET}")
        time.sleep(random.uniform(0.2, 0.4))
        cola.task_done() # se termino de comer el helado
    print(f"{ROJO}Consumidor [{id_con}] no comera mas helados{RESET}")

def main(): 
    productores = [threading.Thread(target = productor, args=(i,)) for i in range(2)]
    consumidores = [threading.Thread(target = consumidor, args=(i,)) for i in range(3)]

    for h in productores + consumidores: h.start()
    for h in productores + consumidores: h.join()
    print("Procesamiento completado")
   
if __name__ == "__main__":
    main()