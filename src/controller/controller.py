import threading
from src.models.producer import Producer
from src.models.consumer import Consumer
from src.view.console import ConsoleView
import time

class Controller:
    def run(self):

        producciones = []
        consumos = []

        inicio = time.time()
        threads = []

        # PRODUCTORES
        for i in range(2):
            def producer_job(i=i):  
                ConsoleView.show_producer_start(i)
                p = Producer(i)
                items = p.produce()
                producciones.extend(items)
                ConsoleView.show_produced(i, items)
                ConsoleView.show_producer_end(i)

            threads.append(threading.Thread(target=producer_job))

        # CONSUMIDORES
        for i in range(3):
            def consumer_job(i=i):
                ConsoleView.show_consumer_start(i)
                c = Consumer(i)
                items = c.consume()
                consumos.extend(items)
                ConsoleView.show_consumed(i, items)
                ConsoleView.show_consumer_end(i)

            threads.append(threading.Thread(target=consumer_job))

        # Ejecutar hilos
        for h in threads:
            h.start()

        for h in threads:
            h.join()

        fin = time.time()

        print("\n===== RESULTADOS =====")
        print("Tareas producidas:", len(producciones))
        print("Tareas consumidas:", len(consumos))
        print("Tiempo total:", round(fin - inicio, 3), "segundos")
