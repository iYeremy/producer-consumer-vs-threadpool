class ConsoleView:
    @staticmethod
    def show_producer_start(name):
        print(f"Iniciando productor [{name}]...")

    @staticmethod
    def show_produced(name, items):
        for item in items:
            print(f"Productor [{name}] produjo {item}")

    @staticmethod
    def show_producer_end(name):
        print(f"Productor [{name}] finalizo produccion")

    @staticmethod
    def show_consumer_start(cid):
        print(f"Consumidor [{cid}] iniciado")

    @staticmethod
    def show_consumed(cid, items):
        for item in items:
            print(f"Consumidor [{cid}] consumio {item}")

    @staticmethod
    def show_consumer_end(cid):
        print(f"Consumidor [{cid}] termino")
