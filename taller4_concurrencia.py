import threading, queue, time, random

cola = queue.Queue(maxsize=10)

def productor(nombre) -> None:
    print(f"Iniciando productor [{nombre}]...")
    for i in range(5):
        item = f"[{nombre} - Helado - {i}]"
        cola.put(item) # bloquea si esta llena la cola
        print(f"Productor [{nombre}] hizo un {item}")
        time.sleep(random.uniform(0.2, 0.6))

    cola.put(None) # senial para los consumidores 
    print(f"{nombre} finalizo produccion")

def consumidor(id_con) -> None:
    print(f"Consumidor [{id_con}] iniciado :)")
    while True:
        item = cola.get() # bloquea si esta vacia
        if item is None:
            print(f"Consumidor [{id_con}] no hay mas heladitos :( )")
            cola.put(None)
            break
        print(f"Consumidor [{id_con}] comio un heladito")
        time.sleep(random.uniform(0.2, 0.6))
        cola.task_done() # se termino de comer el helado

def main():
    pass

if __name__ == "__main__":
    main()