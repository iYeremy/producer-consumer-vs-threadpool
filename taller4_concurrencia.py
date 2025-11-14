import threading, queue, time, random

cola = queue.Queue(maxsize=10)

def productor(nombre):
    print(f"Iniciando productor [{nombre}]...")
    for i in range(5):
        item = f"[{nombre}] - Helado - {i}"
        cola.put(item) # bloquea si esta llena la cola
        print(f"Productor [{nombre}] hizo un {item}")
        time.sleep(random.uniform(0.2, 0.6))

    cola.put(None) # senial para los consumidores 
    print(f"{nombre} finalizo produccion")

def consumidor():
    pass