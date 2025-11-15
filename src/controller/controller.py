import threading
from src.models.producer import Producer
from src.models.consumer import Consumer
from src.view.console import ConsoleView

class Controller:
    def run(self):
        threads = []

        # productores
        for i in range(2):
            def producer_job(i=i):
                ConsoleView.show_producer_start(i)
                p = Producer(i)
                items = p.produce()
                ConsoleView.show_produced(i, items)
                ConsoleView.show_producer_end(i)

            threads.append(threading.Thread(target=producer_job))

        # consumidores
        for i in range(3):
            def consumer_job(i=i):
                ConsoleView.show_consumer_start(i)
                c = Consumer(i)
                items = c.consume()
                ConsoleView.show_consumed(i, items)
                ConsoleView.show_consumer_end(i)

            threads.append(threading.Thread(target=consumer_job))

        # iniciar hilos
        for h in threads:
            h.start()

        # esperar hilos
        for h in threads:
            h.join()

        print("Procesamiento completado")
