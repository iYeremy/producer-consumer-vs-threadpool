import time, random
from src.models.shared_queue import buffer

class Producer:
    def __init__(self, name):
        self.name = name

    def produce(self):
        items = []
        for i in range(5):
            item = f"[(P{self.name})-Helado-{i}]"
            buffer.put(item)
            items.append(item)
            time.sleep(random.uniform(0.2, 0.6))
        return items  # controller decidira como mostrarlos
